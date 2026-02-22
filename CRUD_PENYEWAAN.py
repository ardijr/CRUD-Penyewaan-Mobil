# SISTEM CRUD RENTAL MOBIL 


data_mobil = []

akun = {
    "admin": {"password": "admin123", "role": "admin"},
    "user": {"password": "ardi123", "role": "user"}
}

def header_tabel():
    print("-" * 75)
    print(f"{'No':<5}{'Kode':<10}{'Nama':<20}{'Harga':<15}{'Status':<15}")
    print("-" * 75)


def tampilkan_tabel(data):
    if not data:
        print("Data tidak ditemukan.")
        return

    header_tabel()
    for i, m in enumerate(data, start=1):
        print(f"{i:<5}{m['kode']:<10}{m['nama']:<20}{m['harga']:<15}{m['status']:<15}")
    print("-" * 75)


# Fitur Login
def login():
    kesempatan = 3
    while kesempatan > 0:
        print("\n=== LOGIN ===")
        user = input("Username: ")
        pw = input("Password: ")

        if user in akun and akun[user]["password"] == pw:
            print("Login berhasil sebagai", akun[user]["role"])
            return akun[user]["role"]
        else:
            kesempatan -= 1
            print("Login gagal! Sisa:", kesempatan)

    return None


def konfirmasi():
    jawab = input("Apakah Anda yakin? (y/n): ").lower()
    return jawab == "y"


# Tambah Mobil
def tambah_mobil():
    kode = input("Kode mobil: ")

    for m in data_mobil:
        if m["kode"] == kode:
            print("Kode mobil sudah ada.")
            return

    nama = input("Nama mobil: ")
    harga = int(input("Harga sewa per hari: "))

    if konfirmasi():
        data_mobil.append({
            "kode": kode,
            "nama": nama,
            "harga": harga,
            "status": "Tersedia"
        })
        print("Mobil berhasil ditambahkan!")
    else:
        print("Penambahan dibatalkan.")


# Tampilkan Data Mobil
def tampilkan_semua():
    print("\n=== SEMUA DATA MOBIL ===")
    tampilkan_tabel(data_mobil)


def tampilkan_dipakai():
    print("\n=== MOBIL SEDANG DISEWA ===")
    data = [m for m in data_mobil if m["status"] == "Disewa"]
    tampilkan_tabel(data)


def tampilkan_tersedia():
    print("\n=== MOBIL TERSEDIA ===")
    data = [m for m in data_mobil if m["status"] == "Tersedia"]
    tampilkan_tabel(data)


# Fitur Search Mobil
def search_mobil():
    keyword = input("Masukkan kode atau nama mobil: ").lower()
    hasil = []

    for m in data_mobil:
        if m["status"] == "Tersedia":
            if keyword in m["kode"].lower() or keyword in m["nama"].lower():
                hasil.append(m)

    print("\n=== HASIL PENCARIAN ===")
    tampilkan_tabel(hasil)


# Update data mobil
def update_mobil():
    kode = input("Masukkan kode mobil: ")

    for m in data_mobil:
        if m["kode"] == kode:
            tampilkan_tabel([m])

            if konfirmasi():
                m["nama"] = input("Nama baru: ")
                m["harga"] = int(input("Harga baru: "))
                print("Data berhasil diupdate!")
            else:
                print("Update dibatalkan.")
            return

    print("Mobil tidak ditemukan.")


# Hapus
def hapus_mobil():
    kode = input("Masukkan kode mobil: ")

    for m in data_mobil:
        if m["kode"] == kode:
            tampilkan_tabel([m])

            if konfirmasi():
                data_mobil.remove(m)
                print("Data berhasil dihapus!")
            else:
                print("Penghapusan dibatalkan.")
            return

    print("Mobil tidak ditemukan.")


# Fitur Sewa Mobil
def sewa_mobil():
    tersedia = [m for m in data_mobil if m["status"] == "Tersedia"]

    if not tersedia:
        print("Tidak ada mobil tersedia.")
        return

    print("\nMOBIL TERSEDIA ")
    tampilkan_tabel(tersedia)

    kode = input("Masukkan kode mobil yang disewa: ")

    for m in tersedia:
        if m["kode"] == kode:
            hari = int(input("Berapa hari sewa: "))
            total = m["harga"] * hari

            print("\n=== RINCIAN SEWA ===")
            print("Mobil :", m["nama"])
            print("Harga per hari :", m["harga"])
            print("Lama sewa :", hari, "hari")
            print("Total bayar : Rp", total)

            if konfirmasi():
                m["status"] = "Disewa"
                print("Mobil berhasil disewa!")
            else:
                print("Sewa dibatalkan.")
            return

    print("Mobil tidak ditemukan.")


# Kembalikan mobil
def kembalikan_mobil():
    kode = input("Kode mobil yang dikembalikan: ")

    for m in data_mobil:
        if m["kode"] == kode:
            if m["status"] == "Tersedia":
                print("Mobil belum disewa.")
                return

            if konfirmasi():
                m["status"] = "Tersedia"
                print("Mobil berhasil dikembalikan!")
            else:
                print("Pengembalian dibatalkan.")
            return

    print("Mobil tidak ditemukan.")


# Menu
def menu_awal():
    print("\nSISTEM RENTAL MOBIL")
    print("1. Login")
    print("2. Keluar Program")


def menu_admin():
    print("\nMENU ADMIN")
    print("1. Tambah Mobil")
    print("2. Lihat Semua Mobil")
    print("3. Lihat Mobil Disewa")
    print("4. Lihat Mobil Tersedia")
    print("5. Update Mobil")
    print("6. Hapus Mobil")
    print("7. Logout")


def menu_user():
    print("\nMENU USER")
    print("1. Cari Mobil")
    print("2. Sewa Mobil")
    print("3. Kembalikan Mobil")
    print("4. Logout")


# Main Program
jalan_program = True

while jalan_program:

    menu_awal()
    pilihan_awal = input("Pilih menu: ")

    if pilihan_awal == "1":

        role = login()

        if role == "admin":
            while True:
                menu_admin()
                pilih = input("Pilih menu: ")

                if pilih == "1":
                    tambah_mobil()
                elif pilih == "2":
                    tampilkan_semua()
                elif pilih == "3":
                    tampilkan_dipakai()
                elif pilih == "4":
                    tampilkan_tersedia()
                elif pilih == "5":
                    update_mobil()
                elif pilih == "6":
                    hapus_mobil()
                elif pilih == "7":
                    print("Logout berhasil.")
                    break
                else:
                    print("Menu tidak valid.")

        elif role == "user":
            while True:
                menu_user()
                pilih = input("Pilih menu: ")

                if pilih == "1":
                    search_mobil()
                elif pilih == "2":
                    sewa_mobil()
                elif pilih == "3":
                    kembalikan_mobil()
                elif pilih == "4":
                    print("Logout berhasil.")
                    break
                else:
                    print("Menu tidak valid.")

    elif pilihan_awal == "2":
        print("Program selesai. Terima kasih!")
        jalan_program = False

    else:
        print("Menu tidak valid.")