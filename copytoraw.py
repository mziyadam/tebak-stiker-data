import os
import re
import shutil

def clean_filename(filename):
    # Replace unwanted characters and spaces with underscores
    cleaned_name = re.sub(r'[^a-zA-Z0-9._ ]', '', filename)  # Keep only alphabets, numbers, period, and space
    cleaned_name = cleaned_name.replace(" ", "_")  # Replace spaces with underscores
    return cleaned_name

def clean_and_rename_files(folder_path):
    # List all files in the given folder
    for filename in os.listdir(folder_path):
        # Define the source and destination file paths
        source_path = os.path.join(folder_path, filename)
        
        # Clean the filename
        new_filename = clean_filename(filename)
        
        # Define the destination path with the cleaned filename
        destination_path = os.path.join(folder_path, new_filename)
        
        # Rename the file only if the name has changed
        if source_path != destination_path:
            try:
                # Move (rename) the file
                shutil.move(source_path, destination_path)
                print(f"Renamed: {filename} -> {new_filename}")
            except Exception as e:
                print(f"Error renaming {filename}: {e}")

# Specify the folder path containing your files
folder_path = "photosraw"  # Replace with your folder path
clean_and_rename_files(folder_path)
