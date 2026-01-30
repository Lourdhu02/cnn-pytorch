import os
import random
import shutil

# Paths
SOURCE_DIR = "../data/PetImages"
TARGET_DIR = "../binary_classification"

CATEGORIES = ["Cat", "Dog"]
IMAGES_PER_CLASS = 500

SPLIT = {
    "train": 0.7,
    "val": 0.15,
    "test": 0.15
}

# Create target directories
for split in SPLIT:
    for category in CATEGORIES:
        os.makedirs(os.path.join(TARGET_DIR, split, category), exist_ok=True)

def is_valid_image(filename):
    return filename.lower().endswith((".jpg", ".jpeg", ".png"))

for category in CATEGORIES:
    source_path = os.path.join(SOURCE_DIR, category)

    images = [
        img for img in os.listdir(source_path)
        if is_valid_image(img)
    ]

    random.shuffle(images)
    images = images[:IMAGES_PER_CLASS]

    train_end = int(SPLIT["train"] * IMAGES_PER_CLASS)
    val_end = train_end + int(SPLIT["val"] * IMAGES_PER_CLASS)

    splits = {
        "train": images[:train_end],
        "val": images[train_end:val_end],
        "test": images[val_end:]
    }

    for split, files in splits.items():
        for file in files:
            src = os.path.join(source_path, file)
            dst = os.path.join(TARGET_DIR, split, category, file)

            try:
                shutil.copy(src, dst)
            except Exception as e:
                print(f"Skipping {file}: {e}")

print("Small CPU-friendly dataset created successfully.")
