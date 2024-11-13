import json
import time
import os

import requests


class ComfyUIClient:
    def __init__(self, server_url, client_id, download_path):
        self.server_url = server_url.strip("/")
        self.client_id = client_id
        self.download_path = download_path

    def query_prompt(self, prompt):
        api_url = self.server_url + "/prompt"
        data = {
            "client_id": self.client_id,
            "prompt": prompt
        }
        try:
            response = requests.post(api_url, json=data)
            result = json.loads(response.text)
            prompt_id = result["prompt_id"]
            return prompt_id
        except Exception as e:
            print(f"Error: {e}")
            return None

    def query_history(self, prompt_id, timeout=5):
        api_url = self.server_url + "/history/" + prompt_id
        while timeout > 0:
            try:
                response = requests.get(api_url)
            except Exception as e:
                print(f"Error: {e}")
                return None

            if response.text and response.text != '{}':
                response_json = json.loads(response.text)
                result = {}
                try:
                    for _, v in response_json.items():
                        result = v
                        break
                except Exception as e:
                    print(f"Error: {e}")
                    return None

                if len(result["status"]) == 0:
                    print("Waiting for the task to complete...")
                    time.sleep(1)
                    timeout -= 1 / 60
                    continue
                else:
                    output_images = []
                    try:
                        if result["status"]["status_str"] == "success":
                            for _, output in result["outputs"].items():
                                image = output["images"][0]
                                if image["type"] == "output":
                                    if image["subfolder"]:
                                        image_name = image["subfolder"] + "/" + image["filename"]
                                    else:
                                        image_name = image["filename"]
                                    output_images.append(image_name)
                            return output_images
                        else:
                            print(f"Error: {result}")
                            return None
                    except Exception as e:
                        print(f"Error: {e}")
                        return None
            else:
                print("Waiting for the task to complete...")
                time.sleep(1)
                timeout -= 1 / 60
                continue

    def download_output_image(self, image_name):
        file_path = os.path.join(self.download_path, image_name)

        api_url = f"{self.server_url}/view"
        params = {"filename": image_name, "type": "output"}
        try:
            response = requests.get(api_url, params=params)
            with open(file_path, "wb") as f:
                f.write(response.content)
            print(f"Downloaded: {file_path}")
            return file_path
        except Exception as e:
            print(f"Error: {e}")
            return None

    def upload_image(self, image_path, image_type="input", sub_folder=""):
        api_url = f"{self.server_url}/upload/image"
        files = {"image": open(image_path, "rb")}
        data = {
            "subfolder": sub_folder,
            "type": image_type
        }
        try:
            response = requests.post(api_url, data=data, files=files)
            result = response.json()
            if sub_folder:
                image_name = result["subfolder"] + "/" + result["name"]
            else:
                image_name = result["name"]
            print(f"Uploaded: {image_path} as {image_name}")
            return image_name
        except Exception as e:
            print(f"Error: {e}")
            return None
