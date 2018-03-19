def rvs(metin):

    a = len(metin)
    dizi = []

    for i in range(a):
        a = a - 1
        dizi.extend(metin[a])

    dizi = ''.join(dizi)
    return dizi

klm = input("Çevrilmesini İstediğiniz Metni Giriniz: ")
print(rvs(klm))
