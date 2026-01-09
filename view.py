class Tampilan:
    def tampilkan_tabel(self, data):
        print("\n=========== Data Mahasiswa ===========")
        print("{:<12} {:<20} {:<10} {:<15}".format(
            "NIM", "Nama", "Nilai", "Status"
            ))
        
        print("----------------------------------------")
        
        for d in data:
            print("{:<12} {:<20} {:<10} {:<15}".format(
                d["nim"], d["nama"], d["nilai"], d["status"]
            ))
        print("----------------------------------------\n")