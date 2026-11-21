from abc import ABC, abstractmethod

class Kendaraan(ABC):
    @abstractmethod
    def jalan(self):
        pass

class Motor(Kendaraan):
    def jalan(self):
        return "Motor melaju dengan 2 roda"

class Mobil(Kendaraan):
    def jalan(self):
        return "Mobil melaju dengan 4 roda"

for k in [Motor(), Mobil()]:
    print(k.jalan())

try:
    Kendaraan()
except TypeError as e:
    print("Tidak bisa dibuat langsung:", e)
