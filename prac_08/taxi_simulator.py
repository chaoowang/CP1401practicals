from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    current_taxi = None
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    total_bill = 0

    print("Let' drive!")
    print(MENU)

    user_choose = input("").lower()
    while user_choose != "q":

        if user_choose == "c":
            print("Taxi available:")
            for i, taxi in enumerate(taxis):
                print("{} - {}".format(i, taxi))
            taxi_choose = int(input("Choose taxi:"))
            current_taxi = taxis[taxi_choose]

        elif user_choose == "d":
            distance_driven = float(input("Drive how far?"))
            current_taxi.start_fare()
            current_taxi.drive(distance_driven)
            trip_fare = current_taxi.get_fare()
            print("Your {} trip cost you ${}".format(current_taxi.name, trip_fare))
            total_bill += trip_fare

        print("Bill to date: {}".format(total_bill))
        print(MENU)
        user_choose = input("").lower()

    print("Total trip cost:{}".format(total_bill))
    print("Taxis are now:")
    for i, taxi in enumerate(taxis):
        print("{} - {}".format(i, taxi))

if __name__ == '__main__':
    main()
