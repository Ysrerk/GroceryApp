
basket = {}
basketamount = []

def addbasket( product ,quantity):
    if basket.get(product):
        basket[product] = quantity+basket[product]
    else:
        basket[product] =quantity

def calculateamount(product, quantity):

    basketamount.append(product.cost*quantity )
    return basketamount