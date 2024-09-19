# Taampilkan menu makanan 5 item dan minuman 4 item di sebuah restauran
# Pertanyaan = customer memilih 2 menu makanan dan 1 menu minuman, jika ia membawa uang sebesar 500rb rupiah, berapa yang harus ia bayar dan berapa kembalian nya

# Menu Makanan
menu_makanan = {
    "1": 75000,
    "2": 50000,
    "3": 60000,
    "4": 40000,
    "5": 30000,
}

# Menu Minuman
menu_minuman = {
    "1": 25000,
    "2": 20000,
    "3": 20000,
    "4": 15000
}


print("1.Beef Steak: 75000","\n2.Ayam Kalasam: 50000","\n3.Chicken Steak: 60000","\n4.Gurame Bakar: 40000","\n5.Soto Babat: 30000")
print("\nPilih  menu makanan (Tuliskan angka menu):")
makanan1 = input("Menu Makanan 1: ")
makanan2 = input("Menu Makanan 2: ")
makanan3 = input("Menu Makanan 3: ")


print("1.Milkshake: 25000,"
    "\n2.Chocolate: 20000,"
    "\n3.Cappuccino Latte: 20000,"
    "\n4.Greentea: 15000")
print("\nPilih 1 menu minuman (tuliskan angka menu):")
minuman = input("Menu Minuman: ")
jumlah_uang = int(input("uang yang di bawa adalah :"))


harga_makanan1 = menu_makanan.get(makanan1, 0)
harga_makanan2 = menu_makanan.get(makanan2, 0)
harga_makanan3 = menu_makanan.get(makanan3, 0)
harga_minuman = menu_minuman.get(minuman, 0)

total_harga = harga_makanan1 + harga_makanan2 + harga_makanan3 + harga_minuman


harga_minimalDiskon = 200000
diskon = 0.10 if total_harga >= harga_minimalDiskon else 0
ppn = 0.11


diskon_harga = total_harga * diskon
harga_setelah_diskon = total_harga - diskon_harga
ppn_harga = harga_setelah_diskon * ppn


total_bayar = harga_setelah_diskon + ppn_harga


kembalian = jumlah_uang - total_bayar

if jumlah_uang < total_bayar:
    print(f"Total harga adalah: {total_harga:,}")
    print("Uang Anda kurang!")
    top_up = int(input("Masukkan nominal top up: "))
    total_uang = jumlah_uang + top_up
    kembalian = total_uang - total_bayar

    if total_uang < total_bayar:
        print("Top-up masih kurang, transaksi tidak dapat diselesaikan.")
    else:
        print("Terima kasih telah menyelesaikan pembayaran.")
        if diskon > 0:
            print(f"Anda mendapat diskon sebesar 10% yaitu: {diskon_harga:,}")
            print(f"Uang yang harus dibayar setelah diskon adalah: {harga_setelah_diskon:,}")
            print(f"Anda terkena PPN sebesar 11% yaitu: {ppn_harga:,}")
        else:
            print("Anda tidak terkena diskon maupun PPN.")
        print(f"Total yang harus Anda bayar adalah: {total_bayar:,}")
        print(f"Kembalian Anda adalah: {kembalian:,}")
else:
    kembalian = jumlah_uang - total_bayar
    print(f"Total harga adalah: {total_harga:,}")
    if diskon > 0:
        print(f"Anda mendapat diskon sebesar 10% yaitu: {diskon_harga:,}")
        print(f"Uang yang harus dibayar setelah diskon adalah: {harga_setelah_diskon:,}")
        print(f"Anda terkena PPN sebesar 11% yaitu: {ppn_harga:,}")
    else:
        print("Anda tidak terkena diskon maupun PPN.")
    print(f"Total yang harus Anda bayar adalah: {total_bayar:,}")
    print(f"Kembalian Anda adalah: {kembalian:,}")