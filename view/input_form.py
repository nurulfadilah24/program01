# view/input_form.py

class InputForm:
    def __init__(self):
        self.id_mahasiswa = None
        self.nama = None
        self.jurusan = None

    def input_data(self):
        print("Masukkan Data Mahasiswa:")
        self.id_mahasiswa = input("ID Mahasiswa: ")
        self.nama = input("Nama: ")
        self.jurusan = input("Jurusan: ")

        return self.id_mahasiswa, self.nama, self.jurusan
