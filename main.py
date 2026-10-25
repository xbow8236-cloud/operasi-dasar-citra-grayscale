from PIL import Image
import matplotlib.pyplot as plt
from pathlib import Path

# Pastikan file gambar bernama "gambar.jpg" berada di folder yang sama.
folder = Path(__file__).parent
input_path = folder / "gambar.jpg"
output_path = folder / "hasil_grayscale.png"

# 1. Membaca citra digital
gambar = Image.open(input_path).convert("RGB")

# 2. Mengubah citra RGB menjadi grayscale
lebar, tinggi = gambar.size
piksel_rgb = gambar.load()
gambar_gray = Image.new("L", (lebar, tinggi))
piksel_gray = gambar_gray.load()

for y in range(tinggi):
    for x in range(lebar):
        r, g, b = piksel_rgb[x, y]
        gray = int(0.299 * r + 0.587 * g + 0.114 * b)
        piksel_gray[x, y] = gray

# 3. Menyimpan citra hasil
gambar_gray.save(output_path)

# 4. Menampilkan informasi dan contoh nilai piksel
print("=== HASIL OPERASI DASAR CITRA DIGITAL ===")
print(f"Nama file input : {input_path.name}")
print(f"Ukuran gambar   : {lebar} x {tinggi} piksel")
print(f"Jumlah piksel   : {lebar * tinggi:,}")
print(f"Mode citra awal : {gambar.mode}")
print(f"Mode hasil      : {gambar_gray.mode} (grayscale)")
print(f"Hasil disimpan  : {output_path.name}")
print("\nContoh nilai piksel pada koordinat (0, 0):")
r, g, b = piksel_rgb[0, 0]
print(f"RGB = ({r}, {g}, {b})")
print(f"Grayscale = {piksel_gray[0, 0]}")

# 5. Menampilkan citra sebelum dan sesudah pemrosesan
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.imshow(gambar)
plt.title("Citra Asli (RGB)")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(gambar_gray, cmap="gray", vmin=0, vmax=255)
plt.title("Hasil Grayscale")
plt.axis("off")

plt.tight_layout()
plt.show()
