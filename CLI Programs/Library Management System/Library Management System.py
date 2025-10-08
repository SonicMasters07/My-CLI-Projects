import os
import json
import sys
from Classes import Books, Members, Relation

def library_menu():
    loop = True
    temp = Books("1", "2", "3", "3", "4")
    while loop:
        print("""1. Add Books
2. Check Library Catalogue
3. Remove a Book
4. Book Search
5. Check Status of Book
6.Exit""")
        key2 = input("Select an option to proceed: ")
        os.system("cls")
        if key2 == "1":
            title = input("Enter the book title: ")
            author = input("Enter the author name: ")
            id_number = input("Enter the ID number: ")
            publication_year = input("Enter the publication year: ")
            temp = Books(title, author, id_number, publication_year, True)
            temp.add_books()
            input("Press Enter to Continue...")
            os.system("cls")
        
        elif key2 == "2":
            temp.library_view()
            input("Press Enter to Continue...")
            os.system("cls")

        elif key2 == "3":
            book_name = input("Enter the Books name: ")
            temp.remove_book(book_name)
            input("Press Enter to Continue...")
            os.system("cls")

        elif key2 == "4":
            book_name = input("Enter the Books name: ")
            temp.search_book(book_name)
            input("Press Enter to Continue...")
            os.system("cls")

        elif key2 == "5":
            book_name = input("Enter the Books name: ")
            temp.check_status(book_name)
            input("Press Enter to Continue...")
            os.system("cls")

        elif key2 == "6":
            os.system("cls")
            break
            
        else:
            print("Choose a Valid Option")
            input("Press Enter to Continue...")
            os.system("cls")

def staff_menu():
    loop = True
    attempt = 0
    access = False
    status = ""
    temp = Members("1", "2", "3", "")
    while loop:
        password = input("Enter Admin Access key: ")
        attempt +=1
        if password == "ABCD":
            access = True
            status = "Admin"
            os.system("cls")
            break
        elif attempt >= 4:
            status = "User"
            os.system("cls")
            break
    while loop:
        print(f"""
Your Status is {status}
1. Add a New Member
2. Remove a Member
3. All Member Details
4. Retry Password
5. Exit """)
        key3 = input("Select an option to proceed: ")
        os.system("cls")
        if key3 == "1":
            name = input("Enter the name of New Member: ")
            id_number = input("Enter the ID Number: ")
            email_address = input("Enter the Email Address: ")
            temp = Members(name, id_number, email_address, "")
            temp.add_new_member(access)
            input("Press Enter to Continue...")
            os.system("cls")
        
        elif key3 == "2":
            member_name = input("Enter the Member you want to remove: ")
            temp.remove_members(member_name,access)
            input("Press Enter to Continue...")
            os.system("cls")

        elif key3 == "3":
            temp = Relation()
            temp.all_members_details()
            input("Press Enter to Continue...")
            os.system("cls")
        
        elif key3 == "4":
            os.system("cls")
            staff_menu()

        elif key3 == "5":
            os.system("cls")
            break
        
        else:
            print("Choose a Valid Option")
            input("Press Enter to Continue...")
            os.system("cls")

def member_menu():
    loop = True
    relation = Relation()
    while loop:
        print("""1. Borrow the Book
2. Return the Book
3. View all Borrowed Books
4. Exit""")
        key4 = input("Select an option to proceed: ")
        if key4 == "1":
            temp = Books("1", "2", "3", "3", "4")
            os.system("cls")
            temp.library_view()
            print("---------------------------------")
            book_name = input("What Book you want to borrow: ")
            member_name = input("Confirm your name: ")
            relation.add_borrowed_book(book_name,member_name)
            input("Press Enter to Continue...")
            os.system("cls")

        elif key4 == "2":
            temp = Books("1", "2", "3", "3", "4")
            os.system("cls")
            temp.library_view()
            print("---------------------------------")
            book_name = input("What Book you want to return: ")
            member_name = input("Confirm your name: ")
            relation.return_book(member_name,book_name)
            input("Press Enter to Continue...")
            os.system("cls")

        elif key4 == "3":
            os.system("cls")
            relation.view_borrowed_books()
            input("Press Enter to Continue...")
            os.system("cls")

        elif key4 == "4":
            os.system("cls")
            break

        else:
            print("Choose a Valid Option")
            input("Press Enter to Continue...")
            os.system("cls")

def menu():
    loop = True
    while loop :
        print("""1. Library Menu
2. Staff Menu
3. Member Menu
4.Exit""")
        key1 = input("Which menu will you like to access: ")
        os.system("cls")
        if key1 == "1":
            library_menu()
        elif key1 == "2":
            staff_menu()
        elif key1 == "3":
            member_menu()
        elif key1 == "4":
            finaliza()
        else:
            print("Choose a valid option")
            os.system("cls")

def finaliza():
    with open("Library.json", 'w') as L:
        json.dump(Books.storage, L, indent = 4)

    with open("Database.json", 'w') as L:
        json.dump(Members.database, L, indent = 4)

    with open("Transactions.json", 'w') as L:
        json.dump(Relation.List_of_Borrowed_books, L, indent = 4)
    
    print("All data has been saved")
    confirm = input("Would like to check the whole database (y)or(n): ")
    if confirm == "y":
        with open("Library.json", 'r') as L:
            InformationA = json.load(L)
            print(InformationA)
        with open("Database.json", 'r') as L:
            InformationB = json.load(L)
            print(InformationB)
        with open("Transactions.json", 'r') as L:
            InformationC = json.load(L)
            print(InformationC)
    else:
        print("You have Loged out!")
    sys.exit()

def main():
    try:
        with open("Library.json", 'r') as L:
            Books.storage = json.load(L)
        with open("Database.json", 'r') as L:
            Members.database = json.load(L)
        with open("Transactions.json", 'r') as L:
            Relation.List_of_Borrowed_books = json.load(L)
    except:
        print("Some files are missing")
        input("Press Enter to Continue...")

    os.system("cls")
    menu()


main()