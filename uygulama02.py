print("Sınav 5 sorudan oluşmaktadır.")
print("Her soru 20 puandır.\n")
print("Başarılar Dileriz...\n")
puan=0
print("Sorular : \n")
sorular=["Soru 1 :Süper ligin 2003-2004 sezonu şampiyonu kimdir ?",
        "Soru 2 :Tokat hangi bölgededir ?",
        "Soru 3 :Hacettepe Üniversitesi kaç yılında kurulmuştur ?",
        "Soru 4 :Bilgisaylarda ses çıkışını sağlayan aygıt nedir ?",
        "Soru 5 :İstanbul kaç yılında fethedilmiştir ?\n"]
        
        
sıklar=["A : Fenerbahçe\nB : Beşiktaş\nC : Galatasaray\nD : Trabzonspor\n",
       "A : Akdeniz\nB : Karadeniz\nC : Ege\nD : Marmara\n",
       "A : 1966\nB : 1978\nC : 1967\nD : 1974",
       "A : Mikrofon\nB : Apolyo\nC : Klavye\nD : Hoparlör\n",
       "A : 1456\nB : 1452\nC : 1453\nD : 1478\n"]
       
cevaplar=["A","B","C","D","C"]
for i in range(len(sorular)):
    print(sorular[i])
    print(sıklar[i])
    cevap=input("Cevapınızı giriniz.\n")
    if cevap==cevaplar[i] or cevap==cevaplar[i].lower(): 
        print("\nDoğru cevap!\n")
        puan +=20
    else :
        print("\nYanlış cevap!\n")
   
print("Sınav Bitmiştir.")
print("Puanın : "+str(puan))