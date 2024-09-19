# pak andi memiliki harta Rp.120.000.000 dan sudah mencapai haul selama 1 tahun jika nisob zakat mal adalah 85 gram emas dan harga 1 gram emas Rp.1.000.000. tentukan apakah pak andi wajib berzakat atau tidak

harta =int(input("masukan jumlah harta :"))
haul = int(input("masukan bulan harta di simpan : "))
nisob = 85000000 # 85 gram , per gram 1 juta
haul_waktu = 12 #bulan
hasil = harta * 0.025


if(harta>=nisob==haul_waktu):
    print("wajib zakat")
else:
    print("tidak wajib zakat")


