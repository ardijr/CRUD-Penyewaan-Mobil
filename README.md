Aplikasi CRUD Python untuk Sistem Manajemen Rental Mobil

Aplikasi berbasis Python untuk mengelola data rental mobil menggunakan konsep Create, Read, Update, Delete (CRUD) dengan database MySQL sebagai penyimpanan data.

Business Understanding

Proyek ini dibuat untuk industri rental mobil, yang membutuhkan sistem terstruktur untuk mengelola data kendaraan dan akun pengguna secara efisien.

Dalam bisnis rental mobil, pengelolaan data kendaraan sangat penting karena berkaitan langsung dengan:

Ketersediaan mobil

Harga sewa

Status kendaraan (Tersedia / Disewa)

Kontrol akses pengguna sistem

Tanpa sistem yang terorganisir, pengelolaan data dapat menimbulkan kesalahan pencatatan, duplikasi data, dan kesulitan dalam memantau status kendaraan.

Manfaat Sistem

Meningkatkan akurasi dan konsistensi data

Mempermudah pengelolaan kendaraan

Memantau status mobil secara real-time

Mengurangi kesalahan manual

Membatasi akses sistem berdasarkan peran pengguna

Target Pengguna

Aplikasi ini dirancang untuk:

1. Admin

Menambah data mobil

Melihat daftar mobil

Mengubah data mobil

Menghapus data mobil

2. User

Melihat daftar mobil yang tersedia

Sistem menggunakan mekanisme login untuk membedakan hak akses antara admin dan user.

Fitur Aplikasi
1. Sistem Login

Login menggunakan username dan password

Role-based access (admin dan user)

Hak akses dibatasi sesuai peran

2. Create (Tambah Data)

Menambahkan data mobil baru dengan informasi:

Kode mobil (unik)

Nama mobil

Warna

Harga sewa

Status (default: Tersedia)

Validasi:

Kode mobil tidak boleh duplikat

Field wajib tidak boleh kosong

3. Read (Lihat Data)

Menampilkan seluruh data mobil

Melihat status mobil (Tersedia / Disewa)

Menampilkan data dalam format yang mudah dibaca

4. Update (Ubah Data)

Mengubah nama mobil

Mengubah warna

Mengubah harga sewa

Mengubah status mobil

Sistem memberikan konfirmasi jika update berhasil atau gagal.

5. Delete (Hapus Data)

Menghapus data mobil

Hanya bisa dilakukan oleh admin

Sistem akan menolak jika data tidak ditemukan

Keamanan

Autentikasi pengguna melalui tabel akun

Pembatasan akses berdasarkan role

Admin memiliki akses penuh terhadap data

User hanya memiliki akses baca

Instalasi
Prasyarat

Python 3.11 atau versi yang kompatibel

MySQL Server

mysql-connector-python
