from random import randint

can_sayisi=5
print("Türkiye'de bir şehir ismi\n")
kelimeler=["tokat","ankara","yozgat","sivas","bursa"]
secilen_kelime=kelimeler[randint(0,len(kelimeler)-1)]
bos=[]
for i in range(len(secilen_kelime)):
        bos.append("_")
print(bos)


while (can_sayisi>0):
        print("kalan canınız "+str(can_sayisi))
        girilen_harf=input("Bir harf giriniz.")
        if (girilen_harf in secilen_kelime):
                for k in range(len(secilen_kelime)):
                        if(girilen_harf==secilen_kelime[k]):
                                bos[k]=secilen_kelime[k]
                print(bos)
                if("_" not in bos):
                        print("Bildiniz!!!")
                        break
        else:
                can_sayisi =can_sayisi-1
if(can_sayisi==0):
        print("Hiç canınız kalmadı.Kaybettiniz!!")

