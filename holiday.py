#Using input() to ask the user to choose the city they want to vist and the number of night's stay.
city_flight = input("To where? Constantinopla, Budapest or Praga : ")
num_nights = int(input("Number of nights: "))

#Defining a function with conditional statement to take the user input num_nights as an argument and return the total hotel cost based on the city_flight chosen by the user.
def hotel_cost(num_nights):

    if city_flight == ('Constantinopla'):
        total_hotel_cost = num_nights * 250

    if city_flight == ('Budapest'):
        total_hotel_cost = num_nights * 300

    if city_flight == ('Praga'):
        total_hotel_cost = num_nights * 400
        
    print (total_hotel_cost)
    return(total_hotel_cost)
    
total_hotel_cost = hotel_cost(num_nights)

#Defining a function with conditional statement to take the input city_flight as an argument and return the cost of flight based on the city_flight chosen by the user.
def plane_cost(city_flight):

    if city_flight == ('Constantinopla'):
        flight_cost = 125
        print(flight_cost)
        return(flight_cost)
    
    if city_flight == ('Budapest'):
        flight_cost = 150
        print(flight_cost)
        return(flight_cost)

    if city_flight == ('Praga'):
        flight_cost = 200
        print(flight_cost)
        return(flight_cost)

flight_cost = plane_cost(city_flight)


#Defining a function to take the input rental_days as an argument and return the total cost of the car rental based on the rental_days input by the user.
rental_days = int(input("Days of Car Rental: "))

def car_rental(rental_days):

    car_cost = rental_days * 50
    print(car_cost)
    return(car_cost)

car_cost = car_rental(rental_days)


#Defining a function to call the above three functions (hotel_cost, plane_cost, car_rental) with their respective arguments and return a total cost of the holiday.
def holiday_cost(hotel_cost, plane_cost, car_rental):
    return hotel_cost + plane_cost + car_rental
total_holiday = total_hotel_cost + flight_cost + car_cost

#Using print() to print out all the details about the holiday in a readable way.
print(f'Your trip to {city_flight} will have a total cost of £ {total_holiday}.')
print(f'The total cost includes a {num_nights} nights hotel stay for £{total_hotel_cost}, flight cost of £{flight_cost} and {rental_days} days car rent for £{car_cost}.')


