import qrcode


pasta = "https://github.com/tauanebraz"


qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data(pasta)
qr.make(fit=True)

# Criar e salvar a imagem
img = qr.make_image(fill_color="black", back_color="white")
img.save("qrcode_token.png")

print("QR Code gerado com sucesso!")