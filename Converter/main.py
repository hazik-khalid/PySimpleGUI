import PySimpleGUI as sg

layout =[
    [sg.Text('converter' , enable_events=True) , sg.Spin(['name1','name2'])],
    [sg.Input(key='input')],
    [sg.Button('text')]
        ]

window =sg.Window('converter',layout)

while True:
    event,values=window.read()
      
    if event== sg.WIN_CLOSED:
        break

    if event=='text':
        window['converter'].update(values['input'])

  
        
window.close()
