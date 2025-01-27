import os

image_extensions = [".jpg", ".jpeg", ".png", ".gif", ".webp"]

def get_image_files():
    os.chdir("images")
    images = [
        f for f in os.listdir(".")
        if os.path.isfile(f) and os.path.splitext(f)[1].lower() in image_extensions
    ]
    os.chdir("..")
    return sorted(images)

def update_readme(images):
    with open("README.md", "w") as readme:
        readme.write("# Wallpapers\n\n")

        for image in images:
            readme.write(f"![{image}](./images/{image})\n\n")

if __name__ == "__main__":
    images = get_image_files()
    update_readme(images)

    print(f"Updated README.md with {len(images)} images.")

