print ("\n\t\ Soru 1 ")
metin = "Açık bilim, araştırma çıktılarına ve süreçlerine herkesin serbestçe erişmesini, bunların ortak kullanımını, dağıtımını ve üretimini kolaylaştıran bilim uygulamasıdır."

print(metin)
print("\t\tilk yirmi karakteri ekrana geliyor...")
ilk20 = metin[:21]
print(ilk20) 





 #2.Soru
for s in ["Açık Bilim", "Açık Erişim", "Açık Lisans", "Açık Eğitim", "Açık Veri", "Açık Kültür"]:
    print(s)
    
    
    
    
    
#Soru3
kelime=input("Bir kelime girin :")
sozluk ={"Elma" :"Ağaçta yetişen bir tür meyve",
        " Salatalık" : "Fidan üzerinde büyüyen bir tür sebze"}

if kelime  in sozluk:
    print(sozluk[kelime])
else:
    print("Aradığınız kelime sözlükte bulunamadı")
