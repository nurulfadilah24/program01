# main.py

from data.mahasiswa import Mahasiswa, DataMahasiswa
from view.input_form import InputForm
from view.mahasiswa import MahasiswaView

def main():
    data_mahasiswa = DataMahasiswa()
    input_form = InputForm()
    mahasiswa_view = MahasiswaView()

    while True:
        print("\nMenu Utama:")
        print("1. Tambah Data Mahasiswa")
        print("2. Hapus Data Mahasiswa")
        print("3. Ubah Data Mahasiswa")
        print("4. Cari Data Mahasiswa")
        print("5. Tampilkan Semua Data Mahasiswa")
        print("6. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            # Tambah Data Mahasiswa
            id_mahasiswa, nama, jurusan = input_form.input_data()
            mahasiswa = Mahasiswa(id_mahasiswa, nama, jurusan)
            data_mahasiswa.tambah_mahasiswa(mahasiswa)
            print("Data Mahasiswa berhasil ditambahkan.")

        elif pilihan == "2":
            # Hapus Data Mahasiswa
            id_mahasiswa = input("Masukkan ID Mahasiswa yang ingin dihapus: ")
            data_mahasiswa.hapus_mahasiswa(id_mahasiswa)
            print("Data Mahasiswa berhasil dihapus.")

        elif pilihan == "3":
            # Ubah Data Mahasiswa
            id_mahasiswa = input("Masukkan ID Mahasiswa yang ingin diubah: ")
            mahasiswa = data_mahasiswa.cari_mahasiswa(id_mahasiswa)
            if mahasiswa:
                nama_baru = input("Nama baru: ")
                jurusan_baru = input("Jurusan baru: ")
                data_mahasiswa.ubah_mahasiswa(id_mahasiswa, nama_baru, jurusan_baru)
                print("Data Mahasiswa berhasil diubah.")
            else:
                print("Mahasiswa tidak ditemukan.")

        elif pilihan == "4":
            # Cari Data Mahasiswa
            id_mahasiswa = input("Masukkan ID Mahasiswa yang ingin dicari: ")
            mahasiswa = data_mahasiswa.cari_mahasiswa(id_mahasiswa)
            mahasiswa_view.tampilkan_detail(mahasiswa)

        elif pilihan == "5":
            # Tampilkan Semua Data Mahasiswa
            mahasiswa_view.tampilkan_list(data_mahasiswa.tampilkan_semua())

        elif pilihan == "6":
            # Keluar
            print("Terima kasih!")
            break

        else:
            print("Pilihan tidak valid, silakan coba lagi.")

if __name__ == "__main__":
    main()
