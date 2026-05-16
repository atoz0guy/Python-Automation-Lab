# Your code below:
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
prices = [2, 6, 1, 3, 2, 7, 2 ]
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices, end="\n\n")
num_pizzas =len(toppings)
print(num_pizzas, "\n")
print("Well sell ", [num_pizzas], "different kinds of pizza!", end="\n\n")
pizza_and_prices = list(map(list, zip(prices, toppings)))
print(pizza_and_prices, "\n")
pizza_and_prices.sort()
print(pizza_and_prices, end="\n\n")
cheapest_pizza = pizza_and_prices [0]
print(cheapest_pizza, '\n')
priciest_pizza = pizza_and_prices [6]
pizza_and_prices.pop()
print(str(priciest_pizza) + "\n")
three_cheapest = pizza_and_prices[0:3]
print(three_cheapest, '\n')




