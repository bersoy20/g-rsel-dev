import re # düzenli ifadeleri import ettik

kontrolList = "^[a-z0-9\._]+[@]\w+[.]\w{2,3}([.]\w{2})?$" # karakterlerin olup olmadığını kontrol etmek için
l = input("Bir e-mail adresi giriniz : ") # kullanıcıdan mail adresi girmesini istedik
# liste oluşturuldu.
def kontrolEt(eposta): # kontrol et fonksiyonu tanımladık
    if (re.search(kontrolList, eposta)): # listeden girilen e postanın karakterlerini kontrol ettik
    	print("Girilen e-posta adresi doğru.") # eğer uyumlu ise doğru
    else: # eğer uyumlu değil ise hatalı sonucunu çıkaracak
    	print("Girilen e-posta adresi hatalı.")
k = kontrolEt(l) # k değişkenine kontrol et fonksiyonunu atadık, girilen ifadeyi kontrol etmesi için