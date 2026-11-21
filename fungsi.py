def sapa(nama):
    return f"Halo, {nama}!"

def pangkat(angka, n=2):
    return angka ** n

def jumlah(*angka):
    return sum(angka)

kuadrat = lambda x: x * x

print(sapa("Bilqis"))
print(pangkat(4), pangkat(2, 5))
print(jumlah(1, 2, 3, 4))
print(kuadrat(9))
