import basketm,discount


class Product():
    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name
    breaddisccount = 0

    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

##product defines
milk = Product("milk", 1.3)
soup = Product("soup", 0.65)
bread = Product("bread", 0.8)
apples = Product("apples", 0.1)

####add product loop
while True:
    product = input("Please write  below which product do you want  buy:\n")
    quantity = int(input("Please write below how many do you want this item \n"))

    if product == bread.name:
        basketm.addbasket(bread,quantity)
        basketm.calculateamount(bread,quantity)
        discount.calculatediscount(bread, quantity)

    elif product == milk.name:
        basketm.addbasket(milk,quantity)
        basketm.calculateamount(milk,quantity)
        discount.calculatediscount(milk, quantity)
    elif product == soup.name:
        basketm.addbasket(soup,quantity)
        basketm.calculateamount(soup,quantity)
        discount.calculatediscount(soup, quantity)

    elif product == apples.name:
        basketm.addbasket(apples,quantity)
        basketm.calculateamount(apples,quantity)
        discount.calculatediscount(apples, quantity)
    ####show result
    print(
        "Do you want add new product in the basket?\nif your answer is yes please write 'E' your answer is no please write 'H' ")
    print("Items in the your basket ", basketm.basket)
    secim = input("Please wriye your prefer")

    if secim == ("h" or "H"):
        print("Items in the your basket :", basketm.basket)
        print("#####################################")
        print("Total Amount: ", sum(basketm.basketamount) - sum(discount.discountamount))
        print("#####################################")
        print("Total Discount Amount: ", sum(discount.discountamount))
        break
