#Defines functions for calculating the costs related to a holiday.
#Allows the user to input holiday information.
#Calculates the total cost of the holiday.
#Displays a summary of the holiday details if the inputs are valid.

#Steps:

#Define functions: "hotel_cost", "plane_cost", "car_rental", and "holiday_cost".
#Greet the user.
#Prompt the user to input the destination city, number of hotel nights, and car rental days.
#Call the "holiday_cost" function with the inputs.
#Assign the result to "total_holiday_cost".
#If the city input is invalid, print "Invalid input".
#Otherwise, print a summary of the holiday details and the total cost in pounds.


# Define a function hotel_cost which takes in the number of nights as input
def hotel_cost(num_nights):
    # Set the price per night to 50
    price_per_night = 50
    # Calculate the total cost of the hotel as price_per_night multiplied by num_nights
    total_hotel_cost = num_nights * price_per_night 
    return total_hotel_cost

# Define a function plane_cost which takes in the city_flight as input
def plane_cost(city_flight):
    # If the city_flight is 'UK', set flight_cost to 100
    if city_flight == "UK":
        flight_cost = 100 
    # If the city_flight is 'London', set flight_cost to 200
    elif city_flight == "London":
        flight_cost = 200 
    # If the city_flight is 'South Africa', set flight_cost to 300
    elif city_flight == "South Africa":
        flight_cost = 300 
    # If none of these conditions are met, set flight_cost to None
    else:
        flight_cost = None 
    return flight_cost

# Define a function car_rental which takes in rental_days as input
def car_rental(rental_days):
    # Set the daily rental cost of the car to 50
    daily_rental_cost = 50 
    # Calculate the total cost of the car rental as daily_rental_cost multiplied by rental_days
    total_car_rental_cost = rental_days * daily_rental_cost 
    return total_car_rental_cost

# Define a function holiday_cost which takes in num_nights, city_flight and rental_days as input
def holiday_cost(num_nights, city_flight, rental_days):
    # Call the hotel_cost function and pass in num_nights, then assign it to total_hotel_cost
    total_hotel_cost = hotel_cost(num_nights)
    # Call the plane_cost function and pass in city_flight, then assign it to flight_cost
    flight_cost = plane_cost(city_flight)
    # If the user inputs an invalid city_flight, return None
    if flight_cost == None:
        return None 
    # Call the car_rental function and pass in rental_days, then assign it to total_car_rental_cost
    total_car_rental_cost = car_rental(rental_days)
    # Calculate the total cost of holiday as the sum of hotel cost, flight cost, and car rental cost
    total_holiday_cost = total_hotel_cost + flight_cost + total_car_rental_cost 
    return total_holiday_cost

# Print a welcome message
print("Holiday cost calculator.")
# Ask the user for the city they'll be flying to and assign it to city_flight variable
city_flight = input("Enter the city you will be flying to (options: UK, London, South Africa): ")
# Ask the user for the number of nights they'll be staying at hotel and assign it to num_nights variable
num_nights = int(input("Enter the number of nights you will be staying at a hotel: "))
# Ask the user for the number of days they'll be renting a car and assign it to rental_days variable
rental_days = int(input("Enter the number of days that you will be hiring a car for: "))

# Call holiday_cost function with input values and store result in total_holiday_cost variable
total_holiday_cost = holiday_cost(num_nights, city_flight, rental_days)

# Display summary of the holiday details if city_flight input is valid else display "Invalid input"
if total_holiday_cost != None:
    print("\nHere is the summary of your holiday:")
    print("Flying to:", city_flight)
    print("Staying",num_nights,"nights at a hotel.")
    print("Renting a car for",rental_days,"days.")
    print("Total holiday cost is £",total_holiday_cost)
else:
    print("Invalid input")
