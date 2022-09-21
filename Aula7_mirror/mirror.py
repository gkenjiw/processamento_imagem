from PIL import Image

def mirror(image_path, output_image_path):
    image = Image.open(image_path)
    mirror_image = image.transpose(Image.FLIP_TOP_BOTTOM) #FLIP_LEFT_RIGHT, FLIP_TOP_BOTTOM, TRANSPOSE
    mirror_image.save(output_image_path)

if __name__ == "__main__":
    mirror("raiox.jpg", "raiox_mirrored.jpg")