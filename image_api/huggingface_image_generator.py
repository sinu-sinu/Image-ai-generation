import requests
import os
import uuid
from config.settings import HF_API_KEY

def generate_image_url(prompt, output_dir="outputs", output_format="png"):
    """
    Sends a prompt to Hugging Face's FLUX.1-dev model and saves the image locally.
    Returns the local file path.
    """
    try:
        print(f"[INFO] Sending prompt to FLUX.1-dev: {prompt}")

        endpoint = "https://api-inference.huggingface.co/models/black-forest-labs/FLUX.1-dev"

        headers = {
            "Authorization": f"Bearer {HF_API_KEY}",
            "Accept": "image/png"
        }

        payload = {
            "inputs": prompt,
            "options": {"wait_for_model": True}
        }

        response = requests.post(endpoint, headers=headers, json=payload)

        if response.status_code == 200:
            os.makedirs(output_dir, exist_ok=True)
            filename = f"{uuid.uuid4().hex}.{output_format}"
            filepath = os.path.join(output_dir, filename)

            with open(filepath, 'wb') as f:
                f.write(response.content)

            print(f"[SUCCESS] Image saved at {filepath}")
            return filepath
        else:
            print(f"[ERROR] API returned: {response.status_code} - {response.text}")
            return None

    except Exception as e:
        print(f"[ERROR] Exception occurred: {e}")
        return None
