ilk = int(input("İlk Sayınızı Giriniz : "))
ikinci = int(input("İkinci Sayınızı Giriniz : "))
islem = input("""Yapmak istediiniz İşlemi Giriniz.
(Toplama (+) Çıkarma (-,), Çarpma (x), Bölme(/))""")

if islem == "+":
    print("Sonuç : "+str(ilk+ikinci))

elif islem == "-":
    print("Sonuç : "+str(ilk - ikinci))

elif islem == "x":
    print("Sonuç : "+str(ilk * ikinci))

elif islem == "/":
    print("Sonuç : "+str(ilk / ikinci))



