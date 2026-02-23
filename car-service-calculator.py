def calculate_service (car_mileage, last_service):
    miles_since_service = car_mileage - last_service
    miles_until_next_service = 10000 - miles_since_service
    return miles_since_service, miles_until_next_service

def display_message (miles_until_next_service):
    if miles_until_next_service <= 0:
        print (f"Your car is over due for a service by {-miles_until_next_service} miles")
        return True
    
    elif miles_until_next_service <=1000:
        print (f"Your car is due for a service in {miles_until_next_service} miles")
        return False
    else:
        print (f"you have {miles_until_next_service} miles until your next service")
        return False

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
        print ("3. Update a cars mileage")
        print ("4. Delete a car")
        print ("5. Exit")

        choice = input("Choose an option (1, 2, 3, 4 or 5):")

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

            overdue = display_message (miles_until_next_service)

            if overdue:
                confirm = input ("Has a service been completed? (y/n)")

                if confirm.strip().lower() == "y":
                    selected_car["last_service"]=selected_car["current_mileage"]
                    save_cars(cars) 
                    print("service recorded and saved.")
        
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

        elif choice == "3":
            if not cars:
                print("No cars avalable.")
                continue

            list_cars(cars)

            try:
                selection = int(input("Select a car by its number:")) - 1
                new_mileage = int(input("enter the new curent milage"))
            except ValueError:
                print("Please enter numbers only.")
                continue
            except IndexError:
                print ("Invalid selection")
                continue

            cars[selection]["current_mileage"]=new_mileage
            save_cars(cars)

            print("Mileage updated successfully.")

        elif choice == "4":
            if not cars:
                print("No cars to delete.")
                continue

            list_cars(cars)

            try:
                selection = int(input("Select a car to delete:")) - 1
                car = cars[selection]
            except (ValueError, IndexError):
                print("Invalid selection.")
                continue

            confirm = input(f"Are you sure you want to delete {car['reg']}? (y/n):")

            if confirm.strip().lower() == "y":
                cars.pop(selection)
                save_cars(cars)
                print("The car has been deleted")
            else:
                print("Deletion cancelled")

        elif choice == "5" :
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
