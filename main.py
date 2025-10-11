
from qrcode import QRCode
from qrcode.constants import ERROR_CORRECT_L
from PIL import Image, ImageDraw
from qrcode.image.pil import Image, PilImage

from io import BytesIO



def gen_qrcode(info_qr: str, png_name: str)->None:


    qr = QRCode(
        version=1,
        error_correction=ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(info_qr)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    qr_buffer = BytesIO()
    img.save(qr_buffer, format="PNG")
    qr_buffer.seek(0)
    img.save(f"{png_name}.png")

if __name__ == "__main__":
    while True:
        print("Pt exit keep CTRL+Z")
        qr_info: str = input("Info QR: ").strip()
        nume_qr: str = input("Nume fisier (.png): ").strip()
        gen_qrcode(info_qr=qr_info, png_name=nume_qr)
