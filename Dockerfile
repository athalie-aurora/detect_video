FROM python:3.9

# Menggunakan gambar Python versi 3.9 sebagai basis untuk kontainer.

WORKDIR /security_me
# Mengatur direktori kerja di dalam kontainer sebagai /code_gsg.

COPY . /security_me
# Menyalin seluruh konten dari direktori saat ini ke dalam direktori /code_gsg di dalam kontainer.

RUN apt-get update && apt-get install -y \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    libgl1-mesa-glx \
    libv4l-dev
# Memperbarui dan menginstal dependensi yang diperlukan, seperti paket-paket yang dibutuhkan oleh OpenCV.

RUN pip install --no-cache-dir opencv-python
# Menginstal OpenCV Python package menggunakan pip, dengan opsi --no-cache-dir untuk menghindari penggunaan cache.

CMD ["python3", "security_me.py"]
# Perintah yang akan dijalankan saat kontainer dijalankan, yaitu menjalankan script "security_me.py" menggunakan Python 3.
