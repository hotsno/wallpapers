import os
import re
import random
import string

# Function to generate a random string of length 8
def generate_random_string(length=8):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))

# Regex pattern to match valid filenames
valid_filename_pattern = re.compile(r'^[a-z0-9]{8}$')

os.chdir("images")

# Rename files in the directory
def rename_files():
    for filename in os.listdir("."):
        # Skip directories
        if os.path.isdir(filename):
            continue

        # Get the file extension
        name, ext = os.path.splitext(filename)

        # Skip non-image files
        if ext.lower() not in [".png", ".jpg", ".jpeg", ".webp"]:
            print(f"Skipping file: {filename}")
            continue

        # Check if the filename matches the valid pattern
        if not valid_filename_pattern.fullmatch(name):
            # Generate a new random filename
            new_name = generate_random_string()
            while os.path.exists(f"{new_name}{ext}"):
                new_name = generate_random_string()

            # Rename the file
            os.rename(filename, f"{new_name}{ext}")
            print(f"Renamed: {filename} -> {new_name}{ext}")

if __name__ == "__main__":
    rename_files()

