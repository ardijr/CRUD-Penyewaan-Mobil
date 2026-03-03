import mysql.connector

# ================== KONEKSI DATABASE ==================
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ardijr123",
    database="rental_mobil"
)

cursor = db.cursor(dictionary=True)

# ================== TAMPILKAN TABEL ==================
def tampilkan_tabel(data):
    if not data:
        print("Data kosong.")
        return

    print("=" * 95)
    print(f"{'No':<5}{'Kode':<10}{'Nama Mobil':<25}{'Warna':<15}{'Harga/Hari':<15}{'Status':<15}")
    print("=" * 95)

    for i, m in enumerate(data, start=1):
        print(f"{i:<5}{m['kode']:<10}{m['nama']:<25}{m['warna']:<15}{m['harga']:<15,}{m['status']:<15}")

    print("=" * 95)

# ================== LOGIN ==================
def login():
    kesempatan = 3
    while kesempatan > 0:
        print("\nLOGIN")
        username = input("Username: ")
        password = input("Password: ")

        cursor.execute(
            "SELECT * FROM akun WHERE username=%s AND password=%s",
            (username, password)
        )
        user = cursor.fetchone()

        if user:
            print("Login berhasil sebagai", user["role"])
            return user["role"]
        else:
            kesempatan -= 1
            print("Login gagal! Sisa:", kesempatan)

    return None

# ================== KONFIRMASI ==================
def konfirmasi():
    jawab = input("Apakah Anda yakin? (y/n): ").lower()
    return jawab == "y"

# ================== TAMBAH MOBIL ==================
def tambah_mobil():
    kode = input("Kode mobil: ")
    nama = input("Nama mobil: ")
    warna = input("Warna mobil: ")
    harga = int(input("Harga sewa per hari: "))

    if konfirmasi():
        try:
            cursor.execute(
                "INSERT INTO mobil (kode,nama,warna,harga,status) VALUES (%s,%s,%s,%s,'Tersedia')",
                (kode, nama, warna, harga)
            )
            db.commit()
            print("Mobil berhasil ditambahkan!")
        except:
            print("Kode sudah ada atau terjadi kesalahan.")
    else:
        print("Penambahan dibatalkan.")

# ================== LIHAT DATA ==================
def submenu_lihat_data():
    while True:
        print("\nSUBMENU LIHAT DATA MOBIL")
        print("1. Lihat Semua Mobil")
        print("2. Mobil yang Disewa")
        print("3. Mobil yang Tersedia")
        print("4. Kembali")

        pilih = input("Pilih menu: ")

        if pilih == "1":
            cursor.execute("SELECT * FROM mobil")
            tampilkan_tabel(cursor.fetchall())

        elif pilih == "2":
            cursor.execute("SELECT * FROM mobil WHERE status='Disewa'")
            tampilkan_tabel(cursor.fetchall())

        elif pilih == "3":
            cursor.execute("SELECT * FROM mobil WHERE status='Tersedia'")
            tampilkan_tabel(cursor.fetchall())

        elif pilih == "4":
            break
        else:
            print("Menu tidak valid.")

# ================== UPDATE MOBIL ==================
def update_mobil():
    kode = input("Masukkan kode mobil: ")

    cursor.execute("SELECT * FROM mobil WHERE kode=%s", (kode,))
    data = cursor.fetchone()

    if not data:
        print("Mobil tidak ditemukan.")
        return

    if konfirmasi():
        nama = input("Nama baru: ")
        warna = input("Warna baru: ")
        harga = int(input("Harga baru: "))

        cursor.execute(
            "UPDATE mobil SET nama=%s, warna=%s, harga=%s WHERE kode=%s",
            (nama, warna, harga, kode)
        )
        db.commit()
        print("Data berhasil diupdate!")
    else:
        print("Update dibatalkan.")

# ================== HAPUS MOBIL ==================
def hapus_mobil():
    kode = input("Masukkan kode mobil: ")

    cursor.execute("SELECT status FROM mobil WHERE kode=%s", (kode,))
    data = cursor.fetchone()

    if not data:
        print("Mobil tidak ditemukan.")
        return

    if data["status"] == "Disewa":
        print("Mobil sedang disewa dan tidak bisa dihapus!")
        return

    if konfirmasi():
        cursor.execute("DELETE FROM mobil WHERE kode=%s", (kode,))
        db.commit()
        print("Mobil berhasil dihapus!")
    else:
        print("Penghapusan dibatalkan.")

# ================== SEWA MOBIL ==================
def sewa_mobil():
    cursor.execute("SELECT * FROM mobil WHERE status='Tersedia'")
    mobil_tersedia = cursor.fetchall()

    if not mobil_tersedia:
        print("Tidak ada mobil tersedia.")
        return

    tampilkan_tabel(mobil_tersedia)
    kode = input("Masukkan kode mobil yang ingin disewa: ")

    cursor.execute("SELECT * FROM mobil WHERE kode=%s AND status='Tersedia'", (kode,))
    mobil = cursor.fetchone()

    if not mobil:
        print("Mobil tidak tersedia.")
        return

    hari = int(input("Berapa hari sewa: "))
    total = mobil["harga"] * hari

    print("\nRINCIAN SEWA")
    print("Mobil :", mobil["nama"])
    print("Total bayar : Rp", format(total, ","))

    if konfirmasi():
        cursor.execute(
            "UPDATE mobil SET status='Disewa' WHERE kode=%s",
            (kode,)
        )
        db.commit()
        print("Mobil berhasil disewa!")
    else:
        print("Sewa dibatalkan.")

# ================== KEMBALIKAN ==================
def kembalikan_mobil():
    cursor.execute("SELECT * FROM mobil WHERE status='Disewa'")
    mobil_disewa = cursor.fetchall()

    if not mobil_disewa:
        print("Tidak ada mobil yang disewa.")
        return

    tampilkan_tabel(mobil_disewa)
    kode = input("Masukkan kode mobil yang dikembalikan: ")

    if konfirmasi():
        cursor.execute(
            "UPDATE mobil SET status='Tersedia' WHERE kode=%s",
            (kode,)
        )
        db.commit()
        print("Mobil berhasil dikembalikan!")

# ================== MENU ==================
def menu_awal():
    print("\nSISTEM RENTAL MOBIL")
    print("1. Login")
    print("2. Keluar")

def menu_admin():
    print("\nMENU ADMIN")
    print("1. Tambah Mobil")
    print("2. Lihat Data Mobil")
    print("3. Update Mobil")
    print("4. Hapus Mobil")
    print("5. Logout")

def menu_user():
    print("\nMENU USER")
    print("1. Sewa Mobil")
    print("2. Kembalikan Mobil")
    print("3. Logout")

# ================== MAIN ==================
while True:
    menu_awal()
    pilih_awal = input("Pilih menu: ")

    if pilih_awal == "1":
        role = login()

        if role == "admin":
            while True:
                menu_admin()
                pilih = input("Pilih menu: ")

                if pilih == "1":
                    tambah_mobil()
                elif pilih == "2":
                    submenu_lihat_data()
                elif pilih == "3":
                    update_mobil()
                elif pilih == "4":
                    hapus_mobil()
                elif pilih == "5":
                    break
                else:
                    print("Menu tidak valid.")

        elif role == "user":
            while True:
                menu_user()
                pilih = input("Pilih menu: ")

                if pilih == "1":
                    sewa_mobil()
                elif pilih == "2":
                    kembalikan_mobil()
                elif pilih == "3":
                    break
                else:
                    print("Menu tidak valid.")

    elif pilih_awal == "2":
        print("Program selesai.")
        break
    else:
        print("Menu tidak valid.")
