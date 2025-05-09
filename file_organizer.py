import os
import shutil

# Define the file type categories
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Music": [".mp3", ".wav", ".flac"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Scripts": [".py", ".js", ".html", ".css", ".java", ".cpp"]
}

def create_folder_if_not_exists(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

def get_category(file_extension):
    for category, extensions in FILE_TYPES.items():
        if file_extension.lower() in extensions:
            return category
    return "Others"

def organize_directory(path):
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isfile(item_path):
            _, extension = os.path.splitext(item)
            category = get_category(extension)
            category_folder = os.path.join(path, category)
            create_folder_if_not_exists(category_folder)
            new_location = os.path.join(category_folder, item)
            shutil.move(item_path, new_location)
            print(f"Moved: {item} -> {category}/")

if __name__ == "__main__":
    folder_to_organize = input("Enter the path to organize: ").strip('"')
    if os.path.exists(folder_to_organize):
        organize_directory(folder_to_organize)
        print(" Organization complete!")
    else:
        print(" The provided path does not exist.")
