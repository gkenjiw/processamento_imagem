import io
import os
from pickletools import optimize
import requests
import PySimpleGUI as sg
from PIL import Image
from pathlib import Path
from PIL.ExifTags import TAGS, GPSTAGS

file_types = [("(JPEG (*.jpg)","*.jpg"),
              ("All files (*.*)", "*.*")]

fields = {
    "File name" : "File name",
    "File size" : "File size",
    "Model" : "Camera Model",
    "ExifImageWidth" : "Width",
    "ExifImageHeight" : "Height",
    "DateTime" : "Creating Date",
    "static_line" : "*",
    "MaxApertureValue" : "Aperture",
    "ExposureTime" : "Exposure",
    "FNumber" : "F-Stop",
    "Flash" : "Flash",
    "FocalLength" : "Focal Length",
    "ISOSpeedRatings" : "ISO",
    "ShutterSpeedValue" : "Shutter Speed"
}


def cria_thumbnail(filename):
    if os.path.exists(filename):
        imagem = Image.open(filename)
        imagem.thumbnail((75,75))
        imagem.save('thumbnail.png', format="PNG", optimize=True)

def mostrar_imagem(imagem, window):
    imagem.thumbnail((500,500))
    bio = io.BytesIO()
    imagem.save(bio, "PNG")
    window["-IMAGE-"].draw_image(data=bio.getvalue(), location=(0,400))

def carrega_imagem(filename, window):
    if os.path.exists(filename):
        imagem = Image.open(filename)
        mostrar_imagem(imagem, window)

def reduzir_qualidade(filename, qualidade):
    if os.path.exists(filename):
        imagem = Image.open(filename)
        imagem.save("baixa_qualidade.jpg", format="JPEG", optimize=True, quality=int(qualidade))

def abre_url(url, window):
    imagem = requests.get(url)
    imagem = Image.open(io.BytesIO(imagem.content))
    mostrar_imagem(imagem, window) 

def salvar_url(url):
    imagem = requests.get(url)
    imagem = Image.open(io.BytesIO(imagem.content))
    imagem.save("daweb.png", format="PNG", optimize=True)

def get_exif(filename):
    exif_data = {}
    image = Image.open(filename)
    info = image._getexif()
    if info:
        for tag, value in info.items():
            decoded = TAGS.get(tag, tag)
            if decoded == "GPSInfo":
                gps_data = {}
                for gps_tag in value:
                    sub_decoded = GPSTAGS.get(gps_tag, gps_tag)
                    gps_data[sub_decoded] = value[gps_tag]
                exif_data[decoded] = gps_data
            else:
                exif_data[decoded] = value
    return exif_data

def exibir_exif(filename, path, window):
    if os.path.exists(filename):
        image_path = Path(path)
        exif_data = get_exif(image_path.absolute())
        for field in fields:
            if field == "File name":
                window[field].update(image_path.name)
            elif field == "File size":
                window[field].update(image_path.stat().st_size)
            else:
                window[field].update(exif_data.get(field, "No data"))

def mirror(image_path, output_image_path): #espelhar
    image = Image.open(image_path)
    mirror_image = image.transpose(Image.FLIP_TOP_BOTTOM) #FLIP_LEFT_RIGHT, FLIP_TOP_BOTTOM, TRANSPOSE
    mirror_image.save(output_image_path)

def crop_image(image_path, coords, output_image_path): #recortar
    image = Image.open(image_path)
    cropped_image = image.crop(coords)
    cropped_image.save(output_image_path)

def resize(input_image_path, output_image_path, size):
    image = Image.open(input_image_path)
    resized_image = image.resize(size)
    resized_image.save(output_image_path)

def rotate(image_path, degrees_to_rotate, output_image_path):
    image_obj = Image.open(image_path)
    rotated_image = image_obj.rotate(degrees_to_rotate)
    rotated_image.save(output_image_path)


def main():
    layout = [
        [sg.Graph(key="-IMAGE-", canvas_size=(800,600), graph_bottom_left=(0, 0), graph_top_right=(400, 400), change_submits=True, drag_submits=True)],
        [
            sg.Text("Arquivo de Imagem"),
            sg.Input(size=(25,1), key="-FILE-"),
            sg.FileBrowse(file_types=file_types, key="-LOAD-"),
            sg.Button("Carregar Imagem"),
            sg.Button("Gerar Thumbnail"),
            sg.Text("Selecione a Qualidade:"),
            sg.Combo(['0','25','50','75','100'], default_value="0", key="-QUALITY-"),
            sg.Button("Salvar com a Qualidade"),        
            sg.Button("Abrir URL"),
            sg.Button("Salvar da Web")
        ],
        [
            sg.Button("Metadados")
        ]
    ]

    for field in fields:
        layout += [[sg.Text(fields[field], size=(10,1)),
                    sg.Text("", size=(25,1), key=field)]]

    window = sg.Window("Visualizador de Imagem", layout=layout)
    dragging = False
    ponto_inicial = ponto_final = retangulo = None

    while True:
        event, value = window.read()
        if event == "Exit" or event == sg.WINDOW_CLOSED:
            break
        filename = value["-FILE-"]
        if event == "Carregar Imagem":
            carrega_imagem(filename, window)
        if event == "Gerar Thumbnail":
            cria_thumbnail(filename)
        if event == "Salvar com menos Qualidade":
            reduzir_qualidade(filename, value["-QUALITY-"])
        if event == "Abrir URL":
            abre_url(filename,window)
        if event == "Salvar da Web":
            salvar_url(filename)
        if event == "Metadados":
            exibir_exif(filename, value["-LOAD-"], window)
        if event == "-IMAGE-":
            x, y = value["-IMAGE-"]
            if not dragging:
                ponto_inicial = (x, y)
                dragging = True
            else:
                ponto_final = (x, y)
            if retangulo:
                window["-IMAGE-"].delete_figure(retangulo)
            if None not in (ponto_inicial, ponto_final):
                retangulo = window["-IMAGE-"].draw_rectangle(ponto_inicial, ponto_final, line_color='red')
        elif event.endswith('+UP'):
            dragging = False

    window.close()

if __name__ == "__main__":
    main()