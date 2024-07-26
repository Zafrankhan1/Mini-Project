menu = {
    "Pizza" : 120,
    "Pasta" : 100,
    "Coffee" : 90,
    "Chikken" : 200,
    "Milk Shek" : 100,
    "Rice" : 150,
}

print("Welcome to our Resturant")

print(f"""
      Pizza : Rs 110 \n 
    Pasta :Rs 100\n
    Coffee :Rs 90\n
    Chikken :Rs 200\n
    Milk Shek :Rs 100\n
    Rice :Rs 150""")

total_order = 0

item_1 = input("Enter your order please:")

if item_1 in menu:
    total_order += menu[item_1]

    print(f"Your {item_1} has been added to order")

else:
    print("Not available right now , please order something other")

another_order = input("Do you want another order?(Yess/No)")

if another_order == "Yes":
    item_2 = input("Enter your another order:")

    if item_2 in menu:
        total_order += menu[item_2]

        print(f'Your {item_2} has been added to your order')
else:
    print('We are sorry this  is not present now')        

print(f"Sir your total bill is Rs {total_order}")
