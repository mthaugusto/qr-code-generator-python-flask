# Criando um QR Code para a sua rede wi-fi com Python

import qrcode

ssid = "nomedaredeaqui"
password = "senhaaqui"
security = "WPA" # WPA, WEP ou "" para redes sem segurança

wifi_data = f"WIFI:T:{security};S:{ssid};P:{password};;"

qr = qrcode.QRCode(
    version = 1, 
    error_correction = qrcode.constants.ERROR_CORRECT_L, 
    box_size = 10, 
    border = 4 
)

qr.add_data(wifi_data)
qr.make(fit=True) 

img = qr.make_image(fill_color = 'black', back_color = 'white') 
img.save("qrcode_wifi.png")
img.show()
