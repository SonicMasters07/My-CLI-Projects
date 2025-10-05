import os

def interface(Info):
    loop = True
    update = False
    os.system("cls")
    while loop:
        print("""
1. Add Contact
2. View Contacts
3. Search Contact
4. Delete Contact
5. Exit
          """)
        keys = input("Choose option by pressing its number: ")

        if keys == "1":
            name = input("Enter your name: ").upper()
            phone = input("Enter your phone number: ")
            email = input("Enter GMAIL: ")
            address = input("Enter Address: ")
            Info[name] = [phone, email, address]
            input("Successfully Added Contact...")
            os.system("cls")

        elif keys == "2":
            for person, details in Info.items():
                print(f"{person} - Phone: {details[0]}, Email: {details[1]}, Address: {details[2]}")
            input("Press Enter to continue...")
            os.system("cls")


        elif keys == "3":
            search = input("Enter a Contact you want to search: ").upper()
            if search in Info:
                details = Info[search]
                print(f"info of {search} - Phone: {details[0]}, Email: {details[1]}, Address: {details[2]}")
                input("Press Enter to continue...")
                os.system("cls")

            else:
                input("Not Available...")
                os.system("cls")

        elif keys == "4":
            remove = input("Which contact you want to remove: ").upper()
            if remove in Info:
                Info.pop(remove)
                input("Successfully Removed Contact...")
                os.system("cls")
            else:
                input("Contact does not exist...")
                os.system("cls")

        elif keys == "5":
            break

        else:
            print("Enter a valid option")
            input("Press Enter to continue...")
            os.system("cls")


def main():
    Info = {"HUSSNAIN": [3115555055, "hasnain@gmail.com", "Samundri"]}
    interface(Info)

main()
