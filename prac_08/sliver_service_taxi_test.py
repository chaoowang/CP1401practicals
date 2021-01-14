from prac_08.sliver_service_taxi import SliverServiceTaxi

def main():

    test_car=SliverServiceTaxi("fancy car",20,2)
    test_car.drive(18)
    print(test_car)

if __name__ == '__main__':
    main()