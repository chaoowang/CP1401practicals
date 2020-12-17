def main():
    email_to_name={}
    email=input("Email:")
    while email!="":
        email_name=email.split("@")[0]
        name=email_name.split(".")
        full_name=" ".join(name).title()
        confirmation=input("Is your name {}? (Y/N)".format(full_name)).upper()
        while confirmation!="N" and confirmation!="Y":
            confirmation=input("Is your name {}? (Y/N)".format(full_name)).upper()
        if confirmation=="N":
            full_name=input("Name:")
        else:
            pass
        email_to_name[email]=full_name
        email=input("Email:")

    for email, full_name in email_to_name.items():
        print("{} ({})".format(full_name,email))







if __name__ == '__main__':
    main()