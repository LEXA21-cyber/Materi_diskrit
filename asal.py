# Menu Makanan
menu_makanan = {
    "1": 75000,  # Beef Steak
    "2": 50000,  # Ayam Kalasan
    "3": 60000,  # Chicken Steak
    "4": 40000,  # Gurame Bakar
    "5": 30000   # Soto Babat
}

# Menu Minuman
menu_minuman = {
    "1": 25000,  # Milkshake
    "2": 20000,  # Chocolate
    "3": 20000,  # Cappuccino Latte
    "4": 15000   # Greentea
}

# Tampilkan menu
print("Menu Makanan:")
print("1. Beef Steak: 75000\n2. Ayam Kalasan: 50000\n3. Chicken Steak: 60000\n4. Gurame Bakar: 40000\n5. Soto Babat: 30000")
print("\nPilih 2 menu makanan (Tuliskan angka menu):")
makanan1 = input("Menu Makanan 1: ")
makanan2 = input("Menu Makanan 2: ")
makanan3 = input("Menu Makanan 3: ")

print("\nMenu Minuman:")
print("1. Milkshake: 25000\n2. Chocolate: 20000\n3. Cappuccino Latte: 20000\n4. Greentea: 15000")
print("\nPilih 1 menu minuman (Tuliskan angka menu):")
minuman = input("Menu Minuman: ")

jumlah_uang = int(input("\nUang yang dibawa adalah: "))

# Ambil harga dari menu yang dipilih
harga_makanan1 = menu_makanan.get(makanan1, 0)
harga_makanan2 = menu_makanan.get(makanan2, 0)
harga_makanan3 = menu_makanan.get(makanan3, 0)
harga_minuman = menu_minuman.get(minuman, 0)

# Hitung total harga
total_harga = harga_makanan1 + harga_makanan2 + harga_makanan3 + harga_minuman

# Cek apakah total harga memenuhi syarat untuk diskon
harga_minimalDiskon = 200000
diskon = 0.10 if total_harga >= harga_minimalDiskon else 0
ppn = 0.11

# Hitung diskon dan PPN
diskon_harga = total_harga * diskon
harga_setelah_diskon = total_harga - diskon_harga
ppn_harga = harga_setelah_diskon * ppn

# Hitung total yang harus dibayar
total_bayar = harga_setelah_diskon + ppn_harga

# Hitung kembalian
kembalian = jumlah_uang - total_bayar

# Tampilkan hasil
print("\nTotal Harga: Rp", total_harga)
if jumlah_uang <= total_bayar:
    print("Maaf, uang anda tidak cukup.")
else:
    print(f"Kamu mendapat diskon 10% dan PPN 11%, total yang harus dibayar: Rp {total_bayar:.2f}")
    print(f"Kembalian: Rp {kembalian:.2f}")
