def main():
    num_of_items = int(input("Number of items:"))
    while num_of_items <= 0:
        print("Invalid number of item!")
        num_of_items = int(input("Numer of item:"))
    total_price = 0
    for i in range(num_of_items):
        total_price += float(input("Price of item:"))
    if total_price > 100:
        total_price *= 0.9
    print("Total price for {} is ${:.2f}".format(num_of_items, total_price))


if __name__ == '__main__':
    main()
