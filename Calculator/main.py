import PySimpleGUI as sg

def create_win(theme):


    sg.theme(theme)
    sg.set_options(font='Calibre 14', button_element_size=(6,3))

    btn_size=(6,3)

    layout=[
        [sg.Text('', 
                 font="franklin 26", 
                 justification='right',
                 expand_x=True,
                   pad=(10,20),
                   right_click_menu=theme_menue,
                   key="-text-"
                   
                   )],
        [sg.Button('enter', expand_x=True), sg.Button('clear', expand_x=True)],
        [sg.Button('7', size= btn_size),sg.Button('8', size= btn_size),sg.Button('9', size= btn_size),sg.Button('/', size= btn_size)],
        [sg.Button('4', size= btn_size),sg.Button('5', size= btn_size),sg.Button('6', size= btn_size),sg.Button('*', size= btn_size)],
        [sg.Button('1', size= btn_size),sg.Button('2', size= btn_size),sg.Button('1', size= btn_size),sg.Button('-', size= btn_size)],
        [sg.Button('0', expand_x=True),sg.Button('.', size= btn_size),sg.Button('+', size= btn_size)]
        ]
    return sg.Window('calculator' ,layout)


theme_menue=['menu',['DarkGrey15','Dark','tan','random']]
window=create_win('tan')

current_num=[]
full_opr=[]

while True:
    event,values=window.read()
    if event== sg.WIN_CLOSED:
        break


    if event in theme_menue[1]:
        window.close()
        window= create_win(event)

    if event in ['0','1','2','3','4','5','6','7','8','9','.']:
        current_num.append(event)
        num_string=''.join(current_num)
        window['-text-'].update(num_string)

    if event in ['+','-','/','*']:
        full_opr.append(''.join(current_num))
        current_num=[]
        full_opr.append(event)
        window['-text-'].update('')
    if event == 'enter':
        full_opr.append(''.join(current_num))
        result=eval(''.join(full_opr))
        window['-text-'].update(result)
        full_opr=[]
    if event == "clear":
        current_num=[]
        full_opr=[]
        window['-text-'].update('')

window.close()
