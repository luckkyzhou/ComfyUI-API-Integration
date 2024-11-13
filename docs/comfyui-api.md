# comfyui-api

**Read this in other languages: [中文](comfyui-api-zh.md).**

## **GET /history**

GET /history

Retrieve all historical task data.

### **Request Parameters**

| Name | Parameter | Type | Required | Description |
| --- | --- | --- | --- | --- |
| prompt_id | query | string | No | a4e402f4-ab96-4e52-a4f3-33899599c67b |

## **GET /history/{prompt_id}**

GET /history/a4e402f4-ab96-4e52-a4f3-33899599c67b

Retrieve historical data for a specific task ID.

## **POST /upload/image**

POST /upload/image

Upload the image to the comfyui directory on the server.

> request parameters of body
> 

```
image: string
```

### **请求参数**

| Name | Parameter | Type | Required | Description |
| --- | --- | --- | --- | --- |
| body | body | object | No | none |
| image | body | string(binary) | Yes | The image will be sent to the server in binary format. |

> response example
> 

> success
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

Upload the mask image to the comfyui directory on the server.

> request parameters of body
> 

```
image: string
type: input
subfolder: mask
original_ref: "{"filename":"test.png","type":"input","subfolder":"mask"}"
```

### **Request Parameters**

| Name | Parameter | Type | Required | Description |
| --- | --- | --- | --- | --- |
| body | body | object | No | none |
| image | body | string(binary) | Yes | The image will be sent to the server in binary format. |
| type | body | string | No | Target folder for uploading images. |
| subfolder | body | string | No | Target subfolder for uploading images. |
| original_ref | body | string | Yes | none |

> response example
> 

> success
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

Online preview of the image.

### **Request Parameters**

| Name | Parameter | Type | Required | Description |
| --- | --- | --- | --- | --- |
| filename | query | string | Yes | Image name |
| type | query | string | No | Folder for storing images (input for uploaded images, output for generated images). |
| subfolder | query | string | No | Subfoler |
| preview | query | string | No | Preview |
| channel | query | string | No | none |

> response example
> 

> success
> 

```
"<img src=\"blob:file:///a4e402f4-ab96-4e52-a4f3-33899599c67b\" alt=\"comfyuiapi\" />"
```

## **GET /prompt**

GET /prompt

Retrieve the current remaining number of tasks in the queue.

> response example
> 

> success
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

Execute task issuance based on the JSON of the workflow and return the task ID information. 

> request parameters of body
> 

```
{
  "client_id": "3c5662b1-4b59-47ea-ba7d-e3f2cd9eb36f",
  "prompt": {
		 <workflow.json>
  }
}

```

### **Request Parameters**

| Name | Parameter | Type | Required | Description |
| --- | --- | --- | --- | --- |
| body | body | object | No | none |

> response example
> 

> success
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

Retrieve all components and available parameters in the system.

## **GET /object_info/{node_class}**

GET /object_info/MODEL

Retrieve parameters for a specific component in the system.

## **GET /queue**

GET /queue

Retrieve detailed task queue information.

## **POST /queue**

POST /queue

Delete the queue.

> request parameters of body
> 

```
{
  "delete": "string"
}
```

## **GET /interrupt**

GET /interrupt

Cancel the current task.

## **GET /system_stats**

GET /system_stats

Retrieve the current system status.

> response example
> 

> success
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

Retrieve the list of extension node files.

> response example
> 

> success
> 

```
[
	"/extensions/party/showtext_party.js",
	"/extensions/dzNodes/dz_parse-css.js",
	...
]
```