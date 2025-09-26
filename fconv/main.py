from PIL import Image
import os
import sys
from pathlib import Path

# Converts an image file to WebP and deletes the original on success.
def convert_to_webp(input_path, quality=80):
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


# Process a single file or all images in a directory.
def process_path(path, convert_from='', convert_to='webp', quality=85):
    p = Path(path)
    if not p.exists():
        print(f"Path not found: {path}")
        return

    if p.is_file():
        convert_to_webp(p, quality)
    elif p.is_dir():
        for img_file in p.glob('*'):
            match convert_to:
                case 'webp':
                    if convert_from == '' or convert_from in ['jpg', 'jpeg', 'png']:
                        if (convert_from == '' and img_file.suffix.lower() in ['.jpg', '.jpeg', '.png'] or (convert_from != '' and img_file.suffix.lower() == convert_from.lower())):
                            convert_to_webp(img_file, quality)
                    else:
                        print(f"The file type {(convert_from + ' ') if convert_from else ''}can't currently be converted to {convert_to}")
                case _:
                    print(f"The file type {(convert_from + ' ') if convert_from else ''}can't currently be converted to {convert_to}")
    else:
        print(f"Path is not a file or directory: {path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: fconv <file_or_directory> [convert_from] [convert_to]")
        sys.exit(1)

    input_path = sys.argv[1] if len(sys.argv) > 1 else ''

    convert_from = sys.argv[2] if len(sys.argv) > 2 else '' 
    convert_to = sys.argv[3] if len(sys.argv) > 3 else ''

    process_path(input_path, convert_from, convert_to)

