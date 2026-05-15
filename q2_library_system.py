def add_book(catalog, book_id, title, author, year):
    catalog[book_id] = (title, author, year)
    print(f"Added: '{title}' (ID: {book_id})")

def borrow_book(catalog, borrowed_books, book_id):
    if book_id not in catalog:
        print(f"Error: Book ID {book_id} not found.")
    elif book_id in borrowed_books:
        print(f"Error: '{catalog[book_id][0]}' is already borrowed.")
    else:
        borrowed_books.append(book_id)
        print(f"Borrowed: '{catalog[book_id][0]}' (ID: {book_id})")

def return_book(borrowed_books, book_id):
    if book_id in borrowed_books:
        borrowed_books.remove(book_id)
        print(f"Returned: Book ID {book_id}")
    else:
        print(f"Error: Book ID {book_id} was not borrowed.")

def register_member(members, member_id):
        members.add(member_id)
        print(f"Registered Member ID : {member_id}")

def show_available(catalog, borrowed_books):  
    for book_id,(title, author, year) in catalog.items():
        if book_id not in borrowed_books:
            print(f"ID: {book_id} | '{title}' by {author} ({year})")
            
def main():
    catalog = {}          
    borrowed_books = []   
    members = set()       

    print("--- Adding Books ---")
    add_book(catalog, 101, "The Great Gatsby", "F. Scott Fitzgerald", 1925)
    add_book(catalog, 102, "1984", "George Orwell", 1949)
    add_book(catalog, 103, "To Kill a Mockingbird", "Harper Lee", 1960)
    add_book(catalog, 104, "Moby Dick", "Herman Melville", 1851)

    print("\n--- Registering Members ---")
    register_member(members, "001")
    register_member(members, "002")
    register_member(members, "002") 

    print("\n--- Borrowing Books ---")
    borrow_book(catalog, borrowed_books, 101)
    borrow_book(catalog, borrowed_books, 102)
    borrow_book(catalog, borrowed_books, 101) 

    print("\n--- Returning Books ---")
    return_book(borrowed_books, 101)
    return_book(borrowed_books, 105)
    
    print("\n--- Available Books ---")  
    show_available(catalog, borrowed_books)

if __name__ == "__main__":
    main()