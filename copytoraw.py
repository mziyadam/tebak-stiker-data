import os
import shutil
import re

def process_filename(filename):
    """Clean the filename: remove all characters except alphabets, periods, and spaces, and replace spaces with underscores."""
    cleaned = re.sub(r'[^a-zA-Z. ]', '', filename)  # Remove unwanted characters
    return cleaned # Replace spaces with underscores

def copy_and_rename_files(folder_path):
    """Clean the filenames and copy/rename .webp files in the folder."""
    for filename in os.listdir(folder_path):
        # Only process files that contain a hyphen and end with .webp
        if "-" in filename and filename.endswith(".webp"):
            # Clean the filename by removing unwanted characters and replacing spaces with underscores
            new_filename = process_filename(filename.split("-", 1)[1])  # Remove prefix before hyphen and clean

            # Define source and destination paths
            source_path = os.path.join(folder_path, filename)
            destination_path = os.path.join(folder_path, new_filename)

            # Copy the file to the new name
            shutil.copy(source_path, destination_path)

            print(f"Copied: {filename} -> {new_filename}")

# Specify the folder path containing your files
folder_path = "photos"  # Replace with your folder path

# Run the function to copy and rename files
copy_and_rename_files(folder_path)
