class Mahasiswa:
    def __init__(self, nim, nama, nilai):
        self.nim = nim
        self.nama = nama
        self.nilai = nilai
        
class DataMahasiswa:
    def __init__(self):
        self.data = []
        
    def tambah_data(self, mahasiswa, status):
        self.data.append({
            "nim": mahasiswa.nim,
            "nama": mahasiswa.nama,
            "nilai": mahasiswa.nilai,
            "status": status
        })
        
    def get_data(self):
        return self.data