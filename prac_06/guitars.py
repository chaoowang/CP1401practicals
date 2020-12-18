from prac_06.Guitar import Guitar


def main():
    my_guitars = []
    print("My Guitars!")
    name=input("Name:")
    while name != "":
        year = int(input("Year:"))
        cost = float(input("Cost: $"))
        my_guitars.append(Guitar(name, year, cost))
        print("{} ({}) : ${:,.2f} added.\n".format(name,year,cost))
        name = input("Name:")

    print("These are my guitars:")
    index = 1
    for guitar in my_guitars:
        if guitar.is_vintage():
            print("Guitar {}:{} ({}), worth $ {:,.2f} (vintage)".format(index, guitar.name, guitar.year, guitar.cost))
        else:
            print("Guitar {}:{} ({}), worth $ {:,.2f}".format(index, guitar.name, guitar.year, guitar.cost))
        index += 1


if __name__ == '__main__':
    main()
