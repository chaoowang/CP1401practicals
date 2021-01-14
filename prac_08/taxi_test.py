from prac_08.taxi import Taxi


def main():
    new_taxi = Taxi("Prius 1", 100)
    new_taxi.drive(40)
    print(new_taxi)
    current_fare = new_taxi.get_fare()
    print("current fare: {}".format(current_fare))
    new_taxi.start_fare()
    new_taxi.drive(100)
    print(new_taxi)
    current_fare = new_taxi.get_fare()
    print("current fare: {}".format(current_fare))


if __name__ == '__main__':
    main()
