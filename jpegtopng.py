from PIL import Image
from tkinter import Button, filedialog, messagebox, Tk
import os

def convert_jpeg_to_png():
    # Hide the root Tkinter window
    root.withdraw()
    
    # Ask the user to select a folder
    folder_path = filedialog.askdirectory(title="Select Folder Containing JPEG Files")
    if not folder_path:
        messagebox.showwarning("No folder selected", "Please select a folder to proceed.")
        return
    
    # List all JPEG files in the folder
    jpeg_files = [file for file in os.listdir(folder_path) if file.lower().endswith(('.jpg', '.jpeg'))]
    
    if not jpeg_files:
        messagebox.showinfo("No JPEG Files Found", "No JPEG files were found in the selected folder.")
        return
    
    # Output folder (create one if it doesn't exist)
    output_folder = os.path.join(folder_path, "converted_pngs")
    os.makedirs(output_folder, exist_ok=True)
    
    # Convert JPEG files to PNG
    for jpeg_file in jpeg_files:
        try:
            # Open the JPEG file
            img = Image.open(os.path.join(folder_path, jpeg_file))
            
            # Save as PNG
            png_file_name = os.path.splitext(jpeg_file)[0] + ".png"
            img.save(os.path.join(output_folder, png_file_name))
            print(f"Converted: {jpeg_file} -> {png_file_name}")
        except Exception as e:
            print(f"Error converting {jpeg_file}: {e}")
    
    messagebox.showinfo("Conversion Complete", f"All JPEG files have been converted and saved in: {output_folder}")

# GUI Initialization
root = Tk()
root.title("JPEG to PNG Converter")

# Add a button to start conversion
button = Button(root, text="Convert JPEGs to PNGs", command=convert_jpeg_to_png, padx=10, pady=5)
button.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()
