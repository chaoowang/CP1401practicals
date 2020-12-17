def main():
    COLOR_TO_CODE = {"aliceblue": "f0f8ff", "antiquewhite": "faebd7", "beige": "f5f5dc", "brown": "a52a2a",
                     "cadetblue": "5f9ea0", "burlywood": "#deb887", "burlywood1": "ffd39b", "burlywood2": "eec591",
                     "burlywood3": "cdaa7d", "burlywood4": "8b7355"}
    color = input("Enter the color name:").lower()
    while color != "":
        if color in COLOR_TO_CODE:
            print("#{}".format(COLOR_TO_CODE[color]))
        else:
            print("Invalid color name")
        color = input("Enter the color name:").lower()


if __name__ == '__main__':
    main()
