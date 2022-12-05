from PIL import Image
from PIL import ImageFilter

def filter_detail(input_image, output_image):
    image = Image.open(input_image)
    filtered_image = image.filter(ImageFilter.DETAIL)
    filtered_image.save(output_image)