angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))

operator = input("Masukkan operator (+, -, *, /): ").strip()

if operator == "+":
    hasil = angka1 + angka2
elif operator == "-":
    hasil = angka1 - angka2
elif operator == "*":
    hasil = angka1 * angka2
elif operator == "/":
    if angka2 != 0:
        hasil = angka1 / angka2
    else:
        hasil = "Tidak dapat membagi dengan nol!"
else:
    hasil = "Operator tidak valid!"

print(f"Hasil: {hasil}")
