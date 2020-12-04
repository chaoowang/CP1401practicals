import random

NUMBERS_PER_LINE=6
MAX_NUMBER=45
MIN_NUMBER=1

def main():
    number_generate=int(input("How many quick picks?"))
    for i in range(number_generate):
        quick_pick=[]
        for j in range(NUMBERS_PER_LINE):
            number=random.randint(MIN_NUMBER,MAX_NUMBER)
            while number in quick_pick:
                number=random.randint(MIN_NUMBER,MAX_NUMBER)
            quick_pick.append(number)
        quick_pick.sort()
        print(quick_pick)





if __name__ == '__main__':
    main()