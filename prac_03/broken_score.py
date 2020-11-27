import random


def main():
    score = float(random.randint(1, 100))
    result = score_result(score)
    print(score, result)


def score_result(score):
    if score < 0 or score > 100:
        result = "Invalid score"
    elif score > 90:
        result = "Excellent"
    elif score > 50:
        result = "Passable"
    else:
        result = "Bad"
    return result


if __name__ == '__main__':
    main()
