import os
from PIL import Image

def resize_and_pad_webp(image_path, output_path, size=(512, 512)):
    # Open the WebP image
    img = Image.open(image_path).convert("RGBA")  # Ensure image has transparency
    
    # Resize while maintaining aspect ratio
    img.thumbnail(size, Image.LANCZOS)
    
    # Create a transparent canvas of 512x512
    transparent_canvas = Image.new("RGBA", size, (0, 0, 0, 0))
    
    # Calculate position to center the resized image
    x_offset = (size[0] - img.width) // 2
    y_offset = (size[1] - img.height) // 2
    
    # Paste the resized image onto the transparent canvas
    transparent_canvas.paste(img, (x_offset, y_offset), img)  # Use img as mask to retain transparency
    
    # Save the final image
    transparent_canvas.save(output_path, "WEBP")

def process_folder(input_folder, output_folder, size=(512, 512)):
    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)
    
    # Loop through all files in the input folder
    for file_name in os.listdir(input_folder):
        # Check for .webp files
        if file_name.lower().endswith(".webp"):
            input_path = os.path.join(input_folder, file_name)
            output_path = os.path.join(output_folder, file_name)
            
            try:
                # Process the image
                resize_and_pad_webp(input_path, output_path, size)
                print(f"Processed: {file_name}")
            except Exception as e:
                print(f"Error processing {file_name}: {e}")

# Example usage
input_folder = "photos"    # Folder containing the WebP images
output_folder = "photos"  # Folder to save resized images
process_folder(input_folder, output_folder)
