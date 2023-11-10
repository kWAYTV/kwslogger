import os, qrcode, random, string
from qrcode.constants import ERROR_CORRECT_L

class QRCodeGenerator:
    def __init__(self, box_size=10, border=1, version=1, error_correction=ERROR_CORRECT_L, fill_color="#000000"):
        self.box_size = box_size
        self.border = border
        self.version = version
        self.error_correction = error_correction
        self.fill_color = fill_color

    def generate_qr_code(self, text):
        qr = qrcode.QRCode(
            version=self.version,
            error_correction=self.error_correction,
            box_size=self.box_size,
            border=self.border
        )
        qr.add_data(text)
        qr.make(fit=True)
        img = qr.make_image(fill_color=self.fill_color, back_color="white")
        return img

    def save_qr_code(self, text):
        img = self.generate_qr_code(text)
        img.save(f"{self.random_string(10)}.png")

    def random_string(self, length):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(length))