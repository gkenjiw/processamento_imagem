from PIL import Image
from PIL import ImageFilter

def filter_smooth(input_image, output_image):
    image = Image.open(input_image)
    filtered_image = image.filter(ImageFilter.SMOOTH)
    filtered_image.save(output_image)