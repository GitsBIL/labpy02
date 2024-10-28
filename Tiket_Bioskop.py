harga_reguler = 50000
harga_VIP = 100000

tipe_tiket = input("Masukkan tipe tiket (Reguler/VIP): ").lower()
member = input("Apakah anda memiliki kartu member? (ya/tidak): ").lower()

harga_tiket = harga_reguler if tipe_tiket == "reguler" else harga_VIP

diskon = 0.2 if member == "ya" else 0

total_harga = harga_tiket * (1 - diskon)

print(f"Total harga yang harus dibayar: Rp{total_harga}")
