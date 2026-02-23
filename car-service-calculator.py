def calculate_service (car_mileage, last_service):
    miles_since_service = car_mileage - last_service
    miles_until_next_service = 10000 - miles_since_service
    return miles_since_service, miles_until_next_service

def display_message (miles_until_next_service):
    if miles_until_next_service <= 0:
        print (f"Your car is over due for a service by {-miles_until_next_service} miles")
    elif miles_until_next_service <=1000:
        print (f"Your car is due for a service in {miles_until_next_service} miles")
    else:
        print (f"you have {miles_until_next_service} miles until your next service")

import json

def save_cars (cars):
    with open ("cars.json", "w") as file:
        json.dump(cars, file)

def load_cars ():
    try:
        with open ("cars.json","r") as file:
            content = file.read().strip()
            if not content:
                return[]
            return json.loads(content)
    except (FileNotFoundError, json.JSONDecodeError):
        return[]

def list_cars(cars):
    if not cars:
        print("No cars saved yet.")
        return
    
    for index, car in enumerate(cars):
        print(f"{index + 1}. {car['reg']}")

def main():

    cars = load_cars()

    while True:
        print ("\n Car Service Calculator")
        print ("1. Check service status")
        print ("2. Add car")
        print ("3. Exit")

        choice = input("Choose an option (1, 2 or 3):")

        if choice == "1":
            if not cars:
                print ("No cars available. Add one first!")
                continue

            list_cars(cars)

            try:
                selection = int(input("Select a car buy its number:")) - 1
                selected_car = cars[selection]

            except (ValueError, IndexError):
                print("Invaled selection.")
                continue
            
            miles_since_service, miles_until_next_service = calculate_service(
                selected_car["current_mileage"],
                selected_car["last_service"]
            )

            print(f"\nCar: {selected_car['reg']}")
            print ("Miles driven since last service:", miles_since_service)
            print ("Miles until next service:", miles_until_next_service)

            display_message (miles_until_next_service)
        
        elif choice == "2" :
            reg = input("Enter your cars registration:")

            try:
                mileage = int(input("Enter your current cars mileage:"))
                last_service = int(input("Enter your cars mileage at last service:"))
            except ValueError:
                print("Please enter numbers only.")
                continue

            car = {
                "reg" : reg,
                "current_mileage" : mileage,
                "last_service": last_service
            }

            cars.append(car)
            save_cars(cars)

            print ("Car added successfully.")


        elif choice == "3" :
            print ("Goodbye!")
            break
        
        else:
            print ("Invalid option. Try again")


main()

{
    "reg": "AB12 CDE",
    "current_mileage": 100000,
    "last service": 99500
}

cars = []
