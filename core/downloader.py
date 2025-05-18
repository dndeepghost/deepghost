import requests

def download_file(url, save_path):
    try:
        response = requests.get(url, stream=True, timeout=10)
        with open(save_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
        print(f"[✓] Downloaded: {save_path}")
    except Exception as e:
        print(f"[x] Failed to download: {e}")