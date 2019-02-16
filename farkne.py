txt1=input("ilk yolu veriniz")
txt2=input("ikinci yolu veriniz")

#C:/Users/tatata/Desktop/deneme.txt
#C:/Users/tatata/Desktop/deneme2.txt

txt1=open(txt1,"r")
txt2=open(txt2,"r")

dizi1=txt1.readlines()
dizi2=txt2.readlines()

if(len(dizi1)<len(dizi2)):
    kisalen=len(dizi1)
else:
    kisalen=len(dizi2)
#-------------------------------------
for i in range(kisalen):
    if(dizi1[i]!=dizi2[i]):
        print(str(i+1)+". satir :")
        print("dizi1 de :"+dizi1[i])
        print("dizi2 de :"+dizi2[i])









