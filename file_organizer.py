import os
import shutil

# Folder to organize (current directory)
SOURCE_FOLDER = "to_organize"

# File type categories
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv"],
    "Music": [".mp3"],
    "Others": []
}

def organize_files():
    if not os.path.exists(SOURCE_FOLDER):
        print("Folder does not exist.")
        return

    for file_name in os.listdir(SOURCE_FOLDER):
                if file_name.startswith("."):
            continue
        file_path = os.path.join(SOURCE_FOLDER, file_name)

        if os.path.isfile(file_path):
            moved = False

            for folder, extensions in FILE_TYPES.items():
                if any(file_name.lower().endswith(ext) for ext in extensions):
                    destination = os.path.join(SOURCE_FOLDER, folder)
                    os.makedirs(destination, exist_ok=True)
                    shutil.move(file_path, destination)
                    moved = True
                    break

            if not moved:
                other_folder = os.path.join(SOURCE_FOLDER, "Others")
                os.makedirs(other_folder, exist_ok=True)
                shutil.move(file_path, other_folder)

    print("File organization complete.")

organize_files()
