import qrcode
from PIL import Image

import os
from dotenv import load_dotenv

# Load variabel dari .env
load_dotenv()
data_url = os.getenv("QR_DATA")
logo_path = os.getenv("LOGO_PATH")

# Data yang ingin dimasukkan ke QR Code
data = data_url

# Membuat QR Code dengan pengaturan kustom
qr = qrcode.QRCode(
    version=5,  # Ukuran QR Code (1-40, semakin besar semakin detail)
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # Koreksi error tinggi (bisa menampung logo)
    box_size=10,  # Ukuran setiap kotak QR
    border=4  # Ketebalan border
)
qr.add_data(data)
qr.make(fit=True)

# Membuat gambar QR Code dengan warna kustom
qr_img = qr.make_image(fill_color="black", back_color="white").convert("RGB")  # Convert to RGB to support colors

# **Menambahkan Logo**
logo = Image.open(logo_path)  # Ganti dengan path logo kamu
qr_width, qr_height = qr_img.size

# Resize logo agar pas di tengah
logo_size = qr_width // 4  # 1/4 dari ukuran QR Code
logo = logo.resize((logo_size, logo_size), Image.LANCZOS)  # High-quality resize

# Menentukan posisi logo di tengah
pos = ((qr_width - logo_size) // 2, (qr_height - logo_size) // 2)

# Gabungkan logo dengan QR Code tanpa mengubah warna logo
qr_img.paste(logo, pos)

# Simpan dan tampilkan hasilnya
qr_img.save("qr_code_with_logo.png")
qr_img.show()
