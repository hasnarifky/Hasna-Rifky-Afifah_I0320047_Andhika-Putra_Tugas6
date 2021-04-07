#program menghitung nilai rata-rata

print("Masukkan data-data yang dibutuhkan")
n = int(input("Banyaknya nilai yang akan dihitung : "))
i = 1

print()
list_nilai =[]
jumlah_nilai = 0

while i <= n :
    nilai = int(input("Nilai ke-%d : " % i))
    i = i + 1
    list_nilai.append(nilai)

jumlah_nilai = sum(list_nilai)
rata = jumlah_nilai/n
print(" ")
print("Nilai rata-rata yang diinput pengguna adalah", '%0.3f' % rata)
