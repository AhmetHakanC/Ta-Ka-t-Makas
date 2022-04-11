import random
hareketler = ["taş","makas","kağıt"]
puana = 0
pcpuan = 0
b = int(input("Kaç puan olan kazansın? "))
while (pcpuan != b or puana != b):
    pc = random.choice(hareketler)
    a = input("yapacağınız hareketin baş harfini girin çıkmak için 'q'(taş = 't', makas = 'm', kağıt = 'k'): ")
    if(a == "q"):
        print("Çıkılıyor..")
        break
    if(pc == "taş" and a == "t"):
        print("Berabere")
        print("Bilgisayar: ",pcpuan," Senin puanın: ",puana)
    elif(pc == "taş" and a == "k"):
        print("Tebrikler kazandınız!")
        puana = puana + 1
        print("Bilgisayar: ", pcpuan, " Senin puanın: ", puana)
    elif(pc == "taş" and a == "m"):
        print("Maalesef bilgisayar kazandı")
        pcpuan = pcpuan + 1
        print("Bilgisayar: ", pcpuan, " Senin puanın: ", puana)
    if (pc == "makas" and a == "m"):
        print("Berabere")
        print("Bilgisayar: ", pcpuan, " Senin puanın: ", puana)
    elif (pc == "makas" and a == "t"):
        print("Tebrikler kazandınız!")
        puana = puana + 1
        print("Bilgisayar: ", pcpuan, " Senin puanın: ", puana)
    elif (pc == "makas" and a == "k"):
        print("Maalesef bilgisayar kazandı")
        pcpuan = pcpuan + 1
        print("Bilgisayar: ", pcpuan, " Senin puanın: ", puana)
    if (pc == "kağıt" and a == "k"):
        print("Berabere")
        print("Bilgisayar: ", pcpuan, " Senin puanın: ", puana)
    elif (pc == "kağıt" and a == "m"):
        print("Tebrikler kazandınız!")
        puana = puana + 1
        print("Bilgisayar: ", pcpuan, " Senin puanın: ", puana)
    elif (pc == "kağıt" and a == "t"):
        print("Maalesef bilgisayar kazandı")
        pcpuan = pcpuan + 1
        print("Bilgisayar: ", pcpuan, " Senin puanın: ", puana)
    if(pcpuan == b):
        print("Oyunu bilgisayar kazandı")
        break
    elif(puana == b):
        print("Tebrikler! oyunu kazandınız")
        break

