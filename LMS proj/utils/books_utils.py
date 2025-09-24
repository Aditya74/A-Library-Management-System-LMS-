from assets.data import LMS
from utils.display_utils import(
    display_branch_details,
    display_year_details,
    display_sem_details  
)
        
def add_books():
    status = True
    while status:
        print("=="*60)
        print("BOOK DETAILS")
        print("=="*60)
        print("\nBRANCH DETAILS")
        branch = display_branch_details()
        print("\nYEAR DETAILS")
        year = display_year_details()
        print("\nSEM DETAILS")
        sem = display_sem_details()
        book_no = input("Enter book number : \n")
        book_name = input("Enter book name: \n")
        author = input("Enter author name: \n")
        try:
            quantity = int(input("Enter quantity: \n"))
        except ValueError:
            print("Quantity must be a number. Try again.")
            continue

        book = {
            "book_no": book_no,
            "book_name": book_name,
            "author": author,
            "quantity": quantity
        }

        # Add book to the LMS
        LMS["BOOKS"][branch][year][sem].append(book)
        print(f"\nBook '{book_name}' added successfully to {branch} - {year} - {sem}!\n")
        print(">>"*30)
        choice = input("Do you want to add one more book(Y/N):->")
        print(">>"*30)
        if choice != "Y":
            status = False
            
