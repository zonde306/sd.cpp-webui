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

## Python 调用示例（推荐）
> 使用 `gradio_client` 会自动处理文件上传与返回值解析。

```python
from gradio_client import Client

client = Client("http://localhost:7860/")
api = client.view_api()  # 查看各 endpoint 的参数顺序和默认值

# 以 txt2img 为例，构造参数列表（顺序需与 API Schema 一致）
# data = [...]  # 依据 gradio_api.json 里的 parameters 顺序填充

result = client.predict(*data, api_name="txt2img_api_generate")
# result 为图片列表（通常是 PIL.Image 或本地文件路径，取决于 client 配置）
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
