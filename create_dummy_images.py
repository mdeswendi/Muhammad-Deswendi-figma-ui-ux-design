import base64
# Base64 encoded 1x1 pixel transparent PNG
png_1x1 = "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNkYPhfDwAChwGA60e6kgAAAABJRU5ErkJggg=="

# List of files to create
files = [
    "Login Page.png",
    "Dashboard Page.png", 
    "Verifikasi Page.png",
    "Pelaporan Page.png",
    "Pengajuan Page.png",
    "Pengajuan Proposal Form.png",
    "Pengajuan Reimburse Form.png",
    "Proses Verifikasi Form.png",
    "Dashboard Monitoring Keuangan.png",
    "Notification.png"
]

# Create each file
for filename in files:
    with open(f"screenshots/{filename}", "wb") as f:
        f.write(base64.b64decode(png_1x1))
    print(f"Created: screenshots/{filename}")

print("✅ All placeholder files created")
