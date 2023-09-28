# bab1_Projek_python_nomor_1
# Mengambil input dari pengguna
bilangan1 = float(input("Masukkan bilangan pertama: "))
bilangan2 = float(input("Masukkan bilangan kedua: "))

# Operasi penjumlahan
penjumlahan = bilangan1 + bilangan2
print("Hasil penjumlahan:", penjumlahan)

# Operasi pengurangan
pengurangan = bilangan1 - bilangan2
print("Hasil pengurangan:", pengurangan)

# Operasi perkalian
perkalian = bilangan1 * bilangan2
print("Hasil perkalian:", perkalian)

# Operasi pembagian
if bilangan2 != 0:
    pembagian = bilangan1 / bilangan2
    print("Hasil pembagian:", pembagian)
else:
    print("Pembagian oleh nol tidak diizinkan.")

# Operasi modulus
if bilangan2 != 0:
    modulus = bilangan1 % bilangan2
    print("Hasil modulus:", modulus)
else:
    print("Modulus oleh nol tidak diizinkan.")
