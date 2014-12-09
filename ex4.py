# Sets the value for the number of cars 
cars = 100.0

# Sets the value for the number of spaces in each car
space_in_car = 4.0

# Sets the value for the number of drivers
drivers = 30.0

# Sets the value for the number of passengers
passengers = 90.0

# Subtracts the number of drivers from the number of cars to get the value for the number of cars not driven
cars_not_driven = cars - drivers

# Sets the value for the number of cars driven equal to the number of drivers
cars_driven = drivers

# Multiplies the value for the number of cars driven by the value for the number of spaces in each car to get the value for carpool capacity
carpool_capacity = cars_driven * space_in_car

# Divides the value for the number of passengers by the value for the number of cars driven
average_passengers_per_car = passengers / cars_driven

# Replaces "cars" with previously defined value
# Displays text "There are (#) cars available"
print "There are", cars, "cars available."

# Replaces "drivers" with previously defined value
# Displays text "There are only (#) drivers available."
print "There are only", drivers, "drivers available."

# Subtracts the number of drivers from the number of cars to get value for cars_not_driven
# Replaces "cars_not_driven" with that value
# Displays text "There will be (#) cars empty today."
print "There will be", cars_not_driven, "empty cars today."

# Multiplies the number of cars driven (drivers) by the amount of space in each car to get value for carpool_capacity
# Replaces "carpool_capacity" with that value
# Displays text "We can transport (#) people today."
print "We can transport", carpool_capacity, "people today."

# Divides the number of passengers by the number of cars driven (drivers) to get value for average_passengers_per_car
# Replaces average_passengers_per_car with that value
# Displays text "We need to put about (#) in each car."
print "We need to put about", average_passengers_per_car, "in each car."

# Study Drills

# When I wrote this program the first time I had a mistake, and Python told me about it like this:

# Traceback (most recent call last):
#   File "ex4.py", line 8, in <module>
#     average_passengers_per_car = car_pool_capacity / passenger
# NameError: name 'car_pool_capacity' is not defined

# Explain this error in your own words. Make sure you use line numbers and explain why.

# To calculate average_passengers_per_car (line 8), you need to divide the number of passengers by the number of cars driven:
	# average_passengers_per_car = passengers / cars_driven
	# Also,'passenger' is not a variable