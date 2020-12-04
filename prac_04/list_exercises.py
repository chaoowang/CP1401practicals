def main():
    numbers = []
    for i in range(5):
        numbers.append(int(input("Numbers:")))
    print("The first number is {}".format(numbers[0]))
    print("The last number is {}".format(numbers[-1]))
    print("The smallest number is {}".format(min(numbers)))
    print("The largest number is {}".format(max(numbers)))
    print("average of the numbers is {}".format(sum(numbers) / len(numbers)))

    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']
    your_name = input("Enter your name:")
    if your_name in usernames:
        print("Access granted")
    else:
        print("Access denied")


if __name__ == '__main__':
    main()
