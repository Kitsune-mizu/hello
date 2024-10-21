# menggunakan Git:
1. Instalasi Git:
 * Unduh: Kunjungi situs resmi Git (git-scm.com) dan unduh installer sesuai sistem operasi Anda.
 * Instal: Ikuti petunjuk instalasi yang diberikan.
 * cek di powersell git --version
2. Membuat Repository:
 * buka file, misal : "hello", lalu klik kanan "open git bash here"
 * Otomatis masuk ke command promt.
 * Buat direktori: $ mkdir <nama_file> dan $ cd <nama_file>
 * Inisialisasi Git: Jalankan perintah git init di dalam direktori tersebut. Ini akan membuat repository Git baru.
3. Menambah file baru pada repository
 * Misal buat file "README.md" dengan kode perintah $ echo "# pratikum" >> README.md.
4. Menambahkan File:
 * Tambahkan file: Buat file-file yang ingin Anda kelola dengan Git.
 * Stage perubahan: Gunakan perintah git add <nama_file> untuk menambahkan perubahan pada file ke staging area.
 * Commit perubahan: Jalankan perintah git commit -m "Pesan commit" untuk menyimpan perubahan ke repository lokal. Ganti "Pesan commit" dengan deskripsi singkat mengenai perubahan yang Anda buat.
5. Menggunakan Remote Repository:
 * Buat remote: git remote add origin <url_remote> untuk menghubungkan repository lokal Anda dengan remote repository (misalnya, di GitHub atau GitLab).
 * Push perubahan: git push -u origin main untuk mengirim perubahan dari branch utama ke remote repository.
Perintah-perintah Berguna Lainnya:
 * Melihat status: git status untuk melihat status perubahan yang belum di-commit.
 * Melihat history: git log untuk melihat riwayat commit.
 * Membatalkan perubahan: git checkout -- <nama_file> untuk membatalkan perubahan pada file yang belum di-commit.



