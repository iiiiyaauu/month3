products = {
    'milk' : 1.5,
    'bread' : 0.65,
    'vodka' : 19.2,
    'juice' : 5.1,
    'fish' : 4.2,

    'laptop' : 500.0,
    'tv' : 600.50,
    'smartphone' : 200.12,

    'table' : 40.2,
    'chair': 20.0,
    'sofa' : 100.3,
    'book' : 3.0,
}

cart = dict()

som = 85
tenge = 431
dollar = 1

def show_products(dct: dict):
    for key, values in dct.items():
        print(f"{key} - {round(values, 2)}$")

def add_to_cart(dct: dict, choice):
    for name, price in dct.items():
        if choice == name:
            cart.update({name:price})

def change_price(dct, price = 1):
    new_price = {item: value * price for (item, value) in dct.items()}
    return new_price

def price_sum(dct: dict):
    summary = 0
    for price in dct.values():
        summary += price
    return summary

def main():
    show_products(products)
    while True:
        choice = input("Please choise products(enter 'q' to stop): ")
        if choice == 'q':
            currency = input("Enter currency(som, tenge)enter for Dollar: ")
            if currency == "":
                price = change_price(cart)
                currency = "dollar"
            elif currency == "som":
                price = change_price(cart, som)
            elif currency == "tenge":
                price = change_price(cart, tenge)

            summa = price_sum(price)
            print(f"Cash - {round(summa, 2)} {currency}s")
            cash = int(input(f"How much money do you have?(In {currency}s) "))
            change = lambda cash, summa: cash - summa

            if cash < summa:
                print("not enough money!")
                break
            else:

                print(f"Your change {round(change(cash, summa), 2)} {currency}s")
                break
        else:
            add_to_cart(products, choice)
            print("Your cart: ")
            show_products(cart)

main()