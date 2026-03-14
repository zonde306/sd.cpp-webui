"""sd.cpp-webui - UI interactivity and events module"""

import os

import gradio as gr

import modules.utils.queue as queue_manager
from modules.shared_instance import (
    sd_options, model_state, current_mode
)


def get_ordered_inputs(inputs_map):
    """Utility to ensure keys and components always match up."""
    ordered_keys = sorted(inputs_map.keys())
    ordered_components = [inputs_map[k] for k in ordered_keys]
    return ordered_keys, ordered_components


def bind_generation_pipeline(
    api_func, ordered_keys, ordered_components, outputs_map
):
    """
    Connects the UI components to the generation queue.
    """
    tab_id = api_func.__name__

    def submit_job(*args):
        params = dict(zip(ordered_keys, args))

        queue_manager.add_job(api_func, params, owner=tab_id)

        q_len = queue_manager.get_queue_size()

        print(f"\n\nJob submitted! Position in queue: {q_len}.\n"),

        return (
            gr.update(visible=True, value=0),
            gr.update(visible=True, value="Added to queue...")
        )

    def poll_status():
        state = queue_manager.get_status()
        q_len = queue_manager.get_queue_size()

        if state.get("owner") != tab_id and state.get("owner") is not None:
            return (
                gr.skip(),
                gr.skip(),
                gr.skip(),
                gr.skip(),
                gr.skip(),
                gr.skip(),
                gr.skip()
            )

        if not state["is_running"] and q_len == 0:
            if state.get("is_finished"):
                state["is_finished"] = False
            else:
                return (
                    gr.skip(),
                    gr.skip(),
                    gr.skip(),
                    gr.skip(),
                    gr.skip(),
                    gr.skip(),
                    gr.skip(),
                )

        prog = state["progress"]
        stat = state["status"]

        if not state["is_running"] and q_len > 0:
            prog = gr.skip()
            stat = gr.skip()
        elif prog == 0:
            prog = gr.skip()
            stat = gr.skip()

        queue_display = gr.update(
            value=f"⏳ Jobs in queue: {q_len}" if q_len > 0 else "",
            visible=(q_len > 0)
        )

        # 解密图片
        images = state["images"]
        if images:
            from modules.utils.image_display import decrypt_and_display
            if isinstance(images, list):
                decrypted = []
                for img in images:
                    if isinstance(img, str):
                        result = decrypt_and_display(img)
                        if result:
                            decrypted.append(result)
                    else:
                        decrypted.append(img)
                images = decrypted if decrypted else None
            else:
                result = decrypt_and_display(images)
                images = result

        return (
            state["command"],
            prog,
            stat,
            state["stats"],
            images,
            gr.skip(),
            queue_display
        )

    def run_job_sync(*args):
        params = dict(zip(ordered_keys, args))
        last_result = None

        for result in api_func(params):
            if isinstance(result, (tuple, list)) and len(result) >= 5:
                last_result = result

        images = last_result[4] if last_result else None

        if images:
            image_exts = {
                ".png", ".jpg", ".jpeg", ".webp",
                ".bmp", ".gif", ".tif", ".tiff"
            }

            def is_image_path(item):
                return (
                    isinstance(item, str) and
                    os.path.splitext(item)[1].lower() in image_exts
                )

            if isinstance(images, (list, tuple)):
                should_decrypt = any(is_image_path(img) for img in images)
            else:
                should_decrypt = is_image_path(images)

            if should_decrypt:
                from modules.utils.image_display import decrypt_and_display
                images = decrypt_and_display(images)

            from PIL import Image

            def load_image_from_path(path):
                if path and os.path.exists(path):
                    try:
                        return Image.open(path)
                    except Exception:
                        return None
                return None

            if isinstance(images, (list, tuple)):
                loaded = []
                for img in images:
                    if isinstance(img, str):
                        loaded_img = load_image_from_path(img)
                        loaded.append(loaded_img if loaded_img is not None else img)
                    else:
                        loaded.append(img)
                images = loaded
            elif isinstance(images, str):
                loaded_img = load_image_from_path(images)
                images = loaded_img if loaded_img is not None else images

        if images is None:
            return None

        return list(images) if isinstance(images, (list, tuple)) else [images]

    outputs_map['gen_btn'].click(
        fn=submit_job,
        inputs=ordered_components,
        outputs=[
            outputs_map['progress_slider'],
            outputs_map['progress_textbox'],
        ],
        api_name="generate"
    )

    api_gen_btn = outputs_map.get('api_gen_btn')
    if api_gen_btn is None:
        api_gen_btn = gr.Button(value="API Generate", visible=False)

    api_gen_btn.click(
        fn=run_job_sync,
        inputs=ordered_components,
        outputs=[outputs_map['img_final']],
        api_name=f"{tab_id}_generate"
    )

    outputs_map['timer'].tick(
        poll_status,
        inputs=[],
        outputs=[
            outputs_map['command'],
            outputs_map['progress_slider'],
            outputs_map['progress_textbox'],
            outputs_map['stats'],
            outputs_map['img_final'],
            outputs_map['timer'],
            outputs_map['queue_tracker']
        ]
    )


def apply_lora(
    lora_model, lora_strength, lora_prompt_switch,
    pprompt, nprompt
):
    if lora_model:
        lora_model = os.path.splitext(lora_model)[0]
        lora_string = "<lora:" + lora_model + ":" + str(lora_strength) + ">"
        n_lora_string = "<lora:" + lora_model + ":-" + str(lora_strength) + ">"

        if lora_prompt_switch == "Positive":
            pprompt = "".join([pprompt, lora_string])

        elif lora_prompt_switch == "Negative":
            if nprompt is True:
                nprompt = "".join([nprompt, lora_string])
            elif nprompt.visible is False:
                pprompt = "".join([pprompt, n_lora_string])

    return (pprompt, nprompt)


def unet_tab_switch(*args):
    """Switches to the UNET tab"""
    return (
        gr.update(value=1),                                                # + UNET Tab
        gr.update(value=None),                                             # - Checkpoint Model
        gr.update(value=model_state.bak_unet_model),                       # + UNET Model
        gr.update(value=None),                                             # - Checkpoint VAE
        gr.update(value=model_state.bak_unet_vae),                         # + UNET VAE
        gr.update(value=model_state.bak_clip_g),                           # + clip_g
        gr.update(value=model_state.bak_clip_l),                           # + clip_l
        gr.update(value=model_state.bak_t5xxl),                            # + t5xxl
        gr.update(value=model_state.bak_llm),                              # + llm
        gr.update(value=model_state.bak_guidance_bool, visible=True),      # + guidance_bool
        gr.update(visible=True),                                           # + guidance
        gr.update(value=model_state.bak_flow_shift_bool, visible=True),    # + flow_shift_bool
        gr.update(visible=True),                                           # + flow_shift
    )


def ckpt_tab_switch(*args):
    """Switches to the checkpoint tab"""
    return (
        gr.update(value=0),                             # + Checkpoint Tab
        gr.update(value=model_state.bak_ckpt_model),    # + Checkpoint Model
        gr.update(value=None),                          # - UNET Model
        gr.update(value=model_state.bak_ckpt_vae),      # + Checkpoint VAE
        gr.update(value=None),                          # - UNET VAE
        gr.update(value=None),                          # - clip_g
        gr.update(value=None),                          # - clip_l
        gr.update(value=None),                          # - t5xxl
        gr.update(value=None),                          # - llm
        gr.update(value=False, visible=False),          # - guidance_bool
        gr.update(visible=False),                       # - guidance
        gr.update(value=False, visible=False),          # - flow_shift_bool
        gr.update(visible=False),                       # - flow_shift
    )


def update_interactivity(count, checkbox_value):
    """
    Generates a specified number of gr.update objects to set interactivity.
    """
    is_interactive = bool(checkbox_value)

    if count == 1:
        return gr.update(interactive=is_interactive)

    return tuple(gr.update(interactive=is_interactive) for _ in range(count))


def refresh_all_options():
    sd_options.refresh()
    return [
        gr.update(choices=sd_options.get_opt("samplers")),
        gr.update(choices=sd_options.get_opt("schedulers")),
        gr.update(choices=["none"] + sd_options.get_opt("previews")),
        gr.update(choices=["Default"] + sd_options.get_opt("prediction"))
    ]
