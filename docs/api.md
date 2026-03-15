# Gradio API 文档

## 概览
本项目基于 Gradio Blocks 并启用 `show_api`，支持通过 Gradio API 调用生成并直接返回图片结果（同步接口）。

- WebUI 默认地址：`http://localhost:7860/`
- API Schema：`http://localhost:7860/gradio_api.json`
- 代码入口：[`modules/utils/ui_events.py`](modules/utils/ui_events.py:20)

## API 命名规则
同步生成 API 的 `api_name` 规则为：

```
{tab_id}_generate
```

其中 `tab_id` = 生成函数名（`api_func.__name__`）。

### 端点列表（常用）
| 模式 | 功能 | api_name |
| --- | --- | --- |
| server | txt2img | `txt2img_api_generate` |
| server | img2img | `img2img_api_generate` |
| server | imgedit | `imgedit_api_generate` |
| cli | txt2img | `txt2img_generate` |
| cli | img2img | `img2img_generate` |
| cli | imgedit | `imgedit_generate` |
| cli | any2video | `any2video_generate` |

> 说明：UI 队列接口仍保留 `api_name="generate"`，该接口用于进度展示，不会直接返回图片。

## 获取参数顺序与默认值
所有 API 输入参数顺序与 UI 组件一致，建议通过 API Schema 自动读取：

- 访问 `http://localhost:7860/gradio_api.json`
- 或使用 `gradio_client.Client(...).view_api()`

## view_api 输出示例（仅 *_api_generate）
> 不同运行环境/模型列表会有所不同，以下仅保留同步生成端点。

```text
Client.predict() Usage Info
---------------------------
Named API endpoints: 278

 - predict(..., api_name="txt2img_api_generate") -> img_final
 - predict(..., api_name="img2img_api_generate") -> img_final
 - predict(..., api_name="imgedit_api_generate") -> img_final
```

<!-- view_api_full_output_start
 - predict(x, api_name="/lambda") ->
    Parameters:
     - [Dropdown] x: Literal['[illustrious]JANKUV5NSFWTrainedNoobai_v69.safetensors', '[illustrious]WAI-illustrious-SDXL.safetensors', '[illustrious]miaomiaoHarem_v195.safetensors', '[illustrious]miaomiaoRealskin_epsV14.safetensors'] (required)
    Returns:
     - None

 - predict(models_folder, api_name="/reload_models") -> checkpoint_model
    Parameters:
     - [Textbox] models_folder: str (not required, defaults to:   /kaggle/working/sd.cpp-webui/models/checkpoints/)
    Returns:
     - [Dropdown] checkpoint_model: Literal['[illustrious]JANKUV5NSFWTrainedNoobai_v69.safetensors', '[illustrious]WAI-illustrious-SDXL.safetensors', '[illustrious]miaomiaoHarem_v195.safetensors', '[illustrious]miaomiaoRealskin_epsV14.safetensors']

 - predict(api_name="/lambda_1") ->
    Parameters:
     - None
    Returns:
     - None

 - predict(x, api_name="/lambda_2") ->
    Parameters:
     - [Dropdown] x: Literal['ae.safetensors'] (required)
    Returns:
     - None

 - predict(models_folder, api_name="/reload_models_1") -> checkpoint_vae
    Parameters:
     - [Textbox] models_folder: str (not required, defaults to:   /kaggle/working/sd.cpp-webui/models/vae/)
    Returns:
     - [Dropdown] checkpoint_vae: Literal['ae.safetensors']

 - predict(api_name="/lambda_3") ->
    Parameters:
     - None
    Returns:
     - None

 - predict(x, api_name="/lambda_4") ->
    Parameters:
     - [Dropdown] x: Literal['z_image_turbo-Q8_0.gguf'] (required)
    Returns:
     - None

 - predict(models_folder, api_name="/reload_models_2") -> unet_model
    Parameters:
     - [Textbox] models_folder: str (not required, defaults to:   /kaggle/working/sd.cpp-webui/models/unet/)
    Returns:
     - [Dropdown] unet_model: Literal['z_image_turbo-Q8_0.gguf']

 - predict(api_name="/lambda_5") ->
    Parameters:
     - None
    Returns:
     - None

 - predict(x, api_name="/lambda_6") ->
    Parameters:
     - [Dropdown] x: Literal['ae.safetensors'] (required)
    Returns:
     - None

 - predict(models_folder, api_name="/reload_models_3") -> unet_vae
    Parameters:
     - [Textbox] models_folder: str (not required, defaults to:   /kaggle/working/sd.cpp-webui/models/vae/)
    Returns:
     - [Dropdown] unet_vae: Literal['ae.safetensors']

 - predict(api_name="/lambda_7") ->
    Parameters:
     - None
    Returns:
     - None

 - predict(x, api_name="/lambda_8") ->
    Parameters:
     - [Dropdown] x: Literal['Qwen3-4B-Instruct-2507-Q4_K_M.gguf'] (required)
    Returns:
     - None

 - predict(models_folder, api_name="/reload_models_4") -> clip_g
    Parameters:
     - [Textbox] models_folder: str (not required, defaults to:   /kaggle/working/sd.cpp-webui/models/text_encoders/)
    Returns:
     - [Dropdown] clip_g: Literal['Qwen3-4B-Instruct-2507-Q4_K_M.gguf']

 - predict(api_name="/lambda_9") ->
    Parameters:
     - None
    Returns:
     - None

 - predict(x, api_name="/lambda_10") ->
    Parameters:
     - [Dropdown] x: Literal['Qwen3-4B-Instruct-2507-Q4_K_M.gguf'] (required)
    Returns:
     - None

 - predict(models_folder, api_name="/reload_models_5") -> clip_l
    Parameters:
     - [Textbox] models_folder: str (not required, defaults to:   /kaggle/working/sd.cpp-webui/models/text_encoders/)
    Returns:
     - [Dropdown] clip_l: Literal['Qwen3-4B-Instruct-2507-Q4_K_M.gguf']

 - predict(api_name="/lambda_11") ->
    Parameters:
     - None
    Returns:
     - None

 - predict(x, api_name="/lambda_12") ->
    Parameters:
     - [Dropdown] x: Literal['Qwen3-4B-Instruct-2507-Q4_K_M.gguf'] (required)
    Returns:
     - None

 - predict(models_folder, api_name="/reload_models_6") -> t5xxl
    Parameters:
     - [Textbox] models_folder: str (not required, defaults to:   /kaggle/working/sd.cpp-webui/models/text_encoders/)
    Returns:
     - [Dropdown] t5xxl: Literal['Qwen3-4B-Instruct-2507-Q4_K_M.gguf']

 - predict(api_name="/lambda_13") ->
    Parameters:
     - None
    Returns:
     - None

 - predict(x, api_name="/lambda_14") ->
    Parameters:
     - [Dropdown] x: Literal['Qwen3-4B-Instruct-2507-Q4_K_M.gguf'] (required)
    Returns:
     - None

 - predict(models_folder, api_name="/reload_models_7") -> llm
    Parameters:
     - [Textbox] models_folder: str (not required, defaults to:   /kaggle/working/sd.cpp-webui/models/text_encoders/)
    Returns:
     - [Dropdown] llm: Literal['Qwen3-4B-Instruct-2507-Q4_K_M.gguf']

 - predict(api_name="/lambda_15") ->
    Parameters:
     - None
    Returns:
     - None

 - predict(x, api_name="/lambda_16") ->
    Parameters:
     - [Dropdown] x: Literal['Qwen3-4B-Instruct-2507-Q4_K_M.gguf'] (required)
    Returns:
     - None

 - predict(models_folder, api_name="/reload_models_8") -> llm_vision
    Parameters:
     - [Textbox] models_folder: str (not required, defaults to:   /kaggle/working/sd.cpp-webui/models/text_encoders/)
    Returns:
     - [Dropdown] llm_vision: Literal['Qwen3-4B-Instruct-2507-Q4_K_M.gguf']

 - predict(api_name="/lambda_17") ->
    Parameters:
     - None
    Returns:
     - None

 - predict(_, api_name="/lambda_18") -> lora
    Parameters:
     - [Textbox] _: str (not required, defaults to:   /kaggle/working/sd.cpp-webui/models/loras/)
    Returns:
     - [Dropdown] lora: Literal['[illustrious]NFFA10.3-000080.safetensors', '[illustrious]cunnyfunky3.3-000080.safetensors']

 - predict(name, p_prompt, n_prompt, api_name="/save_and_refresh_prompts") -> prompts
    Parameters:
     - [Textbox] name: str (required)
     - [Textbox] p_prompt: str (required)
     - [Textbox] n_prompt: str (required)
    Returns:
     - [Dropdown] prompts: Literal[]

 - predict(name, api_name="/delete_and_refresh_prompts") -> prompts
    Parameters:
     - [Dropdown] name: Literal[] (required)
    Returns:
     - [Dropdown] prompts: Literal[]

 - predict(api_name="/refresh_prompt_list") -> prompts
    Parameters:
     - None
    Returns:
     - [Dropdown] prompts: Literal[]

 - predict(name, api_name="/get_prompt") -> (positive_prompt, negative_prompt)
    Parameters:
     - [Dropdown] name: Literal[] (required)
    Returns:
     - [Textbox] positive_prompt: str
     - [Textbox] negative_prompt: str

 - predict(height, width, api_name="/switch_sizes") -> (height, width)
    Parameters:
     - [Slider] height: float (not required, defaults to:   1024)
     - [Slider] width: float (not required, defaults to:   1024)
    Returns:
     - [Slider] height: float (numeric value between 64 and 4096)
     - [Slider] width: float (numeric value between 64 and 4096)

 - predict(checkbox_value, api_name="/partial") -> flow_shift
    Parameters:
     - [Checkbox] checkbox_value: bool (not required, defaults to:   False)
    Returns:
     - [Number] flow_shift: float

 - predict(x, api_name="/lambda_19") ->
    Parameters:
     - [Checkbox] x: bool (not required, defaults to:   False)
    Returns:
     - None

 - predict(checkbox_value, api_name="/partial_1") -> guidance
    Parameters:
     - [Checkbox] checkbox_value: bool (not required, defaults to:   False)
    Returns:
     - [Slider] guidance: float (numeric value between 0 and 30)

 - predict(x, api_name="/lambda_20") ->
    Parameters:
     - [Checkbox] x: bool (not required, defaults to:   False)
    Returns:
     - None

 - predict(api_name="/random_seed") -> seed
    Parameters:
     - None
    Returns:
     - [Number] seed: float

 - predict(models_folder, api_name="/reload_models_9") -> upscaler
    Parameters:
     - [Textbox] models_folder: str (not required, defaults to:   /kaggle/working/sd.cpp-webui/models/upscale_models/)
    Returns:
     - [Dropdown] upscaler: Literal[]

 - predict(checkbox_value, api_name="/partial_2") -> (upscaler, upscaler_repeats)
    Parameters:
     - [Checkbox] checkbox_value: bool (not required, defaults to:   False)
    Returns:
     - [Dropdown] upscaler: Literal[]
     - [Slider] upscaler_repeats: float (numeric value between 1 and 5)

 - predict(models_folder, api_name="/reload_models_10") -> controlnet
    Parameters:
     - [Textbox] models_folder: str (not required, defaults to:   /kaggle/working/sd.cpp-webui/models/controlnet/)
    Returns:
     - [Dropdown] controlnet: Literal[]

 - predict(checkbox_value, api_name="/partial_3") -> (controlnet, value_215, controlnet_strength, controlnet_on_cpu, canny_edge_detection)
    Parameters:
     - [Checkbox] checkbox_value: bool (not required, defaults to:   False)
    Returns:
     - [Dropdown] controlnet: Literal[]
     - [Image] value_215: dict(path: str | None (Path to a local file), url: str | None (Publicly available url or base64 encoded image), size: int | None (Size of image in bytes), orig_name: str | None (Original filename), mime_type: str | None (mime type of image), is_stream: bool (Can always be set to False), meta: dict(str, Any))
     - [Slider] controlnet_strength: float (numeric value between 0 and 1)
     - [Checkbox] controlnet_on_cpu: bool
     - [Checkbox] canny_edge_detection: bool

 - predict(models_folder, api_name="/reload_models_11") -> photomaker
    Parameters:
     - [Textbox] models_folder: str (not required, defaults to:   /kaggle/working/sd.cpp-webui/models/photomaker/)
    Returns:
     - [Dropdown] photomaker: Literal[]

 - predict(checkbox_value, api_name="/partial_4") -> (photomaker, photomaker_input_id_images_directory, photomaker_v2_id_embed, photomaker_style_strength)
    Parameters:
     - [Checkbox] checkbox_value: bool (not required, defaults to:   False)
    Returns:
     - [Dropdown] photomaker: Literal[]
     - [Textbox] photomaker_input_id_images_directory: str
     - [Textbox] photomaker_v2_id_embed: str
     - [Slider] photomaker_style_strength: float (numeric value between 0 and 100)

 - predict(checkbox_value, api_name="/partial_5") -> timestep_shift
    Parameters:
     - [Checkbox] checkbox_value: bool (not required, defaults to:   False)
    Returns:
     - [Slider] timestep_shift: float (numeric value between 0 and 2000)

 - predict(checkbox_value, api_name="/partial_6") -> eta
    Parameters:
     - [Checkbox] checkbox_value: bool (not required, defaults to:   False)
    Returns:
     - [Number] eta: float

 - predict(models_folder, api_name="/reload_models_12") -> taesd
    Parameters:
     - [Textbox] models_folder: str (not required, defaults to:   /kaggle/working/sd.cpp-webui/models/taesd/)
    Returns:
     - [Dropdown] taesd: Literal[]

 - predict(checkbox_value, api_name="/partial_7") -> (vae_tile_overlap, vae_tile_size, enable_vae_relative_tile_size)
    Parameters:
     - [Checkbox] checkbox_value: bool (not required, defaults to:   False)
    Returns:
     - [Slider] vae_tile_overlap: float (numeric value between 0 and 1)
     - [Number] vae_tile_size: float
     - [Checkbox] enable_vae_relative_tile_size: bool

 - predict(checkbox_value, api_name="/partial_8") -> vae_relative_tile_size
    Parameters:
     - [Checkbox] checkbox_value: bool (not required, defaults to:   False)
    Returns:
     - [Number] vae_relative_tile_size: float

 - predict(checkbox_value, api_name="/partial_9") -> (cache_mode, cachedit_preset, cache_option, scm_mask, scm_policy)
    Parameters:
     - [Checkbox] checkbox_value: bool (not required, defaults to:   False)
    Returns:
     - [Dropdown] cache_mode: Literal['easycache', 'ucache', 'dbcache', 'taylorseer', 'cache-dit', 'spectrum']
     - [Dropdown] cachedit_preset: Literal['none', 'slow', 'medium', 'fast', 'ultra']
     - [Textbox] cache_option: str
     - [Textbox] scm_mask: str
     - [Dropdown] scm_policy: Literal['none', 'dynamic', 'static']

 - predict(checkbox_value, api_name="/partial_10") -> (preview_mode, preview_interval, taesd_for_preview_only, preview_noisy)
    Parameters:
     - [Checkbox] checkbox_value: bool (not required, defaults to:   False)
    Returns:
     - [Dropdown] preview_mode: Literal['none', 'proj', 'tae', 'vae']
     - [Number] preview_interval: float
     - [Checkbox] taesd_for_preview_only: bool
     - [Checkbox] preview_noisy: bool

 - predict(param_0, param_1, param_2, param_3, param_4, param_5, param_7, param_8, param_9, param_10, param_11, param_12, param_13, param_14, param_15, param_16, param_17, param_18, param_19, param_20, param_21, param_22, param_23, param_24, param_25, param_26, param_27, param_28, param_29, param_30, param_31, param_32, param_33, param_34, param_35, param_36, param_37, param_38, param_39, param_40, param_41, param_42, param_43, param_44, param_45, param_46, param_47, param_48, param_49, param_50, param_51, param_52, param_53, param_54, param_55, param_56, param_57, param_58, param_59, param_60, param_61, param_62, param_63, param_64, param_65, param_66, param_67, param_68, param_69, param_70, param_71, param_72, param_73, param_74, param_75, param_76, param_77, param_78, param_79, param_80, param_81, param_82, param_83, param_84, param_85, param_86, param_87, param_88, param_89, param_90, param_91, param_92, param_93, param_94, param_95, api_name="/submit_job") -> (progress, status)
    Parameters:
     - [Number] param_0: float (not required, defaults to:   0)
     - [Checkbox] param_1: bool (not required, defaults to:   False)
     - [Checkbox] param_2: bool (not required, defaults to:   False)
     - [Number] param_3: float (not required, defaults to:   0)
     - [Checkbox] param_4: bool (not required, defaults to:   False)
     - [Checkbox] param_5: bool (not required, defaults to:   False)
     - [Slider] param_7: float (not required, defaults to:   1)
     - [Checkbox] param_8: bool (not required, defaults to:   False)
     - [Dropdown] param_9: Literal['none', 'slow', 'medium', 'fast', 'ultra'] (not required, defaults to:   none)
     - [Dropdown] param_10: Literal['easycache', 'ucache', 'dbcache', 'taylorseer', 'cache-dit', 'spectrum'] (not required, defaults to:   easycache)
     - [Textbox] param_11: str (required)
     - [Checkbox] param_12: bool (not required, defaults to:   False)
     - [Slider] param_13: float (not required, defaults to:   1.0)
     - [Dropdown] param_14: Literal['None', 'Circular', 'Circular X', 'Circular Y'] (not required, defaults to:   None) 
     - [Dropdown] param_15: Literal['[illustrious]JANKUV5NSFWTrainedNoobai_v69.safetensors', '[illustrious]WAI-illustrious-SDXL.safetensors', '[illustrious]miaomiaoHarem_v195.safetensors', '[illustrious]miaomiaoRealskin_epsV14.safetensors'] (required)
     - [Dropdown] param_16: Literal['ae.safetensors'] (required)
     - [Checkbox] param_17: bool (not required, defaults to:   False)
     - [Dropdown] param_18: Literal['Qwen3-4B-Instruct-2507-Q4_K_M.gguf'] (required)
     - [Dropdown] param_19: Literal['Qwen3-4B-Instruct-2507-Q4_K_M.gguf'] (required)
     - [Slider] param_20: float (not required, defaults to:   -1)
     - [Dropdown] param_21: Literal[] (required)
     - [Checkbox] param_22: bool (not required, defaults to:   False)
     - [Checkbox] param_23: bool (not required, defaults to:   False)
     - [Checkbox] param_24: bool (not required, defaults to:   True)
     - [Image] param_25: dict(path: str | None (Path to a local file), url: str | None (Publicly available url or base64 encoded image), size: int | None (Size of image in bytes), orig_name: str | None (Original filename), mime_type: str | None (mime type of image), is_stream: bool (Can always be set to False), meta: dict(str, Any)) (required)  (For input, either path or url must be provided. For output, path is always provided.)
     - [Slider] param_26: float (not required, defaults to:   0.9)
     - [Checkbox] param_27: bool (not required, defaults to:   False)
     - [Checkbox] param_28: bool (not required, defaults to:   False)
     - [Number] param_29: float (not required, defaults to:   0)
     - [Checkbox] param_30: bool (not required, defaults to:   False)
     - [Checkbox] param_31: bool (not required, defaults to:   False)
     - [Checkbox] param_32: bool (not required, defaults to:   False)
     - [Number] param_33: float (not required, defaults to:   0)
     - [Checkbox] param_34: bool (not required, defaults to:   False)
     - [Checkbox] param_35: bool (not required, defaults to:   False)
     - [Number] param_36: float (not required, defaults to:   3.0)
     - [Checkbox] param_37: bool (not required, defaults to:   False)
     - [Checkbox] param_38: bool (not required, defaults to:   False)
     - [Slider] param_39: float (not required, defaults to:   3.5)
     - [Checkbox] param_40: bool (not required, defaults to:   False)
     - [Slider] param_41: float (not required, defaults to:   1024)
     - [Dropdown] param_42: Literal['Qwen3-4B-Instruct-2507-Q4_K_M.gguf'] (required)
     - [Dropdown] param_43: Literal['Qwen3-4B-Instruct-2507-Q4_K_M.gguf'] (required)
     - [Dropdown] param_44: Literal['auto', 'immediately', 'at_runtime'] (not required, defaults to:   auto)
     - [Dropdown] param_45: Literal['[illustrious]NFFA10.3-000080.safetensors', '[illustrious]cunnyfunky3.3-000080.safetensors'] (required)
     - [Radio] param_46: Literal['Positive', 'Negative'] (not required, defaults to:   Positive)
     - [Slider] param_47: float (not required, defaults to:   0.0)
     - [Checkbox] param_48: bool (not required, defaults to:   True)
     - [Dropdown] param_49: Literal['Default', 'f32', 'f16', 'q8_0', 'q6_K', 'q5_K', 'q5_1', 'q5_0', 'q4_K', 'q4_1', 'q4_0', 'q3_K', 'q2_K'] (not required, defaults to:   Default)
     - [Textbox] param_50: str (required)
     - [Checkbox] param_51: bool (not required, defaults to:   False)
     - [Textbox] param_52: str (not required, defaults to:   )
     - [Dropdown] param_53: Literal[] (not required, defaults to:   )
     - [Checkbox] param_54: bool (not required, defaults to:   False)
     - [Textbox] param_55: str (not required, defaults to:   )
     - [Textbox] param_56: str (not required, defaults to:   )
     - [Slider] param_57: float (not required, defaults to:   20)
     - [Textbox] param_58: str (required)
     - [Dropdown] param_59: Literal['Default', 'eps', 'v', 'edm_v', 'sd3_flow', 'flux_flow', 'flux2_flow'] (not required, defaults to:   Default)
     - [Checkbox] param_60: bool (not required, defaults to:   False)
     - [Number] param_61: float (not required, defaults to:   1)
     - [Dropdown] param_62: Literal['none', 'proj', 'tae', 'vae'] (not required, defaults to:   none)
     - [Checkbox] param_63: bool (not required, defaults to:   False)
     - [Checkbox] param_64: bool (not required, defaults to:   False)
     - [Dropdown] param_65: Literal['std_default', 'cuda', 'cpu'] (not required, defaults to:   cuda)
     - [Dropdown] param_66: Literal['std_default', 'cuda', 'cpu'] (not required, defaults to:   cuda)
     - [Dropdown] param_67: Literal['euler', 'euler_a', 'heun', 'dpm2', 'dpm++2s_a', 'dpm++2m', 'dpm++2mv2', 'ipndm', 'ipndm_v', 'lcm', 'ddim_trailing', 'tcd', 'res_multistep', 'res_2s'] (not required, defaults to:   euler)
     - [Dropdown] param_68: Literal['discrete', 'karras', 'exponential', 'ays', 'gits', 'smoothstep', 'sgm_uniform', 'simple', 'kl_optimal', 'lcm', 'bong_tangent'] (not required, defaults to:   discrete)
     - [Textbox] param_69: str (required)
     - [Dropdown] param_70: Literal['none', 'dynamic', 'static'] (not required, defaults to:   none)
     - [Number] param_71: float (not required, defaults to:   -1)
     - [Textbox] param_72: str (not required, defaults to:   )
     - [Slider] param_73: float (not required, defaults to:   8)
     - [Slider] param_74: float (not required, defaults to:   1)
     - [Dropdown] param_75: Literal['Qwen3-4B-Instruct-2507-Q4_K_M.gguf'] (required)
     - [Dropdown] param_76: Literal[] (required)
     - [Textbox] param_77: str (not required, defaults to:   )
     - [Number] param_78: float (not required, defaults to:   0)
     - [Slider] param_79: float (not required, defaults to:   0)
     - [Checkbox] param_80: bool (not required, defaults to:   False)
     - [Dropdown] param_81: Literal['z_image_turbo-Q8_0.gguf'] (required)
     - [Dropdown] param_82: Literal['ae.safetensors'] (required)
     - [Dropdown] param_83: Literal[] (not required, defaults to:   )
     - [Checkbox] param_84: bool (not required, defaults to:   False)
     - [Slider] param_85: float (not required, defaults to:   1)
     - [Checkbox] param_86: bool (not required, defaults to:   False)
     - [Checkbox] param_87: bool (not required, defaults to:   False)
     - [Checkbox] param_88: bool (not required, defaults to:   False)
     - [Number] param_89: float (not required, defaults to:   0)
     - [Slider] param_90: float (not required, defaults to:   0.5)
     - [Number] param_91: float (not required, defaults to:   32)
     - [Checkbox] param_92: bool (not required, defaults to:   False)
     - [Checkbox] param_93: bool (not required, defaults to:   False)
     - [Slider] param_94: float (not required, defaults to:   1024)
     - [Dropdown] param_95: Literal[] (required)
    Returns:
     - [Slider] progress: float (numeric value between 0 and 100)
     - [Textbox] status: str

 - predict(api_name="/poll_status") -> (stablediffusioncpp_command, progress, status, statistics, generated_images, value_377, value_361)
    Parameters:
     - None
    Returns:
     - [Textbox] stablediffusioncpp_command: str
     - [Slider] progress: float (numeric value between 0 and 100)
     - [Textbox] status: str
     - [Textbox] statistics: str
     - [Gallery] generated_images: list[dict(image: dict(path: str | None (Path to a local file), url: str | None (Publicly available url or base64 encoded image), size: int | None (Size of image in bytes), orig_name: str | None (Original filename), mime_type: str | None (mime type of image), is_stream: bool (Can always be set to False), meta: dict(str, Any)), caption: str | None) | dict(video: filepath, caption: str | None)]
     - [Timer] value_377: float
     - [Textbox] value_361: str

 - predict(api_name="/kill_subprocess") ->
    Parameters:
     - None
    Returns:
     - None

 - predict(lora_model, lora_strength, lora_prompt_switch, pprompt, nprompt, api_name="/apply_lora") -> (positive_prompt, negative_prompt)
    Parameters:
     - [Dropdown] lora_model: Literal['[illustrious]NFFA10.3-000080.safetensors', '[illustrious]cunnyfunky3.3-000080.safetensors'] (required)
     - [Slider] lora_strength: float (not required, defaults to:   0.0)
     - [Radio] lora_prompt_switch: Literal['Positive', 'Negative'] (not required, defaults to:   Positive)
     - [Textbox] pprompt: str (required)
     - [Textbox] nprompt: str (required)
    Returns:
     - [Textbox] positive_prompt: str
     - [Textbox] negative_prompt: str

 - predict(api_name="/ckpt_tab_switch") -> (value_3, checkpoint_model, unet_model, checkpoint_vae, unet_vae, clip_g, clip_l, t5xxl, llm, enable_distilled_guidance, guidance, enable_flow_shift, flow_shift)
    Parameters:
     - None
    Returns:
     - [Number] value_3: float
     - [Dropdown] checkpoint_model: Literal['[illustrious]JANKUV5NSFWTrainedNoobai_v69.safetensors', '[illustrious]WAI-illustrious-SDXL.safetensors', '[illustrious]miaomiaoHarem_v195.safetensors', '[illustrious]miaomiaoRealskin_epsV14.safetensors']
     - [Dropdown] unet_model: Literal['z_image_turbo-Q8_0.gguf']
     - [Dropdown] checkpoint_vae: Literal['ae.safetensors']
     - [Dropdown] unet_vae: Literal['ae.safetensors']
     - [Dropdown] clip_g: Literal['Qwen3-4B-Instruct-2507-Q4_K_M.gguf']
     - [Dropdown] clip_l: Literal['Qwen3-4B-Instruct-2507-Q4_K_M.gguf']
     - [Dropdown] t5xxl: Literal['Qwen3-4B-Instruct-2507-Q4_K_M.gguf']
     - [Dropdown] llm: Literal['Qwen3-4B-Instruct-2507-Q4_K_M.gguf']
     - [Checkbox] enable_distilled_guidance: bool
     - [Slider] guidance: float (numeric value between 0 and 30)
     - [Checkbox] enable_flow_shift: bool
     - [Number] flow_shift: float

 - predict(api_name="/unet_tab_switch") -> (value_3, checkpoint_model, unet_model, checkpoint_vae, unet_vae, clip_g, clip_l, t5xxl, llm, enable_distilled_guidance, guidance, enable_flow_shift, flow_shift)
    Parameters:
     - None
    Returns:
     - [Number] value_3: float
     - [Dropdown] checkpoint_model: Literal['[illustrious]JANKUV5NSFWTrainedNoobai_v69.safetensors', '[illustrious]WAI-illustrious-SDXL.safetensors', '[illustrious]miaomiaoHarem_v195.safetensors', '[illustrious]miaomiaoRealskin_epsV14.safetensors']
     - [Dropdown] unet_model: Literal['z_image_turbo-Q8_0.gguf']
     - [Dropdown] checkpoint_vae: Literal['ae.safetensors']
     - [Dropdown] unet_vae: Literal['ae.safetensors']
     - [Dropdown] clip_g: Literal['Qwen3-4B-Instruct-2507-Q4_K_M.gguf']
     - [Dropdown] clip_l: Literal['Qwen3-4B-Instruct-2507-Q4_K_M.gguf']
     - [Dropdown] t5xxl: Literal['Qwen3-4B-Instruct-2507-Q4_K_M.gguf']
     - [Dropdown] llm: Literal['Qwen3-4B-Instruct-2507-Q4_K_M.gguf']
     - [Checkbox] enable_distilled_guidance: bool
     - [Slider] guidance: float (numeric value between 0 and 30)
     - [Checkbox] enable_flow_shift: bool
     - [Number] flow_shift: float

 - predict(api_name="/refresh_all_options") -> (sampling_method, scheduler, preview_mode, prediction)
    Parameters:
     - None
    Returns:
     - [Dropdown] sampling_method: Literal['euler', 'euler_a', 'heun', 'dpm2', 'dpm++2s_a', 'dpm++2m', 'dpm++2mv2', 'ipndm', 'ipndm_v', 'lcm', 'ddim_trailing', 'tcd', 'res_multistep', 'res_2s']
     - [Dropdown] scheduler: Literal['discrete', 'karras', 'exponential', 'ays', 'gits', 'smoothstep', 'sgm_uniform', 'simple', 'kl_optimal', 'lcm', 'bong_tangent']
     - [Dropdown] preview_mode: Literal['none', 'proj', 'tae', 'vae']
     - [Dropdown] prediction: Literal['Default', 'eps', 'v', 'edm_v', 'sd3_flow', 'flux_flow', 'flux2_flow']

 - predict(x, api_name="/lambda_21") ->
    Parameters:
     - [Dropdown] x: Literal['[illustrious]JANKUV5NSFWTrainedNoobai_v69.safetensors', '[illustrious]WAI-illustrious-SDXL.safetensors', '[illustrious]miaomiaoHarem_v195.safetensors', '[illustrious]miaomiaoRealskin_epsV14.safetensors'] (required)
    Returns:
     - None

 - predict(models_folder, api_name="/reload_models_13") -> checkpoint_model
    Parameters:
     - [Textbox] models_folder: str (not required, defaults to:   /kaggle/working/sd.cpp-webui/models/checkpoints/)
    Returns:
     - [Dropdown] checkpoint_model: Literal['[illustrious]JANKUV5NSFWTrainedNoobai_v69.safetensors', '[illustrious]WAI-illustrious-SDXL.safetensors', '[illustrious]miaomiaoHarem_v195.safetensors', '[illustrious]miaomiaoRealskin_epsV14.safetensors']

 - predict(api_name="/lambda_1_1") ->
    Parameters:
     - None
    Returns:
     - None

 - predict(x, api_name="/lambda_2_1") ->
    Parameters:
     - [Dropdown] x: Literal['ae.safetensors'] (required)
    Returns:
     - None

 - predict(models_folder, api_name="/reload_models_1_1") -> checkpoint_vae
    Parameters:
     - [Textbox] models_folder: str (not required, defaults to:   /kaggle/working/sd.cpp-webui/models/vae/)
    Returns:
     - [Dropdown] checkpoint_vae: Literal['ae.safetensors']

 - predict(api_name="/lambda_3_1") ->
    Parameters:
     - None
    Returns:
     - None

 - predict(x, api_name="/lambda_4_1") ->
    Parameters:
     - [Dropdown] x: Literal['z_image_turbo-Q8_0.gguf'] (required)
    Returns:
     - None

 - predict(models_folder, api_name="/reload_models_2_1") -> unet_model
    Parameters:
     - [Textbox] models_folder: str (not required, defaults to:   /kaggle/working/sd.cpp-webui/models/unet/)
    Returns:
     - [Dropdown] unet_model: Literal['z_image_turbo-Q8_0.gguf']

 - predict(api_name="/lambda_5_1") ->
    Parameters:
     - None
    Returns:
     - None

 - predict(x, api_name="/lambda_6_1") ->
    Parameters:
     - [Dropdown] x: Literal['ae.safetensors'] (required)
    Returns:
     - None

 - predict(models_folder, api_name="/reload_models_3_1") -> unet_vae
    Parameters:
     - [Textbox] models_folder: str (not required, defaults to:   /kaggle/working/sd.cpp-webui/models/vae/)
    Returns:
     - [Dropdown] unet_vae: Literal['ae.safetensors']

 - predict(api_name="/lambda_7_1") ->
    Parameters:
     - None
    Returns:
     - None

 - predict(x, api_name="/lambda_8_1") ->
    Parameters:
     - [Dropdown] x: Literal['Qwen3-4B-Instruct-2507-Q4_K_M.gguf'] (required)
    Returns:
     - None

 - predict(models_folder, api_name="/reload_models_4_1") -> clip_g
    Parameters:
     - [Textbox] models_folder: str (not required, defaults to:   /kaggle/working/sd.cpp-webui/models/text_encoders/)
    Returns:
     - [Dropdown] clip_g: Literal['Qwen3-4B-Instruct-2507-Q4_K_M.gguf']

 - predict(api_name="/lambda_9_1") ->
    Parameters:
     - None
    Returns:
     - None

 - predict(x, api_name="/lambda_10_1") ->
    Parameters:
     - [Dropdown] x: Literal['Qwen3-4B-Instruct-2507-Q4_K_M.gguf'] (required)
    Returns:
     - None

 - predict(models_folder, api_name="/reload_models_5_1") -> clip_l
    Parameters:
     - [Textbox] models_folder: str (not required, defaults to:   /kaggle/working/sd.cpp-webui/models/text_encoders/)
    Returns:
     - [Dropdown] clip_l: Literal['Qwen3-4B-Instruct-2507-Q4_K_M.gguf']

 - predict(api_name="/lambda_11_1") ->
    Parameters:
     - None
    Returns:
     - None

 - predict(x, api_name="/lambda_12_1") ->
    Parameters:
     - [Dropdown] x: Literal['Qwen3-4B-Instruct-2507-Q4_K_M.gguf'] (required)
    Returns:
     - None

 - predict(models_folder, api_name="/reload_models_6_1") -> t5xxl
    Parameters:
     - [Textbox] models_folder: str (not required, defaults to:   /kaggle/working/sd.cpp-webui/models/text_encoders/)
    Returns:
     - [Dropdown] t5xxl: Literal['Qwen3-4B-Instruct-2507-Q4_K_M.gguf']

 - predict(api_name="/lambda_13_1") ->
    Parameters:
     - None
    Returns:
     - None

 - predict(x, api_name="/lambda_14_1") ->
    Parameters:
     - [Dropdown] x: Literal['Qwen3-4B-Instruct-2507-Q4_K_M.gguf'] (required)
    Returns:
     - None

 - predict(models_folder, api_name="/reload_models_7_1") -> llm
    Parameters:
     - [Textbox] models_folder: str (not required, defaults to:   /kaggle/working/sd.cpp-webui/models/text_encoders/)
    Returns:
     - [Dropdown] llm: Literal['Qwen3-4B-Instruct-2507-Q4_K_M.gguf']

 - predict(api_name="/lambda_15_1") ->
    Parameters:
     - None
    Returns:
     - None

 - predict(x, api_name="/lambda_16_1") ->
    Parameters:
     - [Dropdown] x: Literal['Qwen3-4B-Instruct-2507-Q4_K_M.gguf'] (required)
    Returns:
     - None

 - predict(models_folder, api_name="/reload_models_8_1") -> llm_vision
    Parameters:
     - [Textbox] models_folder: str (not required, defaults to:   /kaggle/working/sd.cpp-webui/models/text_encoders/)
    Returns:
     - [Dropdown] llm_vision: Literal['Qwen3-4B-Instruct-2507-Q4_K_M.gguf']

 - predict(api_name="/lambda_17_1") ->
    Parameters:
     - None
    Returns:
     - None

 - predict(_, api_name="/lambda_18_1") -> lora
    Parameters:
     - [Textbox] _: str (not required, defaults to:   /kaggle/working/sd.cpp-webui/models/loras/)
    Returns:
     - [Dropdown] lora: Literal['[illustrious]NFFA10.3-000080.safetensors', '[illustrious]cunnyfunky3.3-000080.safetensors']

 - predict(name, p_prompt, n_prompt, api_name="/save_and_refresh_prompts_1") -> prompts
    Parameters:
     - [Textbox] name: str (required)
     - [Textbox] p_prompt: str (required)
     - [Textbox] n_prompt: str (required)
    Returns:
     - [Dropdown] prompts: Literal[]

 - predict(name, api_name="/delete_and_refresh_prompts_1") -> prompts
    Parameters:
     - [Dropdown] name: Literal[] (required)
    Returns:
     - [Dropdown] prompts: Literal[]

 - predict(api_name="/refresh_prompt_list_1") -> prompts
    Parameters:
     - None
    Returns:
     - [Dropdown] prompts: Literal[]

 - predict(name, api_name="/get_prompt_1") -> (positive_prompt, negative_prompt)
    Parameters:
     - [Dropdown] name: Literal[] (required)
    Returns:
     - [Textbox] positive_prompt: str
     - [Textbox] negative_prompt: str

 - predict(height, width, api_name="/switch_sizes_1") -> (height, width)
    Parameters:
     - [Slider] height: float (not required, defaults to:   1024)
     - [Slider] width: float (not required, defaults to:   1024)
    Returns:
     - [Slider] height: float (numeric value between 64 and 4096)
     - [Slider] width: float (numeric value between 64 and 4096)

 - predict(checkbox_value, api_name="/partial_11") -> image_cfg_inpaint_or_instructpix2pix_models
    Parameters:
     - [Checkbox] checkbox_value: bool (not required, defaults to:   False)
    Returns:
     - [Slider] image_cfg_inpaint_or_instructpix2pix_models: float (numeric value between 1 and 30)

 - predict(x, api_name="/lambda_19_1") ->
    Parameters:
     - [Checkbox] x: bool (not required, defaults to:   False)
    Returns:
     - None

 - predict(checkbox_value, api_name="/partial_1_1") -> guidance
    Parameters:
     - [Checkbox] checkbox_value: bool (not required, defaults to:   False)
    Returns:
     - [Slider] guidance: float (numeric value between 0 and 30)

 - predict(x, api_name="/lambda_20_1") ->
    Parameters:
     - [Checkbox] x: bool (not required, defaults to:   False)
    Returns:
     - None

 - predict(api_name="/random_seed_1") -> seed
    Parameters:
     - None
    Returns:
     - [Number] seed: float

 - predict(models_folder, api_name="/reload_models_9_1") -> upscaler
    Parameters:
     - [Textbox] models_folder: str (not required, defaults to:   /kaggle/working/sd.cpp-webui/models/upscale_models/)
    Returns:
     - [Dropdown] upscaler: Literal[]

 - predict(checkbox_value, api_name="/partial_2_1") -> (upscaler, upscaler_repeats)
    Parameters:
     - [Checkbox] checkbox_value: bool (not required, defaults to:   False)
    Returns:
     - [Dropdown] upscaler: Literal[]
     - [Slider] upscaler_repeats: float (numeric value between 1 and 5)

 - predict(models_folder, api_name="/reload_models_10_1") -> controlnet
    Parameters:
     - [Textbox] models_folder: str (not required, defaults to:   /kaggle/working/sd.cpp-webui/models/controlnet/)
    Returns:
     - [Dropdown] controlnet: Literal[]

 - predict(checkbox_value, api_name="/partial_3_1") -> (controlnet, value_990, controlnet_strength, controlnet_on_cpu, canny_edge_detection)
    Parameters:
     - [Checkbox] checkbox_value: bool (not required, defaults to:   False)
    Returns:
     - [Dropdown] controlnet: Literal[]
     - [Image] value_990: dict(path: str | None (Path to a local file), url: str | None (Publicly available url or base64 encoded image), size: int | None (Size of image in bytes), orig_name: str | None (Original filename), mime_type: str | None (mime type of image), is_stream: bool (Can always be set to False), meta: dict(str, Any))
     - [Slider] controlnet_strength: float (numeric value between 0 and 1)
     - [Checkbox] controlnet_on_cpu: bool
     - [Checkbox] canny_edge_detection: bool

 - predict(models_folder, api_name="/reload_models_11_1") -> photomaker
    Parameters:
     - [Textbox] models_folder: str (not required, defaults to:   /kaggle/working/sd.cpp-webui/models/photomaker/)
    Returns:
     - [Dropdown] photomaker: Literal[]

 - predict(checkbox_value, api_name="/partial_4_1") -> (photomaker, photomaker_input_id_images_directory, photomaker_v2_id_embed, photomaker_style_strength)
    Parameters:
     - [Checkbox] checkbox_value: bool (not required, defaults to:   False)
    Returns:
     - [Dropdown] photomaker: Literal[]
     - [Textbox] photomaker_input_id_images_directory: str
     - [Textbox] photomaker_v2_id_embed: str
     - [Slider] photomaker_style_strength: float (numeric value between 0 and 100)

 - predict(checkbox_value, api_name="/partial_5_1") -> timestep_shift
    Parameters:
     - [Checkbox] checkbox_value: bool (not required, defaults to:   False)
    Returns:
     - [Slider] timestep_shift: float (numeric value between 0 and 2000)

 - predict(checkbox_value, api_name="/partial_6_1") -> eta
    Parameters:
     - [Checkbox] checkbox_value: bool (not required, defaults to:   False)
    Returns:
     - [Number] eta: float

 - predict(models_folder, api_name="/reload_models_12_1") -> taesd
    Parameters:
     - [Textbox] models_folder: str (not required, defaults to:   /kaggle/working/sd.cpp-webui/models/taesd/)
    Returns:
     - [Dropdown] taesd: Literal[]

 - predict(checkbox_value, api_name="/partial_7_1") -> (vae_tile_overlap, vae_tile_size, enable_vae_relative_tile_size)
    Parameters:
     - [Checkbox] checkbox_value: bool (not required, defaults to:   False)
    Returns:
     - [Slider] vae_tile_overlap: float (numeric value between 0 and 1)
     - [Number] vae_tile_size: float
     - [Checkbox] enable_vae_relative_tile_size: bool

 - predict(checkbox_value, api_name="/partial_8_1") -> vae_relative_tile_size
    Parameters:
     - [Checkbox] checkbox_value: bool (not required, defaults to:   False)
    Returns:
     - [Number] vae_relative_tile_size: float

 - predict(checkbox_value, api_name="/partial_9_1") -> (cache_mode, cachedit_preset, cache_option, scm_mask, scm_policy)
    Parameters:
     - [Checkbox] checkbox_value: bool (not required, defaults to:   False)
    Returns:
     - [Dropdown] cache_mode: Literal['easycache', 'ucache', 'dbcache', 'taylorseer', 'cache-dit', 'spectrum']
     - [Dropdown] cachedit_preset: Literal['none', 'slow', 'medium', 'fast', 'ultra']
     - [Textbox] cache_option: str
     - [Textbox] scm_mask: str
     - [Dropdown] scm_policy: Literal['none', 'dynamic', 'static']

 - predict(checkbox_value, api_name="/partial_10_1") -> (preview_mode, preview_interval, taesd_for_preview_only, preview_noisy)
    Parameters:
     - [Checkbox] checkbox_value: bool (not required, defaults to:   False)
    Returns:
     - [Dropdown] preview_mode: Literal['none', 'proj', 'tae', 'vae']
     - [Number] preview_interval: float
     - [Checkbox] taesd_for_preview_only: bool
     - [Checkbox] preview_noisy: bool

 - predict(param_0, param_1, param_2, param_3, param_4, param_5, param_7, param_8, param_9, param_10, param_11, param_12, param_13, param_14, param_15, param_16, param_17, param_18, param_19, param_20, param_21, param_22, param_23, param_24, param_25, param_26, param_27, param_28, param_29, param_30, param_31, param_32, param_33, param_34, param_35, param_36, param_37, param_38, param_39, param_40, param_41, param_42, param_43, param_44, param_45, param_46, param_47, param_48, param_49, param_50, param_51, param_52, param_53, param_54, param_55, param_56, param_57, param_58, param_59, param_60, param_61, param_62, param_63, param_64, param_65, param_66, param_67, param_68, param_69, param_70, param_71, param_72, param_73, param_74, param_75, param_76, param_77, param_78, param_79, param_80, param_81, param_82, param_83, param_84, param_85, param_86, param_87, param_88, param_89, param_90, param_91, param_92, param_93, param_94, param_95, param_96, param_97, param_98, api_name="/submit_job_1") -> (progress, progress)
    Parameters:
     - [Number] param_0: float (not required, defaults to:   0)
     - [Checkbox] param_1: bool (not required, defaults to:   False)
     - [Checkbox] param_2: bool (not required, defaults to:   False)
     - [Number] param_3: float (not required, defaults to:   0)
     - [Checkbox] param_4: bool (not required, defaults to:   False)
     - [Checkbox] param_5: bool (not required, defaults to:   False)
     - [Slider] param_7: float (not required, defaults to:   1)
     - [Checkbox] param_8: bool (not required, defaults to:   False)
     - [Dropdown] param_9: Literal['none', 'slow', 'medium', 'fast', 'ultra'] (not required, defaults to:   none)
     - [Dropdown] param_10: Literal['easycache', 'ucache', 'dbcache', 'taylorseer', 'cache-dit', 'spectrum'] (not required, defaults to:   easycache)
     - [Textbox] param_11: str (required)
     - [Checkbox] param_12: bool (not required, defaults to:   False)
     - [Slider] param_13: float (not required, defaults to:   1.0)
     - [Dropdown] param_14: Literal['None', 'Circular', 'Circular X', 'Circular Y'] (not required, defaults to:   None) 
     - [Dropdown] param_15: Literal['[illustrious]JANKUV5NSFWTrainedNoobai_v69.safetensors', '[illustrious]WAI-illustrious-SDXL.safetensors', '[illustrious]miaomiaoHarem_v195.safetensors', '[illustrious]miaomiaoRealskin_epsV14.safetensors'] (required)
     - [Dropdown] param_16: Literal['ae.safetensors'] (required)
     - [Checkbox] param_17: bool (not required, defaults to:   False)
     - [Dropdown] param_18: Literal['Qwen3-4B-Instruct-2507-Q4_K_M.gguf'] (required)
     - [Dropdown] param_19: Literal['Qwen3-4B-Instruct-2507-Q4_K_M.gguf'] (required)
     - [Slider] param_20: float (not required, defaults to:   -1)
     - [Dropdown] param_21: Literal[] (required)
     - [Checkbox] param_22: bool (not required, defaults to:   False)
     - [Checkbox] param_23: bool (not required, defaults to:   False)
     - [Checkbox] param_24: bool (not required, defaults to:   True)
     - [Image] param_25: dict(path: str | None (Path to a local file), url: str | None (Publicly available url or base64 encoded image), size: int | None (Size of image in bytes), orig_name: str | None (Original filename), mime_type: str | None (mime type of image), is_stream: bool (Can always be set to False), meta: dict(str, Any)) (required)  (For input, either path or url must be provided. For output, path is always provided.)
     - [Slider] param_26: float (not required, defaults to:   0.9)
     - [Checkbox] param_27: bool (not required, defaults to:   False)
     - [Checkbox] param_28: bool (not required, defaults to:   False)
     - [Number] param_29: float (not required, defaults to:   0)
     - [Checkbox] param_30: bool (not required, defaults to:   False)
     - [Checkbox] param_31: bool (not required, defaults to:   False)
     - [Checkbox] param_32: bool (not required, defaults to:   False)
     - [Number] param_33: float (not required, defaults to:   0)
     - [Checkbox] param_34: bool (not required, defaults to:   False)
     - [Checkbox] param_35: bool (not required, defaults to:   False)
     - [Number] param_36: float (not required, defaults to:   3.0)
     - [Checkbox] param_37: bool (not required, defaults to:   False)
     - [Checkbox] param_38: bool (not required, defaults to:   False)
     - [Slider] param_39: float (not required, defaults to:   3.5)
     - [Checkbox] param_40: bool (not required, defaults to:   False)
     - [Slider] param_41: float (not required, defaults to:   1024)
     - [Slider] param_42: float (not required, defaults to:   7.0)
     - [Image] param_43: dict(path: str | None (Path to a local file), url: str | None (Publicly available url or base64 encoded image), size: int | None (Size of image in bytes), orig_name: str | None (Original filename), mime_type: str | None (mime type of image), is_stream: bool (Can always be set to False), meta: dict(str, Any)) (required)  (For input, either path or url must be provided. For output, path is always provided.)
     - [Dropdown] param_44: Literal['Qwen3-4B-Instruct-2507-Q4_K_M.gguf'] (required)
     - [Dropdown] param_45: Literal['Qwen3-4B-Instruct-2507-Q4_K_M.gguf'] (required)
     - [Dropdown] param_46: Literal['auto', 'immediately', 'at_runtime'] (not required, defaults to:   auto)
     - [Dropdown] param_47: Literal['[illustrious]NFFA10.3-000080.safetensors', '[illustrious]cunnyfunky3.3-000080.safetensors'] (required)
     - [Radio] param_48: Literal['Positive', 'Negative'] (not required, defaults to:   Positive)
     - [Slider] param_49: float (not required, defaults to:   0.0)
     - [Checkbox] param_50: bool (not required, defaults to:   True)
     - [Dropdown] param_51: Literal['Default', 'f32', 'f16', 'q8_0', 'q6_K', 'q5_K', 'q5_1', 'q5_0', 'q4_K', 'q4_1', 'q4_0', 'q3_K', 'q2_K'] (not required, defaults to:   Default)
     - [Textbox] param_52: str (required)
     - [Checkbox] param_53: bool (not required, defaults to:   False)
     - [Textbox] param_54: str (not required, defaults to:   )
     - [Dropdown] param_55: Literal[] (not required, defaults to:   )
     - [Checkbox] param_56: bool (not required, defaults to:   False)
     - [Textbox] param_57: str (not required, defaults to:   )
     - [Textbox] param_58: str (not required, defaults to:   )
     - [Slider] param_59: float (not required, defaults to:   20)
     - [Textbox] param_60: str (required)
     - [Dropdown] param_61: Literal['Default', 'eps', 'v', 'edm_v', 'sd3_flow', 'flux_flow', 'flux2_flow'] (not required, defaults to:   Default)
     - [Checkbox] param_62: bool (not required, defaults to:   False)
     - [Number] param_63: float (not required, defaults to:   1)
     - [Dropdown] param_64: Literal['none', 'proj', 'tae', 'vae'] (not required, defaults to:   none)
     - [Checkbox] param_65: bool (not required, defaults to:   False)
     - [Checkbox] param_66: bool (not required, defaults to:   False)
     - [Dropdown] param_67: Literal['std_default', 'cuda', 'cpu'] (not required, defaults to:   cuda)
     - [Dropdown] param_68: Literal['std_default', 'cuda', 'cpu'] (not required, defaults to:   cuda)
     - [Dropdown] param_69: Literal['euler', 'euler_a', 'heun', 'dpm2', 'dpm++2s_a', 'dpm++2m', 'dpm++2mv2', 'ipndm', 'ipndm_v', 'lcm', 'ddim_trailing', 'tcd', 'res_multistep', 'res_2s'] (not required, defaults to:   euler)
     - [Dropdown] param_70: Literal['discrete', 'karras', 'exponential', 'ays', 'gits', 'smoothstep', 'sgm_uniform', 'simple', 'kl_optimal', 'lcm', 'bong_tangent'] (not required, defaults to:   discrete)
     - [Textbox] param_71: str (required)
     - [Dropdown] param_72: Literal['none', 'dynamic', 'static'] (not required, defaults to:   none)
     - [Number] param_73: float (not required, defaults to:   -1)
     - [Textbox] param_74: str (not required, defaults to:   )
     - [Slider] param_75: float (not required, defaults to:   8)
     - [Slider] param_76: float (not required, defaults to:   0.75)
     - [Slider] param_77: float (not required, defaults to:   1)
     - [Dropdown] param_78: Literal['Qwen3-4B-Instruct-2507-Q4_K_M.gguf'] (required)
     - [Dropdown] param_79: Literal[] (required)
     - [Textbox] param_80: str (not required, defaults to:   )
     - [Number] param_81: float (not required, defaults to:   0)
     - [Slider] param_82: float (not required, defaults to:   0)
     - [Checkbox] param_83: bool (not required, defaults to:   False)
     - [Dropdown] param_84: Literal['z_image_turbo-Q8_0.gguf'] (required)
     - [Dropdown] param_85: Literal['ae.safetensors'] (required)
     - [Dropdown] param_86: Literal[] (not required, defaults to:   )
     - [Checkbox] param_87: bool (not required, defaults to:   False)
     - [Slider] param_88: float (not required, defaults to:   1)
     - [Checkbox] param_89: bool (not required, defaults to:   False)
     - [Checkbox] param_90: bool (not required, defaults to:   False)
     - [Checkbox] param_91: bool (not required, defaults to:   False)
     - [Number] param_92: float (not required, defaults to:   0)
     - [Slider] param_93: float (not required, defaults to:   0.5)
     - [Number] param_94: float (not required, defaults to:   32)
     - [Checkbox] param_95: bool (not required, defaults to:   False)
     - [Checkbox] param_96: bool (not required, defaults to:   False)
     - [Slider] param_97: float (not required, defaults to:   1024)
     - [Dropdown] param_98: Literal[] (required)
    Returns:
     - [Slider] progress: float (numeric value between 0 and 100)
     - [Textbox] progress: str

 - predict(api_name="/poll_status_1") -> (stablediffusioncpp_command, progress, progress, statistics, generated_images, value_1154, value_1138)
    Parameters:
     - None
    Returns:
     - [Textbox] stablediffusioncpp_command: str
     - [Slider] progress: float (numeric value between 0 and 100)
     - [Textbox] progress: str
     - [Textbox] statistics: str
     - [Gallery] generated_images: list[dict(image: dict(path: str | None (Path to a local file), url: str | None (Publicly available url or base64 encoded image), size: int | None (Size of image in bytes), orig_name: str | None (Original filename), mime_type: str | None (mime type of image), is_stream: bool (Can always be set to False), meta: dict(str, Any)), caption: str | None) | dict(video: filepath, caption: str | None)]
     - [Timer] value_1154: float
     - [Textbox] value_1138: str

 - predict(api_name="/kill_subprocess_1") ->
    Parameters:
     - None
    Returns:
     - None

 - predict(lora_model, lora_strength, lora_prompt_switch, pprompt, nprompt, api_name="/apply_lora_1") -> (positive_prompt, negative_prompt)
    Parameters:
     - [Dropdown] lora_model: Literal['[illustrious]NFFA10.3-000080.safetensors', '[illustrious]cunnyfunky3.3-000080.safetensors'] (required)
     - [Slider] lora_strength: float (not required, defaults to:   0.0)
     - [Radio] lora_prompt_switch: Literal['Positive', 'Negative'] (not required, defaults to:   Positive)
     - [Textbox] pprompt: str (required)
     - [Textbox] nprompt: str (required)
    Returns:
     - [Textbox] positive_prompt: str
     - [Textbox] negative_prompt: str

 - predict(api_name="/ckpt_tab_switch_1") -> (value_771, checkpoint_model, unet_model, checkpoint_vae, unet_vae, clip_g, clip_l, t5xxl, llm, enable_distilled_guidance, guidance, enable_flow_shift, flow_shift)
    Parameters:
     - None
    Returns:
     - [Number] value_771: float
     - [Dropdown] checkpoint_model: Literal['[illustrious]JANKUV5NSFWTrainedNoobai_v69.safetensors', '[illustrious]WAI-illustrious-SDXL.safetensors', '[illustrious]miaomiaoHarem_v195.safetensors', '[illustrious]miaomiaoRealskin_epsV14.safetensors']
     - [Dropdown] unet_model: Literal['z_image_turbo-Q8_0.gguf']
     - [Dropdown] checkpoint_vae: Literal['ae.safetensors']
     - [Dropdown] unet_vae: Literal['ae.safetensors']
     - [Dropdown] clip_g: Literal['Qwen3-4B-Instruct-2507-Q4_K_M.gguf']
     - [Dropdown] clip_l: Literal['Qwen3-4B-Instruct-2507-Q4_K_M.gguf']
     - [Dropdown] t5xxl: Literal['Qwen3-4B-Instruct-2507-Q4_K_M.gguf']
     - [Dropdown] llm: Literal['Qwen3-4B-Instruct-2507-Q4_K_M.gguf']
     - [Checkbox] enable_distilled_guidance: bool
     - [Slider] guidance: float (numeric value between 0 and 30)
     - [Checkbox] enable_flow_shift: bool
     - [Number] flow_shift: float

 - predict(api_name="/unet_tab_switch_1") -> (value_771, checkpoint_model, unet_model, checkpoint_vae, unet_vae, clip_g, clip_l, t5xxl, llm, enable_distilled_guidance, guidance, enable_flow_shift, flow_shift)
    Parameters:
     - None
    Returns:
     - [Number] value_771: float
     - [Dropdown] checkpoint_model: Literal['[illustrious]JANKUV5NSFWTrainedNoobai_v69.safetensors', '[illustrious]WAI-illustrious-SDXL.safetensors', '[illustrious]miaomiaoHarem_v195.safetensors', '[illustrious]miaomiaoRealskin_epsV14.safetensors']
     - [Dropdown] unet_model: Literal['z_image_turbo-Q8_0.gguf']
     - [Dropdown] checkpoint_vae: Literal['ae.safetensors']
     - [Dropdown] unet_vae: Literal['ae.safetensors']
     - [Dropdown] clip_g: Literal['Qwen3-4B-Instruct-2507-Q4_K_M.gguf']
     - [Dropdown] clip_l: Literal['Qwen3-4B-Instruct-2507-Q4_K_M.gguf']
     - [Dropdown] t5xxl: Literal['Qwen3-4B-Instruct-2507-Q4_K_M.gguf']
     - [Dropdown] llm: Literal['Qwen3-4B-Instruct-2507-Q4_K_M.gguf']
     - [Checkbox] enable_distilled_guidance: bool
     - [Slider] guidance: float (numeric value between 0 and 30)
     - [Checkbox] enable_flow_shift: bool
     - [Number] flow_shift: float

 - predict(api_name="/refresh_all_options_1") -> (sampling_method, scheduler, preview_mode, prediction)
    Parameters:
     - None
    Returns:
     - [Dropdown] sampling_method: Literal['euler', 'euler_a', 'heun', 'dpm2', 'dpm++2s_a', 'dpm++2m', 'dpm++2mv2', 'ipndm', 'ipndm_v', 'lcm', 'ddim_trailing', 'tcd', 'res_multistep', 'res_2s']
     - [Dropdown] scheduler: Literal['discrete', 'karras', 'exponential', 'ays', 'gits', 'smoothstep', 'sgm_uniform', 'simple', 'kl_optimal', 'lcm', 'bong_tangent']
     - [Dropdown] preview_mode: Literal['none', 'proj', 'tae', 'vae']
     - [Dropdown] prediction: Literal['Default', 'eps', 'v', 'edm_v', 'sd3_flow', 'flux_flow', 'flux2_flow']

 - predict(x, api_name="/lambda_22") ->
    Parameters:
     - [Dropdown] x: Literal['z_image_turbo-Q8_0.gguf'] (required)
    Returns:
     - None

 - predict(models_folder, api_name="/reload_models_14") -> unet_model
    Parameters:
     - [Textbox] models_folder: str (not required, defaults to:   /kaggle/working/sd.cpp-webui/models/unet/)
    Returns:
     - [Dropdown] unet_model: Literal['z_image_turbo-Q8_0.gguf']

 - predict(api_name="/lambda_1_2") ->
    Parameters:
     - None
    Returns:
     - None

 - predict(x, api_name="/lambda_2_2") ->
    Parameters:
     - [Dropdown] x: Literal['ae.safetensors'] (required)
    Returns:
     - None

 - predict(models_folder, api_name="/reload_models_1_2") -> unet_vae
    Parameters:
     - [Textbox] models_folder: str (not required, defaults to:   /kaggle/working/sd.cpp-webui/models/vae/)
    Returns:
     - [Dropdown] unet_vae: Literal['ae.safetensors']

 - predict(api_name="/lambda_3_2") ->
    Parameters:
     - None
    Returns:
     - None

 - predict(x, api_name="/lambda_4_2") ->
    Parameters:
     - [Dropdown] x: Literal['Qwen3-4B-Instruct-2507-Q4_K_M.gguf'] (required)
    Returns:
     - None

 - predict(models_folder, api_name="/reload_models_2_2") -> clip_l
    Parameters:
     - [Textbox] models_folder: str (not required, defaults to:   /kaggle/working/sd.cpp-webui/models/text_encoders/)
    Returns:
     - [Dropdown] clip_l: Literal['Qwen3-4B-Instruct-2507-Q4_K_M.gguf']

 - predict(api_name="/lambda_5_2") ->
    Parameters:
     - None
    Returns:
     - None

 - predict(x, api_name="/lambda_6_2") ->
    Parameters:
     - [Dropdown] x: Literal['Qwen3-4B-Instruct-2507-Q4_K_M.gguf'] (required)
    Returns:
     - None

 - predict(models_folder, api_name="/reload_models_3_2") -> t5xxl
    Parameters:
     - [Textbox] models_folder: str (not required, defaults to:   /kaggle/working/sd.cpp-webui/models/text_encoders/)
    Returns:
     - [Dropdown] t5xxl: Literal['Qwen3-4B-Instruct-2507-Q4_K_M.gguf']

 - predict(api_name="/lambda_7_2") ->
    Parameters:
     - None
    Returns:
     - None

 - predict(x, api_name="/lambda_8_2") ->
    Parameters:
     - [Dropdown] x: Literal['Qwen3-4B-Instruct-2507-Q4_K_M.gguf'] (required)
    Returns:
     - None

 - predict(models_folder, api_name="/reload_models_4_2") -> llm
    Parameters:
     - [Textbox] models_folder: str (not required, defaults to:   /kaggle/working/sd.cpp-webui/models/text_encoders/)
    Returns:
     - [Dropdown] llm: Literal['Qwen3-4B-Instruct-2507-Q4_K_M.gguf']

 - predict(api_name="/lambda_9_2") ->
    Parameters:
     - None
    Returns:
     - None

 - predict(x, api_name="/lambda_10_2") ->
    Parameters:
     - [Dropdown] x: Literal['Qwen3-4B-Instruct-2507-Q4_K_M.gguf'] (required)
    Returns:
     - None

 - predict(models_folder, api_name="/reload_models_5_2") -> llm_vision
    Parameters:
     - [Textbox] models_folder: str (not required, defaults to:   /kaggle/working/sd.cpp-webui/models/text_encoders/)
    Returns:
     - [Dropdown] llm_vision: Literal['Qwen3-4B-Instruct-2507-Q4_K_M.gguf']

 - predict(api_name="/lambda_11_2") ->
    Parameters:
     - None
    Returns:
     - None

 - predict(_, api_name="/lambda_12_2") -> lora
    Parameters:
     - [Textbox] _: str (not required, defaults to:   /kaggle/working/sd.cpp-webui/models/loras/)
    Returns:
     - [Dropdown] lora: Literal['[illustrious]NFFA10.3-000080.safetensors', '[illustrious]cunnyfunky3.3-000080.safetensors']

 - predict(name, p_prompt, n_prompt, api_name="/save_and_refresh_prompts_2") -> prompts
    Parameters:
     - [Textbox] name: str (required)
     - [Textbox] p_prompt: str (required)
     - [Textbox] n_prompt: str (required)
    Returns:
     - [Dropdown] prompts: Literal[]

 - predict(name, api_name="/delete_and_refresh_prompts_2") -> prompts
    Parameters:
     - [Dropdown] name: Literal[] (required)
    Returns:
     - [Dropdown] prompts: Literal[]

 - predict(api_name="/refresh_prompt_list_2") -> prompts
    Parameters:
     - None
    Returns:
     - [Dropdown] prompts: Literal[]

 - predict(name, api_name="/get_prompt_2") -> (positive_prompt, negative_prompt)
    Parameters:
     - [Dropdown] name: Literal[] (required)
    Returns:
     - [Textbox] positive_prompt: str
     - [Textbox] negative_prompt: str

 - predict(height, width, api_name="/switch_sizes_2") -> (height, width)
    Parameters:
     - [Slider] height: float (not required, defaults to:   1024)
     - [Slider] width: float (not required, defaults to:   1024)
    Returns:
     - [Slider] height: float (numeric value between 64 and 4096)
     - [Slider] width: float (numeric value between 64 and 4096)

 - predict(checkbox_value, api_name="/partial_12") -> flow_shift
    Parameters:
     - [Checkbox] checkbox_value: bool (not required, defaults to:   False)
    Returns:
     - [Number] flow_shift: float

 - predict(x, api_name="/lambda_13_2") ->
    Parameters:
     - [Checkbox] x: bool (not required, defaults to:   False)
    Returns:
     - None

 - predict(checkbox_value, api_name="/partial_1_2") -> guidance
    Parameters:
     - [Checkbox] checkbox_value: bool (not required, defaults to:   False)
    Returns:
     - [Slider] guidance: float (numeric value between 0 and 30)

 - predict(x, api_name="/lambda_14_2") ->
    Parameters:
     - [Checkbox] x: bool (not required, defaults to:   False)
    Returns:
     - None

 - predict(api_name="/random_seed_2") -> seed
    Parameters:
     - None
    Returns:
     - [Number] seed: float

 - predict(models_folder, api_name="/reload_models_6_2") -> upscaler
    Parameters:
     - [Textbox] models_folder: str (not required, defaults to:   /kaggle/working/sd.cpp-webui/models/upscale_models/)
    Returns:
     - [Dropdown] upscaler: Literal[]

 - predict(checkbox_value, api_name="/partial_2_2") -> (upscaler, upscaler_repeats)
    Parameters:
     - [Checkbox] checkbox_value: bool (not required, defaults to:   False)
    Returns:
     - [Dropdown] upscaler: Literal[]
     - [Slider] upscaler_repeats: float (numeric value between 1 and 5)

 - predict(models_folder, api_name="/reload_models_7_2") -> controlnet
    Parameters:
     - [Textbox] models_folder: str (not required, defaults to:   /kaggle/working/sd.cpp-webui/models/controlnet/)
    Returns:
     - [Dropdown] controlnet: Literal[]

 - predict(checkbox_value, api_name="/partial_3_2") -> (controlnet, value_1735, controlnet_strength, controlnet_on_cpu, canny_edge_detection)
    Parameters:
     - [Checkbox] checkbox_value: bool (not required, defaults to:   False)
    Returns:
     - [Dropdown] controlnet: Literal[]
     - [Image] value_1735: dict(path: str | None (Path to a local file), url: str | None (Publicly available url or base64 encoded image), size: int | None (Size of image in bytes), orig_name: str | None (Original filename), mime_type: str | None (mime type of image), is_stream: bool (Can always be set to False), meta: dict(str, Any))
     - [Slider] controlnet_strength: float (numeric value between 0 and 1)
     - [Checkbox] controlnet_on_cpu: bool
     - [Checkbox] canny_edge_detection: bool

 - predict(models_folder, api_name="/reload_models_8_2") -> photomaker
    Parameters:
     - [Textbox] models_folder: str (not required, defaults to:   /kaggle/working/sd.cpp-webui/models/photomaker/)
    Returns:
     - [Dropdown] photomaker: Literal[]

 - predict(checkbox_value, api_name="/partial_4_2") -> (photomaker, photomaker_input_id_images_directory, photomaker_v2_id_embed, photomaker_style_strength)
    Parameters:
     - [Checkbox] checkbox_value: bool (not required, defaults to:   False)
    Returns:
     - [Dropdown] photomaker: Literal[]
     - [Textbox] photomaker_input_id_images_directory: str
     - [Textbox] photomaker_v2_id_embed: str
     - [Slider] photomaker_style_strength: float (numeric value between 0 and 100)

 - predict(checkbox_value, api_name="/partial_5_2") -> eta
    Parameters:
     - [Checkbox] checkbox_value: bool (not required, defaults to:   False)
    Returns:
     - [Number] eta: float

 - predict(models_folder, api_name="/reload_models_9_2") -> taesd
    Parameters:
     - [Textbox] models_folder: str (not required, defaults to:   /kaggle/working/sd.cpp-webui/models/taesd/)
    Returns:
     - [Dropdown] taesd: Literal[]

 - predict(checkbox_value, api_name="/partial_6_2") -> (vae_tile_overlap, vae_tile_size, enable_vae_relative_tile_size)
    Parameters:
     - [Checkbox] checkbox_value: bool (not required, defaults to:   False)
    Returns:
     - [Slider] vae_tile_overlap: float (numeric value between 0 and 1)
     - [Number] vae_tile_size: float
     - [Checkbox] enable_vae_relative_tile_size: bool

 - predict(checkbox_value, api_name="/partial_7_2") -> vae_relative_tile_size
    Parameters:
     - [Checkbox] checkbox_value: bool (not required, defaults to:   False)
    Returns:
     - [Number] vae_relative_tile_size: float

 - predict(checkbox_value, api_name="/partial_8_2") -> (cache_mode, cachedit_preset, cache_option, scm_mask, scm_policy)
    Parameters:
     - [Checkbox] checkbox_value: bool (not required, defaults to:   False)
    Returns:
     - [Dropdown] cache_mode: Literal['easycache', 'ucache', 'dbcache', 'taylorseer', 'cache-dit', 'spectrum']
     - [Dropdown] cachedit_preset: Literal['none', 'slow', 'medium', 'fast', 'ultra']
     - [Textbox] cache_option: str
     - [Textbox] scm_mask: str
     - [Dropdown] scm_policy: Literal['none', 'dynamic', 'static']

 - predict(checkbox_value, api_name="/partial_9_2") -> (preview_mode, preview_interval, taesd_for_preview_only, preview_noisy)
    Parameters:
     - [Checkbox] checkbox_value: bool (not required, defaults to:   False)
    Returns:
     - [Dropdown] preview_mode: Literal['none', 'proj', 'tae', 'vae']
     - [Number] preview_interval: float
     - [Checkbox] taesd_for_preview_only: bool
     - [Checkbox] preview_noisy: bool

 - predict(param_0, param_1, param_2, param_3, param_4, param_5, param_7, param_8, param_9, param_10, param_11, param_12, param_13, param_14, param_15, param_16, param_17, param_18, param_19, param_20, param_21, param_22, param_23, param_24, param_25, param_26, param_27, param_28, param_29, param_30, param_31, param_32, param_33, param_34, param_35, param_36, param_37, param_38, param_39, param_40, param_41, param_42, param_43, param_44, param_45, param_46, param_47, param_48, param_49, param_50, param_51, param_52, param_53, param_54, param_55, param_56, param_57, param_58, param_59, param_60, param_61, param_62, param_63, param_64, param_65, param_66, param_67, param_68, param_69, param_70, param_71, param_72, param_73, param_74, param_75, param_76, param_77, param_78, param_79, param_80, param_81, param_82, param_83, param_84, param_85, param_86, param_87, param_88, api_name="/submit_job_2") -> (progress, status)
    Parameters:
     - [Number] param_0: float (not required, defaults to:   0)
     - [Checkbox] param_1: bool (not required, defaults to:   False)
     - [Checkbox] param_2: bool (not required, defaults to:   False)
     - [Number] param_3: float (not required, defaults to:   0)
     - [Checkbox] param_4: bool (not required, defaults to:   False)
     - [Checkbox] param_5: bool (not required, defaults to:   False)
     - [Slider] param_7: float (not required, defaults to:   1)
     - [Checkbox] param_8: bool (not required, defaults to:   False)
     - [Dropdown] param_9: Literal['none', 'slow', 'medium', 'fast', 'ultra'] (not required, defaults to:   none)
     - [Dropdown] param_10: Literal['easycache', 'ucache', 'dbcache', 'taylorseer', 'cache-dit', 'spectrum'] (not required, defaults to:   easycache)
     - [Textbox] param_11: str (required)
     - [Checkbox] param_12: bool (not required, defaults to:   False)
     - [Slider] param_13: float (not required, defaults to:   1.0)
     - [Dropdown] param_14: Literal['None', 'Circular', 'Circular X', 'Circular Y'] (not required, defaults to:   None) 
     - [Checkbox] param_15: bool (not required, defaults to:   False)
     - [Dropdown] param_16: Literal['Qwen3-4B-Instruct-2507-Q4_K_M.gguf'] (required)
     - [Slider] param_17: float (not required, defaults to:   -1)
     - [Dropdown] param_18: Literal[] (required)
     - [Checkbox] param_19: bool (not required, defaults to:   False)
     - [Checkbox] param_20: bool (not required, defaults to:   False)
     - [Checkbox] param_21: bool (not required, defaults to:   True)
     - [Image] param_22: dict(path: str | None (Path to a local file), url: str | None (Publicly available url or base64 encoded image), size: int | None (Size of image in bytes), orig_name: str | None (Original filename), mime_type: str | None (mime type of image), is_stream: bool (Can always be set to False), meta: dict(str, Any)) (required)  (For input, either path or url must be provided. For output, path is always provided.)
     - [Slider] param_23: float (not required, defaults to:   0.9)
     - [Checkbox] param_24: bool (not required, defaults to:   False)
     - [Checkbox] param_25: bool (not required, defaults to:   False)
     - [Number] param_26: float (not required, defaults to:   1)
     - [Checkbox] param_27: bool (not required, defaults to:   False)
     - [Number] param_28: float (not required, defaults to:   0)
     - [Checkbox] param_29: bool (not required, defaults to:   False)
     - [Checkbox] param_30: bool (not required, defaults to:   False)
     - [Number] param_31: float (not required, defaults to:   3.0)
     - [Checkbox] param_32: bool (not required, defaults to:   False)
     - [Checkbox] param_33: bool (not required, defaults to:   False)
     - [Slider] param_34: float (not required, defaults to:   3.5)
     - [Checkbox] param_35: bool (not required, defaults to:   False)
     - [Slider] param_36: float (not required, defaults to:   1024)
     - [Dropdown] param_37: Literal['Qwen3-4B-Instruct-2507-Q4_K_M.gguf'] (required)
     - [Dropdown] param_38: Literal['Qwen3-4B-Instruct-2507-Q4_K_M.gguf'] (required)
     - [Dropdown] param_39: Literal['auto', 'immediately', 'at_runtime'] (not required, defaults to:   auto)
     - [Dropdown] param_40: Literal['[illustrious]NFFA10.3-000080.safetensors', '[illustrious]cunnyfunky3.3-000080.safetensors'] (required)
     - [Radio] param_41: Literal['Positive', 'Negative'] (not required, defaults to:   Positive)
     - [Slider] param_42: float (not required, defaults to:   0.0)
     - [Checkbox] param_43: bool (not required, defaults to:   True)
     - [Dropdown] param_44: Literal['Default', 'f32', 'f16', 'q8_0', 'q6_K', 'q5_K', 'q5_1', 'q5_0', 'q4_K', 'q4_1', 'q4_0', 'q3_K', 'q2_K'] (not required, defaults to:   Default)
     - [Textbox] param_45: str (required)
     - [Checkbox] param_46: bool (not required, defaults to:   False)
     - [Textbox] param_47: str (not required, defaults to:   )
     - [Dropdown] param_48: Literal[] (not required, defaults to:   )
     - [Checkbox] param_49: bool (not required, defaults to:   False)
     - [Textbox] param_50: str (not required, defaults to:   )
     - [Textbox] param_51: str (not required, defaults to:   )
     - [Slider] param_52: float (not required, defaults to:   20)
     - [Textbox] param_53: str (required)
     - [Dropdown] param_54: Literal['Default', 'eps', 'v', 'edm_v', 'sd3_flow', 'flux_flow', 'flux2_flow'] (not required, defaults to:   Default)
     - [Checkbox] param_55: bool (not required, defaults to:   False)
     - [Number] param_56: float (not required, defaults to:   1)
     - [Dropdown] param_57: Literal['none', 'proj', 'tae', 'vae'] (not required, defaults to:   none)
     - [Checkbox] param_58: bool (not required, defaults to:   False)
     - [Checkbox] param_59: bool (not required, defaults to:   False)
     - [Image] param_60: dict(path: str | None (Path to a local file), url: str | None (Publicly available url or base64 encoded image), size: int | None (Size of image in bytes), orig_name: str | None (Original filename), mime_type: str | None (mime type of image), is_stream: bool (Can always be set to False), meta: dict(str, Any)) (required)  (For input, either path or url must be provided. For output, path is always provided.)
     - [Dropdown] param_61: Literal['std_default', 'cuda', 'cpu'] (not required, defaults to:   cuda)
     - [Dropdown] param_62: Literal['std_default', 'cuda', 'cpu'] (not required, defaults to:   cuda)
     - [Dropdown] param_63: Literal['euler', 'euler_a', 'heun', 'dpm2', 'dpm++2s_a', 'dpm++2m', 'dpm++2mv2', 'ipndm', 'ipndm_v', 'lcm', 'ddim_trailing', 'tcd', 'res_multistep', 'res_2s'] (not required, defaults to:   euler)
     - [Dropdown] param_64: Literal['discrete', 'karras', 'exponential', 'ays', 'gits', 'smoothstep', 'sgm_uniform', 'simple', 'kl_optimal', 'lcm', 'bong_tangent'] (not required, defaults to:   discrete)
     - [Textbox] param_65: str (required)
     - [Dropdown] param_66: Literal['none', 'dynamic', 'static'] (not required, defaults to:   none)
     - [Number] param_67: float (not required, defaults to:   -1)
     - [Textbox] param_68: str (not required, defaults to:   )
     - [Slider] param_69: float (not required, defaults to:   8)
     - [Dropdown] param_70: Literal['Qwen3-4B-Instruct-2507-Q4_K_M.gguf'] (required)
     - [Dropdown] param_71: Literal[] (required)
     - [Textbox] param_72: str (not required, defaults to:   )
     - [Number] param_73: float (not required, defaults to:   0)
     - [Dropdown] param_74: Literal['z_image_turbo-Q8_0.gguf'] (required)
     - [Dropdown] param_75: Literal['ae.safetensors'] (required)
     - [Dropdown] param_76: Literal[] (not required, defaults to:   )
     - [Checkbox] param_77: bool (not required, defaults to:   False)
     - [Slider] param_78: float (not required, defaults to:   1)
     - [Checkbox] param_79: bool (not required, defaults to:   False)
     - [Checkbox] param_80: bool (not required, defaults to:   False)
     - [Checkbox] param_81: bool (not required, defaults to:   False)
     - [Number] param_82: float (not required, defaults to:   0)
     - [Slider] param_83: float (not required, defaults to:   0.5)
     - [Number] param_84: float (not required, defaults to:   32)
     - [Checkbox] param_85: bool (not required, defaults to:   False)
     - [Checkbox] param_86: bool (not required, defaults to:   False)
     - [Slider] param_87: float (not required, defaults to:   1024)
     - [Dropdown] param_88: Literal[] (required)
    Returns:
     - [Slider] progress: float (numeric value between 0 and 100)
     - [Textbox] status: str

 - predict(api_name="/poll_status_2") -> (stablediffusioncpp_command, progress, status, statistics, generated_images, value_1884, value_1868)
    Parameters:
     - None
    Returns:
     - [Textbox] stablediffusioncpp_command: str
     - [Slider] progress: float (numeric value between 0 and 100)
     - [Textbox] status: str
     - [Textbox] statistics: str
     - [Gallery] generated_images: list[dict(image: dict(path: str | None (Path to a local file), url: str | None (Publicly available url or base64 encoded image), size: int | None (Size of image in bytes), orig_name: str | None (Original filename), mime_type: str | None (mime type of image), is_stream: bool (Can always be set to False), meta: dict(str, Any)), caption: str | None) | dict(video: filepath, caption: str | None)]
     - [Timer] value_1884: float
     - [Textbox] value_1868: str

 - predict(api_name="/kill_subprocess_2") ->
    Parameters:
     - None
    Returns:
     - None

 - predict(lora_model, lora_strength, lora_prompt_switch, pprompt, nprompt, api_name="/apply_lora_2") -> (positive_prompt, negative_prompt)
    Parameters:
     - [Dropdown] lora_model: Literal['[illustrious]NFFA10.3-000080.safetensors', '[illustrious]cunnyfunky3.3-000080.safetensors'] (required)
     - [Slider] lora_strength: float (not required, defaults to:   0.0)
     - [Radio] lora_prompt_switch: Literal['Positive', 'Negative'] (not required, defaults to:   Positive)
     - [Textbox] pprompt: str (required)
     - [Textbox] nprompt: str (required)
    Returns:
     - [Textbox] positive_prompt: str
     - [Textbox] negative_prompt: str

 - predict(api_name="/refresh_all_options_2") -> (sampling_method, scheduler, preview_mode, prediction)
    Parameters:
     - None
    Returns:
     - [Dropdown] sampling_method: Literal['euler', 'euler_a', 'heun', 'dpm2', 'dpm++2s_a', 'dpm++2m', 'dpm++2mv2', 'ipndm', 'ipndm_v', 'lcm', 'ddim_trailing', 'tcd', 'res_multistep', 'res_2s']
     - [Dropdown] scheduler: Literal['discrete', 'karras', 'exponential', 'ays', 'gits', 'smoothstep', 'sgm_uniform', 'simple', 'kl_optimal', 'lcm', 'bong_tangent']
     - [Dropdown] preview_mode: Literal['none', 'proj', 'tae', 'vae']
     - [Dropdown] prediction: Literal['Default', 'eps', 'v', 'edm_v', 'sd3_flow', 'flux_flow', 'flux2_flow']

 - predict(x, api_name="/lambda_23") ->
    Parameters:
     - [Dropdown] x: Literal['z_image_turbo-Q8_0.gguf'] (required)
    Returns:
     - None

 - predict(models_folder, api_name="/reload_models_15") -> unet_model
    Parameters:
     - [Textbox] models_folder: str (not required, defaults to:   /kaggle/working/sd.cpp-webui/models/unet/)
    Returns:
     - [Dropdown] unet_model: Literal['z_image_turbo-Q8_0.gguf']

 - predict(api_name="/lambda_1_3") ->
    Parameters:
     - None
    Returns:
     - None

 - predict(x, api_name="/lambda_2_3") ->
    Parameters:
     - [Dropdown] x: Literal['ae.safetensors'] (required)
    Returns:
     - None

 - predict(models_folder, api_name="/reload_models_1_3") -> unet_vae
    Parameters:
     - [Textbox] models_folder: str (not required, defaults to:   /kaggle/working/sd.cpp-webui/models/vae/)
    Returns:
     - [Dropdown] unet_vae: Literal['ae.safetensors']

 - predict(api_name="/lambda_3_3") ->
    Parameters:
     - None
    Returns:
     - None

 - predict(x, api_name="/lambda_4_3") ->
    Parameters:
     - [Dropdown] x: Literal['Qwen3-4B-Instruct-2507-Q4_K_M.gguf'] (required)
    Returns:
     - None

 - predict(models_folder, api_name="/reload_models_2_3") -> clip_vision_h
    Parameters:
     - [Textbox] models_folder: str (not required, defaults to:   /kaggle/working/sd.cpp-webui/models/text_encoders/)
    Returns:
     - [Dropdown] clip_vision_h: Literal['Qwen3-4B-Instruct-2507-Q4_K_M.gguf']

 - predict(api_name="/lambda_5_3") ->
    Parameters:
     - None
    Returns:
     - None

 - predict(x, api_name="/lambda_6_3") ->
    Parameters:
     - [Dropdown] x: Literal['Qwen3-4B-Instruct-2507-Q4_K_M.gguf'] (required)
    Returns:
     - None

 - predict(models_folder, api_name="/reload_models_3_3") -> umt5_xxl
    Parameters:
     - [Textbox] models_folder: str (not required, defaults to:   /kaggle/working/sd.cpp-webui/models/text_encoders/)
    Returns:
     - [Dropdown] umt5_xxl: Literal['Qwen3-4B-Instruct-2507-Q4_K_M.gguf']

 - predict(api_name="/lambda_7_3") ->
    Parameters:
     - None
    Returns:
     - None

 - predict(models_folder, api_name="/reload_models_4_3") -> high_noise_model
    Parameters:
     - [Textbox] models_folder: str (not required, defaults to:   /kaggle/working/sd.cpp-webui/models/unet/)
    Returns:
     - [Dropdown] high_noise_model: Literal['z_image_turbo-Q8_0.gguf']

 - predict(_, api_name="/lambda_8_3") -> lora
    Parameters:
     - [Textbox] _: str (not required, defaults to:   /kaggle/working/sd.cpp-webui/models/loras/)
    Returns:
     - [Dropdown] lora: Literal['[illustrious]NFFA10.3-000080.safetensors', '[illustrious]cunnyfunky3.3-000080.safetensors']

 - predict(name, p_prompt, n_prompt, api_name="/save_and_refresh_prompts_3") -> prompts
    Parameters:
     - [Textbox] name: str (required)
     - [Textbox] p_prompt: str (required)
     - [Textbox] n_prompt: str (required)
    Returns:
     - [Dropdown] prompts: Literal[]

 - predict(name, api_name="/delete_and_refresh_prompts_3") -> prompts
    Parameters:
     - [Dropdown] name: Literal[] (required)
    Returns:
     - [Dropdown] prompts: Literal[]

 - predict(api_name="/refresh_prompt_list_3") -> prompts
    Parameters:
     - None
    Returns:
     - [Dropdown] prompts: Literal[]

 - predict(name, api_name="/get_prompt_3") -> (positive_prompt, negative_prompt)
    Parameters:
     - [Dropdown] name: Literal[] (required)
    Returns:
     - [Textbox] positive_prompt: str
     - [Textbox] negative_prompt: str

 - predict(height, width, api_name="/switch_sizes_3") -> (height, width)
    Parameters:
     - [Slider] height: float (not required, defaults to:   1024)
     - [Slider] width: float (not required, defaults to:   1024)
    Returns:
     - [Slider] height: float (numeric value between 64 and 4096)
     - [Slider] width: float (numeric value between 64 and 4096)

 - predict(checkbox_value, api_name="/partial_13") -> flow_shift
    Parameters:
     - [Checkbox] checkbox_value: bool (not required, defaults to:   False)
    Returns:
     - [Number] flow_shift: float

 - predict(x, api_name="/lambda_9_3") ->
    Parameters:
     - [Checkbox] x: bool (not required, defaults to:   False)
    Returns:
     - None

 - predict(checkbox_value, api_name="/partial_1_3") -> guidance
    Parameters:
     - [Checkbox] checkbox_value: bool (not required, defaults to:   False)
    Returns:
     - [Slider] guidance: float (numeric value between 0 and 30)

 - predict(x, api_name="/lambda_10_3") ->
    Parameters:
     - [Checkbox] x: bool (not required, defaults to:   False)
    Returns:
     - None

 - predict(api_name="/random_seed_3") -> seed
    Parameters:
     - None
    Returns:
     - [Number] seed: float

 - predict(models_folder, api_name="/reload_models_5_3") -> upscaler
    Parameters:
     - [Textbox] models_folder: str (not required, defaults to:   /kaggle/working/sd.cpp-webui/models/upscale_models/)
    Returns:
     - [Dropdown] upscaler: Literal[]

 - predict(checkbox_value, api_name="/partial_2_3") -> (upscaler, upscaler_repeats)
    Parameters:
     - [Checkbox] checkbox_value: bool (not required, defaults to:   False)
    Returns:
     - [Dropdown] upscaler: Literal[]
     - [Slider] upscaler_repeats: float (numeric value between 1 and 5)

 - predict(models_folder, api_name="/reload_models_6_3") -> controlnet
    Parameters:
     - [Textbox] models_folder: str (not required, defaults to:   /kaggle/working/sd.cpp-webui/models/controlnet/)
    Returns:
     - [Dropdown] controlnet: Literal[]

 - predict(checkbox_value, api_name="/partial_3_3") -> (controlnet, value_2409, controlnet_strength, controlnet_on_cpu, canny_edge_detection)
    Parameters:
     - [Checkbox] checkbox_value: bool (not required, defaults to:   False)
    Returns:
     - [Dropdown] controlnet: Literal[]
     - [Image] value_2409: dict(path: str | None (Path to a local file), url: str | None (Publicly available url or base64 encoded image), size: int | None (Size of image in bytes), orig_name: str | None (Original filename), mime_type: str | None (mime type of image), is_stream: bool (Can always be set to False), meta: dict(str, Any))
     - [Slider] controlnet_strength: float (numeric value between 0 and 1)
     - [Checkbox] controlnet_on_cpu: bool
     - [Checkbox] canny_edge_detection: bool

 - predict(checkbox_value, api_name="/partial_4_3") -> eta
    Parameters:
     - [Checkbox] checkbox_value: bool (not required, defaults to:   False)
    Returns:
     - [Number] eta: float

 - predict(models_folder, api_name="/reload_models_7_3") -> taesd
    Parameters:
     - [Textbox] models_folder: str (not required, defaults to:   /kaggle/working/sd.cpp-webui/models/taesd/)
    Returns:
     - [Dropdown] taesd: Literal[]

 - predict(checkbox_value, api_name="/partial_5_3") -> (vae_tile_overlap, vae_tile_size, enable_vae_relative_tile_size)
    Parameters:
     - [Checkbox] checkbox_value: bool (not required, defaults to:   False)
    Returns:
     - [Slider] vae_tile_overlap: float (numeric value between 0 and 1)
     - [Number] vae_tile_size: float
     - [Checkbox] enable_vae_relative_tile_size: bool

 - predict(checkbox_value, api_name="/partial_6_3") -> vae_relative_tile_size
    Parameters:
     - [Checkbox] checkbox_value: bool (not required, defaults to:   False)
    Returns:
     - [Number] vae_relative_tile_size: float

 - predict(checkbox_value, api_name="/partial_7_3") -> (cache_mode, cachedit_preset, cache_option, scm_mask, scm_policy)
    Parameters:
     - [Checkbox] checkbox_value: bool (not required, defaults to:   False)
    Returns:
     - [Dropdown] cache_mode: Literal['easycache', 'ucache', 'dbcache', 'taylorseer', 'cache-dit', 'spectrum']
     - [Dropdown] cachedit_preset: Literal['none', 'slow', 'medium', 'fast', 'ultra']
     - [Textbox] cache_option: str
     - [Textbox] scm_mask: str
     - [Dropdown] scm_policy: Literal['none', 'dynamic', 'static']

 - predict(checkbox_value, api_name="/partial_8_3") -> (preview_mode, preview_interval, taesd_for_preview_only, preview_noisy)
    Parameters:
     - [Checkbox] checkbox_value: bool (not required, defaults to:   False)
    Returns:
     - [Dropdown] preview_mode: Literal['none', 'proj', 'tae', 'vae']
     - [Number] preview_interval: float
     - [Checkbox] taesd_for_preview_only: bool
     - [Checkbox] preview_noisy: bool

 - predict(param_0, param_1, param_2, param_3, param_4, param_5, param_7, param_8, param_9, param_10, param_11, param_12, param_13, param_14, param_15, param_16, param_17, param_18, param_19, param_20, param_21, param_22, param_23, param_24, param_25, param_26, param_27, param_28, param_29, param_30, param_31, param_32, param_33, param_34, param_35, param_36, param_37, param_38, param_39, param_40, param_41, param_42, param_43, param_44, param_45, param_46, param_47, param_48, param_49, param_50, param_51, param_52, param_53, param_54, param_55, param_56, param_57, param_58, param_59, param_60, param_61, param_62, param_63, param_64, param_65, param_66, param_67, param_68, param_69, param_70, param_71, param_72, param_73, param_74, param_75, param_76, param_77, param_78, param_79, param_80, param_81, param_82, param_83, api_name="/submit_job_3") -> (progress, status)
    Parameters:
     - [Number] param_0: float (not required, defaults to:   0)
     - [Checkbox] param_1: bool (not required, defaults to:   False)
     - [Checkbox] param_2: bool (not required, defaults to:   False)
     - [Number] param_3: float (not required, defaults to:   0)
     - [Checkbox] param_4: bool (not required, defaults to:   False)
     - [Checkbox] param_5: bool (not required, defaults to:   False)
     - [Slider] param_7: float (not required, defaults to:   1)
     - [Checkbox] param_8: bool (not required, defaults to:   False)
     - [Dropdown] param_9: Literal['none', 'slow', 'medium', 'fast', 'ultra'] (not required, defaults to:   none)
     - [Dropdown] param_10: Literal['easycache', 'ucache', 'dbcache', 'taylorseer', 'cache-dit', 'spectrum'] (not required, defaults to:   easycache)
     - [Textbox] param_11: str (required)
     - [Checkbox] param_12: bool (not required, defaults to:   False)
     - [Slider] param_13: float (not required, defaults to:   1.0)
     - [Checkbox] param_14: bool (not required, defaults to:   False)
     - [Slider] param_15: float (not required, defaults to:   -1)
     - [Dropdown] param_16: Literal['Qwen3-4B-Instruct-2507-Q4_K_M.gguf'] (required)
     - [Dropdown] param_17: Literal[] (required)
     - [Checkbox] param_18: bool (not required, defaults to:   False)
     - [Checkbox] param_19: bool (not required, defaults to:   False)
     - [Checkbox] param_20: bool (not required, defaults to:   True)
     - [Image] param_21: dict(path: str | None (Path to a local file), url: str | None (Publicly available url or base64 encoded image), size: int | None (Size of image in bytes), orig_name: str | None (Original filename), mime_type: str | None (mime type of image), is_stream: bool (Can always be set to False), meta: dict(str, Any)) (required)  (For input, either path or url must be provided. For output, path is always provided.)
     - [Slider] param_22: float (not required, defaults to:   0.9)
     - [Checkbox] param_23: bool (not required, defaults to:   False)
     - [Checkbox] param_24: bool (not required, defaults to:   False)
     - [Number] param_25: float (not required, defaults to:   0)
     - [Checkbox] param_26: bool (not required, defaults to:   False)
     - [Image] param_27: dict(path: str | None (Path to a local file), url: str | None (Publicly available url or base64 encoded image), size: int | None (Size of image in bytes), orig_name: str | None (Original filename), mime_type: str | None (mime type of image), is_stream: bool (Can always be set to False), meta: dict(str, Any)) (required)  (For input, either path or url must be provided. For output, path is always provided.)
     - [Checkbox] param_28: bool (not required, defaults to:   False)
     - [Number] param_29: float (not required, defaults to:   3.0)
     - [Checkbox] param_30: bool (not required, defaults to:   False)
     - [Checkbox] param_31: bool (not required, defaults to:   False)
     - [Number] param_32: float (not required, defaults to:   24)
     - [Number] param_33: float (not required, defaults to:   1)
     - [Slider] param_34: float (not required, defaults to:   3.5)
     - [Checkbox] param_35: bool (not required, defaults to:   False)
     - [Slider] param_36: float (not required, defaults to:   1024)
     - [Dropdown] param_37: Literal['z_image_turbo-Q8_0.gguf'] (required)
     - [Image] param_38: dict(path: str | None (Path to a local file), url: str | None (Publicly available url or base64 encoded image), size: int | None (Size of image in bytes), orig_name: str | None (Original filename), mime_type: str | None (mime type of image), is_stream: bool (Can always be set to False), meta: dict(str, Any)) (required)  (For input, either path or url must be provided. For output, path is always provided.)
     - [Image] param_39: dict(path: str | None (Path to a local file), url: str | None (Publicly available url or base64 encoded image), size: int | None (Size of image in bytes), orig_name: str | None (Original filename), mime_type: str | None (mime type of image), is_stream: bool (Can always be set to False), meta: dict(str, Any)) (required)  (For input, either path or url must be provided. For output, path is always provided.)
     - [Dropdown] param_40: Literal['auto', 'immediately', 'at_runtime'] (not required, defaults to:   auto)
     - [Dropdown] param_41: Literal['[illustrious]NFFA10.3-000080.safetensors', '[illustrious]cunnyfunky3.3-000080.safetensors'] (required)
     - [Radio] param_42: Literal['Positive', 'Negative'] (not required, defaults to:   Positive)
     - [Slider] param_43: float (not required, defaults to:   0.0)
     - [Checkbox] param_44: bool (not required, defaults to:   True)
     - [Dropdown] param_45: Literal['Default', 'f32', 'f16', 'q8_0', 'q6_K', 'q5_K', 'q5_1', 'q5_0', 'q4_K', 'q4_1', 'q4_0', 'q3_K', 'q2_K'] (not required, defaults to:   Default)
     - [Textbox] param_46: str (required)
     - [Checkbox] param_47: bool (not required, defaults to:   False)
     - [Textbox] param_48: str (not required, defaults to:   )
     - [Textbox] param_49: str (required)
     - [Dropdown] param_50: Literal['Default', 'eps', 'v', 'edm_v', 'sd3_flow', 'flux_flow', 'flux2_flow'] (not required, defaults to:   Default)
     - [Checkbox] param_51: bool (not required, defaults to:   False)
     - [Number] param_52: float (not required, defaults to:   1)
     - [Dropdown] param_53: Literal['none', 'proj', 'tae', 'vae'] (not required, defaults to:   none)
     - [Checkbox] param_54: bool (not required, defaults to:   False)
     - [Checkbox] param_55: bool (not required, defaults to:   False)
     - [Dropdown] param_56: Literal['std_default', 'cuda', 'cpu'] (not required, defaults to:   cuda)
     - [Dropdown] param_57: Literal['std_default', 'cuda', 'cpu'] (not required, defaults to:   cuda)
     - [Dropdown] param_58: Literal['euler', 'euler_a', 'heun', 'dpm2', 'dpm++2s_a', 'dpm++2m', 'dpm++2mv2', 'ipndm', 'ipndm_v', 'lcm', 'ddim_trailing', 'tcd', 'res_multistep', 'res_2s'] (not required, defaults to:   euler)
     - [Dropdown] param_59: Literal['discrete', 'karras', 'exponential', 'ays', 'gits', 'smoothstep', 'sgm_uniform', 'simple', 'kl_optimal', 'lcm', 'bong_tangent'] (not required, defaults to:   discrete)
     - [Textbox] param_60: str (required)
     - [Dropdown] param_61: Literal['none', 'dynamic', 'static'] (not required, defaults to:   none)
     - [Number] param_62: float (not required, defaults to:   -1)
     - [Textbox] param_63: str (not required, defaults to:   )
     - [Slider] param_64: float (not required, defaults to:   8)
     - [Dropdown] param_65: Literal[] (required)
     - [Textbox] param_66: str (not required, defaults to:   )
     - [Number] param_67: float (not required, defaults to:   0)
     - [Dropdown] param_68: Literal['Qwen3-4B-Instruct-2507-Q4_K_M.gguf'] (required)
     - [Dropdown] param_69: Literal['z_image_turbo-Q8_0.gguf'] (required)
     - [Dropdown] param_70: Literal['ae.safetensors'] (required)
     - [Dropdown] param_71: Literal[] (not required, defaults to:   )
     - [Checkbox] param_72: bool (not required, defaults to:   False)
     - [Slider] param_73: float (not required, defaults to:   1)
     - [Checkbox] param_74: bool (not required, defaults to:   False)
     - [Checkbox] param_75: bool (not required, defaults to:   False)
     - [Checkbox] param_76: bool (not required, defaults to:   False)
     - [Number] param_77: float (not required, defaults to:   0)
     - [Slider] param_78: float (not required, defaults to:   0.5)
     - [Number] param_79: float (not required, defaults to:   32)
     - [Checkbox] param_80: bool (not required, defaults to:   False)
     - [Checkbox] param_81: bool (not required, defaults to:   False)
     - [Slider] param_82: float (not required, defaults to:   1024)
     - [Dropdown] param_83: Literal[] (required)
    Returns:
     - [Slider] progress: float (numeric value between 0 and 100)
     - [Textbox] status: str

 - predict(api_name="/poll_status_3") -> (stablediffusioncpp_command, progress, status, statistics, generated_videos, value_2534, value_2518)
    Parameters:
     - None
    Returns:
     - [Textbox] stablediffusioncpp_command: str
     - [Slider] progress: float (numeric value between 0 and 100)
     - [Textbox] status: str
     - [Textbox] statistics: str
     - [Gallery] generated_videos: list[dict(image: dict(path: str | None (Path to a local file), url: str | None (Publicly available url or base64 encoded image), size: int | None (Size of image in bytes), orig_name: str | None (Original filename), mime_type: str | None (mime type of image), is_stream: bool (Can always be set to False), meta: dict(str, Any)), caption: str | None) | dict(video: filepath, caption: str | None)]
     - [Timer] value_2534: float
     - [Textbox] value_2518: str

 - predict(api_name="/kill_subprocess_3") ->
    Parameters:
     - None
    Returns:
     - None

 - predict(lora_model, lora_strength, lora_prompt_switch, pprompt, nprompt, api_name="/apply_lora_3") -> (positive_prompt, negative_prompt)
    Parameters:
     - [Dropdown] lora_model: Literal['[illustrious]NFFA10.3-000080.safetensors', '[illustrious]cunnyfunky3.3-000080.safetensors'] (required)
     - [Slider] lora_strength: float (not required, defaults to:   0.0)
     - [Radio] lora_prompt_switch: Literal['Positive', 'Negative'] (not required, defaults to:   Positive)
     - [Textbox] pprompt: str (required)
     - [Textbox] nprompt: str (required)
    Returns:
     - [Textbox] positive_prompt: str
     - [Textbox] negative_prompt: str

 - predict(api_name="/refresh_all_options_3") -> (sampling_method, scheduler, preview_mode, prediction)
    Parameters:
     - None
    Returns:
     - [Dropdown] sampling_method: Literal['euler', 'euler_a', 'heun', 'dpm2', 'dpm++2s_a', 'dpm++2m', 'dpm++2mv2', 'ipndm', 'ipndm_v', 'lcm', 'ddim_trailing', 'tcd', 'res_multistep', 'res_2s']
     - [Dropdown] scheduler: Literal['discrete', 'karras', 'exponential', 'ays', 'gits', 'smoothstep', 'sgm_uniform', 'simple', 'kl_optimal', 'lcm', 'bong_tangent']
     - [Dropdown] preview_mode: Literal['none', 'proj', 'tae', 'vae']
     - [Dropdown] prediction: Literal['Default', 'eps', 'v', 'edm_v', 'sd3_flow', 'flux_flow', 'flux2_flow']

 - predict(checkbox_value, api_name="/partial_9_3") -> flow_shift
    Parameters:
     - [Checkbox] checkbox_value: bool (not required, defaults to:   False)
    Returns:
     - [Number] flow_shift: float

 - predict(api_name="/get_img_info") -> (positive_prompt, negative_prompt, width, height, steps, sampler, scheduler, cfg, seed, path, metadata)
    Parameters:
     - None
    Returns:
     - [Textbox] positive_prompt: str
     - [Textbox] negative_prompt: str
     - [Number] width: float
     - [Number] height: float
     - [Number] steps: float
     - [Textbox] sampler: str
     - [Textbox] scheduler: str
     - [Number] cfg: float
     - [Number] seed: float
     - [Textbox] path: str
     - [Textbox] metadata: str

 - predict(page_num, ctrl_inp, sort_inp, api_name="/reload_gallery") -> (txt2img, page, txt2img, txt2img)
    Parameters:
     - [Textbox] page_num: str (not required, defaults to:   1)
     - [Textbox] ctrl_inp: str (not required, defaults to:   0)
     - [Radio] sort_inp: Literal['Date (Oldest First)', 'Date (Newest First)', 'Name (A-Z)', 'Name (Z-A)'] (not required, defaults to:   Date (Oldest First))
    Returns:
     - [Gallery] txt2img: list[dict(image: dict(path: str | None (Path to a local file), url: str | None (Publicly available url or base64 encoded image), size: int | None (Size of image in bytes), orig_name: str | None (Original filename), mime_type: str | None (mime type of image), is_stream: bool (Can always be set to False), meta: dict(str, Any)), caption: str | None) | dict(video: filepath, caption: str | None)]
     - [Number] page: float
     - [Gallery] txt2img: list[dict(image: dict(path: str | None (Path to a local file), url: str | None (Publicly available url or base64 encoded image), size: int | None (Size of image in bytes), orig_name: str | None (Original filename), mime_type: str | None (mime type of image), is_stream: bool (Can always be set to False), meta: dict(str, Any)), caption: str | None) | dict(video: filepath, caption: str | None)]
     - [Gallery] txt2img: list[dict(image: dict(path: str | None (Path to a local file), url: str | None (Publicly available url or base64 encoded image), size: int | None (Size of image in bytes), orig_name: str | None (Original filename), mime_type: str | None (mime type of image), is_stream: bool (Can always be set to False), meta: dict(str, Any)), caption: str | None) | dict(video: filepath, caption: str | None)]

 - predict(page_num, ctrl_inp, sort_inp, api_name="/reload_gallery_1") -> (txt2img, page, txt2img, txt2img)
    Parameters:
     - [Textbox] page_num: str (not required, defaults to:   1)
     - [Textbox] ctrl_inp: str (not required, defaults to:   1)
     - [Radio] sort_inp: Literal['Date (Oldest First)', 'Date (Newest First)', 'Name (A-Z)', 'Name (Z-A)'] (not required, defaults to:   Date (Oldest First))
    Returns:
     - [Gallery] txt2img: list[dict(image: dict(path: str | None (Path to a local file), url: str | None (Publicly available url or base64 encoded image), size: int | None (Size of image in bytes), orig_name: str | None (Original filename), mime_type: str | None (mime type of image), is_stream: bool (Can always be set to False), meta: dict(str, Any)), caption: str | None) | dict(video: filepath, caption: str | None)]
     - [Number] page: float
     - [Gallery] txt2img: list[dict(image: dict(path: str | None (Path to a local file), url: str | None (Publicly available url or base64 encoded image), size: int | None (Size of image in bytes), orig_name: str | None (Original filename), mime_type: str | None (mime type of image), is_stream: bool (Can always be set to False), meta: dict(str, Any)), caption: str | None) | dict(video: filepath, caption: str | None)]
     - [Gallery] txt2img: list[dict(image: dict(path: str | None (Path to a local file), url: str | None (Publicly available url or base64 encoded image), size: int | None (Size of image in bytes), orig_name: str | None (Original filename), mime_type: str | None (mime type of image), is_stream: bool (Can always be set to False), meta: dict(str, Any)), caption: str | None) | dict(video: filepath, caption: str | None)]

 - predict(page_num, ctrl_inp, sort_inp, api_name="/reload_gallery_2") -> (txt2img, page, txt2img, txt2img)
    Parameters:
     - [Textbox] page_num: str (not required, defaults to:   1)
     - [Textbox] ctrl_inp: str (not required, defaults to:   2)
     - [Radio] sort_inp: Literal['Date (Oldest First)', 'Date (Newest First)', 'Name (A-Z)', 'Name (Z-A)'] (not required, defaults to:   Date (Oldest First))
    Returns:
     - [Gallery] txt2img: list[dict(image: dict(path: str | None (Path to a local file), url: str | None (Publicly available url or base64 encoded image), size: int | None (Size of image in bytes), orig_name: str | None (Original filename), mime_type: str | None (mime type of image), is_stream: bool (Can always be set to False), meta: dict(str, Any)), caption: str | None) | dict(video: filepath, caption: str | None)]
     - [Number] page: float
     - [Gallery] txt2img: list[dict(image: dict(path: str | None (Path to a local file), url: str | None (Publicly available url or base64 encoded image), size: int | None (Size of image in bytes), orig_name: str | None (Original filename), mime_type: str | None (mime type of image), is_stream: bool (Can always be set to False), meta: dict(str, Any)), caption: str | None) | dict(video: filepath, caption: str | None)]
     - [Gallery] txt2img: list[dict(image: dict(path: str | None (Path to a local file), url: str | None (Publicly available url or base64 encoded image), size: int | None (Size of image in bytes), orig_name: str | None (Original filename), mime_type: str | None (mime type of image), is_stream: bool (Can always be set to False), meta: dict(str, Any)), caption: str | None) | dict(video: filepath, caption: str | None)]

 - predict(page_num, ctrl_inp, sort_inp, api_name="/reload_gallery_3") -> (txt2img, page, txt2img, txt2img)
    Parameters:
     - [Textbox] page_num: str (not required, defaults to:   1)
     - [Textbox] ctrl_inp: str (not required, defaults to:   3)
     - [Radio] sort_inp: Literal['Date (Oldest First)', 'Date (Newest First)', 'Name (A-Z)', 'Name (Z-A)'] (not required, defaults to:   Date (Oldest First))
    Returns:
     - [Gallery] txt2img: list[dict(image: dict(path: str | None (Path to a local file), url: str | None (Publicly available url or base64 encoded image), size: int | None (Size of image in bytes), orig_name: str | None (Original filename), mime_type: str | None (mime type of image), is_stream: bool (Can always be set to False), meta: dict(str, Any)), caption: str | None) | dict(video: filepath, caption: str | None)]
     - [Number] page: float
     - [Gallery] txt2img: list[dict(image: dict(path: str | None (Path to a local file), url: str | None (Publicly available url or base64 encoded image), size: int | None (Size of image in bytes), orig_name: str | None (Original filename), mime_type: str | None (mime type of image), is_stream: bool (Can always be set to False), meta: dict(str, Any)), caption: str | None) | dict(video: filepath, caption: str | None)]
     - [Gallery] txt2img: list[dict(image: dict(path: str | None (Path to a local file), url: str | None (Publicly available url or base64 encoded image), size: int | None (Size of image in bytes), orig_name: str | None (Original filename), mime_type: str | None (mime type of image), is_stream: bool (Can always be set to False), meta: dict(str, Any)), caption: str | None) | dict(video: filepath, caption: str | None)]

 - predict(page_num, ctrl_inp, sort_inp, api_name="/reload_gallery_4") -> (txt2img, page, txt2img, txt2img)
    Parameters:
     - [Textbox] page_num: str (not required, defaults to:   1)
     - [Textbox] ctrl_inp: str (not required, defaults to:   4)
     - [Radio] sort_inp: Literal['Date (Oldest First)', 'Date (Newest First)', 'Name (A-Z)', 'Name (Z-A)'] (not required, defaults to:   Date (Oldest First))
    Returns:
     - [Gallery] txt2img: list[dict(image: dict(path: str | None (Path to a local file), url: str | None (Publicly available url or base64 encoded image), size: int | None (Size of image in bytes), orig_name: str | None (Original filename), mime_type: str | None (mime type of image), is_stream: bool (Can always be set to False), meta: dict(str, Any)), caption: str | None) | dict(video: filepath, caption: str | None)]
     - [Number] page: float
     - [Gallery] txt2img: list[dict(image: dict(path: str | None (Path to a local file), url: str | None (Publicly available url or base64 encoded image), size: int | None (Size of image in bytes), orig_name: str | None (Original filename), mime_type: str | None (mime type of image), is_stream: bool (Can always be set to False), meta: dict(str, Any)), caption: str | None) | dict(video: filepath, caption: str | None)]
     - [Gallery] txt2img: list[dict(image: dict(path: str | None (Path to a local file), url: str | None (Publicly available url or base64 encoded image), size: int | None (Size of image in bytes), orig_name: str | None (Original filename), mime_type: str | None (mime type of image), is_stream: bool (Can always be set to False), meta: dict(str, Any)), caption: str | None) | dict(video: filepath, caption: str | None)]

 - predict(api_name="/prev_page") -> (txt2img, page, txt2img, txt2img)
    Parameters:
     - None
    Returns:
     - [Gallery] txt2img: list[dict(image: dict(path: str | None (Path to a local file), url: str | None (Publicly available url or base64 encoded image), size: int | None (Size of image in bytes), orig_name: str | None (Original filename), mime_type: str | None (mime type of image), is_stream: bool (Can always be set to False), meta: dict(str, Any)), caption: str | None) | dict(video: filepath, caption: str | None)]
     - [Number] page: float
     - [Gallery] txt2img: list[dict(image: dict(path: str | None (Path to a local file), url: str | None (Publicly available url or base64 encoded image), size: int | None (Size of image in bytes), orig_name: str | None (Original filename), mime_type: str | None (mime type of image), is_stream: bool (Can always be set to False), meta: dict(str, Any)), caption: str | None) | dict(video: filepath, caption: str | None)]
     - [Gallery] txt2img: list[dict(image: dict(path: str | None (Path to a local file), url: str | None (Publicly available url or base64 encoded image), size: int | None (Size of image in bytes), orig_name: str | None (Original filename), mime_type: str | None (mime type of image), is_stream: bool (Can always be set to False), meta: dict(str, Any)), caption: str | None) | dict(video: filepath, caption: str | None)]

 - predict(api_name="/next_page") -> (txt2img, page, txt2img, txt2img)
    Parameters:
     - None
    Returns:
     - [Gallery] txt2img: list[dict(image: dict(path: str | None (Path to a local file), url: str | None (Publicly available url or base64 encoded image), size: int | None (Size of image in bytes), orig_name: str | None (Original filename), mime_type: str | None (mime type of image), is_stream: bool (Can always be set to False), meta: dict(str, Any)), caption: str | None) | dict(video: filepath, caption: str | None)]
     - [Number] page: float
     - [Gallery] txt2img: list[dict(image: dict(path: str | None (Path to a local file), url: str | None (Publicly available url or base64 encoded image), size: int | None (Size of image in bytes), orig_name: str | None (Original filename), mime_type: str | None (mime type of image), is_stream: bool (Can always be set to False), meta: dict(str, Any)), caption: str | None) | dict(video: filepath, caption: str | None)]
     - [Gallery] txt2img: list[dict(image: dict(path: str | None (Path to a local file), url: str | None (Publicly available url or base64 encoded image), size: int | None (Size of image in bytes), orig_name: str | None (Original filename), mime_type: str | None (mime type of image), is_stream: bool (Can always be set to False), meta: dict(str, Any)), caption: str | None) | dict(video: filepath, caption: str | None)]

 - predict(api_name="/reload_gallery_5") -> (txt2img, page, txt2img, txt2img)
    Parameters:
     - None
    Returns:
     - [Gallery] txt2img: list[dict(image: dict(path: str | None (Path to a local file), url: str | None (Publicly available url or base64 encoded image), size: int | None (Size of image in bytes), orig_name: str | None (Original filename), mime_type: str | None (mime type of image), is_stream: bool (Can always be set to False), meta: dict(str, Any)), caption: str | None) | dict(video: filepath, caption: str | None)]
     - [Number] page: float
     - [Gallery] txt2img: list[dict(image: dict(path: str | None (Path to a local file), url: str | None (Publicly available url or base64 encoded image), size: int | None (Size of image in bytes), orig_name: str | None (Original filename), mime_type: str | None (mime type of image), is_stream: bool (Can always be set to False), meta: dict(str, Any)), caption: str | None) | dict(video: filepath, caption: str | None)]
     - [Gallery] txt2img: list[dict(image: dict(path: str | None (Path to a local file), url: str | None (Publicly available url or base64 encoded image), size: int | None (Size of image in bytes), orig_name: str | None (Original filename), mime_type: str | None (mime type of image), is_stream: bool (Can always be set to False), meta: dict(str, Any)), caption: str | None) | dict(video: filepath, caption: str | None)]

 - predict(api_name="/last_page") -> (txt2img, page, txt2img, txt2img)
    Parameters:
     - None
    Returns:
     - [Gallery] txt2img: list[dict(image: dict(path: str | None (Path to a local file), url: str | None (Publicly available url or base64 encoded image), size: int | None (Size of image in bytes), orig_name: str | None (Original filename), mime_type: str | None (mime type of image), is_stream: bool (Can always be set to False), meta: dict(str, Any)), caption: str | None) | dict(video: filepath, caption: str | None)]
     - [Number] page: float
     - [Gallery] txt2img: list[dict(image: dict(path: str | None (Path to a local file), url: str | None (Publicly available url or base64 encoded image), size: int | None (Size of image in bytes), orig_name: str | None (Original filename), mime_type: str | None (mime type of image), is_stream: bool (Can always be set to False), meta: dict(str, Any)), caption: str | None) | dict(video: filepath, caption: str | None)]
     - [Gallery] txt2img: list[dict(image: dict(path: str | None (Path to a local file), url: str | None (Publicly available url or base64 encoded image), size: int | None (Size of image in bytes), orig_name: str | None (Original filename), mime_type: str | None (mime type of image), is_stream: bool (Can always be set to False), meta: dict(str, Any)), caption: str | None) | dict(video: filepath, caption: str | None)]

 - predict(page_num, api_name="/reload_gallery_6") -> (txt2img, page, txt2img, txt2img)
    Parameters:
     - [Number] page_num: float (not required, defaults to:   1)
    Returns:
     - [Gallery] txt2img: list[dict(image: dict(path: str | None (Path to a local file), url: str | None (Publicly available url or base64 encoded image), size: int | None (Size of image in bytes), orig_name: str | None (Original filename), mime_type: str | None (mime type of image), is_stream: bool (Can always be set to False), meta: dict(str, Any)), caption: str | None) | dict(video: filepath, caption: str | None)]
     - [Number] page: float
     - [Gallery] txt2img: list[dict(image: dict(path: str | None (Path to a local file), url: str | None (Publicly available url or base64 encoded image), size: int | None (Size of image in bytes), orig_name: str | None (Original filename), mime_type: str | None (mime type of image), is_stream: bool (Can always be set to False), meta: dict(str, Any)), caption: str | None) | dict(video: filepath, caption: str | None)]
     - [Gallery] txt2img: list[dict(image: dict(path: str | None (Path to a local file), url: str | None (Publicly available url or base64 encoded image), size: int | None (Size of image in bytes), orig_name: str | None (Original filename), mime_type: str | None (mime type of image), is_stream: bool (Can always be set to False), meta: dict(str, Any)), caption: str | None) | dict(video: filepath, caption: str | None)]

 - predict(page_num, api_name="/reload_gallery_7") -> (txt2img, page, txt2img, txt2img)
    Parameters:
     - [Number] page_num: float (not required, defaults to:   1)
    Returns:
     - [Gallery] txt2img: list[dict(image: dict(path: str | None (Path to a local file), url: str | None (Publicly available url or base64 encoded image), size: int | None (Size of image in bytes), orig_name: str | None (Original filename), mime_type: str | None (mime type of image), is_stream: bool (Can always be set to False), meta: dict(str, Any)), caption: str | None) | dict(video: filepath, caption: str | None)]
     - [Number] page: float
     - [Gallery] txt2img: list[dict(image: dict(path: str | None (Path to a local file), url: str | None (Publicly available url or base64 encoded image), size: int | None (Size of image in bytes), orig_name: str | None (Original filename), mime_type: str | None (mime type of image), is_stream: bool (Can always be set to False), meta: dict(str, Any)), caption: str | None) | dict(video: filepath, caption: str | None)]
     - [Gallery] txt2img: list[dict(image: dict(path: str | None (Path to a local file), url: str | None (Publicly available url or base64 encoded image), size: int | None (Size of image in bytes), orig_name: str | None (Original filename), mime_type: str | None (mime type of image), is_stream: bool (Can always be set to False), meta: dict(str, Any)), caption: str | None) | dict(video: filepath, caption: str | None)]

 - predict(page_num, sort_inp, api_name="/reload_gallery_8") -> (txt2img, page, txt2img, txt2img)
    Parameters:
     - [Number] page_num: float (not required, defaults to:   1)
     - [Radio] sort_inp: Literal['Date (Oldest First)', 'Date (Newest First)', 'Name (A-Z)', 'Name (Z-A)'] (not required, defaults to:   Date (Oldest First))
    Returns:
     - [Gallery] txt2img: list[dict(image: dict(path: str | None (Path to a local file), url: str | None (Publicly available url or base64 encoded image), size: int | None (Size of image in bytes), orig_name: str | None (Original filename), mime_type: str | None (mime type of image), is_stream: bool (Can always be set to False), meta: dict(str, Any)), caption: str | None) | dict(video: filepath, caption: str | None)]
     - [Number] page: float
     - [Gallery] txt2img: list[dict(image: dict(path: str | None (Path to a local file), url: str | None (Publicly available url or base64 encoded image), size: int | None (Size of image in bytes), orig_name: str | None (Original filename), mime_type: str | None (mime type of image), is_stream: bool (Can always be set to False), meta: dict(str, Any)), caption: str | None) | dict(video: filepath, caption: str | None)]
     - [Gallery] txt2img: list[dict(image: dict(path: str | None (Path to a local file), url: str | None (Publicly available url or base64 encoded image), size: int | None (Size of image in bytes), orig_name: str | None (Original filename), mime_type: str | None (mime type of image), is_stream: bool (Can always be set to False), meta: dict(str, Any)), caption: str | None) | dict(video: filepath, caption: str | None)]

 - predict(api_name="/delete_img") -> (txt2img, page, txt2img, positive_prompt, negative_prompt, width, height, steps, sampler, scheduler, cfg, seed, path, metadata)
    Parameters:
     - None
    Returns:
     - [Gallery] txt2img: list[dict(image: dict(path: str | None (Path to a local file), url: str | None (Publicly available url or base64 encoded image), size: int | None (Size of image in bytes), orig_name: str | None (Original filename), mime_type: str | None (mime type of image), is_stream: bool (Can always be set to False), meta: dict(str, Any)), caption: str | None) | dict(video: filepath, caption: str | None)]
     - [Number] page: float
     - [Gallery] txt2img: list[dict(image: dict(path: str | None (Path to a local file), url: str | None (Publicly available url or base64 encoded image), size: int | None (Size of image in bytes), orig_name: str | None (Original filename), mime_type: str | None (mime type of image), is_stream: bool (Can always be set to False), meta: dict(str, Any)), caption: str | None) | dict(video: filepath, caption: str | None)]
     - [Textbox] positive_prompt: str
     - [Textbox] negative_prompt: str
     - [Number] width: float
     - [Number] height: float
     - [Number] steps: float
     - [Textbox] sampler: str
     - [Textbox] scheduler: str
     - [Number] cfg: float
     - [Number] seed: float
     - [Textbox] path: str
     - [Textbox] metadata: str

 - predict(models_folder, api_name="/reload_models_16") -> upscaler
    Parameters:
     - [Textbox] models_folder: str (not required, defaults to:   /kaggle/working/sd.cpp-webui/models/upscale_models/)
    Returns:
     - [Dropdown] upscaler: Literal[]

 - predict(height, width, api_name="/switch_sizes_4") -> (initial_height, initial_width)
    Parameters:
     - [Slider] height: float (not required, defaults to:   1024)
     - [Slider] width: float (not required, defaults to:   1024)
    Returns:
     - [Slider] initial_height: float (numeric value between 1 and 4096)
     - [Slider] initial_width: float (numeric value between 1 and 4096)

 - predict(img_inp, api_name="/size_updater") -> (initial_width, initial_height)
    Parameters:
     - [Image] img_inp: dict(path: str | None (Path to a local file), url: str | None (Publicly available url or base64 encoded image), size: int | None (Size of image in bytes), orig_name: str | None (Original filename), mime_type: str | None (mime type of image), is_stream: bool (Can always be set to False), meta: dict(str, Any)) (required)  (For input, either path or url must be provided. For output, path is always provided.)
    Returns:
     - [Slider] initial_width: float (numeric value between 1 and 4096)
     - [Slider] initial_height: float (numeric value between 1 and 4096)

 - predict(checkbox_value, api_name="/partial_14") -> (initial_width, initial_height)
    Parameters:
     - [Checkbox] checkbox_value: bool (not required, defaults to:   False)
    Returns:
     - [Slider] initial_width: float (numeric value between 1 and 4096)
     - [Slider] initial_height: float (numeric value between 1 and 4096)

 - predict(param_0, param_1, param_2, param_3, param_4, param_5, param_6, param_7, param_8, param_9, param_10, param_11, param_12, param_13, param_14, param_15, api_name="/upscale_wrapper") -> (stablediffusioncpp_command, progress, progress, statistics, generated_images)
    Parameters:
     - [Number] param_0: float (not required, defaults to:   0)
     - [Checkbox] param_1: bool (not required, defaults to:   False)
     - [Checkbox] param_2: bool (not required, defaults to:   False)
     - [Number] param_3: float (not required, defaults to:   0)
     - [Checkbox] param_4: bool (not required, defaults to:   False)
     - [Checkbox] param_5: bool (not required, defaults to:   False)
     - [Checkbox] param_6: bool (not required, defaults to:   True)
     - [Checkbox] param_7: bool (not required, defaults to:   False)
     - [Checkbox] param_8: bool (not required, defaults to:   False)
     - [Image] param_9: dict(path: str | None (Path to a local file), url: str | None (Publicly available url or base64 encoded image), size: int | None (Size of image in bytes), orig_name: str | None (Original filename), mime_type: str | None (mime type of image), is_stream: bool (Can always be set to False), meta: dict(str, Any)) (required)  (For input, either path or url must be provided. For output, path is always provided.)
     - [Slider] param_10: float (not required, defaults to:   1024)
     - [Slider] param_11: float (not required, defaults to:   1024)
     - [Textbox] param_12: str (not required, defaults to:   )
     - [Dropdown] param_13: Literal[] (not required, defaults to:   )
     - [Slider] param_14: float (not required, defaults to:   1)
     - [Checkbox] param_15: bool (not required, defaults to:   False)
    Returns:
     - [Textbox] stablediffusioncpp_command: str
     - [Slider] progress: float (numeric value between 0 and 100)
     - [Textbox] progress: str
     - [Textbox] statistics: str
     - [Gallery] generated_images: list[dict(image: dict(path: str | None (Path to a local file), url: str | None (Publicly available url or base64 encoded image), size: int | None (Size of image in bytes), orig_name: str | None (Original filename), mime_type: str | None (mime type of image), is_stream: bool (Can always be set to False), meta: dict(str, Any)), caption: str | None) | dict(video: filepath, caption: str | None)]

 - predict(api_name="/kill_subprocess_4") ->
    Parameters:
     - None
    Returns:
     - None

 - predict(model_type, api_name="/model_choice") -> value_2669
    Parameters:
     - [Dropdown] model_type: Literal['Checkpoint', 'UNET', 'VAE', 'clip_g', 'clip_l', 't5xxl', 'llm', 'TAESD', 'Lora', 'Embeddings', 'Upscaler', 'ControlNet'] (not required, defaults to:   Checkpoint)
    Returns:
     - [Textbox] value_2669: str

 - predict(models_folder, api_name="/reload_models_17") -> model
    Parameters:
     - [Textbox] models_folder: str (not required, defaults to:   /kaggle/working/sd.cpp-webui/models/checkpoints/)
    Returns:
     - [Dropdown] model: Literal['[illustrious]JANKUV5NSFWTrainedNoobai_v69.safetensors', '[illustrious]WAI-illustrious-SDXL.safetensors', '[illustrious]miaomiaoHarem_v195.safetensors', '[illustrious]miaomiaoRealskin_epsV14.safetensors']

 - predict(param_0, param_1, param_2, param_3, param_4, param_5, param_6, api_name="/convert_wrapper") -> (stablediffusioncpp_command, progress, status)
    Parameters:
     - [Checkbox] param_0: bool (not required, defaults to:   True)
     - [Textbox] param_1: str (not required, defaults to:   )
     - [Textbox] param_2: str (not required, defaults to:   /kaggle/working/sd.cpp-webui/models/checkpoints/)
     - [Dropdown] param_3: Literal['[illustrious]JANKUV5NSFWTrainedNoobai_v69.safetensors', '[illustrious]WAI-illustrious-SDXL.safetensors', '[illustrious]miaomiaoHarem_v195.safetensors', '[illustrious]miaomiaoRealskin_epsV14.safetensors'] (not required, defaults to:   [illustrious]JANKUV5NSFWTrainedNoobai_v69.safetensors)
     - [Dropdown] param_4: Literal['Default', 'f32', 'f16', 'q8_0', 'q6_K', 'q5_K', 'q5_1', 'q5_0', 'q4_K', 'q4_1', 'q4_0', 'q3_K', 'q2_K'] (not required, defaults to:   Default)
     - [Textbox] param_5: str (not required, defaults to:   )
     - [Checkbox] param_6: bool (not required, defaults to:   False)
    Returns:
     - [Textbox] stablediffusioncpp_command: str
     - [Slider] progress: float (numeric value between 0 and 100)
     - [Textbox] status: str

 - predict(api_name="/kill_subprocess_5") ->
    Parameters:
     - None
    Returns:
     - None

 - predict(models_folder, api_name="/reload_models_1_4") -> model
    Parameters:
     - [Textbox] models_folder: str (not required, defaults to:   /kaggle/working/sd.cpp-webui/models/checkpoints/)
    Returns:
     - [Dropdown] model: Literal['[illustrious]JANKUV5NSFWTrainedNoobai_v69.safetensors', '[illustrious]WAI-illustrious-SDXL.safetensors', '[illustrious]miaomiaoHarem_v195.safetensors', '[illustrious]miaomiaoRealskin_epsV14.safetensors']

 - predict(x, api_name="/lambda_24") ->
    Parameters:
     - [Dropdown] x: Literal['[illustrious]JANKUV5NSFWTrainedNoobai_v69.safetensors', '[illustrious]WAI-illustrious-SDXL.safetensors', '[illustrious]miaomiaoHarem_v195.safetensors', '[illustrious]miaomiaoRealskin_epsV14.safetensors'] (required)
    Returns:
     - None

 - predict(models_folder, api_name="/reload_models_18") -> checkpoint_model
    Parameters:
     - [Textbox] models_folder: str (not required, defaults to:   /kaggle/working/sd.cpp-webui/models/checkpoints/)
    Returns:
     - [Dropdown] checkpoint_model: Literal['[illustrious]JANKUV5NSFWTrainedNoobai_v69.safetensors', '[illustrious]WAI-illustrious-SDXL.safetensors', '[illustrious]miaomiaoHarem_v195.safetensors', '[illustrious]miaomiaoRealskin_epsV14.safetensors']

 - predict(api_name="/lambda_1_4") ->
    Parameters:
     - None
    Returns:
     - None

 - predict(x, api_name="/lambda_2_4") ->
    Parameters:
     - [Dropdown] x: Literal['ae.safetensors'] (required)
    Returns:
     - None

 - predict(models_folder, api_name="/reload_models_1_5") -> checkpoint_vae
    Parameters:
     - [Textbox] models_folder: str (not required, defaults to:   /kaggle/working/sd.cpp-webui/models/vae/)
    Returns:
     - [Dropdown] checkpoint_vae: Literal['ae.safetensors']

 - predict(api_name="/lambda_3_4") ->
    Parameters:
     - None
    Returns:
     - None

 - predict(x, api_name="/lambda_4_4") ->
    Parameters:
     - [Dropdown] x: Literal['z_image_turbo-Q8_0.gguf'] (required)
    Returns:
     - None

 - predict(models_folder, api_name="/reload_models_2_4") -> unet_model
    Parameters:
     - [Textbox] models_folder: str (not required, defaults to:   /kaggle/working/sd.cpp-webui/models/unet/)
    Returns:
     - [Dropdown] unet_model: Literal['z_image_turbo-Q8_0.gguf']

 - predict(api_name="/lambda_5_4") ->
    Parameters:
     - None
    Returns:
     - None

 - predict(x, api_name="/lambda_6_4") ->
    Parameters:
     - [Dropdown] x: Literal['ae.safetensors'] (required)
    Returns:
     - None

 - predict(models_folder, api_name="/reload_models_3_4") -> unet_vae
    Parameters:
     - [Textbox] models_folder: str (not required, defaults to:   /kaggle/working/sd.cpp-webui/models/vae/)
    Returns:
     - [Dropdown] unet_vae: Literal['ae.safetensors']

 - predict(api_name="/lambda_7_4") ->
    Parameters:
     - None
    Returns:
     - None

 - predict(x, api_name="/lambda_8_4") ->
    Parameters:
     - [Dropdown] x: Literal['Qwen3-4B-Instruct-2507-Q4_K_M.gguf'] (required)
    Returns:
     - None

 - predict(models_folder, api_name="/reload_models_4_4") -> clip_g
    Parameters:
     - [Textbox] models_folder: str (not required, defaults to:   /kaggle/working/sd.cpp-webui/models/text_encoders/)
    Returns:
     - [Dropdown] clip_g: Literal['Qwen3-4B-Instruct-2507-Q4_K_M.gguf']

 - predict(api_name="/lambda_9_4") ->
    Parameters:
     - None
    Returns:
     - None

 - predict(x, api_name="/lambda_10_4") ->
    Parameters:
     - [Dropdown] x: Literal['Qwen3-4B-Instruct-2507-Q4_K_M.gguf'] (required)
    Returns:
     - None

 - predict(models_folder, api_name="/reload_models_5_4") -> clip_l
    Parameters:
     - [Textbox] models_folder: str (not required, defaults to:   /kaggle/working/sd.cpp-webui/models/text_encoders/)
    Returns:
     - [Dropdown] clip_l: Literal['Qwen3-4B-Instruct-2507-Q4_K_M.gguf']

 - predict(api_name="/lambda_11_3") ->
    Parameters:
     - None
    Returns:
     - None

 - predict(x, api_name="/lambda_12_3") ->
    Parameters:
     - [Dropdown] x: Literal['Qwen3-4B-Instruct-2507-Q4_K_M.gguf'] (required)
    Returns:
     - None

 - predict(models_folder, api_name="/reload_models_6_4") -> clip_vision_h
    Parameters:
     - [Textbox] models_folder: str (not required, defaults to:   /kaggle/working/sd.cpp-webui/models/text_encoders/)
    Returns:
     - [Dropdown] clip_vision_h: Literal['Qwen3-4B-Instruct-2507-Q4_K_M.gguf']

 - predict(api_name="/lambda_13_3") ->
    Parameters:
     - None
    Returns:
     - None

 - predict(x, api_name="/lambda_14_3") ->
    Parameters:
     - [Dropdown] x: Literal['Qwen3-4B-Instruct-2507-Q4_K_M.gguf'] (required)
    Returns:
     - None

 - predict(models_folder, api_name="/reload_models_7_4") -> t5xxl
    Parameters:
     - [Textbox] models_folder: str (not required, defaults to:   /kaggle/working/sd.cpp-webui/models/text_encoders/)
    Returns:
     - [Dropdown] t5xxl: Literal['Qwen3-4B-Instruct-2507-Q4_K_M.gguf']

 - predict(api_name="/lambda_15_2") ->
    Parameters:
     - None
    Returns:
     - None

 - predict(x, api_name="/lambda_16_2") ->
    Parameters:
     - [Dropdown] x: Literal['Qwen3-4B-Instruct-2507-Q4_K_M.gguf'] (required)
    Returns:
     - None

 - predict(models_folder, api_name="/reload_models_8_3") -> umt5_xxl
    Parameters:
     - [Textbox] models_folder: str (not required, defaults to:   /kaggle/working/sd.cpp-webui/models/text_encoders/)
    Returns:
     - [Dropdown] umt5_xxl: Literal['Qwen3-4B-Instruct-2507-Q4_K_M.gguf']

 - predict(api_name="/lambda_17_2") ->
    Parameters:
     - None
    Returns:
     - None

 - predict(x, api_name="/lambda_18_2") ->
    Parameters:
     - [Dropdown] x: Literal['Qwen3-4B-Instruct-2507-Q4_K_M.gguf'] (required)
    Returns:
     - None

 - predict(models_folder, api_name="/reload_models_9_3") -> llm
    Parameters:
     - [Textbox] models_folder: str (not required, defaults to:   /kaggle/working/sd.cpp-webui/models/text_encoders/)
    Returns:
     - [Dropdown] llm: Literal['Qwen3-4B-Instruct-2507-Q4_K_M.gguf']

 - predict(api_name="/lambda_19_2") ->
    Parameters:
     - None
    Returns:
     - None

 - predict(height, width, api_name="/switch_sizes_5") -> (height, width)
    Parameters:
     - [Slider] height: float (not required, defaults to:   1024)
     - [Slider] width: float (not required, defaults to:   1024)
    Returns:
     - [Slider] height: float (numeric value between 64 and 4096)
     - [Slider] width: float (numeric value between 64 and 4096)

 - predict(checkbox_value, api_name="/partial_15") -> flow_shift
    Parameters:
     - [Checkbox] checkbox_value: bool (not required, defaults to:   False)
    Returns:
     - [Number] flow_shift: float

 - predict(x, api_name="/lambda_20_2") ->
    Parameters:
     - [Checkbox] x: bool (not required, defaults to:   False)
    Returns:
     - None

 - predict(checkbox_value, api_name="/partial_1_4") -> guidance
    Parameters:
     - [Checkbox] checkbox_value: bool (not required, defaults to:   False)
    Returns:
     - [Slider] guidance: float (numeric value between 0 and 30)

 - predict(x, api_name="/lambda_21_1") ->
    Parameters:
     - [Checkbox] x: bool (not required, defaults to:   False)
    Returns:
     - None

 - predict(api_name="/random_seed_4") -> seed
    Parameters:
     - None
    Returns:
     - [Number] seed: float

 - predict(models_folder, api_name="/reload_models_10_2") -> taesd
    Parameters:
     - [Textbox] models_folder: str (not required, defaults to:   /kaggle/working/sd.cpp-webui/models/taesd/)
    Returns:
     - [Dropdown] taesd: Literal[]

 - predict(checkbox_value, api_name="/partial_2_4") -> (vae_tile_overlap, vae_tile_size, enable_vae_relative_tile_size)
    Parameters:
     - [Checkbox] checkbox_value: bool (not required, defaults to:   False)
    Returns:
     - [Slider] vae_tile_overlap: float (numeric value between 0 and 1)
     - [Number] vae_tile_size: float
     - [Checkbox] enable_vae_relative_tile_size: bool

 - predict(checkbox_value, api_name="/partial_3_4") -> vae_relative_tile_size
    Parameters:
     - [Checkbox] checkbox_value: bool (not required, defaults to:   False)
    Returns:
     - [Number] vae_relative_tile_size: float

 - predict(checkbox_value, api_name="/partial_4_4") -> (cache_mode, cachedit_preset, cache_option, scm_mask, scm_policy)
    Parameters:
     - [Checkbox] checkbox_value: bool (not required, defaults to:   False)
    Returns:
     - [Dropdown] cache_mode: Literal['easycache', 'ucache', 'dbcache', 'taylorseer', 'cache-dit', 'spectrum']
     - [Dropdown] cachedit_preset: Literal['none', 'slow', 'medium', 'fast', 'ultra']
     - [Textbox] cache_option: str
     - [Textbox] scm_mask: str
     - [Dropdown] scm_policy: Literal['none', 'dynamic', 'static']

 - predict(checkbox_value, api_name="/partial_5_4") -> (preview_mode, preview_interval, taesd_for_preview_only, preview_noisy)
    Parameters:
     - [Checkbox] checkbox_value: bool (not required, defaults to:   False)
    Returns:
     - [Dropdown] preview_mode: Literal['none', 'proj', 'tae', 'vae']
     - [Number] preview_interval: float
     - [Checkbox] taesd_for_preview_only: bool
     - [Checkbox] preview_noisy: bool

 - predict(param_0, param_1, param_2, param_3, param_4, param_5, param_6, param_7, param_8, param_9, param_10, param_11, param_12, param_13, param_14, param_15, param_16, param_17, param_18, param_19, param_20, param_21, param_22, param_23, param_24, param_25, param_26, param_27, param_28, param_29, param_30, param_31, param_32, param_33, param_34, param_35, param_36, param_37, param_38, param_39, param_40, param_41, param_42, param_43, param_44, param_45, param_46, param_47, param_48, param_49, param_50, param_51, param_52, param_53, param_54, param_55, param_56, param_57, param_58, param_59, param_60, param_61, param_62, param_63, param_64, param_65, param_66, param_67, param_68, param_69, param_70, param_71, param_72, param_73, param_74, param_75, param_76, param_77, param_78, param_79, param_80, api_name="/save_settings_wrapper") -> status
    Parameters:
     - [Textbox] param_0: str (not required, defaults to:   /kaggle/working/sd.cpp-webui/outputs/any2video/)
     - [Textbox] param_1: str (not required, defaults to:   /kaggle/working/sd.cpp-webui/models/checkpoints/)
     - [Textbox] param_2: str (not required, defaults to:   /kaggle/working/sd.cpp-webui/models/controlnet/)
     - [Slider] param_3: float (not required, defaults to:   1)
     - [Checkbox] param_4: bool (not required, defaults to:   False)
     - [Dropdown] param_5: Literal['none', 'slow', 'medium', 'fast', 'ultra'] (not required, defaults to:   none)
     - [Dropdown] param_6: Literal['easycache', 'ucache', 'dbcache', 'taylorseer', 'cache-dit', 'spectrum'] (not required, defaults to:   easycache)
     - [Slider] param_7: float (not required, defaults to:   1.0)
     - [Dropdown] param_8: Literal['[illustrious]JANKUV5NSFWTrainedNoobai_v69.safetensors', '[illustrious]WAI-illustrious-SDXL.safetensors', '[illustrious]miaomiaoHarem_v195.safetensors', '[illustrious]miaomiaoRealskin_epsV14.safetensors'] (required)
     - [Dropdown] param_9: Literal['ae.safetensors'] (required)
     - [Checkbox] param_10: bool (not required, defaults to:   False)
     - [Dropdown] param_11: Literal['Qwen3-4B-Instruct-2507-Q4_K_M.gguf'] (required)
     - [Dropdown] param_12: Literal['Qwen3-4B-Instruct-2507-Q4_K_M.gguf'] (required)
     - [Slider] param_13: float (not required, defaults to:   -1)
     - [Dropdown] param_14: Literal['Qwen3-4B-Instruct-2507-Q4_K_M.gguf'] (required)
     - [Checkbox] param_15: bool (not required, defaults to:   True)
     - [Checkbox] param_16: bool (not required, defaults to:   False)
     - [Number] param_17: float (not required, defaults to:   0)
     - [Checkbox] param_18: bool (not required, defaults to:   False)
     - [Checkbox] param_19: bool (not required, defaults to:   False)
     - [Number] param_20: float (not required, defaults to:   0)
     - [Checkbox] param_21: bool (not required, defaults to:   False)
     - [Checkbox] param_22: bool (not required, defaults to:   False)
     - [Checkbox] param_23: bool (not required, defaults to:   False)
     - [Number] param_24: float (not required, defaults to:   3.0)
     - [Checkbox] param_25: bool (not required, defaults to:   False)
     - [Checkbox] param_26: bool (not required, defaults to:   False)
     - [Radio] param_27: Literal['Date (Oldest First)', 'Date (Newest First)', 'Name (A-Z)', 'Name (Z-A)'] (not required, defaults to:   Date (Oldest First))
     - [Slider] param_28: float (not required, defaults to:   3.5)
     - [Checkbox] param_29: bool (not required, defaults to:   False)
     - [Slider] param_30: float (not required, defaults to:   1024)
     - [Dropdown] param_31: Literal['Qwen3-4B-Instruct-2507-Q4_K_M.gguf'] (required)
     - [Dropdown] param_32: Literal['auto', 'immediately', 'at_runtime'] (not required, defaults to:   auto)
     - [Checkbox] param_33: bool (not required, defaults to:   False)
     - [Textbox] param_34: str (not required, defaults to:   )
     - [Checkbox] param_35: bool (not required, defaults to:   False)
     - [Dropdown] param_36: Literal['Sequential', 'Timestamp', 'TimestampMS', 'EpochTime'] (not required, defaults to:   Sequential)
     - [Checkbox] param_37: bool (not required, defaults to:   False)
     - [Dropdown] param_38: Literal['Default', 'eps', 'v', 'edm_v', 'sd3_flow', 'flux_flow', 'flux2_flow'] (not required, defaults to:   Default)
     - [Checkbox] param_39: bool (not required, defaults to:   False)
     - [Number] param_40: float (not required, defaults to:   1)
     - [Dropdown] param_41: Literal['none', 'proj', 'tae', 'vae'] (not required, defaults to:   none)
     - [Checkbox] param_42: bool (not required, defaults to:   False)
     - [Checkbox] param_43: bool (not required, defaults to:   False)
     - [Dropdown] param_44: Literal['std_default', 'cuda', 'cpu'] (not required, defaults to:   cuda)
     - [Dropdown] param_45: Literal['std_default', 'cuda', 'cpu'] (not required, defaults to:   cuda)
     - [Dropdown] param_46: Literal['euler', 'euler_a', 'heun', 'dpm2', 'dpm++2s_a', 'dpm++2m', 'dpm++2mv2', 'ipndm', 'ipndm_v', 'lcm', 'ddim_trailing', 'tcd', 'res_multistep', 'res_2s'] (not required, defaults to:   euler)
     - [Dropdown] param_47: Literal['discrete', 'karras', 'exponential', 'ays', 'gits', 'smoothstep', 'sgm_uniform', 'simple', 'kl_optimal', 'lcm', 'bong_tangent'] (not required, defaults to:   discrete)
     - [Number] param_48: float (not required, defaults to:   -1)
     - [Slider] param_49: float (not required, defaults to:   8)
     - [Dropdown] param_50: Literal['Qwen3-4B-Instruct-2507-Q4_K_M.gguf'] (required)
     - [Dropdown] param_51: Literal[] (required)
     - [Dropdown] param_52: Literal['base', 'default', 'origin', 'citrus', 'monochrome', 'soft', 'glass', 'ocean'] (not required, defaults to:   default)
     - [Number] param_53: float (not required, defaults to:   0)
     - [Dropdown] param_54: Literal['Qwen3-4B-Instruct-2507-Q4_K_M.gguf'] (required)
     - [Dropdown] param_55: Literal['z_image_turbo-Q8_0.gguf'] (required)
     - [Dropdown] param_56: Literal['ae.safetensors'] (required)
     - [Checkbox] param_57: bool (not required, defaults to:   False)
     - [Checkbox] param_58: bool (not required, defaults to:   False)
     - [Checkbox] param_59: bool (not required, defaults to:   False)
     - [Number] param_60: float (not required, defaults to:   0)
     - [Slider] param_61: float (not required, defaults to:   0.5)
     - [Number] param_62: float (not required, defaults to:   32)
     - [Checkbox] param_63: bool (not required, defaults to:   False)
     - [Checkbox] param_64: bool (not required, defaults to:   False)
     - [Slider] param_65: float (not required, defaults to:   1024)
     - [Textbox] param_66: str (not required, defaults to:   /kaggle/working/sd.cpp-webui/models/embeddings/)
     - [Checkbox] param_67: bool (not required, defaults to:   True)
     - [Textbox] param_68: str (not required, defaults to:   123)
     - [Textbox] param_69: str (not required, defaults to:   /kaggle/working/sd.cpp-webui/outputs/img2img/)
     - [Dropdown] param_70: Literal['Default', 'f32', 'f16', 'q8_0', 'q6_K', 'q5_K', 'q5_1', 'q5_0', 'q4_K', 'q4_1', 'q4_0', 'q3_K', 'q2_K'] (not required, defaults to:   Default)
     - [Textbox] param_71: str (not required, defaults to:   )
     - [Textbox] param_72: str (not required, defaults to:   /kaggle/working/sd.cpp-webui/models/loras/)
     - [Textbox] param_73: str (not required, defaults to:   /kaggle/working/sd.cpp-webui/models/photomaker/)
     - [Dropdown] param_74: Literal['Default', 'eps', 'v', 'edm_v', 'sd3_flow', 'flux_flow', 'flux2_flow'] (not required, defaults to:   Default)
     - [Textbox] param_75: str (not required, defaults to:   /kaggle/working/sd.cpp-webui/models/taesd/)
     - [Textbox] param_76: str (not required, defaults to:   /kaggle/working/sd.cpp-webui/outputs/txt2img/)
     - [Textbox] param_77: str (not required, defaults to:   /kaggle/working/sd.cpp-webui/models/text_encoders/)
     - [Textbox] param_78: str (not required, defaults to:   /kaggle/working/sd.cpp-webui/models/unet/)
     - [Textbox] param_79: str (not required, defaults to:   /kaggle/working/sd.cpp-webui/models/upscale_models/)
     - [Textbox] param_80: str (not required, defaults to:   /kaggle/working/sd.cpp-webui/models/vae/)
    Returns:
     - [Textbox] status: str

 - predict(api_name="/reset_defaults") -> status
    Parameters:
     - None
    Returns:
     - [Textbox] status: str

 - predict(api_name="/refresh_all_options_4") -> (sampling_method, scheduler, preview_mode, prediction)
    Parameters:
     - None
    Returns:
     - [Dropdown] sampling_method: Literal['euler', 'euler_a', 'heun', 'dpm2', 'dpm++2s_a', 'dpm++2m', 'dpm++2mv2', 'ipndm', 'ipndm_v', 'lcm', 'ddim_trailing', 'tcd', 'res_multistep', 'res_2s']
     - [Dropdown] scheduler: Literal['discrete', 'karras', 'exponential', 'ays', 'gits', 'smoothstep', 'sgm_uniform', 'simple', 'kl_optimal', 'lcm', 'bong_tangent']
     - [Dropdown] preview_mode: Literal['none', 'proj', 'tae', 'vae']
     - [Dropdown] prediction: Literal['Default', 'eps', 'v', 'edm_v', 'sd3_flow', 'flux_flow', 'flux2_flow']

 - predict(page, ctrl, api_name="/lazy_load_gallery") -> (txt2img, page, txt2img, txt2img)
    Parameters:
     - [Textbox] page: str (not required, defaults to:   1)
     - [Textbox] ctrl: str (not required, defaults to:   0)
    Returns:
     - [Gallery] txt2img: list[dict(image: dict(path: str | None (Path to a local file), url: str | None (Publicly available url or base64 encoded image), size: int | None (Size of image in bytes), orig_name: str | None (Original filename), mime_type: str | None (mime type of image), is_stream: bool (Can always be set to False), meta: dict(str, Any)), caption: str | None) | dict(video: filepath, caption: str | None)]
     - [Number] page: float
     - [Gallery] txt2img: list[dict(image: dict(path: str | None (Path to a local file), url: str | None (Publicly available url or base64 encoded image), size: int | None (Size of image in bytes), orig_name: str | None (Original filename), mime_type: str | None (mime type of image), is_stream: bool (Can always be set to False), meta: dict(str, Any)), caption: str | None) | dict(video: filepath, caption: str | None)]
     - [Gallery] txt2img: list[dict(image: dict(path: str | None (Path to a local file), url: str | None (Publicly available url or base64 encoded image), size: int | None (Size of image in bytes), orig_name: str | None (Original filename), mime_type: str | None (mime type of image), is_stream: bool (Can always be set to False), meta: dict(str, Any)), caption: str | None) | dict(video: filepath, caption: str | None)]

 - predict(param_0, param_1, param_2, param_3, param_4, param_5, param_6, param_7, param_8, api_name="/copy_fn") -> (positive_prompt, negative_prompt, width, height, steps, sampling_method, scheduler, cfg_scale, seed)
    Parameters:
     - [Textbox] param_0: str (not required, defaults to:   )
     - [Textbox] param_1: str (not required, defaults to:   )
     - [Number] param_2: float (required)
     - [Number] param_3: float (required)
     - [Number] param_4: float (required)
     - [Textbox] param_5: str (not required, defaults to:   )
     - [Textbox] param_6: str (not required, defaults to:   )
     - [Number] param_7: float (required)
     - [Number] param_8: float (required)
    Returns:
     - [Textbox] positive_prompt: str
     - [Textbox] negative_prompt: str
     - [Slider] width: float (numeric value between 64 and 4096)
     - [Slider] height: float (numeric value between 64 and 4096)
     - [Slider] steps: float (numeric value between 1 and 100)
     - [Dropdown] sampling_method: Literal['euler', 'euler_a', 'heun', 'dpm2', 'dpm++2s_a', 'dpm++2m', 'dpm++2mv2', 'ipndm', 'ipndm_v', 'lcm', 'ddim_trailing', 'tcd', 'res_multistep', 'res_2s']
     - [Dropdown] scheduler: Literal['discrete', 'karras', 'exponential', 'ays', 'gits', 'smoothstep', 'sgm_uniform', 'simple', 'kl_optimal', 'lcm', 'bong_tangent']
     - [Slider] cfg_scale: float (numeric value between 1 and 30)
     - [Number] seed: float

 - predict(param_0, param_1, param_2, param_3, param_4, param_5, param_6, param_7, param_8, param_9, api_name="/copy_fn_1") -> (positive_prompt, negative_prompt, width, height, steps, sampling_method, scheduler, cfg_scale, seed, value_1132)
    Parameters:
     - [Textbox] param_0: str (not required, defaults to:   )
     - [Textbox] param_1: str (not required, defaults to:   )
     - [Number] param_2: float (required)
     - [Number] param_3: float (required)
     - [Number] param_4: float (required)
     - [Textbox] param_5: str (not required, defaults to:   )
     - [Textbox] param_6: str (not required, defaults to:   )
     - [Number] param_7: float (required)
     - [Number] param_8: float (required)
     - [Textbox] param_9: str (not required, defaults to:   )
    Returns:
     - [Textbox] positive_prompt: str
     - [Textbox] negative_prompt: str
     - [Slider] width: float (numeric value between 64 and 4096)
     - [Slider] height: float (numeric value between 64 and 4096)
     - [Slider] steps: float (numeric value between 1 and 100)
     - [Dropdown] sampling_method: Literal['euler', 'euler_a', 'heun', 'dpm2', 'dpm++2s_a', 'dpm++2m', 'dpm++2mv2', 'ipndm', 'ipndm_v', 'lcm', 'ddim_trailing', 'tcd', 'res_multistep', 'res_2s']
     - [Dropdown] scheduler: Literal['discrete', 'karras', 'exponential', 'ays', 'gits', 'smoothstep', 'sgm_uniform', 'simple', 'kl_optimal', 'lcm', 'bong_tangent']
     - [Slider] cfg_scale: float (numeric value between 1 and 30)
     - [Number] seed: float
     - [Image] value_1132: dict(path: str | None (Path to a local file), url: str | None (Publicly available url or base64 encoded image), size: int | None (Size of image in bytes), orig_name: str | None (Original filename), mime_type: str | None (mime type of image), is_stream: bool (Can always be set to False), meta: dict(str, Any))

 - predict(param_0, param_1, param_2, api_name="/copy_fn_2") -> (width, height, value_1862)
    Parameters:
     - [Number] param_0: float (required)
     - [Number] param_1: float (required)
     - [Textbox] param_2: str (not required, defaults to:   )
    Returns:
     - [Slider] width: float (numeric value between 64 and 4096)
     - [Slider] height: float (numeric value between 64 and 4096)
     - [Image] value_1862: dict(path: str | None (Path to a local file), url: str | None (Publicly available url or base64 encoded image), size: int | None (Size of image in bytes), orig_name: str | None (Original filename), mime_type: str | None (mime type of image), is_stream: bool (Can always be set to False), meta: dict(str, Any))

 - predict(param_0, param_1, param_2, param_3, param_4, param_5, param_6, param_7, param_8, param_9, api_name="/copy_fn_3") -> (positive_prompt, negative_prompt, width, height, steps, sampling_method, scheduler, cfg_scale, seed)
    Parameters:
     - [Textbox] param_0: str (not required, defaults to:   )
     - [Textbox] param_1: str (not required, defaults to:   )
     - [Number] param_2: float (required)
     - [Number] param_3: float (required)
     - [Number] param_4: float (required)
     - [Textbox] param_5: str (not required, defaults to:   )
     - [Textbox] param_6: str (not required, defaults to:   )
     - [Number] param_7: float (required)
     - [Number] param_8: float (required)
     - [Textbox] param_9: str (not required, defaults to:   )
    Returns:
     - [Textbox] positive_prompt: str
     - [Textbox] negative_prompt: str
     - [Slider] width: float (numeric value between 64 and 4096)
     - [Slider] height: float (numeric value between 64 and 4096)
     - [Slider] steps: float (numeric value between 1 and 100)
     - [Dropdown] sampling_method: Literal['euler', 'euler_a', 'heun', 'dpm2', 'dpm++2s_a', 'dpm++2m', 'dpm++2mv2', 'ipndm', 'ipndm_v', 'lcm', 'ddim_trailing', 'tcd', 'res_multistep', 'res_2s']
     - [Dropdown] scheduler: Literal['discrete', 'karras', 'exponential', 'ays', 'gits', 'smoothstep', 'sgm_uniform', 'simple', 'kl_optimal', 'lcm', 'bong_tangent']
     - [Slider] cfg_scale: float (numeric value between 1 and 30)
     - [Number] seed: float

 - predict(param_0, api_name="/copy_fn_4") -> value_2542
    Parameters:
     - [Textbox] param_0: str (not required, defaults to:   )
    Returns:
     - [Image] value_2542: dict(path: str | None (Path to a local file), url: str | None (Publicly available url or base64 encoded image), size: int | None (Size of image in bytes), orig_name: str | None (Original filename), mime_type: str | None (mime type of image), is_stream: bool (Can always be set to False), meta: dict(str, Any))

 - predict(api_name="/restart_server") ->
    Parameters:
     - None
    Returns:
     - None
```
-->

## Python 调用示例（推荐）
> 使用 `gradio_client` 会自动处理文件上传与返回值解析。

```python
from gradio_client import Client

client = Client("http://localhost:7860/")
api = client.view_api()  # 查看各 endpoint 的参数顺序和默认值

# 仅保留同步生成端点（*_api_generate）
for name, info in api.items():
    if name.endswith("_api_generate"):
        print(name, "->", info["returns"])

# 示例：txt2img
# data = [...]  # 依据 gradio_api.json 里的 parameters 顺序填充
result = client.predict(*data, api_name="txt2img_api_generate")

# 示例：img2img
# data = [...]  # 依据 gradio_api.json 里的 parameters 顺序填充
result = client.predict(*data, api_name="img2img_api_generate")

# 示例：imgedit
# data = [...]  # 依据 gradio_api.json 里的 parameters 顺序填充
result = client.predict(*data, api_name="imgedit_api_generate")
```

## HTTP 调用示例（REST）
> REST 需要按顺序构造 `data` 数组。

```bash
curl -X POST http://localhost:7860/api/txt2img_api_generate \
  -H "Content-Type: application/json" \
  -d '{"data": [/* 与 API Schema 顺序一致的参数 */]}'
```

## 常用输入参数（非完整列表）
以下为常用参数名示例（以 `in_` 前缀为主），具体以 `gradio_api.json` 为准：

- 文本提示：`in_pprompt`, `in_nprompt`
- 图像尺寸：`in_width`, `in_height`
- 采样设置：`in_steps`, `in_cfg`, `in_sampling`, `in_scheduler`, `in_seed`
- 批量：`in_batch_count`
- img2img 输入图：`in_img_inp`
- img2img 遮罩：`in_img_mask`

## 输出说明
同步生成 API 返回 `img_final` 对应的结果：

- 图像类任务：返回图片列表
- any2video：返回视频列表（与 UI 的 `Gallery` 行为一致）

## 注意事项
- `server` 模式下必须先在 UI 中点击 **Start server** 启动 sd.cpp 后端，否则生成会失败。
- 如果启用加密输出，API 仍会返回可展示的解密后图片（逻辑见 [`modules/utils/ui_events.py`](modules/utils/ui_events.py:114)）。
