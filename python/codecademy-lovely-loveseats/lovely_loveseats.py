#The lovely loveseat store 

#Receipt information
storeName = 'Lovely loveseats'
from datetime import date
fdate = date.today().strftime('%d/%m/%Y')
cashierName = 'Røskva Bjørgfinsdóttir'
headerReceipt = storeName + '\n' + 'Date of purchase: ' + str(fdate) + '\n' + 'Your cashier: ' + cashierName + '\n\n'

#List of items
lovely_loveseat_description = 'Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white.'
stylish_settee_description = 'Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black.'
luxurious_lamp_description = 'Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade.'

#Price list
lovely_loveseat_price = 254.00
stylish_settee_price = 180.50
luxurious_lamp_price = 52.15

#Sales tax
sales_tax = 0.088

#Purchases
customer_one_total = 0 

#Items for the first customer
customer_one_itemization = lovely_loveseat_description + "\n\n" + luxurious_lamp_description

#First customer prices
customer_one_total += lovely_loveseat_price
customer_one_total += luxurious_lamp_price
#Added tax
customer_one_tax = customer_one_total * sales_tax
customer_one_total += customer_one_tax

#Printed receipt
print(headerReceipt)
print('Items: \n\n' + customer_one_itemization)
print('\nYour total will be $' + str(round(customer_one_total, 2)) + ". Thank you for your purchase.")
