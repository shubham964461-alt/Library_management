from datetime import date 
 
# --------------------------- 
# Base Class: Person 
# --------------------------- 
class Person: 
    def __init__(self, name, phone): 
        self.name = name 
        self.phone = phone 
 
    def show_info(self): 
        print(f"Name: {self.name} | Phone: {self.phone}") 
 
 
# --------------------------- 
# Derived Class: Member 
# --------------------------- 
class Member(Person): 
    def __init__(self, member_id, name, phone): 
        super().__init__(name, phone) 
        self.member_id = member_id 
 
    def show_info(self): 
        print(f"[Member] ID: {self.member_id} | Name: {self.name} | Phone: {self.phone}") 
 
 
# --------------------------- 
# Book Class 
# --------------------------- 
class Book: 
    def __init__(self, book_id, title, author, quantity): 
        self.book_id = book_id 
        self.title = title 
        self.author = author 
        self.quantity = quantity 
 
    def show_info(self): 
        print(f"[Book] ID: {self.book_id} | {self.title} by {self.author} | Qty: {self.quantity}") 
 
 
# --------------------------- 
# Library Class (Main) 
# --------------------------- 
class Library: 
    def __init__(self): 
        self.__books = []      # private list of books 
        self.__members = []    # private list of members 
        self.__issued_books = []  # issued record 
 
    # --- Book Operations --- 
    def add_book(self, book): 
        self.__books.append(book) 
        print("Book added successfully!") 
 
    def view_books(self): 
        if not self.__books: 
            print("No books available.") 
        else: 
            print("\nAll Books:") 
            for book in self.__books: 
                book.show_info() 
 
    # --- Member Operations --- 
    def add_member(self, member): 
        self.__members.append(member) 
        print("Member added successfully!") 
 
    def view_members(self): 
        if not self.__members: 
            print("No members registered.") 
        else: 
            print("\nLibrary Members:") 
            for member in self.__members: 
                member.show_info() 
 
    # --- Issue & Return Books --- 
    def issue_book(self, book_id, member_id): 
        book = next((b for b in self.__books if b.book_id == book_id), None) 
        member = next((m for m in self.__members if m.member_id == member_id), None) 
 
        if not book or not member: 
            print("Invalid Book ID or Member ID.") 
            return 
 
        if book.quantity > 0: 
            book.quantity -= 1 
            self.__issued_books.append({"book": book, "member": member, "issue_date": 
date.today()}) 
            print(f"Book '{book.title}' issued to {member.name} on {date.today()}") 
        else: 
            print("Book not available!") 
 
    def return_book(self, book_id, member_id): 
        for record in self.__issued_books: 
            if record["book"].book_id == book_id and record["member"].member_id == member_id: 
                record["book"].quantity += 1 
                self.__issued_books.remove(record) 
                print(f"Book '{record['book'].title}' returned by {record['member'].name}") 
                return 
        print("No record found for return.") 
 
    def view_issued_books(self): 
        if not self.__issued_books: 
            print("No books issued yet.") 
        else: 
            print("\nIssued Books:") 
            for record in self.__issued_books: 
                print(f"{record['book'].title} -> {record['member'].name} | Issued on {record['issue_date']}") 
 
 
# --------------------------- 
# Main Function 
# --------------------------- 
def main(): 
    lib = Library() 
 
    while True: 
        print(""" 
======= LIBRARY MANAGEMENT SYSTEM (OOP) ======= 
1. Add Book 
2. View Books 
3. Add Member 
4. View Members 
5. Issue Book 
6. Return Book 
7. View Issued Books 
8. Exit 
""") 
        choice = input("Enter your choice: ") 
 
        if choice == '1': 
            book_id = int(input("Book ID: ")) 
            title = input("Title: ") 
            author = input("Author: ") 
            qty = int(input("Quantity: ")) 
            lib.add_book(Book(book_id, title, author, qty)) 
 
        elif choice == '2': 
            lib.view_books() 
 
        elif choice == '3': 
            member_id = int(input("Member ID: ")) 
            name = input("Name: ") 
            phone = input("Phone: ") 
            lib.add_member(Member(member_id, name, phone)) 
 
        elif choice == '4': 
            lib.view_members() 
 
        elif choice == '5': 
            book_id = int(input("Enter Book ID: ")) 
            member_id = int(input("Enter Member ID: ")) 
            lib.issue_book(book_id, member_id) 
 
        elif choice == '6': 
            book_id = int(input("Enter Book ID: ")) 
            member_id = int(input("Enter Member ID: ")) 
            lib.return_book(book_id, member_id) 
 
        elif choice == '7': 
            lib.view_issued_books() 
 
        elif choice == '8': 
            print("Exiting... Thank you!") 
            break 
 
        else: 
            print("Invalid choice, please try again.") 
 
 
# Run the program 
if __name__ == "__main__": 
    main()