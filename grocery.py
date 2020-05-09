
class Product():
    #stock = {"soup": 0.65, "bread": 0.8, "milk": 1.3, "apples": 0.10}
    def __init__(self,prdname,unit):
        self.prdname=prdname
        self.unit=unit



    def updatecost(self,cost):
        self.cost=cost
    def productdisplay(self):
        print("urunun adi:{} \n urunun Birimi :{}\n urunun fiyati:{}".format(self.prdname,self.unit,self.cost))
    def urunekle(self):
        stock[self.prdname]=self.cost
    def sepeteekle(self,miktar):
        self.miktar=miktar
        sepet[self.prdname]=self.miktar
    def sepethesapla(self,miktar):
        self.miktar=miktar
        sepettutar+=float(stock[self.prdname])*int(self.miktar)
        return  sepettutar


sepettutar=0
stock = {}
sepet={}





soup=Product("soup","tin")
soup.updatecost(0.65)
soup.productdisplay()
soup.urunekle()
print(stock)
bread=Product("bread","loaf")
bread.updatecost(0.8)
bread.urunekle()
print(stock)
#####
milk=Product("milk","bottle")
milk.updatecost(1.3)
milk.urunekle()
#######
apples=Product("apples","single")
apples.updatecost(0.1)
apples.urunekle()
print(stock)
MyApp

# for key,value in stock.items():
#     print(key,":",value)

###
#
while True:

    urun=input("Lutfen almak istediginiz urunu yaziniz")
    miktar=int(input("Almak istedoiginiz urunun miktarini yaziniz"))
    if urun==bread.prdname:
        bread.sepeteekle(miktar)
        bread.sepethesapla(miktar)

    elif urun==milk.prdname:
        milk.sepeteekle(miktar)
        milk.sepethesapla(miktar)
    elif urun==soup.prdname:
        soup.sepeteekle(miktar)
        soup.sepethesapla(miktar)

    elif urun==apples.prdname:
        apples.sepeteekle(miktar)
        apples.sepethesapla(miktar)


    print("sepete yeni urun eklemek istiyormusunuz Evet ise E ye basin Hayir Ise H ye Basin ")
    print("sepenizdeki mevcut urunler ve miktarlari su sekildedir ",sepet,"sepet tutari",sepettutar)
    secim=input("seciminizi giriniz")
    if secim==("h"or "H"):
        break


t=list((m,x,a,y)for (m,x)  in sepet.items() for (a,y)in stock.items())
print(t)
sepett=0
for key,value in sepet.items():
    if key==stock.keys():
        sepett+=(value*stock[key][value])











