from PIL import Image
from PIL import ImageFilter

def filter_edge_enhance(input_image, output_image):
    image = Image.open(input_image)
    filtered_image = image.filter(ImageFilter.EDGE_ENHANCE)
    filtered_image.save(output_image)