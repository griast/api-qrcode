from flask import Flask,request
from flask import send_file
from flask_qrcode import QRcode

app = Flask(__name__)
qrcode = QRcode(app)

def generateQrCode(properties):    
    img = qrcode(
    properties['content'],
    version=1,
    error_correction='H',
    box_size=10,
    border=2,
    icon_img=properties['iconImg'],
    mode="raw",
    fill_color='black'
    )
    return img

@app.route('/qrcode', methods=['POST'])
def createQrCode():
    json = request.get_json()
    img = generateQrCode(json)
    return send_file(img, mimetype="image/png")

    

if __name == '__main__':
    app.run(debug=True, host='0.0.0.0')