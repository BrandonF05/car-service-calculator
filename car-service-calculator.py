car_mileage = int(input("Enter current car mileage: "))
last_service = int(input("Enter mileage at last service: "))

miles_since_service = car_mileage - last_service 
miles_until_next_service = 10000 - miles_since_service

print ("Miles driven since last service:" , miles_since_service)
print ("miles until next service:" , miles_until_next_service)

if miles_until_next_service <=0:
    print ("Your car is overdue for a service!")
else:
    print ("you are not overdue yet.")