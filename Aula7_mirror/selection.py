import io
import os
import PySimpleGUI as sg
from PIL import Image

file_types = [
    ("JPEG (*.jpg)", "*.jpg"),
    ("PNG (*.png)", "*.png"),
    ("Todos os arquivos (*.*)", "*.*")
]

def main():
    layout = [
        [sg.Graph(key="-IMAGE-", canvas_size=(500,500), graph_bottom_left=(0, 0), graph_top_right=(400, 400), change_submits=True, drag_submits=True)],
        [
            sg.Text("Arquivo de Imagem"),
            sg.Input(size=(25,1), key="-FILE-"),
            sg.FileBrowse(file_types=file_types),
            sg.Button("Carregar Imagem")
        ]
    ]

    window = sg.Window("Visualizador de Imagem", layout=layout)
    dragging = False
    ponto_inicial = ponto_final = retangulo = None

    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "Carregar Imagem":
            filename = values["-FILE-"]
            if os.path.exists(filename):
                image = Image.open(filename)
                image.thumbnail((500,500))
                bio = io.BytesIO()
                image.save(bio, format="PNG")
                window["-IMAGE-"].draw_image(data=bio.getvalue(), location=(0,400))

        if event == "-IMAGE-":
            x, y = values["-IMAGE-"]
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