a = int(input("1. Sayiyi Giriniz : "))
b = int(input("2. Sayiyi Giriniz : "))

dekor = "*********************************"

print("Yapmak Istediginiz Islemi Seciniz :")

print(dekor)
print("1. Toplama\n2. Cikarma\n3. Carpma\n4. Bolme")
print(dekor)
print("hall0")
islem = int(input())

if (islem == 1):
    print("Isleminizi Sonucu : ",a+b)

elif (islem == 2):
    print("Isleminizi Sonucu : ",a-b)

elif (islem == 3):
    print("Isleminizi Sonucu : ",a*b)

elif (islem == 4):
    print("Isleminizi Sonucu : ",a/b)

else:
    print("Gecersiz Islem")
