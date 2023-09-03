a=int(input("7ga bo'linadigan son kiriting: "))
if a % 7 == 0 :
    print("Son 7ga bulinadi")
else:
    print("Xato son")    

yoshlar=[12,34,6,24]
eng_kichigi=min(yoshlar)
print("Eng kichik yosh:",eng_kichigi, )
print("ruyxatdagi yoshlar:",yoshlar)

ishchi=("Ish haqqingizni kiriting va qancha yil davomida ishlaganingizni kiriting:")
print(ishchi)
oylik=int(input( ))
staj=int(input())
if staj==10 and oylik==100 :
    print("Sizning maoshingizga ",oylik+(oylik/100*15),"ming bonus qushildi" )
elif staj==20:
    print("Sizning maoshingizga ",oylik+(oylik/100*25),"ming bonus qushildi")
elif staj==35:
    print("Sizning maoshingizga ",oylik+(oylik/100*42.5),"ming bonus qushildi")
else:
    print("Xato kirittingiz!")       

c=("Yurgan masofangizni va u uchun ketgan vaqtni kiriting:")
print(c)
m=int(input( ))
s=int(input( ))
v=m/s
print("Sizning tezligingiz",v)

books=['Qushlar','Qizil kitob','Sirli Ertaklar','Hayot imtihoni','Dunyo va Oxirat','Guzal Jannat','Matematik formulalar','Gullar']
d=input("Kitob nomini kiriting bor yoki yo'qligini aytaman: ")
if d in books :
    print("Bu kitob bazada bor")
else:
    d is not books 
    print("bu kitob baza yoq !")  
    y=("1ni va kitob nomini kiriting va bazaga yozib olamiz!")
    print(y) 
    n=int(input( ))
    name=input( )
books.append(name) 
print(books)



