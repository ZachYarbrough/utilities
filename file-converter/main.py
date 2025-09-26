from PIL import Image
import os
import sys
from pathlib import Path

def convert_to_webp(input_path, quality=80):
    """
    Converts an image file to WebP and deletes the original on success.
    """
    output_path = input_path.with_suffix('.webp')
    try:
        image = Image.open(input_path)
        if image.mode not in ('RGB', 'RGBA'):
            image = image.convert('RGB')
        image.save(output_path, 'webp', quality=quality)
        print(f"Converted: {input_path} -> {output_path}")

        # Remove original file
        os.remove(input_path)
    except Exception as e:
        print(f"Failed to convert {input_path}: {e}")

def process_path(path, quality=85):
    """
    Process a single file or all images in a directory.
    """
    p = Path(path)
    if not p.exists():
        print(f"Path not found: {path}")
        return

    if p.is_file():
        convert_to_webp(p, quality)
    elif p.is_dir():
        # Loop through jpg/jpeg/png files
        for img_file in p.glob('*'):
            if img_file.suffix.lower() in ['.jpg', '.jpeg', '.png']:
                convert_to_webp(img_file, quality)
    else:
        print(f"Path is not a file or directory: {path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <file_or_directory>")
        sys.exit(1)

    input_path = sys.argv[1]
    process_path(input_path, quality=85)

