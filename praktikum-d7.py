pwd_benar = 'si23d'
a = True
limit = 3
i = 0
while a:
    i +=1
    pwd = input('Masukkan Password:')
    if pwd == pwd_benar:
        print('Password Benar! Selamat Anda login')
        a = False
    else:
        print('Password Salah!')
        if i == limit:
            print('Kesempatan Anda Habis')
            a = False
        else:
            print('Kesempatan Anda Tersisa {limit-i}kali')
