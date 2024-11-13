import argparse
from comfyui_api_integration import WorkflowManager


def initialize_config():
    parser = argparse.ArgumentParser()
    # 添加服务器 URL 参数
    parser.add_argument(
        '--server-url',
        type=str,
        required=True,
        help="The base URL of the ComfyUI server (e.g., http://127.0.0.1:8188)",
    )

    # 可选的下载路径参数
    parser.add_argument(
        '--download-path',
        type=str,
        help="The directory path to save output images (e.g.: /Downloads)",
    )

    # 任务等待时长
    parser.add_argument(
        '--timeout',
        type=int,
        default=5,
        help="The maximum time to wait for a task to complete (in minutes)"
    )

    parser.add_argument(
        '--workflow-path',
        type=str,
        required=True,
        help="The path to the workflow JSON file",
    )

    parser.add_argument(
        '--parameters',
        type=str,
        required=True,
        help='Parameters in JSON format, e.g., \'{"5": ["text", "masterpiece best quality man"], "10": ["image", "/Downloads/test.png"]}\'',
    )

    return parser.parse_args()


if __name__ == '__main__':
    args = initialize_config()
    manager = WorkflowManager(args)
    manager.execute_workflow()
