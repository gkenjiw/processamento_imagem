from PIL import Image
from PIL import ImageFilter

def filter_contour(input_image, output_image):
    image = Image.open(input_image)
    filtered_image = image.filter(ImageFilter.CONTOUR)
    filtered_image.save(output_image)