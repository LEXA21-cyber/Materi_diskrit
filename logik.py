# jika seorang suami meninggal meninggalkan istri 1 anak laki-laki 2 dan anak perempuan 1 dengan junlah harta 120 juta

def hitung_pembagian_waris(harta):
    # Bagian Istri
    bagian_istri = harta * (1/8)
    
    # Harta yang tersisa setelah bagian istri
    sisa_harta = harta - bagian_istri
    
    # Jumlah anak laki-laki dan perempuan
    jumlah_anak_laki = 2
    jumlah_anak_perempuan = 1
    
    # Total bagian anak-anak (laki-laki dan perempuan)
    total_bagian_anak = (jumlah_anak_laki * 2) + (jumlah_anak_perempuan * 1)
    
    # Bagian masing-masing anak laki-laki dan perempuan
    bagian_anak_laki = sisa_harta * 2 / total_bagian_anak
    bagian_anak_perempuan = sisa_harta * 1 / total_bagian_anak
    
    return {
        'bagian_istri': bagian_istri,
        'bagian_anak_laki': bagian_anak_laki,
        'bagian_anak_perempuan': bagian_anak_perempuan
    }

# Jumlah harta yang ditinggalkan
harta = 120_000_000  # Harta yang ditinggalkan
pembagian = hitung_pembagian_waris(harta)

print(f"Bagian Istri: Rp {pembagian['bagian_istri']:.2f}")
print(f"Bagian Anak Laki-laki (per anak): Rp {pembagian['bagian_anak_laki']:.2f}")
print(f"Bagian Anak Perempuan (per anak): Rp {pembagian['bagian_anak_perempuan']:.2f}")
