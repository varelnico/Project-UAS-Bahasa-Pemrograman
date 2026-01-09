class NilaiProcess:
    def tentukan_status(self, nilai):
        if nilai >= 75:
            return "Lulus"
        else:
            return "Tidak Lulus"