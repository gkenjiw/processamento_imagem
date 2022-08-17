from pickletools import optimize
from PIL import Image

def image_converter(input_file, output_file, format):
    image = Image.open(input_file)
    image.save(output_file, format=format, optimize = True, quality = 1)
    image.thumbnail((75,75))
    image.save("thumbnail.jpg")

def image_format(input_file):
    image = Image.open(input_file)
    print(f"Formato: {image.format_description}")

if __name__ == "__main__":
    image_converter("pizza-de-brocolis.jpg", "corno.png", "PNG")
    image_converter("corno.png", "teste.jpg", "JPEG")
    image_format("pizza-de-brocolis.jpg")
    image_format("corno.png")