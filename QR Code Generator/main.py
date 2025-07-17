
import qrcode
from PIL import Image

def generate_qr(data, size=10, border=4, logo_path=None, output_file='qr_code.png'):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # high for logo overlay
        box_size=size,
        border=border,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white").convert('RGB')

    if logo_path:
        logo = Image.open(logo_path)
        # Resize logo
        img_w, img_h = img.size
        factor = 4
        size_w = int(img_w / factor)
        size_h = int(img_h / factor)
        logo = logo.resize((size_w, size_h))
        # Position in center
        pos = ((img_w - size_w) // 2, (img_h - size_h) // 2)
        img.paste(logo, pos, mask=logo if logo.mode == 'RGBA' else None)

    img.save(output_file)
    print(f"QR code saved to: {output_file}")

if __name__ == "__main__":
    print("=== QR Code Generator ===")
    data = input("Enter text or URL: ")
    size = int(input("Box size (default 10): ") or "10")
    border = int(input("Border size (default 4): ") or "4")
    logo_path = input("Logo file path (optional): ") or None
    output_file = input("Output filename (default 'qr_code.png'): ") or "qr_code.png"
    generate_qr(data, size, border, logo_path, output_file)
