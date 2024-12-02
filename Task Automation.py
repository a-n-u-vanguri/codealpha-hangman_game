import os
import shutil

# Define paths and mappings for organization
DOWNLOAD_FOLDER = "/path/to/your/download/folder"
ORGANIZED_FOLDER = "/path/to/organized/folder"

# Define how to organize files by extensions or keywords
FILE_CATEGORIES = {
    "Documents": [".pdf", ".docx", ".txt", ".pptx"],
    "Spreadsheets": [".xls", ".xlsx", ".csv"],
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Code": [".py", ".java", ".c", ".cpp", ".js", ".html", ".css"],
    "Archives": [".zip", ".tar", ".gz", ".rar"],
}

def get_category_by_extension(file_ext):
    """Returns the category based on file extension."""
    for category, extensions in FILE_CATEGORIES.items():
        if file_ext in extensions:
            return category
    return None

def move_file_to_category(file_path, filename, category):
    """Moves the file to the specified category folder."""
    category_folder = os.path.join(ORGANIZED_FOLDER, category)
    os.makedirs(category_folder, exist_ok=True)
    shutil.move(file_path, os.path.join(category_folder, filename))

def move_to_miscellaneous(file_path, filename):
    """Moves the file to the 'Miscellaneous' folder."""
    misc_folder = os.path.join(ORGANIZED_FOLDER, "Miscellaneous")
    os.makedirs(misc_folder, exist_ok=True)
    shutil.move(file_path, os.path.join(misc_folder, filename))

def organize_files():
    """Organizes files from the download folder into categorized folders."""
    for filename in os.listdir(DOWNLOAD_FOLDER):
        file_path = os.path.join(DOWNLOAD_FOLDER, filename)

        # Skip directories
        if os.path.isdir(file_path):
            continue
        
        file_ext = os.path.splitext(filename)[1].lower()
        category = get_category_by_extension(file_ext)

        if category:
            move_file_to_category(file_path, filename, category)
        else:
            move_to_miscellaneous(file_path, filename)

# Call the organize_files function
organize_files()
