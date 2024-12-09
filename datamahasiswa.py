class Mahasiswa:
    def __init__(self):
        self.data_mahasiswa = []

    def tambah(self, nama, nim, nilai):
        mahasiswa = {"nama": nama, "nim": nim, "nilai": nilai}
        self.data_mahasiswa.append(mahasiswa)
        print(f"Data mahasiswa {nama} berhasil ditambahkan!") 

    def tampilkan(self):
        if not self.data_mahasiswa:
            print("Belum ada data mahasiswa!")
        else:
            print("\nDaftar Nilai Mahasiswa")
            print("=" * 40)
            print("| No | Nama        | NIM     | Nilai |")
            print("-" * 40)
            for i, mhs in enumerate(self.data_mahasiswa, start=1):
                print(f"| {i:2} | {mhs['nama']:10} | {mhs['nim']:7} | {mhs['nilai']:5} |")
            print("=" * 40)

    def hapus(self, nama):
        for mhs in self.data_mahasiswa:
            if mhs["nama"].lower() == nama.lower():
                self.data_mahasiswa.remove(mhs)
                print(f"Data mahasiswa {nama} berhasil dihapus!")
                return
        print(f"Data mahasiswa dengan nama {nama} tidak ditemukan.")

    def ubah(self, nama):
        for mhs in self.data_mahasiswa:
            if mhs["nama"].lower() == nama.lower():
                try:
                    mhs["nim"] = input(f"Masukkan NIM baru untuk {nama}: ")
                    mhs["nilai"] = float(input(f"Masukkan nilai baru untuk {nama}: "))
                    print(f"Data mahasiswa {nama} berhasil diubah!")
                except ValueError:
                    print("Nilai harus berupa angka.")
                return
        print(f"Data mahasiswa dengan nama {nama} tidak ditemukan.")

def menu():
    data = Mahasiswa()
    while True:
        print("\nMenu:")
        print("1. Tambah Data")
        print("2. Tampilkan Data")
        print("3. Hapus Data")
        print("4. Ubah Data")
        print("5. Keluar")
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            nama = input("Masukkan nama: ")
            nim = input("Masukkan NIM: ")
            try:
                nilai = float(input("Masukkan nilai: "))
                data.tambah(nama, nim, nilai)
            except ValueError:
                print("Nilai harus berupa angka.")
        elif pilihan == "2":
            data.tampilkan()
        elif pilihan == "3":
            nama = input("Masukkan nama mahasiswa yang ingin dihapus: ")
            data.hapus(nama)
        elif pilihan == "4":
            nama = input("Masukkan nama mahasiswa yang ingin diubah: ")
            data.ubah(nama)
        elif pilihan == "5":
            print("Program selesai. Terima kasih!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

menu()