#pip install qrcode[pil]
import qrcode

#criar um código QR
qr = qrcode.QRCode(version=1, box_size=10, border=5)

#adicionar dados ao código QR
data = "https://sp.senai.br/unidade/taubate/"
qr.add_data(data)
qr.make(fit=True)

#criar imagem do código QR
img = qr.make_image(fill_color="white", back_color="black")

#salvar imagem em um arquivo
img.save("qr_code.png")