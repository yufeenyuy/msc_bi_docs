#!/usr/bin/env python3
"""
Generate a QR code with green position markers and NMS label.
The QR code encodes: https://development.wirngoh.com/survey

Install:
    pip install qrcode[pil] Pillow

Run:
    python generate_qrcode.py

Output:
    prodqrcode.png
"""

import qrcode
from qrcode.constants import ERROR_CORRECT_H
from PIL import Image, ImageDraw, ImageFont

# Settings
SURVEY_URL = "https://wirngoh.com/survey"
OUTPUT_FILE = "prodqrcode.png"
QR_SIZE = 800  # Pixel size of the QR code

# Colors
NAVY = "#0B2344"
GREEN = "#09A77E"
DEEP_GREEN = "#006B45"
WHITE = "#FFFFFF"

def generate_qrcode():
    """Generate QR code with styled center badge."""
    
    # Create QR code with high error correction
    qr = qrcode.QRCode(
        version=None,  # Auto-detect version
        error_correction=ERROR_CORRECT_H,
        box_size=10,
        border=2
    )
    
    qr.add_data(SURVEY_URL)
    qr.make(fit=True)
    
    # Generate QR code image with navy modules on white background
    qr_img = qr.make_image(
        fill_color=NAVY,
        back_color=WHITE
    ).convert("RGB")
    
    # Resize to desired pixel size
    qr_img = qr_img.resize(
        (QR_SIZE, QR_SIZE),
        Image.Resampling.NEAREST
    )
    
    # Add center badge with NMS label
    draw = ImageDraw.Draw(qr_img)
    center = QR_SIZE // 2

    # Style the three finder patterns with rounded green frames and
    # round deep-green centers.
    module_size = QR_SIZE / (qr.modules_count + 2 * qr.border)
    finder_size = 7 * module_size
    finder_center_size = 3 * module_size
    finder_radius = module_size * 1.25
    finder_centers = (
        (qr.border * module_size + finder_size / 2,
         qr.border * module_size + finder_size / 2),
        ((qr.border + qr.modules_count - 7) * module_size + finder_size / 2,
         qr.border * module_size + finder_size / 2),
        (qr.border * module_size + finder_size / 2,
         (qr.border + qr.modules_count - 7) * module_size + finder_size / 2),
    )

    for finder_center_x, finder_center_y in finder_centers:
        draw.rectangle(
            (finder_center_x - finder_size / 2,
             finder_center_y - finder_size / 2,
             finder_center_x + finder_size / 2,
             finder_center_y + finder_size / 2),
            fill=WHITE
        )
        draw.rounded_rectangle(
            (finder_center_x - finder_size / 2,
             finder_center_y - finder_size / 2,
             finder_center_x + finder_size / 2,
             finder_center_y + finder_size / 2),
            radius=finder_radius,
            fill=GREEN
        )
        draw.rounded_rectangle(
            (finder_center_x - 5 * module_size / 2,
             finder_center_y - 5 * module_size / 2,
             finder_center_x + 5 * module_size / 2,
             finder_center_y + 5 * module_size / 2),
            radius=module_size * 0.5,
            fill=WHITE
        )
        draw.ellipse(
            (finder_center_x - finder_center_size / 2,
             finder_center_y - finder_center_size / 2,
             finder_center_x + finder_center_size / 2,
             finder_center_y + finder_center_size / 2),
            fill=DEEP_GREEN
        )
    
    # Round green border around the center mark
    outer_radius = int(QR_SIZE * 0.12)
    draw.ellipse(
        (center - outer_radius, center - outer_radius,
         center + outer_radius, center + outer_radius),
        fill=GREEN
    )
    
    # Deep-green cross-shaped center
    cross_radius = int(QR_SIZE * 0.088)
    cross_arm = int(QR_SIZE * 0.045)
    draw.rectangle(
        (center - cross_arm, center - cross_radius,
         center + cross_arm, center + cross_radius),
        fill=DEEP_GREEN
    )
    draw.rectangle(
        (center - cross_radius, center - cross_arm,
         center + cross_radius, center + cross_arm),
        fill=DEEP_GREEN
    )
    
    # Add "NMS" text on badge
    try:
        # Try to use a system font, fall back to default if not available
        font_size = int(QR_SIZE * 0.08)
        try:
            fnt = ImageFont.truetype("arial.ttf", font_size)
        except:
            try:
                fnt = ImageFont.truetype("DejaVuSans-Bold.ttf", font_size)
            except:
                fnt = ImageFont.load_default()
    except:
        fnt = ImageFont.load_default()
    
    text = "NMS"
    bbox = draw.textbbox((0, 0), text, font=fnt)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    text_x = center - text_width // 2
    text_y = center - text_height // 2 - int(QR_SIZE * 0.01)
    
    draw.text(
        (text_x, text_y),
        text,
        fill=WHITE,
        font=fnt
    )
    
    # Save the QR code
    qr_img.save(OUTPUT_FILE)
    print(f"✓ QR code generated: {OUTPUT_FILE}")
    print(f"  URL: {SURVEY_URL}")
    print(f"  Size: {QR_SIZE}x{QR_SIZE} pixels")

if __name__ == "__main__":
    generate_qrcode()
