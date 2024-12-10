# view/mahasiswa.py

class MahasiswaView:
    def tampilkan_list(self, mahasiswa_list):
        print("Daftar Mahasiswa:")
        if not mahasiswa_list:
            print("Tidak ada data mahasiswa.")
        else:
            print(mahasiswa_list)

    def tampilkan_detail(self, mahasiswa):
        if mahasiswa:
            print(f"Detail Mahasiswa: {mahasiswa}")
        else:
            print("Mahasiswa tidak ditemukan.")
