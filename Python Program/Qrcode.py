import Qrcode
from PIL import image
qr = qecode.QRCde(
    version =15,
    box_size =10,
    border =5,
)
data="https://www.youtube.com/channel/UCaWT4KW-mKTxnQyW5M9oIKA"
qr.add_data(data)
qe.make(fit= True)
img=qr.make_image(fill="black",back_color="white")
image.save("test.png")