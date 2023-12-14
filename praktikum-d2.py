print('Praktikum-2')
print('==============Ini and=================')
a = True
b = False
hasil = a and a
print('Nilai',a,'and',a,'adalah',hasil)
hasil = a and b
print('Nilai',a,'and',b,'adalah',hasil)
hasil = b and b
print('Nilai',b,'and',b,'adalah',hasil)
hasil = b and a
print('Nilai',b,'and',a,'adalah',hasil)

print('\n==============Ini or=================')
a = True
b = False
hasil = a or a
print('Nilai',a,'or',a,'adalah',hasil)
hasil = a or b
print('Nilai',a,'or',b,'adalah',hasil)
hasil = b or a  
print('Nilai',b,'or',a,'adalah',hasil)
hasil = b or b
print('Nilai',b,'or',b,'adalah',hasil)

print('\n==============Ini not=================')
hasil = not a
print('hasil not',a,'adalah',hasil)
hasil = not b
print('hasil not',b,'adalah',hasil)


print('\n==============Ini xor=================')
hasil = a^a
print('Nilai',a,'xor',a,'adalah',hasil)
hasil = a^b
print('Nilai',a,'xor',b,'adalah',hasil)
hasil = b^a
print('Nilai',b,'xor',a,'adalah',hasil)
hasil = b^b
print('Nilai',b,'xor',b,'adalah',hasil)

print('==============Ini nand=================')
hasil = not (a and a)
print('Nilai',a,'nand',a,'adalah',hasil)
hasil = not (a and b)
print('Nilai',a,'nand',b,'adalah',hasil)
hasil =  not(b and b)
print('Nilai',b,'nand',b,'adalah',hasil)
hasil = not (b and a)
print('Nilai',b,'nand',a,'adalah',hasil)

print('\n==============Ini nor=================')
hasil = not (a or a)
print('Nilai',a,'nor',a,'adalah',hasil)
hasil = not (a or b)
print('Nilai',a,'nor',b,'adalah',hasil)
hasil = not (b or a)
print('Nilai',b,'nor',a,'adalah',hasil)
hasil = not (b or b)
print('Nilai',b,'nor',b,'adalah',hasil)

print('\n==============Ini nxor=================')
hasil = a^a
print('Nilai',a,'nxor',a,'adalah',not hasil)
hasil = a^b
print('Nilai',a,'nxor',b,'adalah',not hasil)
hasil = b^a
print('Nilai',b,'nxor',a,'adalah',not hasil)
hasil = b^b
print('Nilai',b,'nxor',b,'adalah',not hasil)

print('================ IS ================')
a = 5
b = 6
print('Nilai',a,'memiliki identitas=',hex(id(a)))
print('Nilai',b,'memiliki identitas=',hex(id(b)))
hasil = a is b
print('a is b =',hasil)

print('================ IS ================')
a = 6
b = 6
print('Nilai',a,'memiliki identitas=',hex(id(a)))
print('Nilai',b,'memiliki identitas=',hex(id(b)))
hasil = a is b
print('a is b =',hasil)


print('================ IS NOT ================')
a = 5
b = 6
print('Nilai',a,'memiliki identitas=',hex(id(a)))
print('Nilai',b,'memiliki identitas=',hex(id(b)))
hasil = a is not b
print('a is not b =',hasil)
a = 6
b = 6
print('Nilai',a,'memiliki identitas=',hex(id(a)))
print('Nilai',b,'memiliki identitas=',hex(id(b)))
hasil = a is not b
print('a is not b =',hasil)

print('\n============= in')
nama = 'Bacharuddin Jusuf Habibie'
test = 'rud'
cek = test in nama
print(test,'terdapat di',nama,'adalah '+str(cek))

test = 'bach'
cek = test in nama
print(test,'terdapat di',nama,'adalah '+str(cek))

test = 'ib'
cek = test in nama
print(test,'terdapat di',nama,'adalah '+str(cek))

test = 'a'
cek = test in nama
print(test,'terdapat di',nama,'adalah '+str(cek))

test = 'i'
cek = test in nama
print(test,'terdapat di',nama,'adalah '+str(cek))

test = 'u'
cek = test in nama
print(test,'terdapat di',nama,'adalah '+str(cek))

test = 'e'
cek = test in nama
print(test,'terdapat di',nama,'adalah '+str(cek))

test = 'o'
cek = test in nama
print(test,'terdapat di',nama,'adalah '+str(cek))

print('\n============= not in')
#Tugas Buat nama menjadi lengkap masing-masing)

print('\n============= not in')
data = ['Institut',
        'Teknologi',
        'Bacharuddin',
        'Jusuf',
        'Habibie']
print('Data adalah',data)
test1 = 'Habibie'
test2 = 'Parepare'
test3 = 'Kampus'
test4 = 'Institut'

cek = test1 in data
print(test1,'terdapat di data adalah '+str(cek))
cek = test2 in data
print(test2,'terdapat di data adalah '+str(cek))
cek = test3 in data
print(test3,'terdapat di data adalah '+str(cek))
cek = test4 in data
print(test4,'terdapat di data adalah '+str(cek))


#Tugas dengan cara yang sama buat operator untuk not in



#INI OPERATOR BITWISE
a = 5
b = 8
print('\n============= AND')
print('Nilai',a,'dalam biner=',format(a,'08b'))
print('Nilai',b,'dalam biner=',format(b,'08b'))

a = 5
b = 8
b += 80
print('Nilai',a,'dalam biner     =',format(a,'08b'))
print('Nilai',b,'dalam biner    =',format(b,'08b'))
print('-------------------AND')
c = a & b
print('Nilai',a,'&',b,'dalam biner adalah',format(c,'08b'))


print('\n============= OR')
print('Nilai',a,'dalam biner=',format(a,'08b'))
print('Nilai',b,'dalam biner=',format(b,'08b'))

a = 5
b = 8
b += 80
print('Nilai',a,'dalam biner     =',format(a,'08b'))
print('Nilai',b,'dalam biner    =',format(b,'08b'))
print('-------------------OR')
c = a & b
print('Nilai',a,'&',b,'dalam biner adalah',format(c,'08b'))



print('\n============= TUGAS ==========================')
#Tugas Buat nama menjadi lengkap masing-masing)
nama = 'Yesi'
test = 'Ye'
cek = test in nama
print(test,'terdapat di',nama,'adalah '+str(cek))

test = 'yes'
cek = test in nama
print(test,'terdapat di',nama,'adalah '+str(cek))

test = 'esi'
cek = test in nama
print(test,'terdapat di',nama,'adalah '+str(cek))

test = 'a'
cek = test in nama
print(test,'terdapat di',nama,'adalah '+str(cek))

test = 'i'
cek = test in nama
print(test,'terdapat di',nama,'adalah '+str(cek))

test = 'u'
cek = test in nama
print(test,'terdapat di',nama,'adalah '+str(cek))

test = 'e'
cek = test in nama
print(test,'terdapat di',nama,'adalah '+str(cek))

test = 'o'
cek = test in nama
print(test,'terdapat di',nama,'adalah '+str(cek))


print()
print('\n============= not in')
data = ['Institut',
        'Teknologi',
        'Bacharuddin',
        'Jusuf',
        'Habibie']
print('Data adalah',data)
test1 = 'Habibie'
test2 = 'Parepare'
test3 = 'Kampus'
test4 = 'Institut'

cek = test1  not in data
print(test1,'terdapat di data adalah '+str(cek))
cek = test2 not in data
print(test2,'terdapat di data adalah '+str(cek))
cek = test3 not in data
print(test3,'terdapat di data adalah '+str(cek))
cek = test4 not in data
print(test4,'terdapat di data adalah '+str(cek))



print('\n============== XOR =================')
hasil = a^b
print('Nilai',a,'dalam biner     =',format(a,'08b'))
print('Nilai',b,'dalam biner    =',format(b,'08b'))
c = a^b
print('Nilai',a,'^',b,'dalam biner adalah',format(c,'08b'))


print('\n============== NOT =================')
hasil = ~a
c = ~a
print('Nilai',a,'dalam biner      =',format(a,'08b'))
print('Nilai ~',a,'dalam biner    =',format(c,'08b'))

hasil = ~b
c = ~b
print('Nilai',b,'dalam biner      =',format(b,'08b'))
print('Nilai ~',b,'dalam biner    =',format(c,'08b'))

print('\n============== GESER KANAN =================')
c = a >> 2
print('Nilai',a,'dalam biner       =',format(b,'08b'))
print('nilai',a,'>> 2 dalam biner adalah',format(a,'08'))

print('\n============== GESER KIRI =================')
c = a << 2
print('Nilai',a,'dalam biner       =',format(b,'08b'))
print('nilai',a,'<< 2 dalam biner adalah',format(a,'08'))


#operator not

print('\n============== NOT AND =================')
a = 5
b = 8
b &= 80
print('Nilai',a,'nand','dalam biner     =',format(a,'08b'))
print('Nilai',b,'nand','dalam biner     =',format(b,'08b'))
c = ~a & b
print('Nilai not ~',a,'&',b,'dalam biner adalah',format(c,'08b'))


print('\n============== NOT OR  =================')
a = 5
b = 8
b |= 80
print('Nilai',a,'nor','dalam biner     =',format(a,'08b'))
print('Nilai',b,'nor','dalam biner    =',format(b,'08b'))
c = ~a | b
print('Nilai not~',a,'|=',b,'dalam biner adalah',format(c,'08b'))



print('\n==============  NOT  XOR =================')
a = 5
b = 8
b = 80
hasil = a^b
print('Nilai',a,'nxor','dalam biner     =',format(a,'08b'))
print('Nilai',b,'nxor','dalam biner    =',format(b,'08b'))
c = a^b
print('Nilai not',a,'^',b,'dalam biner adalah',format(c,'08b'))


print('\n============== NOT GESER KANAN =================')
c = a >> 2
print('Nilai not',a,'dalam biner       =',format(b,'08b'))
print('nilai not',a,'>> 2 dalam biner adalah',format(a,'08'))

print('\n==============  NOT GESER KIRI =================')
c = a << 2
print('Nilai not',a,'dalam biner       =',format(b,'08b'))
print('nilai not',a,'<< 2 dalam biner adalah',format(a,'08'))










