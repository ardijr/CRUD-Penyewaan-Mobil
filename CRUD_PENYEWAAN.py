# SISTEM CRUD RENTAL MOBIL


data_mobil = [
    {"kode": "M01", "nama": "Toyota Avanza", "warna": "Hitam", "harga": 475000, "status": "Tersedia"},
    {"kode": "M02", "nama": "Honda Brio", "warna": "Putih", "harga": 375000, "status": "Tersedia"},
    {"kode": "M03", "nama": "Suzuki Ertiga", "warna": "Silver", "harga": 450000, "status": "Tersedia"},
    {"kode": "M04", "nama": "Mitsubishi Pajero", "warna": "Hitam", "harga": 900000, "status": "Disewa"},
    {"kode": "M05", "nama": "Toyota Fortuner", "warna": "Putih", "harga": 850000, "status": "Tersedia"}
]

akun = {
    "admin": {"password": "admin123", "role": "admin"},
    "user": {"password": "ardi123", "role": "user"}
}
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


# LOGIN 
def login():
    kesempatan = 3
    while kesempatan > 0:
        print("\n LOGIN ")
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


# TAMBAH MOBIL 
def tambah_mobil():
    kode = input("Kode mobil: ")

    for m in data_mobil:
        if m["kode"] == kode:
            print("Kode mobil sudah ada.")
            return

    nama = input("Nama mobil: ")
    warna = input("Warna mobil: ")
    harga = int(input("Harga sewa per hari: "))

    if konfirmasi():
        data_mobil.append({
            "kode": kode,
            "nama": nama,
            "warna": warna,
            "harga": harga,
            "status": "Tersedia"
        })
        print("Mobil berhasil ditambahkan!")
    else:
        print("Penambahan dibatalkan.")


def submenu_lihat_data():
    while True:
        print("\nSUBMENU LIHAT DATA")
        print("1. Mobil yang Disewa")
        print("2. Mobil yang Tersedia")
        print("3. Kembali")

        pilih = input("Pilih menu: ")

        if pilih == "1":
            mobil_disewa = [m for m in data_mobil if m["status"] == "Disewa"]
            print("\nMOBIL YANG DISEWA")
            tampilkan_tabel(mobil_disewa)

        elif pilih == "2":
            mobil_tersedia = [m for m in data_mobil if m["status"] == "Tersedia"]
            print("\nMOBIL YANG TERSEDIA")
            tampilkan_tabel(mobil_tersedia)

        elif pilih == "3":
            break
        else:
            print("Menu tidak valid.")


# UPDATE MOBIL
def update_mobil():
    kode = input("Masukkan kode mobil: ")

    for m in data_mobil:
        if m["kode"] == kode:
            if konfirmasi():
                m["nama"] = input("Nama baru: ")
                m["warna"] = input("Warna baru: ")
                m["harga"] = int(input("Harga baru: "))
                print("Data berhasil diupdate!")
            else:
                print("Update dibatalkan.")
            return

    print("Mobil tidak ditemukan.")


# HAPUS MOBIL
def hapus_mobil():
    kode = input("Masukkan kode mobil: ")

    for m in data_mobil:
        if m["kode"] == kode:

            if m["status"] == "Disewa":
                print("Mobil sedang disewa dan tidak bisa dihapus!")
                return

            if konfirmasi():
                data_mobil.remove(m)
                print("Mobil berhasil dihapus!")
            else:
                print("Penghapusan dibatalkan.")
            return

    print("Mobil tidak ditemukan.")


# SEWA MOBIL
def sewa_mobil():
    mobil_tersedia = [m for m in data_mobil if m["status"] == "Tersedia"]

    if not mobil_tersedia:
        print("Tidak ada mobil tersedia.")
        return

    print("\n MOBIL TERSEDIA ")
    tampilkan_tabel(mobil_tersedia)

    kode = input("Masukkan kode mobil yang ingin disewa: ")

    for m in mobil_tersedia:
        if m["kode"] == kode:
            hari = int(input("Berapa hari sewa: "))
            total = m["harga"] * hari

            print("\n RINCIAN SEWA ")
            print("Mobil :", m["nama"])
            print("Harga per hari :", m["harga"])
            print("Lama sewa :", hari, "hari")
            print("Total bayar : Rp", format(total, ","))

            if konfirmasi():
                m["status"] = "Disewa"
                print("Mobil berhasil disewa!")
            else:
                print("Sewa dibatalkan.")
            return

    print("Kode mobil tidak ditemukan atau tidak tersedia.")


# KEMBALIKAN MOBIL
def kembalikan_mobil():
    mobil_disewa = [m for m in data_mobil if m["status"] == "Disewa"]

    if not mobil_disewa:
        print("Tidak ada mobil yang sedang disewa.")
        return

    print("\nMOBIL YANG DISEWA ")
    tampilkan_tabel(mobil_disewa)

    kode = input("Masukkan kode mobil yang dikembalikan: ")

    for m in mobil_disewa:
        if m["kode"] == kode:
            if konfirmasi():
                m["status"] = "Tersedia"
                print("Mobil berhasil dikembalikan!")
            else:
                print("Pengembalian dibatalkan.")
            return

    print("Kode mobil tidak ditemukan.")


#  SEARCH USER 
def search_mobil():
    keyword = input("Cari berdasarkan kode, nama, atau warna: ").lower()

    hasil = [
        m for m in data_mobil
        if m["status"] == "Tersedia" and
        (keyword in m["kode"].lower() or
         keyword in m["nama"].lower() or
         keyword in m["warna"].lower())
    ]

    if hasil:
        print("\nHASIL PENCARIAN")
        tampilkan_tabel(hasil)
    else:
        print("Mobil tidak ditemukan atau tidak tersedia.")


# MENU 
def menu_awal():
    print("\n SISTEM RENTAL MOBIL ")
    print("1. Login")
    print("2. Keluar")


def menu_admin():
    print("\n MENU ADMIN ")
    print("1. Tambah Mobil")
    print("2. Lihat Data Mobil")
    print("3. Update Mobil")
    print("4. Hapus Mobil")
    print("5. Logout")


def menu_user():
    print("\n MENU USER ")
    print("1. Cari Mobil")
    print("2. Sewa Mobil")
    print("3. Kembalikan Mobil")
    print("4. Logout")


#  MAIN
jalan_program = True

while jalan_program:

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

    elif pilih_awal == "2":
        print("Program selesai.")
        jalan_program = False

    else:
        print("Menu tidak valid.")