import os
import requests
import tarfile
import zipfile
from pathlib import Path

def download_file(url, output_path):
    """Download a file from a URL to the specified path."""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(output_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"Downloaded: {output_path}")
    else:
        print(f"Failed to download: {url}")

def extract_tar_gz(file_path, extract_dir):
    """Extract a .tar.gz file."""
    os.makedirs(extract_dir, exist_ok=True)
    with tarfile.open(file_path, 'r:gz') as tar:
        tar.extractall(extract_dir)
    print(f"Extracted: {file_path} to {extract_dir}")

def extract_zip(file_path, extract_dir):
    """Extract a .zip file."""
    os.makedirs(extract_dir, exist_ok=True)
    with zipfile.ZipFile(file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_dir)
    print(f"Extracted: {file_path} to {extract_dir}")

def download_common_voice(language, output_dir):
    """Download a small subset of Mozilla Common Voice for a given language."""
    # Note: Common Voice requires signing in or API access; use a small pre-downloaded subset or adjust for API
    # For simplicity, assume a direct link to a small subset (replace with actual URL or local path)
    print(f"Placeholder: Download Common Voice {language} to {output_dir}")
    # Example: Use a small sample if available or download manually from https://commonvoice.mozilla.org/en/datasets
    # You may need to register and download manually, then place in output_dir

def download_librispeech(subset, output_dir):
    """Download LibriSpeech dev-clean subset."""
    url = f"http://www.openslr.org/resources/12/{subset}.tar.gz"
    output_path = os.path.join(output_dir, f"{subset}.tar.gz")
    download_file(url, output_path)
    extract_tar_gz(output_path, output_dir)

def download_coco_captions(output_dir):
    """Download COCO Captions validation set."""
    url = "http://images.cocodataset.org/annotations/annotations_trainval2014.zip"
    output_path = os.path.join(output_dir, "annotations_trainval2014.zip")
    download_file(url, output_path)
    extract_zip(output_path, output_dir)

def main():
    # Define output directories
    base_dir = Path("data")
    common_voice_dir = base_dir / "audio" / "common_voice"
    librispeech_dir = base_dir / "audio" / "librispeech"
    coco_dir = base_dir / "images" / "coco"

    # Download datasets
    download_common_voice("english", common_voice_dir / "english")
    download_common_voice("urdu", common_voice_dir / "urdu")
    download_common_voice("arabic", common_voice_dir / "arabic")
    download_librispeech("dev-clean", librispeech_dir)
    download_coco_captions(coco_dir)

if __name__ == "__main__":
    main()