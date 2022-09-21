from PIL import Image

def rotate(image_path, degrees_to_rotate, output_image_path):
    image_obj = Image.open(image_path)
    rotated_image = image_obj.rotate(degrees_to_rotate)
    rotated_image.save(output_image_path)

if __name__ == "__main__":
    rotate("raiox.jpg", 45, "raiox_rotated.jpg")