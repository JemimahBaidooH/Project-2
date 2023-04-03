import PySimpleGUI as sg
import pyttsx3 as pt

# Set a theme for the layout
sg.theme('DarkTeal')
font= ('Verdana',12)
# All the staff inside the window.
index = 1
color = {0: ("white", "purple"), 1: ("yellow", "purple")}
layout = [
    [sg.Text(''), sg.Input(text_color= 'white', key= 'INPUT' ), sg.Button('Speak', key='LISTENER',  mouseover_colors=color[index], use_ttk_buttons=True, size= (7,1)), sg.Text(), sg.Button('Close', key='close',  mouseover_colors=color[index], use_ttk_buttons=True, size= (7,1))],
    [sg.Text('Select voice type:'), sg.Radio("male", "RADIO", default= False, key='-MALE-'),sg.Radio('female', 'RADIO', default = True, key ='-FEMALE-' )],
    [sg.Text( key= 'RESULT')],
]

# Create the Window
window = sg.Window('Text to Speech App', layout, font = font)

# Event loop
while True:
    event , values = window.read()
    if event == sg.WIN_CLOSED or event == 'close':
        break
    elif event == 'LISTENER':
        Text = str(values['INPUT'])
        eng = pt.init() # Initialise the instance
        eng.setProperty('rate', 140)
        eng.setProperty('volume',2.0)
               
        voice = eng.getProperty('voices') # get the available voice 
        male = values['-MALE-']
        female= values['-FEMALE-']
        if male:
            eng.setProperty('voice', voice[0].id) # set the voice to index 0 for male voice
        elif female :
            eng.setProperty('voice', voice[1].id) # set the voice to index 1 for female voice
        
        result = eng.say(Text)    
        eng.runAndWait()
        window['RESULT'].update(result)
window.close()
