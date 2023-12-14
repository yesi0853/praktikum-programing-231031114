 nama = 'YESI'
nim = '231031114'
prodi = 'Sistem Informasi'
meet = 'Praktikum 3'
email = 'ybii00008gmail.com'

#print(len(nama))
sp= 48
print('-'.center(sp,'-'))
      
print(nama.center(sp))
print(nim.center(sp))
print('\n'*2)
print(meet.rjust(sp))
print(prodi.rjust(sp))
print(email.rjust(sp))

print('-'.center(sp,'-'))

paragraf = ''' Halo, selamat datang perkenalkan nama saya {} dengan Nim {} dari prodi {}, Ini adalah file {},'''

p = paragraf.format(nama,nim,prodi,meet)
print(p)

paragraf = '''\tHalo, selamat datang perkenalkan nama saya {} dengan Nim {} dari prodi {}, Ini adalah file {},'''

p = paragraf.format(nama,nim,prodi,meet)
print(p)

#==============5++++++++++9=============
#1. input nilai x
x = int(input('Masukkan Nilai= '))
print(int)
#2. cek1 apakahx>5 true
cek1 = x>5
#3. cek2 apakah x<9 true
cek2 = x<9
#4. status = cek1 and cek2
status = cek1 and cek2
#5. cek status
print('hasilnya adalah',status)



#++++++++++++++++5--------------9++++++++++++
#1. input x
x = int(input('Masukkan Nilai +++5---9= '))
#2.cek1 apakah x<5 true
cek1 = x>=5
#3.cek2 apakah x>9 false
cek2 =x>=9
#4.status = cek1 or cek2 true
status = cek1 or cek2
#5. cetak status
print('Hasilnya adalah',status)

x = int(input('Masukkan Nilai +++5---9= '))
cek1 = x<=5
cek2 =x>=9
status = cek1 or cek2
print('Hasilnya adalah',status)


#+++++5-----9+++++13--------
x = int(input('Masukkan Nilai ++5--9++13--= '))
#1. input nilai x
x = int(input('Masukkan Nilai= '))
print(int)
#2. cek1 apakahx>5 true
cek1 = x<5
#3. cek2 apakah x<9 true
cek2 = x>9
#4. status = cek1 and cek2
cek3 = x<13
#5.status =cek1 or and cek3
status = cek1 and cek2
#6. cek status
print('hasilnya adalah',status)


x = int(input('Masukkan Nilai ++5--9++13--= '))
cek1 = x<=5
cek2 =x>=9
cek3 =x<13
status = cek1 or cek2 and cek3
print('Hasilnya adalah',status)


#TUGAS 1
#-----5++++9------13++++16----
x = int(input('Masukkan Nilai --5++9--13++16--= '))
cek1 = x>=5
cek2 = x<=9
cek3 = x>=13
cek4 = x<=16
status = cek1 and cek2 or cek3 and cek4
print('Hasilnya adalah',status) 

#TUGAS 2
#++++5----9++++13----16++++
x = int(input('Masukkan Nilai ++5--9++13--16++= '))
cek1 = x<=5
cek2 = x>=9
cek3 = x>=13
cek4 = x<=16
status = cek1 or cek2 and cek3 or cek4
print('Hasilnya adalah',status)

#TUGAS 3
#----5++++9----13++++16----20++++24----
x = int(input('Masukkan Nilai --5++9--13++16--20++24--= '))
cek1 = x>=5
cek2 = x<=9
cek3 = x>=13
cek4 = x<=16
cek5 = x>=20
cek6 = x<=24
status = cek1 and cek2 or cek3 and cek4 or cek5 and cek6
print('Hasilnya adalah',status)

#TUGAS 4
#++++5----9++++13----16++++20----24
x = int(input('Masukkan Nilai ++5--9++13--16++20--24= '))
cek1 = x<=5
cek2 = x>=9
cek3 = x>=13
cek4 = x<=16
cek5 = x>=20
cek6 = x<=24
status = cek1 or cek2 and cek3 or cek4 and cek5 or cek6
print('Hasilnya adalah',status)















































