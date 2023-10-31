from flask import Flask, render_template, request, url_for
import qrcode

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html', titulo='Wi-Fi QR Code Generator')


@app.route('/criar', methods=['POST'])
def criar():

    # hidden_ssid = request.form['hidden-ssid'] # Adicionar depois

    ssid = request.form['ssid']
    password = request.form['password']
    security = request.form['security']
  
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
    img.save("static/qrcode_wifi.png")

    return render_template('index.html', titulo='Wi-Fi QR Code Generator', qr_code_image_data=url_for('static', filename='qrcode_wifi.png'))

if __name__ == '__main__':
    app.run(debug=True)