import os

# Directory containing the images
image_directory = "images"
readme_file = "README.md"

# Supported image extensions
image_extensions = [".jpg", ".jpeg", ".png", ".gif", ".webp"]

def get_image_files():
    """Get a list of image files in the directory."""
    return [
        f for f in os.listdir(".")
        if os.path.isfile(f) and os.path.splitext(f)[1].lower() in image_extensions
    ]

def update_readme(images):
    """Update the README.md file with the list of images."""
    with open(readme_file, "w") as readme:
        # Write the header
        readme.write("# Wallpapers\n\n")

        # Add each image as a Markdown image
        for image in images:
            print("yo")
            readme.write(f"![{image}](./images/{image})\n\n")

if __name__ == "__main__":
    # Get the list of image files
    os.chdir("./images")
    images = get_image_files()

    # Update the README.md file
    os.chdir("..")
    update_readme(images)

    print(f"Updated {readme_file} with {len(images)} images.")

