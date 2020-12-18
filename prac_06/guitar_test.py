from prac_06.Guitar import Guitar

def main():
    gibson=Guitar("Gibson L-5 CES", 1922, 16035.40)
    another_guitar=Guitar("Another Guitar", 2013)

    print("{}, age:{}, is vintage:{}".format(gibson.name, gibson.get_age(), gibson.is_vintage()))
    print("{}, age:{}, is vintage:{}".format(another_guitar.name, another_guitar.get_age(), another_guitar.is_vintage()))

if __name__ == '__main__':
    main()