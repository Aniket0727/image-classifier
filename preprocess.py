from PIL import Image
import os

def preprocess_images(folder):
    for file in os.listdir(folder):
        path = os.path.join(folder, file)
        try:
            img = Image.open(path).convert("RGB").resize((128, 128))
            img.save(path)
        except Exception as e:
            print(f"Error processing {path}: {e}")

if __name__ == "__main__":
    # Process all category folders inside 'data'
    base_dir = "data"
    for category in os.listdir(base_dir):
        folder_path = os.path.join(base_dir, category)
        if os.path.isdir(folder_path):
            print(f"Processing {category}...")
            preprocess_images(folder_path)
