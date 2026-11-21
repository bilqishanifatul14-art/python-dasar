with open("catatan.txt", "w", encoding="utf-8") as f:
    f.write("Baris 1: belajar Python\n")
    f.write("Baris 2: belajar Git\n")

with open("catatan.txt", "a", encoding="utf-8") as f:
    f.write("Baris 3: belajar GitHub\n")

with open("catatan.txt", "r", encoding="utf-8") as f:
    for nomor, baris in enumerate(f, start=1):
        print(nomor, baris.strip())
