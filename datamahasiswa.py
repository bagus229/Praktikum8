class DaftarNilaiMahasiswa:
    def __init__(self):
        self.data_mahasiswa = []

    def tambah(self, nama, nilai):
        """Menambah data mahasiswa."""
        self.data_mahasiswa.append({"nama": nama, "nilai": nilai})
        print(f"Data {nama} berhasil ditambahkan.")

    def tampilkan(self):
        """Menampilkan daftar nilai mahasiswa."""
        if not self.data_mahasiswa:
            print("Belum ada data mahasiswa.")
        else:
            print("Daftar Nilai Mahasiswa:")
            for idx, mahasiswa in enumerate(self.data_mahasiswa, start=1):
                print(f"{idx}. Nama: {mahasiswa['nama']}, Nilai: {mahasiswa['nilai']}")

    def hapus(self, nama):
        """Menghapus data mahasiswa berdasarkan nama."""
        for mahasiswa in self.data_mahasiswa:
            if mahasiswa['nama'] == nama:
                self.data_mahasiswa.remove(mahasiswa)
                print(f"Data {nama} berhasil dihapus.")
                return
        print(f"Data dengan nama {nama} tidak ditemukan.")

    def ubah(self, nama, nilai_baru):
        """Mengubah data mahasiswa berdasarkan nama."""
        for mahasiswa in self.data_mahasiswa:
            if mahasiswa['nama'] == nama:
                mahasiswa['nilai'] = nilai_baru
                print(f"Data {nama} berhasil diubah.")
                return
        print(f"Data dengan nama {nama} tidak ditemukan.")

if __name__ == "__main__":
    daftar_nilai = DaftarNilaiMahasiswa()
    
    daftar_nilai.tambah("Hendrawan", 80)
    daftar_nilai.tambah("Fatah", 90)

    daftar_nilai.tampilkan()

    daftar_nilai.ubah("Hendrawan", 99)

    daftar_nilai.tampilkan()

    daftar_nilai.hapus("Fatah")

    daftar_nilai.tampilkan()