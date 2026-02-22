# CRUD-Penyewaan-Mobil

Program ini adalah sistem rental mobil sederhana berbasis Command Line Interface (CLI) menggunakan Python.  
Sistem ini menerapkan konsep CRUD, login berbasis role (admin & user), serta perhitungan biaya sewa tanpa menggunakan database.


## 📌 Gambaran Umum

Aplikasi ini memiliki dua jenis pengguna:

- **Admin** → Mengelola data mobil
- **User** → Mencari, menyewa, dan mengembalikan mobil

Semua data disimpan sementara di dalam program (menggunakan list dan dictionary).

## 🎯 Fitur Utama

### 🔐 Sistem Login
- Login menggunakan username dan password
- Maksimal 3 kali percobaan login
- Menu berbeda sesuai role (admin/user)
- Logout kembali ke menu utama

### 👨‍💼 Fitur Admin
- Menambah mobil baru
- Melihat semua data mobil
- Melihat mobil yang sedang disewa
- Melihat mobil yang tersedia
- Mengupdate data mobil
- Menghapus data mobil
- Konfirmasi sebelum aksi penting (update/hapus/tambah)

### 👤 Fitur User
- Mencari mobil berdasarkan kode atau nama
- Menyewa mobil
- Mengembalikan mobil
- Sistem otomatis menghitung total biaya sewa

## 🧱 Struktur Penyimpanan Data

Data mobil disimpan dalam list:

```python
data_mobil = []
