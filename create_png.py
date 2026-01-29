#!/usr/bin/env python3
import base64
import os

# Base64 encoded 1x1 pixel transparent PNG
png_base64 = "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNkYPhfDwAChwGA60e6kgAAAABJRU5ErkJggg=="

# List semua file yang diperlukan
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

# Buat folder screenshots jika belum ada
os.makedirs("screenshots", exist_ok=True)

# Buat setiap file
for filename in files:
    filepath = os.path.join("screenshots", filename)
    with open(filepath, "wb") as f:
        f.write(base64.b64decode(png_base64))
    print(f"✅ Created: {filepath}")

print(f"\n🎉 Created {len(files)} placeholder PNG files")
print("📁 Location: screenshots/")
