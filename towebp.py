from PIL import Image
import os

# Input and output paths
input_folder = "photos"
output_folder = "photoswebp"

# Ensure output folder exists
os.makedirs(output_folder, exist_ok=True)

# Convert PNG to WebP
for file in os.listdir(input_folder):
    if file.endswith(".png"):
        image = Image.open(os.path.join(input_folder, file))
        output_file = os.path.splitext(file)[0] + ".webp"
        image.save(os.path.join(output_folder, output_file), "WEBP")
        print(f"Converted: {file} -> {output_file}")
