import os
import re

valid_filename_pattern = re.compile(r'^[0-9]{3}$')

# Get last properly named file number
def get_last_properly_named():
    res = 0
    for filename in os.listdir("."):
        if os.path.isdir(filename):
            continue

        name, ext = os.path.splitext(filename)
        if ext.lower() not in [".png", ".jpg", ".jpeg", ".webp"]:
            print(f"Skipping file: {filename}")
            continue

        if valid_filename_pattern.fullmatch(name):
            res = max(res, int(name))

    return res

# Rename files in the directory
def rename_files(dir):
    os.chdir(dir)

    start = get_last_properly_named() + 1

    for filename in os.listdir("."):
        if os.path.isdir(filename):
            continue

        name, ext = os.path.splitext(filename)

        if ext.lower() not in [".png", ".jpg", ".jpeg", ".webp"]:
            print(f"Skipping file: {filename}")
            continue

        if not valid_filename_pattern.fullmatch(name):
            new_filename = str(start).zfill(3) + ext
            start += 1

            if os.path.exists(new_filename):
                raise ValueError(f"Unexpected state: {new_full_filename} already exists")

            os.rename(filename, new_filename)
            print(f"Renamed: {filename} -> {new_filename}")

    os.chdir("..")

if __name__ == "__main__":
    rename_files("images")

