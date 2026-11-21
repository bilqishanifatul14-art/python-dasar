class Rekening:
    def __init__(self, pemilik, saldo):
        self.pemilik = pemilik
        self.__saldo = saldo

    def setor(self, jumlah):
        if jumlah > 0:
            self.__saldo += jumlah

    def tarik(self, jumlah):
        if 0 < jumlah <= self.__saldo:
            self.__saldo -= jumlah
        else:
            print("Saldo tidak cukup")

    def lihat_saldo(self):
        return self.__saldo

r = Rekening("Bilqis", 100000)
r.setor(50000)
r.tarik(30000)
r.tarik(999999)
print("Saldo:", r.lihat_saldo())
