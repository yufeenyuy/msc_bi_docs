#!/usr/bin/env python3
"""Replace the QR code in the survey artwork with the production QR code."""

from pathlib import Path

from PIL import Image


BASE_IMAGE = Path("nwafrqrcode.png")
QR_IMAGE = Path("prodqrcode.png")
OUTPUT_IMAGE = Path("frprodqrcode.png")
QR_POSITION = (542, 249)
QR_SIZE = (660, 660)


def combine_images() -> None:
    artwork = Image.open(BASE_IMAGE).convert("RGB")
    qr_code = Image.open(QR_IMAGE).convert("RGB").resize(
        QR_SIZE,
        Image.Resampling.LANCZOS,
    )
    artwork.paste(qr_code, QR_POSITION)
    artwork.save(OUTPUT_IMAGE)
    print(f"Combined image generated: {OUTPUT_IMAGE}")


if __name__ == "__main__":
    combine_images()