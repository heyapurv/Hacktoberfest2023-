import qrcode

#QRCode object
qr = qrcode.QRCode(
    version=1, 
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
    box_size=10,  # Size of each "box" in the QR code
    border=4,  # Border size 
)
data = "Hello, World!"
qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

img.save("my_qr_code.png")
