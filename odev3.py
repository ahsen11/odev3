sayilar = [3,5,7,2,12,32,45]

# 1- "sayilar" listesindeki her bir elemanı yazdırınız.
for x in sayilar:
    print(x)

# 2- "sayilar" listesinde hangi sayılar 3' ün katıdır?
for i in sayilar: 
    if i %3 == 0:
        print(i)

# 3- "sayilar" listesinde tüm sayıların toplamı nedir?
print(sum(sayilar))


urunler = ["iphone 13","samsung s24","samsung s22","iphone 15","iphone 14"]

# 4- "urunler" listesindeki tüm iphone marka ürünleri listeleyiniz. (index ve find komutlarından faydalanınız.)
iphoneUrunler=[]
for urun in urunler:
    if urun.find("iphone") != -1:
        iphoneUrunler.append(urun)

print("iphone marka ürünler: ", iphoneUrunler)
# 5- "urunler" listesinde kaç adet samsung ürünü vardır? (find metodu)
samsungUrunler=[]
for urun in urunler:
    if urun.find("samsung") != -1:
        samsungUrunler.append(urun)

print(len(samsungUrunler))