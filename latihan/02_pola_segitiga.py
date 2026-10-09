print("=== PROGRAM POLA SEGITIGA BINTANG ===")

# 1. Input nilai n positif dari pengguna
n = int(input("Masukkan nilai n: "))

# 2. Nested loop untuk membentuk pola segitiga bertambah
for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()