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

def main():

    while True:
        print ("\n Car Service Calculator")
        print ("1. Check service status")
        print ("2. Exit")

        choice = input("Choose an option (1 or 2):")

        if choice == "1":
            
            
            car_mileage = int(input("Enter your current cars mileage:"))
            last_service = int(input("Enter your cars mileage at last service:"))
            
            miles_since_service, miles_until_next_service = calculate_service(car_mileage, last_service)

            print ("Miles driven since last service:", miles_since_service)
            print ("Miles until next service:", miles_until_next_service)

            display_message (miles_until_next_service)
        
        elif choice == "2" :
            print ("Goodbye!")
            break
        
        else:
            print ("Invalid option. Try again")


main()