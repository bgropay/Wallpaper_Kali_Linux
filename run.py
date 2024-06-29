import os
import shutil
import imghdr

def move_images(source_dir, target_dir):
    # Membuat folder target jika belum ada
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    # Iterasi semua file dan direktori di dalam source_dir
    for root, _, files in os.walk(source_dir):
        for filename in files:
            file_path = os.path.join(root, filename)
            # Mengecek apakah file adalah gambar berdasarkan ekstensinya
            if imghdr.what(file_path) is not None:
                # Memindahkan file gambar ke folder target
                shutil.move(file_path, os.path.join(target_dir, filename))

source_directory = '/usr/share/wallpapers'  # Ganti dengan direktori sumber Anda
target_directory = 'tempat_sampah'  # Ganti dengan direktori tujuan Anda

move_images(source_directory, target_directory)
