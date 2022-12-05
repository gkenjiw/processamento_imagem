from PIL import Image
from PIL import ImageFilter

def filter_gaussian_blur(input_image, output_image):
    image = Image.open(input_image)
    filtered_image = image.filter(ImageFilter.GaussianBlur)
    filtered_image.save(output_image)