#Creating a header for the project
header = "Len's slice\norganized sales data\n"
print(header)

#1 Making an inventory
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]

#2 Pizza prices
prices = [2, 6, 1, 3, 2, 7, 2]

#3 How many slices are $2?
num_two_dollar_slices = prices.count(2)
print("There are " + str(num_two_dollar_slices) + " two dollar slices.\n")

#4&5 How many pizzas do we have?
num_pizzas = len(toppings)
print("We sell " + str(num_pizzas) + " different kinds of pizza!")

#6 Combining the pizza toppings and prices to a menu
pizza_and_prices = [list(item) for item in zip(prices, toppings)]

#12 Adding a menu option
pizza_and_prices.append([2.5, "peppers"])

#7Printing everything
#print(pizza_and_prices)

#8 Sorting pizzas
pizza_and_prices.sort()
sorted_pizza = sorted(pizza_and_prices)

#9 Storing the cheapest pizza
cheapest_pizza = sorted_pizza[0]
print("Our most affordable option is " + str(cheapest_pizza) + "!\n")

#Obliging the shouting customer with 2the priciest pizza
priciest_pizza = sorted_pizza[-1]
print("For the fancypants feinschmeckers we also have a more refined option, the " + str(priciest_pizza) + ", which is sure to satisfy even the most discerning palate.\n")

#11 This is starting to look more like a chatlog. Removing the last shred of fine dining this place had to offer
sorted_pizza.pop()

#13 special prices for my special little mouse friends. List of the three cheapest pizzas coming up
three_cheapest = sorted_pizza[0:3]
print("Special menu for our little friends: " + str(three_cheapest) + ".\n")
