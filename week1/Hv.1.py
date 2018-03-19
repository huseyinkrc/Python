sayi1 = int (input("sayi 1 giriniz"))
sayi2 = int (input("sayi 2 giriniz"))
islem = input("islemi giriniz(+,-,*/) =>" )
if islem == "+":
    sonuc =sayi1 +sayi2
    print(sonuc)
elif islem == "-":
    sonuc = sayi1 - sayi2
    print(sonuc)
elif islem == "*":
    sonuc = sayi1 * sayi2
    print(sonuc)
elif islem == "/" and sayi2 != 0:
    sonuc = sayi1 / sayi2
    print(sonuc)
else:
    print("hatalı gris yaptınız...!")
