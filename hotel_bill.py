print(
    """
Menu

1. Idly
2. Vada
3. Poori
4.Biriyani
5.icecream

"""
)

items = []
costs = []
quantities = []

while True:
    x = int(input("Enter the item number (or 0 to finish): "))

    if x == 0:
        break

    if x == 1:
        item = 'Idly'
        cost = 30
    elif x == 2:
        item = 'Vada'
        cost = 20
    elif x == 3:
        item = 'Poori'
        cost = 40
    elif x==4:
        item = 'Biriyani'
        cost = 250
    elif x==5:
        item='icecream'
        cost = 45
    else:
        print("Invalid selection, please try again.")
        continue

    quantity = int(input(f"Enter quantity for {item}: "))

    items.append(item)
    costs.append(cost)
    quantities.append(quantity)

print(*zip(costs, quantities))

total = sum(cost * quantity for cost, quantity in zip(costs, quantities))
tax = total * 10 / 100
tax_total = tax + total

print(
    f"""
               Shivara Thindi
-----------------------------------------------------
                                    Date:21/01/2024
GSTIN: PENTAGON                                    
-----------------------------------------------------                            
SL NO       ITEMS            QUANTITY          PRICE
"""
)

for i, (item, cost, quantity) in enumerate(zip(items, costs, quantities), start=1):
    print(f"{i}           {item}                {quantity}               {cost}")

print(
    f"""
-----------------------------------------------------

                                        TOTAL: {total}
                                        TAX  : 10%
-----------------------------------------------------
                    TOTAL (INC OF ALL TAX)   : {tax_total}

"""
)