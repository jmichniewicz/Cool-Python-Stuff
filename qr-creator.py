import qrcode
img = None
def generate_code(text):
    qr = qrcode.QRCode(
        version = 1,
        #error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size = 10,
        border = 4
    )

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qrimage.png")
link = input("What is the URL you want a QR code for?  ")
#if link.startswith("http://")

generate_code(link)