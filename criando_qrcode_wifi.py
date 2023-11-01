# Criando um QR Code para a sua rede wi-fi com Python

import qrcode

ssid = "nomedaredeaqui"
password = "senhaaqui"
security = "WPA" # WPA, WEP ou "" para redes sem segurança

wifi_data = f"WIFI:T:{security};S:{ssid};P:{password};;"

qr = qrcode.QRCode(
    version = 1, #  A versão do código QR, que varia de 1 a 40. Quanto maior a versão, mais dados o código QR pode armazenar.
    error_correction = qrcode.constants.ERROR_CORRECT_L, # Define o nível de correção de erros a ser aplicado ao código QR. Existem quatro níveis possíveis: qrcode.constants.ERROR_CORRECT_L: correção de erro de baixo nível (7% ou menos de correção de erros) | qrcode.constants.ERROR_CORRECT_M: correção de erro moderada (15% ou menos de correção de erros). | qrcode.constants.ERROR_CORRECT_Q: correção de erro de qualidade (25% ou menos de correção de erros). | qrcode.constants.ERROR_CORRECT_H: correção de erro de alta (30% ou menos de correção de erros).
    box_size = 10, #  Tamanho do pixel em unidades de células (módulos) no código QR. Um valor maior resulta em um código QR maior.
    border = 4 # A margem ao redor do código QR, representada como o número de células vazias. Um valor maior aumenta a margem ao redor do código QR.
)

qr.add_data(wifi_data)
qr.make(fit=True) 

img = qr.make_image(fill_color = 'black', back_color = 'white') # Você pode personalizar as cores com strings ou tuplas RGB
img.save("qrcode_wifi.png")
img.show()
