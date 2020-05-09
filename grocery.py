

sepettutar=0

class Product():
    #stock = {"soup": 0.65, "bread": 0.8, "milk": 1.3, "apples": 0.10}
    def __init__(self,prdname,unit):
        self.prdname=prdname
        self.unit=unit

    def updatecost(self,cost):
        self.cost=cost
    def productdisplay(self):
        print("urunun adi:{} \n urunun Birimi :{}\n urunun fiyati:{}".format(self.prdname,self.unit,self.cost))
    def addproduct(self):
        stock[self.prdname]=self.cost
    def addbasket(self,miktar):
        self.miktar=miktar
        sepet[self.prdname]=self.miktar
    def calculatebasket(self,miktar):
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
soup.addproduct()
#print(stock)
bread=Product("bread","loaf")
bread.updatecost(20)
bread.addproduct()
#print(stock)
#####
milk=Product("milk","bottle")
milk.updatecost(30)
milk.addproduct()
#######
apples=Product("apples","single")
apples.updatecost(40)
apples.addproduct()
#print(stock)
# x="bread"
# print(stock[x]*3)

# for key,value in stock.items():
#     print(key,":",value)


while True:

    urun=input("Please write  below which product do you want  buy:\n")
    miktar=int(input("Please write below how many do you want this item \n"))
    if urun==bread.prdname:
        bread.addbasket(miktar)
        bread.calculatebasket(miktar)

    elif urun==milk.prdname:
        milk.addbasket(miktar)
        milk.calculatebasket(miktar)
    elif urun==soup.prdname:
        soup.addbasket(miktar)
        soup.calculatebasket(miktar)

    elif urun==apples.prdname:
        apples.addbasket(miktar)
        apples.calculatebasket(miktar)


    print("Do you want add new product in the basket?\nif your answer is yes please write 'E' your answer is no please write 'H' ")
    print("Items in the your basket ",sepet)
    secim=input("Please wriye your prefer")
    if secim==("h"or "H"):

        print("#####################################")
        print("Items in the your basket :", sepet)
        print("#####################################")
        print("Total Amount: ",sum(basketamount))
        break














