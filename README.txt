PROGRAM OPERASI DASAR CITRA DIGITAL: GRAYSCALE

Isi folder:
- main.py             : program utama
- gambar.jpg          : letakkan gambar yang ingin diproses di sini
- hasil_grayscale.png : dibuat otomatis saat program dijalankan
- requirements.txt    : daftar library yang diperlukan

CARA MENJALANKAN (Windows / VS Code):
1. Pasang Python jika belum ada.
2. Buka terminal pada folder ini.
3. Jalankan: python -m pip install -r requirements.txt
4. Salin sebuah gambar ke folder ini dan ubah namanya menjadi gambar.jpg.
5. Jalankan: python main.py

METODE:
Konversi RGB ke grayscale dengan rumus:
Gray = 0.299R + 0.587G + 0.114B

Program menghitung nilai grayscale setiap piksel secara manual dengan perulangan,
menyimpan hasil, menampilkan perbandingan gambar, serta mencetak informasi piksel.

Catatan: Jika gambar asli berformat PNG, buka dan simpan salinannya sebagai JPG,
atau sesuaikan nama input_path di main.py dengan nama file tersebut.
