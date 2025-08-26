import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
import os, csv

# ========================
# CONFIGURATION
# ========================
EMAIL = "cfckoshi@gmail.com"             
PASSWORD = "app password"         
SUBJECT = "🎉 Your Certificate from Code for Change"
CSV_FILE = "students.csv"                  
HTML_TEMPLATE_FILE = "template.html"       
CERTIFICATE_FOLDER = "certificates"       

# ========================
# HELPER FUNCTION
# ========================
def embed_inline_image(msg, filepath, cid_name):
    """Attach image inline using Content-ID (cid)."""
    if os.path.exists(filepath):
        with open(filepath, "rb") as f:
            img = MIMEImage(f.read())
            img.add_header("Content-ID", f"<{cid_name}>")
            img.add_header("Content-Disposition", "inline", filename=os.path.basename(filepath))
            msg.attach(img)
    else:
        print(f"⚠️ Image not found: {filepath}")

# ========================
# LOAD TEMPLATE
# ========================
with open(HTML_TEMPLATE_FILE, "r", encoding="utf-8") as f:
    html_template = f.read()

context = ssl.create_default_context()

# ========================
# SEND EMAILS
# ========================
with open(CSV_FILE, newline="", encoding="utf-8") as csvfile :
    reader = csv.DictReader(csvfile)
    for row in reader:
        recipient = row["email"].strip()
        name = row["name"].strip()
        cert_file = os.path.join(CERTIFICATE_FOLDER, f"{recipient}.png")

        if not os.path.exists(cert_file):
            print(f"⚠️ Certificate not found: {cert_file}")
            continue

        # Personalize HTML
        html_body = html_template.format(name=name)

        # Create email
        msg = MIMEMultipart("related")
        msg["From"] = EMAIL
        msg["To"] = recipient
        msg["Subject"] = SUBJECT

        # Alternative part (HTML)
        alt = MIMEMultipart("alternative")
        msg.attach(alt)
        alt.attach(MIMEText(html_body, "html"))

        # Embed images inline
        embed_inline_image(msg, cert_file, "certificate")  # inline certificate

        # Attach certificate as downloadable file
        with open(cert_file, "rb") as f:
            attach = MIMEImage(f.read())
            attach.add_header("Content-Disposition", "attachment", filename=os.path.basename(cert_file))
            msg.attach(attach)

        # Send email
        try:
            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls(context=context)
                server.login(EMAIL, PASSWORD)
                server.sendmail(EMAIL, recipient, msg.as_string())
                print(f"✅ Sent to {recipient} ({name})")
        except Exception as e:
            print(f"❌ Failed to send to {recipient}: {e}")
