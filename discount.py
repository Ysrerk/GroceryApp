import basketm

discountamount = []

discbrdcount = []
soupcontrol = []
breadcontrol=[]
def calculatediscount( product, quantity):

    if product.name == "soup" and quantity>=2:
        soupcontrol.append(1)
    if product.name=="bread":
        breadcontrol.append(1)
    if (product.name=="bread"or len(breadcontrol)==1) and len(soupcontrol)==1 and (sum(discbrdcount)<1):
        discountamount.append(0.8/2)
        discbrdcount.append(1)

    else:
        discountamount.append(0)

    if product.name == "apples":
        discountamount.append((basketm.basket[product] * product.cost * 0.1))

    return discountamount