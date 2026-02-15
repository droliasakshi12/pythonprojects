# A beginner friendly project for calculating rent 

rent_input = int(input("Enter your total  rent:"))
food = int(input("enter amount spent on food:"))
electricity = int(input("enter amount spent on electricity:"))

charge_per_unit = int(input("Enter the charge per unit:"))

no_of_person = int(input("enter the total number of person in the room:"))

total_electricity_charge = electricity*charge_per_unit

output = (rent_input + food + total_electricity_charge)//no_of_person
print("each person will pay: ",output)

-----------------------------------------------------------------------------------
