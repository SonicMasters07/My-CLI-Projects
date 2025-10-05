class Books:
    storage = {}
    def __init__(self,title,author,id_number,publication_year,availability):
        self.title = title
        self.author = author
        self.id_number = id_number
        self.publication = publication_year
        self.availability = availability
    
    def add_books(self):
        Books.storage[self.title] = [self.author, self.id_number, self.publication, self.availability]
        print("Book has been added")
    
    def library_view(self):
        for books,details in Books.storage.items():
            print(f"""Book's name is: {books}
Author name is {details[0]}
ID Number is {details[1]}
Publication is {details[2]}
Availability is {details[3]}
----------------------------""")
            
    def remove_book(self,book_name):
        if book_name in Books.storage:
            if Books.storage[book_name][3] is True:
                del Books.storage[book_name]
                print("Book was removed")
            else:
                print("Book is currently borrowed")
        else:
            print("There is no such book in Library ")

    def search_book(self,book_name):
        if book_name in Books.storage:
            details = Books.storage[book_name]
            print(f"""Book's name is: {book_name}
Author name is {details[0]}
ID Number is {details[1]}
Publication is {details[2]}
Availability is {details[3]}""")
        else:
            print("There is no such book in Library")

    def check_status(self, book_name):
        if book_name in Books.storage:
            if Books.storage[book_name][3] is True:
                print("Book is available")
            else:
                print("Book is borrowed")
        else:
            print("Book is not available")

class Members:
    database = {}
    def __init__(self,name,id_number,email,borrowed_books):
        self.name = name
        self.id_number = id_number
        self.email_address = email
        self.borrowed_books = borrowed_books
    
    def add_new_member(self,access):
        if access is True:
            Members.database[self.name] = [self.id_number, self.email_address, []]
            print("New Member was added")
        else:
            print("You don't have access")

    def remove_members(self,member_name,access):
        if access is True:
            if member_name in Members.database:
                try:
                    del Members.database[member_name]
                    print("Member has been removed")
                except:
                    print("Member not in database")
            else:
                print("Member not in database")    
        else:
            print("You don't have access") 
           
class Relation():
    List_of_Borrowed_books = []
    def __init__(self):
        pass

    def return_book(self,member_name,book_name):
        if member_name in Members.database:
            if book_name in Books.storage:
                if Books.storage[book_name][3] is False:
                    if book_name in Members.database[member_name][2]:
                        Members.database[member_name][2].remove(book_name)
                        Books.storage[book_name][3] = True
                        Relation.List_of_Borrowed_books.remove(book_name)
                        print("Book has been returned")
                    else:
                        print(f"Not borrowed by this {member_name}")
                else:
                    print("Book is not borrowed")
            else:
                print("Book is not in library")
        else:
            print("Member does not exist")

    def add_borrowed_book(self,book_name,member_name):
        if member_name in Members.database:
            if book_name in Books.storage:
                if Books.storage[book_name][3] is True:
                    Relation.List_of_Borrowed_books.append(book_name)
                    Members.database[member_name][2].append(book_name)
                    Books.storage[book_name][3] = False
                    print("Book has been Borrowed")
                else:
                    print("Book is already borrowed")
            else:
                print("Book is not in library")
        else:
            print("Member does not exist")

    def view_borrowed_books(self):
        print(f"{Relation.List_of_Borrowed_books} ")
    
    def all_members_details(self):
        for members,details in Members.database.items():
            print(f"""Member's name is: {members}
ID Number is {details[0]}
Email_Address is {details[1]}
Borrowed Books are {details[2]}
-------------------------------""")
          