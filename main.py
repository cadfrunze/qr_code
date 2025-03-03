
from qrcode import QRCode
from qrcode.constants import ERROR_CORRECT_L
from PIL import Image, ImageDraw
from qrcode.image.pil import Image, PilImage

from io import BytesIO



def gen_qrcode(stringul:str)->None:


    qr = QRCode(
        version=1,
        error_correction=ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(stringul)
    # qr.add_data(client_final["nume"])
    # qr.add_data(client_final["prenume"])
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    qr_buffer = BytesIO()
    img.save(qr_buffer, format="PNG")
    qr_buffer.seek(0)
    img.save("qr.png")


gen_qrcode(stringul="http://192.168.0.66:5000".strip())
