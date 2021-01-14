from prac_08.unreliable_car import Unreliable_car


def main():
    unreliable_car = Unreliable_car("car", 100, 23.5)
    unreliable_car.drive(20)
    print(unreliable_car)


if __name__ == '__main__':
    main()
