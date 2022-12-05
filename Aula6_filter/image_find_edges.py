from PIL import Image
from PIL import ImageFilter

def filter_find_edges(input_image, output_image):
    image = Image.open(input_image)
    filtered_image = image.filter(ImageFilter.FIND_EDGES)
    filtered_image.save(output_image)