
basket={}
basketamount=[]
discountamount=[]
discbrdcount=[]

class Product():
    breaddisccount = 0
    def __init__(self,name,cost):
        self.name=name
        self.cost=cost

    def addbasket(self,quantity):
        self.quantity=quantity
        basket[self.name]=self.quantity

    def calculateamount(self,quantity):
        self.quantity=quantity
        basketamount.append(self.quantity*self.cost)
        return basketamount
    def calculatediscount(self,name,quantity):
        self.name=name
        self.quantity=quantity
        soupcontrol = lambda x: 1 if "soup" in basket.keys() and basket["soup"] >= 2 else 0

        if self.name=="soup" or self.name=="bread":
            if (soupcontrol("soup")==1) and ("bread" in basket.keys())and (sum(discbrdcount)<1):
                discountamount.append(bread.cost/2)
                discbrdcount.append(1)
            else:
                discountamount.append(0)

        if self.name=="apples":
            discountamount.append(basket["apples"]*apples.cost*0.1)

        return discountamount
##product defines
milk=Product("milk",1.3)
soup=Product("soup",0.65)
bread=Product("bread",0.8)
apples=Product("apples",0.1)

####add product loop
while True:
    product = input("Please write  below which product do you want  buy:\n")
    if product in basket.keys():
        print("you can not add same product in the basket")
        answer = input("we will clear your basket do you want to continue")
        if answer == "e":
            basket.clear()
            product = input("Please write  below which product do you want  buy:\n")
        else:
            break

    quantity = int(input("Please write below how many do you want this item \n"))
    if product == bread.name:
        bread.addbasket(quantity)
        bread.calculateamount(quantity)
        bread.calculatediscount(product,quantity)

    elif product == milk.name:
        milk.addbasket(quantity)
        milk.calculateamount(quantity)
        milk.calculatediscount(product, quantity)
    elif product == soup.name:
        soup.addbasket(quantity)
        soup.calculateamount(quantity)
        soup.calculatediscount(product, quantity)

    elif product == apples.name:
        apples.addbasket(quantity)
        apples.calculateamount(quantity)
        apples.calculatediscount(product, quantity)
####show result
    print("Do you want add new product in the basket?\nif your answer is yes please write 'E' your answer is no please write 'H' ")
    print("Items in the your basket ", basket)
    secim = input("Please wriye your prefer")
    # sayac += 1
    if secim == ("h" or "H"):
        print("Items in the your basket :", basket)
        print("#####################################")
        print("Total Amount: ", sum(basketamount)-sum(discountamount))
        print("#####################################")
        print("Total Discount Amount: ", sum(discountamount))
        break






