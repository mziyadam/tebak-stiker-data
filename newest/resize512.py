import os
from PIL import Image

def resize_images_in_folder(input_folder, output_folder, max_size):
    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)
    
    # Supported image formats
    supported_formats = (".jpg", ".jpeg", ".png", ".bmp", ".gif")

    # Loop through all files in the input folder
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(supported_formats):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            # Open the image
            image = Image.open(input_path)
            
            # Resize while maintaining aspect ratio
            image.thumbnail(max_size, Image.LANCZOS)
            
            # Save the resized image
            image.save(output_path)
            print(f"Resized image saved to: {output_path}")

# Input folder with images
input_folder = "photos"  # Replace with your input folder path
output_folder = "output_images"  # Replace with your output folder path
max_size = (512, 512)  # Max width and height

# Run the function
resize_images_in_folder(input_folder, output_folder, max_size)

print("All images have been resized and saved.")
