class Bentuk:
    def luas(self):
        return 0

class Persegi(Bentuk):
    def __init__(self, s):
        self.s = s
    def luas(self):
        return self.s ** 2

class Lingkaran(Bentuk):
    def __init__(self, r):
        self.r = r
    def luas(self):
        return 3.14 * self.r ** 2

for bentuk in [Persegi(4), Lingkaran(7)]:
    print(type(bentuk).__name__, "luas:", bentuk.luas())
