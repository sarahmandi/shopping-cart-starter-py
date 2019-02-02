# shopping_cart.py
import datetime
now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017


shopping_list = []


#print(products)
#INFO CAPTURE

while True: 
    try:
        user_input = input("Please input a product identifier, or 'DONE' if there are no more items: ") #> input is a string
        number = int(user_input)
        if number < 0 or number > 20:
            print("Are you sure that you entered a valid product id? Please try again!")
        if number <21 and number > 0:
            shopping_list.append(str(user_input)) 
    except ValueError:
        if user_input == "DONE":
            break  #>ends loop if user inputs DONE
        else:
            print("Are you sure that you entered a valid product id? Please try again!")
    
#INFO DISPLAY

print("--------------------------------------")
print("SARAH'S SUPERMARKET")
print("--------------------------------------")
print("Web: "+ "www.sarahsupermarket.com")
print("Phone: " + "123.456.789")
print("Checkout Time: " + str(now))
print("--------------------------------------")
print("Shopping Cart Items:")

#print(shopping_list)

running_total = 0


#PRINT ITEMS IN RECEIPT

for item in shopping_list:
    matching_products = [p for p in products if str(p["id"]) == str(item)]
    #print(matching_products)
    matching_product = matching_products[0]
    running_total = running_total + matching_product["price"]
    print(" +  " + matching_product["name"] +  " (" + '${:,.2f}'.format(int(matching_product["price"]))+ ")")


tax = 0.06*running_total
total = running_total + tax

print("--------------------------------------")
print("Subtotal:" + str('${:,.2f}'.format(running_total)))
print("Plus DC Sales Tax (6%): " + str('${:,.2f}'.format(tax)))
print("Total: " + str('${:,.2f}'.format(total)))
print("--------------------------------------")
print("We appreciate your business! Please come again.")


