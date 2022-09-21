from PIL import Image

def crop_image(image_path, coords, output_image_path):
    image = Image.open(image_path)
    cropped_image = image.crop(coords)
    cropped_image.save(output_image_path)

if __name__ == "__main__":
    crop_image("raiox.jpg",
               (140, 61, 328, 383), # Left, Upper, Right, Lower
               "raiox_cropped.jpg")