from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    test_car = SilverServiceTaxi("fancy car", 20, 2)
    test_car.drive(18)
    print(test_car)
    current_fare = test_car.get_fare()
    print("current fare: ${}".format(current_fare))


if __name__ == '__main__':
    main()
