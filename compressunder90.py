from PIL import Image
import os

def compress_image_to_size(input_path, output_path, max_size_kb=90):
    """
    Compress an image to be under the specified max size (in KB).

    Args:
        input_path (str): Path to the input image.
        output_path (str): Path to save the compressed image.
        max_size_kb (int): Maximum file size in KB.
    """
    quality = 95  # Start with high quality
    step = 5      # Decrement step for quality
    img_format = "JPEG"  # Default format

    try:
        # Open the image
        img = Image.open(input_path)
        
        # Convert PNG to RGB to save as JPEG if needed
        if img.format == "PNG":
            img = img.convert("RGB")
            img_format = "JPEG"

        # Compress iteratively until file size is under max_size_kb
        while quality > 10:
            img.save(output_path, img_format, optimize=True, quality=quality)
            file_size = os.path.getsize(output_path) / 1024  # Size in KB
            
            if file_size <= max_size_kb:
                print(f"Compressed {input_path} to {round(file_size, 2)} KB")
                return
            quality -= step  # Reduce quality for further compression

        print(f"Could not compress {input_path} below {max_size_kb} KB. Final size: {round(file_size, 2)} KB")
    except Exception as e:
        print(f"Error compressing {input_path}: {e}")

def batch_compress_images(input_folder, output_folder, max_size_kb=90):
    """
    Compress all PNG and JPEG images in a folder that exceed max_size_kb.

    Args:
        input_folder (str): Path to the folder containing images.
        output_folder (str): Path to save compressed images.
        max_size_kb (int): Maximum file size in KB.
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for file_name in os.listdir(input_folder):
        if file_name.lower().endswith(('.jpg', '.jpeg', '.png')):
            input_path = os.path.join(input_folder, file_name)
            output_path = os.path.join(output_folder, file_name)

            # Check the size of the original file
            original_size = os.path.getsize(input_path) / 1024  # Size in KB
            if original_size > max_size_kb:
                print(f"Processing {file_name} (size: {round(original_size, 2)} KB)...")
                compress_image_to_size(input_path, output_path, max_size_kb)
            else:
                # Copy the file if it's already under the size limit
                img = Image.open(input_path)
                img.save(output_path)
                print(f"Skipped {file_name} (size: {round(original_size, 2)} KB - already under {max_size_kb} KB)")

# Example Usage
input_folder = "photos"      # Folder containing images
output_folder = "compressed_images"  # Folder to save compressed images
batch_compress_images(input_folder, output_folder, max_size_kb=80)
