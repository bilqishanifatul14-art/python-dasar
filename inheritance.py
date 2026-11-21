class Hewan:
    def __init__(self, nama):
        self.nama = nama

    def info(self):
        return f"Nama hewan: {self.nama}"

class Kucing(Hewan):
    def suara(self):
        return f"{self.nama} berkata meong"

class Anjing(Hewan):
    def suara(self):
        return f"{self.nama} berkata guk"

k = Kucing("Mimi")
a = Anjing("Doggo")
print(k.info(), "|", k.suara())
print(a.info(), "|", a.suara())
