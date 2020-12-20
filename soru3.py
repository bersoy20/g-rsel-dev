a = input ( "Bir Metin Giriniz: " )
ana_metin = a

b = input ( "Metinde Aranacak İfade: " )
aranacak_ifade = b
arama_komutu = ana_metin.find(aranacak_ifade)
if (arama_komutu > 0):
    onceki = ana_metin[arama_komutu - 1]
    sonraki = ana_metin[arama_komutu + len(aranacak_ifade)]
    print(onceki + aranacak_ifade + sonraki)
else:
    print("Aranan ifade bulunamadı!")