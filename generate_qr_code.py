import qrcode  # Ensure no name conflicts

try:
    obj_qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    obj_qr.add_data("https://www.javatpoint.com/python-tutorial")
    obj_qr.make(fit=True)
    qr_img = obj_qr.make_image(fill_color="cyan", back_color="black")
    qr_img.save("qr-img1.png")

    print("QR code generated and saved as 'qr-img1.png'")

except Exception as e:
    print(f"An error occurred: {e}")
