import datetime 

class Book:
    def __init__(self, title, author, book_id, copies):
        self.title = title
        self.author = author
        self.book_id = book_id
        self.copies = copies

    def __str__(self):
        return f"{self.title} by {self.author}, Copies: {self.copies}"

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"Member ID: {self.member_id}, Name: {self.name}, Borrowed Books: {[book.title for book in self.borrowed_books]}"

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)
        print(f" '{book.title}' added!1.")

    def remove_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                self.books.remove(book)
                print(f" '{book.title}' removed!.")
                return
        print(f"No {book_id}.")

    def view_books(self):
        if not self.books:
            print("No books rn!.")
        else:
            for book in self.books:
                print(book)

    def add_member(self, member):
        self.members.append(member)
        print(f"Member '{member.name}' added, welcoeme.")

    def remove_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                self.members.remove(member)
                print(f"Member '{member.name}' removed, cuz bye!!.")
                return
        print(f"No member found with {member_id}.")

    def view_members(self):
        if not self.members:
            print("No members hehe")
        else:
            for member in self.members:
                print(member)

    def borrow_book(self, member_id, book_id):
        member = next((m for m in self.members if m.member_id == member_id), None)
        if member is None:
            print(f"No member found with {member_id}.")
            return

        book = next((b for b in self.books if b.book_id == book_id), None)
        if book is None:
            print(f"No book found with {book_id}.")
            return

        if book.copies == 0:
            print(f"All of '{book.title}' are borrowed, be early next time smh.")
            return

        member.borrowed_books.append(book)
        book.copies -= 1
        print(f" '{book.title}' borrowed by  '{member.name}'.")

    def return_book(self, member_id, book_id):
        member = next((m for m in self.members if m.member_id == member_id), None)
        if member is None:
            print(f"No member with {member_id}.")
            return

        book = next((b for b in member.borrowed_books if b.book_id == book_id), None)
        if book is None:
            print(f"No book found with {book_id} in member '{member.name}'  list.")
            return

        member.borrowed_boo.title}' returned by '{member.name}'.")

# Helper Functions
def display_menu():
    print("\nLibrary System")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. View Books")
    print("4. Add Member")
    print("5. Remove Member")
    print("6. View Members")
    print("7. Borrow Book")
    print("8. Return Book")
    print("0. Exit")

def main():
    library = Library()
    
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            book_id = input("Enter book ID: ")
            copies = int(input("Enter number of copies: "))
            book = Book(title, author, book_id, copies)
            library.add_book(book)

        elif choice == '2':
            book_id = input("Enter book ID to remove: ")
            library.remove_book(book_id)

        elif choice == '3':
            library.view_books()

        elif choice == '4':
            member_id = input("Enter member ID: ")
            name = input("Enter member name: ")
            member = Member(member_id, name)
            library.add_member(member)

        elif choice == '5':
            member_id = input("Enter member ID to remove: ")
            library.remove_member(member_id)

        elif choice == '6':
            library.view_members()

        elif choice == '7':
            member_id = input("Enter member ID: ")
            book_id = input("Enter book ID to borrow: ")
            library.borrow_book(member_id, book_id)

        elif choice == '8':
            member_id = input("Enter member ID: ")
            book_id = input("Enter book ID to return: ")
            library.return_book(member_id, book_id)

        elif choic=t("ok leaving buee!")
            break

        else:
            print("pls write a vlalid choice")

if __name__ == "__main__":
    main()
