import PySimpleGUI as sg

def create_win(theme):


    sg.theme(theme)
    sg.set_options(font='Calibre 14', button_element_size=(6,3))

    btn_size=(6,3)

    layout=[
        [sg.Text('output', 
                 font="franklin 26", 
                 justification='right',
                 expand_x=True,
                   pad=(10,20)
                   
                   )],
        [sg.Button('enter', expand_x=True), sg.Button('clear', expand_x=True)],
        [sg.Button('7', size= btn_size),sg.Button('8', size= btn_size),sg.Button('9', size= btn_size),sg.Button('/', size= btn_size)],
        [sg.Button('4', size= btn_size),sg.Button('5', size= btn_size),sg.Button('6', size= btn_size),sg.Button('*', size= btn_size)],
        [sg.Button('1', size= btn_size),sg.Button('2', size= btn_size),sg.Button('1', size= btn_size),sg.Button('-', size= btn_size)],
        [sg.Button('0', expand_x=True),sg.Button('.', size= btn_size),sg.Button('+', size= btn_size)]
        ]
    return sg.Window('calculator' ,layout)

window=create_win('tan')

while True:
    event,values=window.read()
    if event== sg.WIN_CLOSED:
        break
    

window.close()
