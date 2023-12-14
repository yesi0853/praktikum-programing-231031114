print('praktikum-d4')
print()

a = [2,3,1,0,3,1,1,1,4]
# akses item
print(a)
print(f'item indeks:0 {a[0]}')
print(f'item indeks:3 {a[3]}')
print(f'item indeks:terakhir {a[len(a)-1]}')
# akses item indeks negatif
print(f'item indeks:terakhir (-1) {a[-1]}')
print(f'item indeks:pertama (-9){a[-len(a)]}')
print(f'item indeks:1 (-8){a[-8]}')
print(f'item indeks:5 (-4){a[-4]}')
# akses indeks batas
print(f'item indeks:1,2,3 {a[1:4]}')
print(f'item indeks:1,2,... {a[1:]}')
print(f'item indeks:3,4,... {a[3:]}')
print(f'item indeks:0,1,2 {a[:3]}')
print(f'item indeks:0,1,2,3,4 {a[:5]}')
print(f'item indeks:semua {a[:]}')

# pengirisan indeks
print(f'item indeks:1,2,3 {a[1:4]}')
print(f'item indeks:2,3,4 {a[2:5]}')
print(f'item indeks:[1:8] {a[1:-1]}')

# Nested list
kelas = [('Kalkulus Dasar',3),
          ('Pengantar Teknologi Informasi',3),
          ('Bahasa Idonesia',2)]
print(f'data kelas {kelas}')
kelas.append(('Pancasila',2))

#Tugas
# tambah matkul5 dan jumlah sks
kelas = [('Kalkulus Dasar',3),
          ('Pengantar Teknologi Informasi',3),
          ('Bahasa Idonesia',2),
         ('Pancasila',2),
         ('Sains Terpadu',3)]
print(f'data kelas {kelas}')
# Nama Mata kuliah 1: Kalkulus Dasar dengan jumlah sks:3
# Nama Mata kuliah 2: Pengantar Teknologi Informasi dengan jumlah sks:3
# Nama Mata kuliah 3: Bahasa Indonesia dengan jumlah sks:2
 # Nama Mata kuliah 4: Pancasila dengan jumlah sks:2
# Nama Mata kuliah 5: Sains Terpadu dengan jumlah sks:3


data = [('Yesi',2023,'Aktif'),
        ('231031114'),
        (90,89,93,97,100),
        (20,23),
        ('S1-Reguler','Sistem Informasi D','Ganjil')]
print(f'Nama Mahasiswa:',data[0][0])
print(f'Nim Yesi:',data[1])
print(f'Program Pendidikan Yesi:',data[4][1],data[4][0])
print(f'Angkatan yesi:',data[0][1],data[4][2])
print(f'Jumlah nilai Yesi adalah:',len(data[2]))
print(f'Data terbesar Yesi adalah:',max(data[2]))
print(f'Data terkecil Yesi adalah;',min(data[2]))
print(f' Rata-rata nilai Yesi adalah:',data[3])


# print(data[0][0])
# print(data[-1][0])
# print(data[2][0:])
