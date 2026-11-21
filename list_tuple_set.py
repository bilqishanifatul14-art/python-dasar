buah = ["apel", "jeruk", "mangga"]
buah.append("pisang")
buah.remove("jeruk")
print(buah, len(buah), buah[0], buah[-1])

koordinat = (10, 20)
x, y = koordinat
print(koordinat, x, y)

a = {1, 2, 3, 3}
b = {3, 4, 5}
print(a, a | b, a & b, a - b)
