# Name: Armeen Farooqui 
# Period: AM - AI Engineering
# Disneyland Trip Calculator

# Introduced the program
print("Welcome to the Disneyland Trip Planner!")
print("Let's plan your Disneyland vacation together.")
print("I'll ask you a few questions and estimate the total cost of your trip.")
print()

# Get basic trip information
name = input ("What is your name?: ")
number_of_people = int(input("How many people are going?: "))
number_of_parkdays = int(input("How many days will you spend at Disneyland?: "))
number_of_nights = int(input("How many nights will you stay at a hotel?: "))
# Calculate ticket cost
park_hopper_price = float(input("What is the Park hopper ticket per person?: "))
total_ticket_cost = park_hopper_price * number_of_people
# Calculate food cost
food_cost_per_person = float(input("How much will one person spend on food?: "))
total_food_cost = food_cost_per_person * number_of_people
# Calculate souvenir cost
souvenir_cost_per_person = float(input("How much will one person spend on souvenirs?: "))
total_souvenir_cost = souvenir_cost_per_person * number_of_people
# Calculate hotel cost
hotel_cost_per_room = float(input("How much does one hotel room cost per night?: "))
number_of_rooms = int(input("How many hotel rooms will your group need?: "))
total_hotel_cost = hotel_cost_per_room * number_of_nights * number_of_rooms
one_way_distance = int(input("How many miles away from Disneyland do you live?: "))
vehicle_mpg = int(input("How many miles per gallon does your vehicle get?: "))
round_trip_distance = one_way_distance * 2 
# Calculate gas cost
gas_price = float(input("What is today's price of regular gas per gallon?: "))
gallons_needed = round_trip_distance/vehicle_mpg
total_gas_cost = gallons_needed * gas_price 
# Calculate parking cost
parking_cost_per_day = float(input("How much does Disneyland parking cost per day?: "))
total_parking_cost = parking_cost_per_day * number_of_parkdays
# Calculate total trip cost
final_trip_cost = total_ticket_cost + total_food_cost + total_souvenir_cost + total_hotel_cost + total_gas_cost + total_parking_cost
cost_per_person = final_trip_cost/number_of_people
cost_per_day = final_trip_cost/number_of_parkdays
# Calculate the budget difference
trip_budget = float(input("How much money does your group have available for the Disneyland trip?: "))
budget_difference = trip_budget - final_trip_cost
print()

#Trip results 
print("--------- DISNEYLAND TRIP REPORT ---------")
print()
# Show traveler information
print("Traveler:", name)
print()
print("People Going:", number_of_people)
print("Disneyland Park Days:", number_of_parkdays)
print("Hotel Nights:", number_of_nights)

print()
print("--------- TICKETS ---------")
# Show ticket information
print()
print("Park Hopper Price Per Person: ", park_hopper_price,)
print("Total Park Hopper Cost: ", total_ticket_cost)


print()
print("--------- FOOD & SOUVENIRS ---------")
print()
# Show food and souvenir costs
print("Total Food Cost: ", total_food_cost)
print("Total Souvenir Cost: ", total_souvenir_cost)

print()
print("--------- HOTEL ---------")
print()
# Show hotel costs
print("Total Hotel Cost: ", total_hotel_cost)

print()
print("--------- DRIVING ---------")
print()
# Show driving and parking information
print("One-Way Driving Distance: ", str(one_way_distance) + "miles")
print("Round-Trip Driving Distance: ", str(round_trip_distance) + "miles")
print("Vehicle MPG: ", vehicle_mpg, )
print("Gas Price: ", gas_price)
print("Gallons of Gas Needed: ", (gallons_needed))
print("Total Gas Cost: ", total_gas_cost)
print("Total Parking Cost: ", total_parking_cost)
print()

print("--------- TRIP TOTAL ---------")
print()
# Show the total trip costs
print("Final Disneyland Trip Cost: ", final_trip_cost)
print("Cost Per Person: ", cost_per_person)
print("Cost Per Park Day: ", number_of_parkdays)

print()
print("--------- BUDGET ---------")
print()
# Show the budget information
print("Trip Budget: ", trip_budget,)
print("Budget Difference: ", budget_difference)

#Goodbye message 
print()
print("Have a magical trip to Disneyland,", name + "!")
print("Thank you for your time!")

