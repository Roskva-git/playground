#Sal's shipping 
#This program calculates the cheapest shipping price available.

#Price list 
#Ground shipping
#Weight 	Price/pound 	Flat Charge
#class 1 <=2 lb         $1.50 	$20.00
#class 2 >2 lb <=6 lb 	$3.00 	$20.00
#class 3 >6 lb <= 10lb 	$4.00 	$20.00
#class 4 >10 lb 	      $4.75 	$20.00
#class 5 flat charge $20
#class 6 (Ground shipping premium) $125 flat charge
ground_class_1 = 1.50
ground_class_2 = 3.00
ground_class_3 = 4.00
ground_class_4 = 4.75
ground_flat_charge = 20
ground_premium_charge = 125

#Enter weight
weight = 41.5


#Here come the ground calculations
if weight <= 2:
  print("The ground shipping cost for your package is $" + str(ground_class_1*weight+ground_flat_charge) + ".")
elif weight >2 and weight <=6:
  print("The ground shipping cost for your package is $" + str(ground_class_2*weight+ground_flat_charge) + ".")
elif weight >6 and weight <=10:
  print("The ground shipping cost for your package is $" + str(ground_class_3*weight+ground_flat_charge) + ".")
elif weight >=10 and weight <=22:
  print("The ground shipping cost for your package is $" + str(ground_class_4*weight+ground_flat_charge) + ".")
else:
  print("We recommend using the Ground Shipping Premium flat-rate package for $" + str(ground_premium_charge))

#Drone shipping
#Weight 	Price/pound 	Flat Charge
#class 1 <= 2lbs       	$4.50 	$0.00
#class 2 >2 lb <=6 lb 	$9.00 	$0.00
#class 3 >6 lb <= 10lb 	$12.00 	$0.00
#class 4 >10 lb       	$14.25 	$0.00
drone_class_1 = 4.50
drone_class_2 = 9.00
drone_class_3 = 12.00
drone_class_4 = 14.25
drone_flat_charge = 0.00

#Drone calculations
if weight <= 2:
  print("The drone shipping cost for your package is $" + str(drone_class_1*weight+drone_flat_charge) + ".")
elif weight >2 and weight <=6:
  print("The drone shipping cost for your package is $" + str(drone_class_2*weight+drone_flat_charge) + ".")
elif weight >6 and weight <=10:
  print("The drone shipping cost for your package is $" + str(drone_class_3*weight+drone_flat_charge) + ".")
elif weight >=10:
  print("The drone shipping cost for your package is $" + str(drone_class_4*weight+drone_flat_charge) + ".")
