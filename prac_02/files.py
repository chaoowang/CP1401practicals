name = input("Enter your name:")
name_file = open("name.txt", "w")
print(name, file=name_file)
name_file.close()

read_name_file = open("name.txt", "r")
name = read_name_file.read()
print("Your name is", name)

number_file = open("numbers.txt", "w")
print("17\n42\n400", file=number_file)
number_file.close()

number_file = open("numbers.txt", "r")
number1 = int(number_file.readline())
number2 = int(number_file.readline())
number_file.close()
print(number1 + number2)

number_file = open("numbers.txt", "r")
total = 0
for line in number_file:
    total += int(line)
number_file.close()
print(total)
