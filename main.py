import PySimpleGUI as sg
from PIL import Image, ImageFilter, ImageOps
from io import BytesIO

sg.theme("BlueMono")
sg.set_options(font="Calibre 15")
image_col = sg.Column([[sg.Image("Pic/question.png", key="-BMIIMAGE-", size=(120, 250))]])

control_col = sg.Column([
    [sg.Text("Your BMI", key="-BMIVALUE-", font="Calibre 25", expand_x=True, justification="center")],
    [sg.Frame("Weight(kg)", layout=[[sg.Slider(range=(1, 200), orientation="h", key="-WEIGHT-", size=(500, 25))]]
              , expand_x=True, size=(500, 100))],
    [sg.Frame("Height(cm)", layout=[[sg.Slider(range=(100, 250), orientation="h", key="-HEIGHT-"
                                               , size=(500, 25))]]
              , expand_x=True, size=(500, 100))],
    [sg.Button("Ok", expand_x=True, key="-OK-")],
])

layout = [
    [control_col, image_col]
]

window = sg.Window("BMI", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event == "-OK-":
        W = values["-WEIGHT-"]
        H = values["-HEIGHT-"]
        H = H * 10 ** -2
        BMI = W/(H**2)
        if BMI < 18.5:
            window["-BMIVALUE-"].update(f"Your BMI: {round(BMI, 2)} thin")
            window["-BMIIMAGE-"].update("Pic/thin.png")
        elif 18.5 <= BMI <= 24.9:
            window["-BMIVALUE-"].update(f"Your BMI: {round(BMI, 2)} normal")
            window["-BMIIMAGE-"].update("Pic/normal.png")
        elif 25 <= BMI <= 29.9:
            window["-BMIVALUE-"].update(f"Your BMI: {round(BMI, 2)} Overweight")
            window["-BMIIMAGE-"].update("Pic/over.png")
        elif 30 <= BMI <= 34.9:
            window["-BMIVALUE-"].update(f"Your BMI: {round(BMI, 2)} fat")
            window["-BMIIMAGE-"].update("Pic/fat.png")
        elif 35 <= BMI:
            window["-BMIVALUE-"].update(f"Your BMI: {round(BMI, 2)} very fat")
            window["-BMIIMAGE-"].update("Pic/veryfat.png")

window.close()
