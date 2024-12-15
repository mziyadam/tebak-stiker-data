import os
import shutil

def copy_and_rename_files(folder_path):
    # List all files in the given folder
    for filename in os.listdir(folder_path):
        # Check if the filename contains a hyphen and ends with .webp
        if "-" in filename and filename.endswith(".webp"):
            # Split the filename at the first hyphen and take the part after it
            new_filename = filename.split("-", 1)[1]

            # Define source and destination paths
            source_path = os.path.join(folder_path, filename)
            destination_path = os.path.join(folder_path, new_filename)

            # Copy the file to the new name
            shutil.copy(source_path, destination_path)

            print(f"Copied: {filename} -> {new_filename}")

# Specify the folder path containing your files
folder_path = "photos"  # Replace with your folder path
copy_and_rename_files(folder_path)
