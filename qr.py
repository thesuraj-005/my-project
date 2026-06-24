import qrcode
data='https://www.instagram.com'

img = qrcode.make(data)
img.save('qr1.png')