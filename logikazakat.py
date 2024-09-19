# Jika seorang laki laki meninggal dan meninggalkan 1 istri, 2 anak laki laki dan 1 anak perempuan dan meninggalkan harta sebesar 120.000.000
# hitunglah bagian per masing-masing-nya

harta = 120000000
anakLK = 2
AnakPR =1
bagian_total = 2*2+1


bagian_istri = harta *(1/8)

sisa_istri = harta-bagian_istri


bagian_anakPR = sisa_istri/bagian_total
bagian_anakLK = bagian_anakPR*2

print("Maka bagian istri adalah :",bagian_istri)
print("Maka bagian anak perempuan adalah :",bagian_anakPR)
print("Maka bagian anak laki laki adalah :",bagian_anakLK)
