from PIL import Image
from PIL import ImageFilter

def filter_blur(input_image):
    image = Image.open(input_image)
    filtered_image = image.filter(ImageFilter.BLUR)
    file = input_image.split('.')
    file = f'{file[0]}_blur.jpg'
    filtered_image.save(file, format="JPEG")
    return file
    

def filter_box_blur(input_image):
    image = Image.open(input_image)
    filtered_image = image.filter(ImageFilter.BoxBlur(radius=3))
    file = input_image.split('.')
    file = f'{file[0]}_boxblur.jpg'
    filtered_image.save(file, format="JPEG")
    return file
    

def filter_contour(input_image):
    image = Image.open(input_image)
    filtered_image = image.filter(ImageFilter.CONTOUR)
    file = input_image.split('.')
    file = f'{file[0]}_contour.jpg'
    filtered_image.save(file, format="JPEG")
    return file
    

def filter_detail(input_image):
    image = Image.open(input_image)
    filtered_image = image.filter(ImageFilter.DETAIL)
    file = input_image.split('.')
    file = f'{file[0]}_detail.jpg'
    filtered_image.save(file, format="JPEG")
    return file
    

def filter_edge_enhance(input_image):
    image = Image.open(input_image)
    filtered_image = image.filter(ImageFilter.EDGE_ENHANCE)
    file = input_image.split('.')
    file = f'{file[0]}_edgeenhance.jpg'
    filtered_image.save(file, format="JPEG")
    return file
    

def filter_emboss(input_image):
    image = Image.open(input_image)
    filtered_image = image.filter(ImageFilter.EMBOSS)
    file = input_image.split('.')
    file = f'{file[0]}_emboss.jpg'
    filtered_image.save(file, format="JPEG")
    return file
    

def filter_find_edges(input_image):
    image = Image.open(input_image)
    filtered_image = image.filter(ImageFilter.FIND_EDGES)
    file = input_image.split('.')
    file = f'{file[0]}_findedgges.jpg'
    filtered_image.save(file, format="JPEG")
    return file
    

def filter_gaussian_blur(input_image):
    image = Image.open(input_image)
    filtered_image = image.filter(ImageFilter.GaussianBlur)
    file = input_image.split('.')
    file = f'{file[0]}_gaussianblur.jpg'
    filtered_image.save(file, format="JPEG")
    return file
    

def filter_sharpen(input_image):
    image = Image.open(input_image)
    filtered_image = image.filter(ImageFilter.SHARPEN)
    file = input_image.split('.')
    file = f'{file[0]}_sharpen.jpg'
    filtered_image.save(file, format="JPEG")
    return file
    

def filter_smooth(input_image):
    image = Image.open(input_image)
    filtered_image = image.filter(ImageFilter.SMOOTH)
    file = input_image.split('.')
    file = f'{file[0]}_smooth.jpg'
    filtered_image.save(file, format="JPEG")
    return file
    