
from qrcode import QRCode
from qrcode.constants import ERROR_CORRECT_L
from PIL import Image, ImageDraw
from qrcode.image.pil import Image, PilImage

from io import BytesIO



def gen_qrcode(continut: str, png_name: str)->None:


    qr = QRCode(
        version=1,
        error_correction=ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(continut)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    qr_buffer = BytesIO()
    img.save(qr_buffer, format="PNG")
    qr_buffer.seek(0)
    img.save(f"{png_name}.png")

if __name__ == "__main__":
    while True:
        print("For exit keep CTRL+Z\n")
        qr_info: str = input("Info QR: ").strip()
        nume_qr: str = input("Nume fisier (.png): ").strip()
        gen_qrcode(continut=qr_info, png_name=nume_qr)
