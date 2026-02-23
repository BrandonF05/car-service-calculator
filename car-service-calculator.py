car_mileage = int(input("Enter current car mileage: "))
last_service = int(input("Enter mileage at last service: "))

miles_since_service = car_mileage - last_service 
miles_until_next_service = 10000 - miles_since_service
amiles_until_next_service = miles_until_next_service*-1

print ("Miles driven since last service:" , miles_since_service)
print ("miles until next service:" , miles_until_next_service)

if miles_until_next_service <= 0:
    print (f"Your car is {amiles_until_next_service} overdue for a service!")
elif miles_until_next_service <= 1000:
    print (f"Your service is due soon. only {miles_until_next_service} remaining")
else:
    print (f"There is no service due yet. You have {miles_until_next_service} remaining")
