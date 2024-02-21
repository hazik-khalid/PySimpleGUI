import PySimpleGUI as sg

layout = [
    [sg.Input(key="-input-"),
      sg.Spin(['km to mile', 
               'kg to pound','sec to min'],key='-units-'), sg.Button('convert' ,key='-convert-')],
    [sg.Text('output', key='-output-')]
        ]

window = sg.Window("converter", layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break
    if event=='-convert-':
        input_value=values["-input-"]
        print(input_value)


window.close()
