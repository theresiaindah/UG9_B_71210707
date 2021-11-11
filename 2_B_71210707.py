#input
r_alas_tabung = int(input("Masukkan jari-jari alas tabung : "))
tinggi_tabung = int(input("Masukkan tinggi tabung : "))
phi = 22/7
#proses
luas_alas = phi*r_alas_tabung*r_alas_tabung
luas_selimut = 2*phi*r_alas_tabung*tinggi_tabung
luas_permukaan_tabung = 2*luas_alas+luas_selimut
print("luas permukaan tabung : ", luas_permukaan_tabung)

#input
r_alas_tabung = int(input("Masukkan jari-jari alas tabung : "))
tinggi_tabung = int(input("Masukkan tinggi tabung : "))
phi = 22/7

#proses
luas_alas = phi*r_alas_tabung*r_alas_tabung
luas_selimut = 2*phi*r_alas_tabung*tinggi_tabung
luas_permukaan_tabung = 2*luas_alas+luas_selimut
print("luas permukaan tabung : ",luas_permukaan_tabung)
