import qrcode as qr
import PySimpleGUI as sg 

sg.theme('DarkTeal')
font =('Verdana', 12)

qrImage = [sg.Image('', key = 'qrCode')]

# the layout
index = 0
color = {0: ("white", "purple"), 1: ("red", "purple")}
layout = [
    [sg.Text('Enter URL:'), sg.Input(text_color= 'black', key= 'URL' )],
    [sg.Button('Create', key='Submit', mouseover_colors= color[index], use_ttk_buttons=True, size= (7,1)),  sg.Button('Close', key='CLOSE', mouseover_colors= color[index], use_ttk_buttons=True, size= (7,1))],
    [sg.Column([qrImage], justification= 'center')],
]

 # Create the Window
window = sg.Window('QR coode Generator', layout, font= font)

# Event loop  
while True:
    event , values = window.read()
    if event == sg.WIN_CLOSED or event == 'CLOSE':
        break
    elif event == 'Submit':
        url = values['URL']
        if url:
            qr_code = qr.QRCode(
                version=1,
                error_correction=qr.constants.ERROR_CORRECT_L,
                box_size=20,
                border=4,
                )
            qr_code.add_data('Some data')
            qr_code.make(fit=True)
            img = qr_code.make_image(fback_color=(255, 255, 255), fill_color=(0, 0, 0))
            img.save('qr_code.png')
            window['qrCode'].update('qr_code.png')
window.close()