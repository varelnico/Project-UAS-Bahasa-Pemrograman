from data_mahasiswa import Mahasiswa, DataMahasiswa
from process import NilaiProcess
from view import Tampilan


def main():
    data_mahasiswa = DataMahasiswa()
    proses = NilaiProcess()
    view = Tampilan()

    print("PROGRAM MANAJEMEN NILAI MAHASISWA")

    while True:
        try:
            nim = input("Masukkan NIM           : ")
            nama = input("Masukkan Nama          : ")
            nilai = int(input("Masukkan Nilai (0-100) : "))

            if nilai < 0 or nilai > 100:
                raise ValueError("Nilai harus 0–100")

            mhs = Mahasiswa(nim, nama, nilai)
            status = proses.tentukan_status(nilai)

            data_mahasiswa.tambah_data(mhs, status)

            lanjut = input("Tambah data lagi? (y/n): ")
            if lanjut.lower() != "y":
                break

        except ValueError as e:
            print("ERROR:", e)

    view.tampilkan_tabel(data_mahasiswa.get_data())


if __name__ == "__main__":
    main()
