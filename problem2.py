def find_top_seller(products: dict, sales: dict) -> str:
    maximal = 0
    name = ""

    for product in products:
        sotuv = products[product]*sales[product]
        if sotuv > maximal:
            maximal = sotuv 
            name = product

    return name
            


print(find_top_seller(
    {"Olma": 5000, "Banan": 8000, "Uzum": 7000},
    {"Olma": 10,   "Banan": 5,    "Uzum": 8}
))