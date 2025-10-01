from PIL import Image, ImageFilter
import os
import sys
from pathlib import Path

# Converts an image file to WebP, create a blured WebP image for lazy loading, and deletes the original on success.
def convert_to_webp(input_path, quality=80, blur_resize=(20, 20)):
    output_path = input_path.with_suffix('.webp')

    try:
        image = Image.open(input_path)
        if image.mode not in ('RGB', 'RGBA'):
            image = image.convert('RGB')
  
        image.save(output_path, 'webp', quality=quality)
        print(f"Converted: {input_path} -> {output_path}")
        
        return output_path
    except Exception as e:
        print(f"Failed to convert {input_path}: {e}")
        return None


def blur(input_path, quality=80, blur_resize=(20, 20)):
    blurred_output_path = input_path.with_name(input_path.stem + "_blurred.webp")
    
    if input_path.stem.endswith("_blurred"):
        print(f"Skipping {input_path.name}: already a blurred file")
        return

    try:
        image = Image.open(input_path)
        if image.mode not in ('RGB', 'RGBA'):
            image = image.convert('RGB')

        blurred_image = image.resize(blur_resize)

        blurred_image = blurred_image.filter(ImageFilter.GaussianBlur(4))
        blurred_image.save(blurred_output_path, 'webp', quality=quality)
        print(f"Created blurred version: {blurred_output_path}")

    except Exception as e:
        print(f"Failed to blur {input_path}: {e}")


# Process a single file or all images in a directory.
def process_path(path, convert_from='', quality=85):
    p = Path(path)
    if not p.exists():
        print(f"Path not found: {path}")
        return

    if p.is_file():
        if p.suffix.lower() != ".webp":

            # Convert to webp if not already 
            webp_file = convert_to_webp(p, quality)
            if webp_file:
                blur(webp_file, quality)
            
                # Remove original file
                os.remove(p)
        else:
            print(f"Skipping {p.name}: already a webp file")
            blur(p, quality)

    elif p.is_dir():
        for img_file in p.glob('*'):
            suffix = img_file.suffix.lower()
            if (not convert_from and suffix in ['.jpg', '.jpeg', '.png', '.webp']) or \
               (convert_from and suffix == f'.{convert_from.lower()}'):

                # Convert to webp if not already 
                if img_file.suffix.lower() != '.webp':
                    webp_file = convert_to_webp(img_file, quality)
                    if webp_file:
                        blur(webp_file, quality)

                        # Remove original file 
                        os.remove(img_file)
                else:
                    print(f"Skipping {img_file.name}: already a webp file")
                    blur(img_file, quality)
    else:
        print(f"Path is not a file or directory: {path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: blur <file_or_directory> [convert_from]")
        sys.exit(1)

    input_path = sys.argv[1] if len(sys.argv) > 1 else ''

    convert_from = sys.argv[2] if len(sys.argv) > 2 else '' 
    process_path(input_path, convert_from)

