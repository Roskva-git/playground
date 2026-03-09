hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

#1 making a variable for the summed haircut prices
total_price = 0

#2 Looping through the prices and adding them to the total
for price in prices:
  total_price += price

#3 Creating the average price variable
average_price = total_price/len(prices)

#4 Printing the output of average prices
print("Average Haircut Price: \n" + str(average_price))

#5 Making a list comprehension to reduce all prices by $5
new_prices = [price - 5 for price in prices]

#6 Printing new prices
print(new_prices)

##Revenue##
#7 We want to find out the total revenue for last week. First step is creating a variable
total_revenue = 0

#8 & 9 Creating a for-loop
for index in range(len(hairstyles)):
  total_revenue += prices[index]

#10 Printing total revenue
print("Total revenue: \n" + str(total_revenue))

#11 Finding average daily revenue
average_daily_revenue = total_revenue/7
print(average_daily_revenue)

#12 Finding haircuts under $30
cuts_under_30 = [hairstyles[i] for i in range(len(hairstyles)) if new_prices[i] < 30]

#13 Printing cuts under $30
print(cuts_under_30)


