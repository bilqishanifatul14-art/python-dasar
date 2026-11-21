nilai = 85
if nilai >= 90:
    print("Grade A")
elif nilai >= 75:
    print("Grade B")
else:
    print("Grade C")

for i in range(1, 6):
    print("for ke-", i)

hitung = 3
while hitung > 0:
    print("while:", hitung)
    hitung -= 1

for i in range(1, 11):
    if i == 3:
        continue
    if i == 6:
        break
    print(i)
