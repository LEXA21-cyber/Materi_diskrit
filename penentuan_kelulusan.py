# Nilai KKM yg harus di penuhi adalah 80 untuk dapat lulus jika terdapat 5 mata pelajaran dan 2 di antara nya adalah pelajaran unggulan.
# 1. jika 3 mata pelajaran non unggulan nilai nya di bawah KKM tetapi lebih dari 70 dan 2 mata pelajaran unggulan di atas KKM maka dianggap lulus
# Jika 1 satu pelajaran unggulan di bawah KKM maka tidak lulus

kkm = 80
pelajaran_unggulan = 80
non_unggulan= 70

mapel_no= int(input("masukan nilai fiqih :"))
mapel_no= int(input("masukan nilai siroh :"))
mapel_no= int(input("masukan nilai b. arab:"))
mapel_unggulan= int(input("masukan IT:"))
mapel_unggulan= int(input("masukan nilai Quran:"))

if(mapel_no>=non_unggulan and mapel_unggulan>=kkm):
    print("lulus")
else:
    print("tidak lulus")