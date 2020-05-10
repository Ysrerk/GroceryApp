

sepettutar=0
sayac=0

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
        for key, value in sepet.items():#yeni
            temp2.append((key, value), )#yeni


    def calculatebasket(self,miktar):
        self.miktar=miktar
        product=self.prdname
        sepettutar=float(stock[product])*int(self.miktar)

        basketamount.append(sepettutar)
        if product=="bread":
            breadindex=(basketamount.index(sepettutar))#yeni
            breadindexl.append(breadindex)
            return sepettutar, breadindexl[0]
        else:
            breadindex=""
            return sepettutar, breadindex


stock = {}
sepet={}
basketamount=[]
temp2=[]#yeni
temp3=[]#yeni
tempsoup=[]#yeni
breadindexl=[]#yeni

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



while True:

    urun=input("Please write  below which product do you want  buy:\n")
    if urun in sepet.keys():
        print("you can not add same product in the basket")
        answer=input("we will clear your basket do you want to continue")
        if answer=="e":
            sepet.clear()
            urun = input("Please write  below which product do you want  buy:\n")
        else:
            break


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
    sayac+=1
    if secim==("h"or "H"):
        temp3 = temp2[::-1]#yeni
        temp2=[]#yeni
        temp2=temp3[0:sayac]#yeni
        #basketamount=basketamount[::-1]#

        for i in temp2:#yeni
            for j in i:#yeni
                if j == "soup":#yeni
                    tempsoup.append(i[1])#yeni
                    if sum(tempsoup)>=2:#yeni
                        if "bread" in sepet.keys():#yeni
                            basketamount[breadindexl[0]] = basketamount[breadindexl[0]] / 2#yeni


        print("#####################################")
        print("Items in the your basket :", sepet)
        print("#####################################")
        print("Total Amount: ",sum(basketamount))

        # print(temp2)###yeni
        # print(temp3)
        # print(sayac)#yeni
        # print(basketamount)
        break














