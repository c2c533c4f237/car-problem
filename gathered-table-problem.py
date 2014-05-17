class Car:

	def __init__(self, manufacturer, model, kind):
		self.manufacturer = manufacturer
		self.model = model
		self.kind = kind
		self.favorite = False

	def __repr__(self):
		return ("Manufacturer: %s, Model: %s, Class: %s" % (self.manufacturer, self.model, self.kind))

cars = []
current_cars = []
car_schedule = []
rev_schedule = []

import csv
from random import randint

with open("cars.csv", "rb") as csvfile:
	reader = csv.reader(csvfile, delimiter=",")
	for row in reader:
		cars.append(Car(row[0].strip(), row[1].strip(), row[2].strip()))

for i, car in enumerate(cars):
	print "#%d " % (i + 1) + str(car)

index = int(raw_input("Hi, here are the cars. Please input favorite car.")) - 1


cars[index].favorite = True
favorite_car = cars[index]
set_fav_car = False
cars.remove(favorite_car)
current_cars.extend(cars)

def randCar():
	rand_index = randint(0, (len(sample_cars) - 1))
	picked_car = sample_cars[rand_index]
	car_schedule.append(picked_car)
	current_cars.remove(picked_car)


for i in range(7 * 6):

	if len(current_cars) == 0:
		current_cars = cars

	if i == 0:
		sample_cars = current_cars

	if i % 7 == 1 and i != 1:
		set_fav_car = False
   
	if i != 0:
		sample_cars = filter(lambda x: x.manufacturer != car_schedule[i-1].manufacturer, current_cars)

	if i % 7 == 6 or i % 7 == 0:
		fast_cars = filter(lambda x: x.kind == "Fast", sample_cars)
		if len(fast_cars) > 0:
			sample_cars = fast_cars
	else:
		offroad_cars = filter(lambda x: x.kind == "Offroad", sample_cars)
		if len(offroad_cars) > 0:
			sample_cars = offroad_cars


	if set_fav_car == False and (i == 0 or car_schedule[i-1].manufacturer != favorite_car.manufacturer):

		if (favorite_car.kind == "Fast" and not(i % 7 == 6) and not(i % 7 == 0)) or (favorite_car.kind == "Offroad" and (i % 7 == 6) or(i % 7 == 0)): 
			randCar()
		else:
			car_schedule.append(favorite_car)
			set_fav_car = True
	else:
		randCar()

print "Here's your car schedule for the next 6 weeks!"
for i, car in enumerate(car_schedule):
	if i % 7 == 0:
		print "---------Week %d---------" % (i/7 + 1)
	print "%s " % ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'][i % 7] + str(car)