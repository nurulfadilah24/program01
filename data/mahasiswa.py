# data/mahasiswa.py

class Mahasiswa:
    def __init__(self, id_mahasiswa, nama, jurusan):
        self.id_mahasiswa = id_mahasiswa
        self.nama = nama
        self.jurusan = jurusan

    def __str__(self):
        return f"ID: {self.id_mahasiswa}, Nama: {self.nama}, Jurusan: {self.jurusan}"

class DataMahasiswa:
    def __init__(self):
        self.mahasiswa_list = []

    def tambah_mahasiswa(self, mahasiswa):
        self.mahasiswa_list.append(mahasiswa)

    def hapus_mahasiswa(self, id_mahasiswa):
        self.mahasiswa_list = [mhs for mhs in self.mahasiswa_list if mhs.id_mahasiswa != id_mahasiswa]

    def ubah_mahasiswa(self, id_mahasiswa, nama_baru, jurusan_baru):
        for mhs in self.mahasiswa_list:
            if mhs.id_mahasiswa == id_mahasiswa:
                mhs.nama = nama_baru
                mhs.jurusan = jurusan_baru
                break

    def cari_mahasiswa(self, id_mahasiswa):
        for mhs in self.mahasiswa_list:
            if mhs.id_mahasiswa == id_mahasiswa:
                return mhs
        return None

    def tampilkan_semua(self):
        return "\n".join(str(mhs) for mhs in self.mahasiswa_list)
