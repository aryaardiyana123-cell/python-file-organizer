import os
import shutil

folder_path = "sample_files"

file_types = {
    ".jpg": "Images",
    ".png": "Images",

    ".pdf": "Documents",
    ".docx": "Documents",
    ".xlsx": "Documents",
    ".pptx": "Documents",

    ".mp4": "Videos",
    ".avi": "Videos",

    ".mp3": "Audio",

    ".zip": "Archives",
    ".rar": "Archives",

    ".txt": "Text"
}
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)

    if os.path.isfile(file_path):
        ext = os.path.splitext(filename)[1].lower()

        if ext in file_types:
            target_folder = os.path.join(folder_path, file_types[ext])

            os.makedirs(target_folder, exist_ok=True)

            shutil.move(
                file_path,
                os.path.join(target_folder, filename)
            )

print("Done! File berhasil dirapikan.")