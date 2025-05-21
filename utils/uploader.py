import requests
from config.settings import IMGUR_CLIENT_ID

def upload_to_imgur(image_path):
    try:
        headers = {
            "Authorization": f"Client-ID {IMGUR_CLIENT_ID}"
        }

        with open(image_path, 'rb') as img:
            response = requests.post(
                "https://api.imgur.com/3/image",
                headers=headers,
                files={"image": img}
            )

        if response.status_code == 200:
            link = response.json()['data']['link']
            print(f"[UPLOAD SUCCESS] {image_path} → {link}")
            return link
        else:
            print(f"[UPLOAD FAIL] Status: {response.status_code} - {response.text}")
            return None
    except Exception as e:
        print(f"[ERROR] Exception during upload: {e}")
        return None
