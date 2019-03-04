def katakan(a):
    angka=("","satu","dua","tiga","empat","lima","enam","tujuh","delapan","sembilan","sepuluh","sebelas")
    hasil=""
    n=int(a)
    if n >=0 and n<=11:
        hasil=hasil+angka[n]
    elif n<20:
        hasil=angka[(n%10)]+" belas"
    elif n<100:
        hasil=katakan(n/10)+" puluh "+katakan(n%10)
    elif n<200:
        hasil="seratus "+katakan(n-100)
    elif n<1000:
        hasil=katakan(n/100)+" ratus "+katakan(n%100)
    elif n<2000:
        hasil="seribu "+katakan(n-1000)
    elif n<1000000:
        hasil=katakan(n/1000)+" ribu "+katakan(n%1000)
    elif n<1000000000:
        hasil=katakan(n/1000000)+" juta "+katakan(n%1000000)
    return hasil
print(katakan(3125750))
