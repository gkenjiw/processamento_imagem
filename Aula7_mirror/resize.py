from PIL import Image

def resize(input_image_path, output_image_path, size):
    image = Image.open(input_image_path)
    resized_image = image.resize(size)
    resized_image.save(output_image_path)

if __name__ == "__main__":
    resize("raiox.jpg", "raiox_resized.jpg", (100,300))