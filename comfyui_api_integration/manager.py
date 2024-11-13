import json
import os

from comfyui_api_integration.api import ComfyUIClient, generate_client_id, generate_seed


class WorkflowManager:
    def __init__(self, args):
        self.client = ComfyUIClient(args.server_url, generate_client_id(), args.download_path)
        self.timeout = args.timeout
        self.workflow_path = args.workflow_path
        try:
            parameters = json.loads(args.parameters)
            self.parameters = {k: tuple(v) if isinstance(v, list) else v for k, v in parameters.items()}
        except json.JSONDecodeError:
            raise ValueError('Parameters should in JSON format, e.g., \'{"5": ["text", "masterpiece best quality man"], "10": ["image", "/Downloads/test.png"]}\'')

    def execute_workflow(self):
        print('Executing workflow...')
        with open(self.workflow_path) as f:
            workflow = json.load(f)
        for idx, (t, v) in self.parameters.items():
            if t == 'image':
                comfyui_image_path = self.client.upload_image(v)
                if not comfyui_image_path:
                    raise ValueError(f'Failed to upload image {v}')
                self.parameters[idx] = (t, comfyui_image_path)
        for idx, (t, v) in self.parameters.items():
            if not t or not v:
                raise ValueError(f'Missing parameter type or value for step {idx}')
            workflow[idx]['inputs'][t] = v
        for idx, step in workflow.items():
            if 'seed' in step['inputs']:
                workflow[idx]['inputs']['seed'] = generate_seed()

        prompt_id = self.client.query_prompt(workflow)
        if prompt_id is None:
            raise ValueError('Failed to query prompt')
        print(f'Prompt ID: {prompt_id}')

        output_images = self.client.query_history(prompt_id, self.timeout)
        if output_images is None:
            raise ValueError('Failed to query history')
        elif not output_images:
            raise ValueError('No output images found')
        else:
            print(f'Output images: {output_images}')

        if not self.client.download_path:
            print('No download path specified')
            return None
        if not os.path.exists(self.client.download_path):
            print(f'Download path {self.client.download_path} does not exist, creating it...')
            os.makedirs(self.client.download_path)
        for output_image_path in output_images:
            image_path = self.client.download_output_image(output_image_path)
            if image_path is None:
                raise ValueError(f'Failed to download image {output_image_path}')
            print(f'Output image saved to {image_path}')

        print('Workflow execution completed.')
