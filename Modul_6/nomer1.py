import mahasiswa as mhs

c1=mhs.mhsTIF("dandi",21,"solo",240000)
c2=mhs.mhsTIF("dinda",22,"klaten",220000)
c3=mhs.mhsTIF("kaneki",23,"jogja",260000)
c4=mhs.mhsTIF("wibu",24,"klaten",250000)
c5=mhs.mhsTIF("saki",25,"magelang",240000)
c6=mhs.mhsTIF("sora",26,"jakarta",250000)
c7=mhs.mhsTIF("iko",27,"solo",220000)

x = [c1, c2, c3, c4, c5, c6, c7]


def merge(a):
    if len(a) > 1:
        mid = len(a) // 2
        kiri = a[:mid]
        kanan = a[mid:]

        merge(kiri)
        merge(kanan)

        i = 0;
        j = 0;
        k = 0
        while (i < len(kiri) and j < len(kanan)):
            if kiri[i].uang < kanan[j].uang:
                a[k] = kiri[i]
                i = i + 1
            else:
                a[k] = kanan[j]
                j = j + 1
            k = k + 1

        while i < len(kiri):
            a[k] = kiri[i]
            i = i + 1
            k = k + 1

        while j < len(kanan):
            a[k] = kanan[j]
            j = j + 1
            k = k + 1

def partition( arr, low, high):
    i = (low - 1)
    pivot = arr[high].uang
    for j in range(low, high):
        if arr[j].uang <= pivot:
            i = i + 1
            arr[i].uang, arr[j].uang = arr[j].uang, arr[i].uang
    arr[i + 1].uang, arr[high].uang = arr[high].uang, arr[i + 1].uang
    return (i + 1)

def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)


merge(x)
for i in x:
    print(i.uang)

print("================================================")
quickSort(x,0,len(x)-1)
for i in x:
    print(i.uang)
