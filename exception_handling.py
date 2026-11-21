def bagi(a, b):
    try:
        hasil = a / b
    except ZeroDivisionError:
        print("Error: tidak bisa membagi dengan nol")
        return None
    except TypeError:
        print("Error: input harus angka")
        return None
    else:
        return hasil
    finally:
        print("Proses pembagian selesai")

print(bagi(10, 2))
print(bagi(10, 0))
print(bagi(10, "a"))
