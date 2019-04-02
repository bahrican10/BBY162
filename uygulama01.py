print("Sınav 5 sorudan oluşmaktadır.")
print("Her soru 20 puandır.\n")
print("Başarılar Dileriz...")
puan=0
#1.Soru
print("Süper ligin 2003-2004 sezonu şampiyonu kimdir ?\n")
print("Cevabınızı giriniz : \n")
cevap=input()
if cevap=="Fenerbahçe" or cevap=="fenerbahçe" or cevap=="Fenerbahce" or cevap=="fenerbahce":
	puan =puan+20
	print("\nTebrikler! Cevabınız doğru.")
	print("Mevcut puanınız: "+ " " + str(puan)+"\n")
else:
	print("Cevabınız yanlış.")
	print("Bu sorudan hiç puan alamadınız.")
	print("Mevcut puanınız "+" "+str(puan)+"\n")
	
#2.Soru

print("Tokat hangi bölgededir ?\n")
print("Cevabınızı giriniz : \n")
cevap=input()
if cevap=="Karadeniz" or cevap=="karadeniz" :
	puan =puan+20
	print("\nTebrikler! Cevabınız doğru.")
	print("Mevcut puanınız: "+ " " + str(puan)+"\n")
else:
	print("Cevabınız yanlış.")
	print("Bu sorudan hiç puan alamadınız.")
	print("Mevcut puanınız "+" "+str(puan)+"\n")

#3.soru


print("Hacettepe Üniversitesi kaç yılında kurulmuştur ?\n")
print("Cevabınızı giriniz : \n")
cevap=input()
if cevap=="1967":
	puan =puan+20
	print("\nTebrikler! Cevabınız doğru.")
	print("Mevcut puanınız: "+ " " + str(puan)+"\n")
else:
	print("Cevabınız yanlış.")
	print("Bu sorudan hiç puan alamadınız.")
	print("Mevcut puanınız "+" "+str(puan)+"\n")
	
	
#4.Soru

print("Bilgisaylarda ses çıkışını sağlayan aygıt nedir ?\n")
print("Cevabınızı giriniz : \n")
cevap=input()
if cevap=="Hoparlör" or cevap=="hoparlör":
	puan =puan+20
	print("\nTebrikler! Cevabınız doğru.")
	print("Mevcut puanınız: "+ " " + str(puan)+"\n")
else:
	print("Cevabınız yanlış.")
	print("Bu sorudan hiç puan alamadınız.")
	print("Mevcut puanınız "+" "+str(puan)+"\n")
	
#5.Soru

print("İstanbul kaç yılında fethedilmiştir ?\n")
print("Cevabınızı giriniz : \n")
cevap=input()
if cevap=="1453":
	puan =puan+20
	print("\nTebrikler! Cevabınız doğru.")
	print("Mevcut puanınız: "+ " " + str(puan)+"\n")
else:
	print("Cevabınız yanlış.")
	print("Bu sorudan hiç puan alamadınız.")
	print("Mevcut puanınız "+" "+str(puan)+"\n")
print("Sınav bitmiştir .")	
