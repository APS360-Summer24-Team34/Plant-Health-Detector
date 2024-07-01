import os

def rename_images_in_folder(folder_path):
    for root, _, files in os.walk(folder_path):
        for i, filename in enumerate(files):
            file_extension = os.path.splitext(filename)[1]
            new_filename = f"{os.path.basename(root)}_{i+1}{file_extension}"
            os.rename(os.path.join(root, filename), os.path.join(root, new_filename))
            print(f"Renamed {filename} to {new_filename}")


base_folder = "database\\rice"
subfolders = [
    "bacterial_leaf_blight",
    "brown_spot",
    "leaf_blast",
    "leaf_scald",
    "narrow_brown_spot",
    "healthy"
]

for subfolder in subfolders:
    folder_path = os.path.join(base_folder, subfolder)
    rename_images_in_folder(folder_path)