# comfyui-api-zh

**其他语言版本: [English](comfyui-api.md)

## **GET /history**

GET /history

获取所有历史任务数据

### **请求参数**

| **名称** | **位置** | **类型** | **必选** | **说明** |
| --- | --- | --- | --- | --- |
| prompt_id | query | string | 否 | a4e402f4-ab96-4e52-a4f3-33899599c67b |

## **GET /history/{prompt_id}**

GET /history/a4e402f4-ab96-4e52-a4f3-33899599c67b

获取特定任务ID的历史数据

## **POST /upload/image**

POST /upload/image

上传图片至服务器comfyui目录下

> Body 请求参数
> 

```
image: string
```

### **请求参数**

| **名称** | **位置** | **类型** | **必选** | **说明** |
| --- | --- | --- | --- | --- |
| body | body | object | 否 | none |
| image | body | string(binary) | 是 | 图片将以二进制格式发送到服务器 |

> 返回示例
> 

> 成功
> 

```
{
  "name": "test.png",
  "subfolder": "",
  "type": "input"
}
```

## **POST /upload/mask**

POST /upload/mask

上传蒙版图片至服务器comfyui目录下

> Body 请求参数
> 

```
image: string
type: input
subfolder: mask
original_ref: "{"filename":"test.png","type":"input","subfolder":"mask"}"
```

### **请求参数**

| **名称** | **位置** | **类型** | **必选** | **说明** |
| --- | --- | --- | --- | --- |
| body | body | object | 否 | none |
| image | body | string(binary) | 是 | 图片将以二进制格式发送到服务器 |
| type | body | string | 否 | 上传图片的目标文件夹 |
| subfolder | body | string | 否 | 上传图片的目标子文件夹 |
| original_ref | body | string | 是 | 无 |

> 返回示例
> 

> 成功
> 

```
{
  "name": "test.png",
  "subfolder": "mask",
  "type": "input"
}
```

## **GET /view**

GET /view

在线预览图片

### **请求参数**

| **名称** | **位置** | **类型** | **必选** | **说明** |
| --- | --- | --- | --- | --- |
| filename | query | string | 是 | 图片名称 |
| type | query | string | 否 | 图片存放位置的文件夹（input为上传的图片，output为生成的图片） |
| subfolder | query | string | 否 | 子文件夹(没有可不填) |
| preview | query | string | 否 | 预览 |
| channel | query | string | 否 | 无 |

> 返回示例
> 

> 成功
> 

```
"<img src=\"blob:file:///a4e402f4-ab96-4e52-a4f3-33899599c67b\" alt=\"comfyuiapi\" />"
```

## **GET /prompt**

GET /prompt

获取当前剩余任务列队的数量

> 返回示例
> 

> 成功
> 

```
{
  "exec_info": {
    "queue_remaining": 1
  }
}
```

## **POST /prompt**

POST /prompt

根据workflow的json执行任务下发，返回任务ID信息。 

> Body 请求参数
> 

```
{
  "client_id": "3c5662b1-4b59-47ea-ba7d-e3f2cd9eb36f",
  "prompt": {
		 <workflow.json>
  }
}

```

### **请求参数**

| **名称** | **位置** | **类型** | **必选** | **说明** |
| --- | --- | --- | --- | --- |
| body | body | object | 否 | none |

> 返回示例
> 

> 成功
> 

```
{
  "prompt_id": "a4e402f4-ab96-4e52-a4f3-33899599c67b",
  "number": 20,
  "node_errors": {}
}
```

## **GET /object_info**

GET /object_info

获取系统中所有组件及可用参数

## **GET /object_info/{node_class}**

GET /object_info/MODEL

获取系统中某个组件参数

## **GET /queue**

GET /queue

获取详细任务队列信息

## **POST /queue**

POST /queue

删除队列

> Body 请求参数
> 

```
{
  "delete": "string"
}
```

## **GET /interrupt**

GET /interrupt

取消当前任务

## **GET /system_stats**

GET /system_stats

获取当前系统状态

> 返回示例
> 

> 成功
> 

```
{
  "system": {
    "os": "posix",
    "ram_total": 540847067136,
    "ram_free": 240545492992,
    "comfyui_version": "v0.2.2-87-gd854ed0",
    "python_version": "3.10.12 (main, Jul  5 2023, 18:54:27) [GCC 11.2.0]",
    "pytorch_version": "2.4.0+cu121",
    "embedded_python": false
  },
  "devices": [
    {
      "name": "cuda:0 NVIDIA GeForce RTX 4090 D : cudaMallocAsync",
      "type": "cuda",
      "index": 0,
      "vram_total": 25386352640,
      "vram_free": 24229016988,
      "torch_vram_total": 905969664,
      "torch_vram_free": 276526492
    }
  ]
}
```

## **GET /extensions**

GET /extensions

获取扩展节点文件列表

> 返回示例
> 

> 成功
> 

```
[
	"/extensions/party/showtext_party.js",
	"/extensions/dzNodes/dz_parse-css.js",
	...
]
```