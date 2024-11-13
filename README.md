# ComfyUI API Integration Automated Suite

**Read this in other languages: [中文](README_zh.md).**

## Project Overview

This project provides a comprehensive suite for developers to integrate ComfyUI APIs and automate image generation workflows. By encapsulating API input and output, this suite enables developers to input any workflow json file and receive the processed output image directly. It simplifies the integration process with ComfyUI, enhances efficiency, and includes several practical custom workflows.

## Motivation

The motivation behind this project was that I developed a program to easily use ComfyUI's workflows to provide users with AI image processing features such as model outfit changing, model generation, face swapping, and intelligent object removal. When a user sends a request, the backend needs to correctly load the parameters, upload the input image to ComfyUI, trigger the workflow execution, and ultimately obtain the execution status and output image result.

## Features

- **ComfyUI API Collection & Testing**: A complete set of ComfyUI APIs, with specific testing on all APIs required for this streamlined workflow.
- **ComfyUI API Encapsulation**: Streamlines API usage by handling input/output formats for seamless integration.
- **Automated Workflow Execution**: Allows users to input images and receive the processed result based on selected workflows.

## ComfyUI API
[API Documentation](docs/comfyui-api.md)

Additionally, to address cases where the server cannot open the WebSocket protocol, the code does not use WebSocket to query task status. If needed, you can refer to the official sample code.

[Official API Example](https://github.com/comfyanonymous/ComfyUI/blob/master/script_examples/websockets_api_example.py)

## Quick Start

1. **Installation**

```bash
# Clone the repository
git clone https://github.com/yourusername/comfyui-workflow-suite.git
cd comfyui-workflow-suite

# Install dependencies
pip install -r requirements.txt
```

1. **Usage**

```bash
python main.py --server-url 'your-server-address' --download-path 'path-to-save-image' --workflow-path 'workflow-json-path' --parameters 'workflow-json-parameters'

e.g. python main.py --server-url 'http://127.0.0.1:8188' --download-path '/Downloads' --workflow-path '/Documents/generate_image.json' --paramters '{"5": ["text", "masterpiece best quality man"], "10": ["image", "/Downloads/test.png"]}'
```

Setting of parameters, example:

```
prompt_text = """
{
    "3": {
        "class_type": "KSampler",
        "inputs": {
            "cfg": 8,
            "denoise": 1,
            "latent_image": [
                "5",
                0
            ],
            "model": [
                "4",
                0
            ],
            "negative": [
                "7",
                0
            ],
            "positive": [
                "6",
                0
            ],
            "sampler_name": "euler",
            "scheduler": "normal",
            "seed": 8566257,
            "steps": 20
        }
    },
    "4": {
        "class_type": "CheckpointLoaderSimple",
        "inputs": {
            "ckpt_name": "v1-5-pruned-emaonly.safetensors"
        }
    },
    "5": {
        "class_type": "EmptyLatentImage",
        "inputs": {
            "batch_size": 1,
            "height": 512,
            "width": 512
        }
    },
    "6": {
        "class_type": "CLIPTextEncode",
        "inputs": {
            "clip": [
                "4",
                1
            ],
            "text": "masterpiece best quality girl"
        }
    },
    "7": {
        "class_type": "CLIPTextEncode",
        "inputs": {
            "clip": [
                "4",
                1
            ],
            "text": "bad hands"
        }
    },
    "8": {
        "class_type": "VAEDecode",
        "inputs": {
            "samples": [
                "3",
                0
            ],
            "vae": [
                "4",
                2
            ]
        }
    },
    "9": {
        "class_type": "SaveImage",
        "inputs": {
            "filename_prefix": "ComfyUI",
            "images": [
                "8",
                0
            ]
        }
    }
}
"""

#set the text prompt for our positive CLIPTextEncode
prompt["6"]["inputs"]["text"] = "masterpiece best quality man"

#set the seed for our KSampler node
prompt["3"]["inputs"]["seed"] = 5
```

### Example 1: Model Outfit Change

<img src="images/cloth_change_body.png" alt="Model" width="45%"><img src="images/cloth_change_result.png" alt="Result" width="45%">

### Example 2: Model Face Change

<img src="images/model_change_body.png" alt="Model" width="45%"><img src="images/model_change_result.png" alt="Result" width="45%">