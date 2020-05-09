sepettutar=0

class Product():
    #stock = {"soup": 0.65, "bread": 0.8, "milk": 1.3, "apples": 0.10}
    def __init__(self,prdname,unit):
        self.prdname=prdname
        self.unit=unit

#message only

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
        product=self.prdname
        sepettutar=float(stock[product])*int(self.miktar)
        basketamount.append(sepettutar)
        return sepettutar



stock = {}
sepet={}
basketamount=[]





soup=Product("soup","tin")
soup.updatecost(10)
soup.productdisplay()
soup.urunekle()
print(stock)
bread=Product("bread","loaf")
bread.updatecost(20)
bread.urunekle()
print(stock)
#####
milk=Product("milk","bottle")
milk.updatecost(30)
milk.urunekle()
#######
apples=Product("apples","single")
apples.updatecost(40)
apples.urunekle()
print(stock)
# x="bread"
# print(stock[x]*3)

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
    print("Items in the your basket ",sepet)
    secim=input("seciminizi giriniz")
    if secim==("h"or "H"):
        print("Items in the your basket ", sepet)
        print("Total Amount ",sum(basketamount))
        break


# t=list((m,x,a,y)for (m,x)  in sepet.items() for (a,y)in stock.items())
# print(t)
# sepett=0
# for key,value in sepet.items():
#     if key==stock.keys():
#         sepett+=(value*stock[key][value])











