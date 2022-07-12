import qrcode

data = "https://www.freecodecamp.org/news/python-projects-for-beginners/"

# img = qrcode.make(data)

qr = qrcode.QRCode(version = 1, box_size = 20, border = 5)

qr.add_data(data)

img = qr.make_image(fill_color = 'green', back_color = 'black')

img.save('/home/rasmesxiii/forTry/firstQR.png')