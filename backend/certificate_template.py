from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import qrcode
from reportlab.lib.utils import ImageReader

def generate_certificate(name, course, grade, date, certificate_id, output_file):
    c = canvas.Canvas(output_file, pagesize=A4)

    # Title
    c.setFont("Helvetica-Bold", 26)
    c.drawCentredString(300, 780, "Certificate of Completion")

    # Issuer
    c.setFont("Helvetica", 16)
    c.drawCentredString(300, 745, "Issued by example.com")

    # Certificate info
    c.setFont("Helvetica", 14)
    c.drawString(80, 680, f"Certificate ID: {certificate_id}")
    c.drawString(80, 650, f"Name: {name}")
    c.drawString(80, 620, f"Course: {course}")
    c.drawString(80, 590, f"Grade: {grade}")
    c.drawString(80, 560, f"Date: {date}")

    # Generate QR Code (auto verification link)
    qr_url = f"https://example.com/verify/{certificate_id}"
    qr = qrcode.make(qr_url)
    qr_img = ImageReader(qr)

    # Draw QR code in the bottom-right
    c.drawImage(qr_img, 420, 500, width=150, height=150)

    c.save()
