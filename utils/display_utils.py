
from config import (
    DEPTS,
    YEARS,
    SEMS
)
from assets.data import *
from commons.login import login
def display_admin_options():
    status=True
    while(status):
        print("\n")
        print("ADMIN MENU")
        print("\n")
        print("1.Adding Student\n2.Adding a Teacher\n3.Adding a Book\n4.Adding Admin\n5.LOG OUT")
        try:
            choice=input("\nPlease enter your choice 1/2/3/4/5-->:")
            if choice == "1":
                return choice#return 1
                #print("Adding Students.")
            elif choice == "2":
                return choice#return 2
            elif choice == "3":
                return choice#return 3
            elif choice == "4":
                return choice#return 4
            elif choice == "5":
                return choice
                status = False
            else:
             print("Invalid input")
        except:
            print("\nEnter a number only !!! invalid input !!!\n.")
            
def display_login_options():
    status = True
    turn_off = False
    login_status = None
    selected = None
    while(status):
        print("\n")
        print("Who do you belong to? Select from the options below -->")
        print("\n")
        print("1.ADMIN\n2.STUDENT\n3.TEACHER\n4.TURN OFF")
        choice=input("\nPlease enter your choice 1/2/3/4-->:")
        if choice == "1":
            login_status = login("ADMIN")
            #print("Adding Students.")
            status = False 
            selected = "ADMIN"
        elif choice == "2":
            login_status = login("STUDENT")
            status = False
            selected = "STUDENT"
        elif choice == "3":
            login_status=login("TEACHER")
            status = False
            selected = "TEACHER"
        elif choice == "4":
            print("Turn Off")
            status = False
            turn_off = True
        else:
            print("Invalid input")
    return (login_status,turn_off,selected)

def display_student_options():
    status = True
    while status:
        print("\n")
        print("STUDENT MENU")
        print("\n")
        print("1.View Available Books\n2.Taking  a Book\n3.Return a Book\n4.Log Out")
        try:
            
            choice = input("\nPlease enter your choice 1/2/3/4 -->: ").strip()

            if choice == "1":
                view_books()
            elif choice == "2":
                taking_book()
            elif choice == "3":
                return_book()
            elif choice == "4":
                print("Logging out from Teachers dashboard...\n")
                status = False
            else:
                print("\nInvalid input, please try again.\n")
        except:
                print("\nEnter a number only !!! invalid input !!!\n.")
                
def view_student_details():
    name = input("Enter your name to view details: ")
    found = False
    for branch in LMS["STUDENTS"]:
        for year in LMS["STUDENTS"][branch]:
            for sem in LMS["STUDENTS"][branch][year]:
                for student in LMS["STUDENTS"][branch][year][sem]:
                    if student["name"] == name:
                        print(f"\nName: {student['name']}")
                        print(f"Roll No: {student['roll_no']}")
                        print(f"Address: {student['address']}")
                        print(f"Phone: {student['phone_no']}")
                        print(f"Branch: {branch}, Year: {year}, Sem: {sem}\n")
                        found = True
    if not found:
        print("Student not found.")
        
def view_books():
    print("\nAvailable Books:")
    any_books = False  # Track if any book exists
    serial = 1  # Serial number for books

    for branch in LMS["BOOKS"]:
        for year in LMS["BOOKS"][branch]:
            for sem in LMS["BOOKS"][branch][year]:
                books = LMS["BOOKS"][branch][year][sem]
                if books:  # Only display if books exist
                    any_books = True
                    print(f"\nBranch: {branch}, Year: {year}, Sem: {sem}")
                    for book in books:
                        print(f"{serial}. Book Name: {book['book_name']}, "
                              f"Author: {book['author']}, "
                              f"ISBN: {book['book_no']}, "
                              f"Quantity: {book['quantity']}")
                        serial += 1

    if not any_books:
        print("\nNo books available in the library.\n")

def taking_book():
    branch = display_branch_details()
    year = display_year_details()
    sem = display_sem_details()
    book_no = input("Enter ISBN/Book Number to take a book: ")

    if branch in LMS["BOOKS"] and year in LMS["BOOKS"][branch] and sem in LMS["BOOKS"][branch][year]:
        books = LMS["BOOKS"][branch][year][sem]
        for book in books:
            if book["book_no"] == book_no:
                if book["quantity"] > 0:
                    book["quantity"] -= 1
                    print(f"\nYou taken '{book['book_name']}' successfully!")
                else:
                    print("\nSorry, this book is currently not available.")
                return
        print("\nBook not found in this semester.")
    else:
        print("\nInvalid branch/year/semester entered.")
        
def return_book():
    branch = display_branch_details()
    year = display_year_details()
    sem = display_sem_details()
    book_no = input("Enter ISBN/Book Number to return: ")

    if branch in LMS["BOOKS"] and year in LMS["BOOKS"][branch] and sem in LMS["BOOKS"][branch][year]:
        books = LMS["BOOKS"][branch][year][sem]
        for book in books:
            if book["book_no"] == book_no:
                book["quantity"] += 1
                print(f"\nYou returned '{book['book_name']}' successfully ***")
                return
        print("\nBook not found in this semester.")
    else:
        print("\nInvalid branch/year/semester entered.")
            
def display_teacher_options(): 
    status = True
    while status:
        print("\n")
        print("TEACHERS MENU")
        print("\n")
        print("1.View Available Books\n2.Taking a book \n3.Return a Book\n4.Logging Out")
        try:
            
            choice = input("\nPlease enter your choice 1/2/3/4 -->: ").strip()

            if choice == "1":
                view_books()
            elif choice == "2":
                taking_book()
            elif choice == "3":
                return_book()
            elif choice == "4":
                print("Logging out from Teachers dashboard...\n")
                status = False
            else:
                print("\nInvalid input, please try again.\n")
        except:
                print("\nEnter a number only !!! invalid input !!!\n.")
                
            

def display_branch_details():
    status = True
    while(status):
        s_num=1
        print("\nDEPARTMENT DETAILS\n")
        for dept in DEPTS:   
            print(f"{s_num}.{dept}")
            s_num += 1
        status = True
        while status:
            try:
                choice = int(input("\nSelect any branch:->"))
                status = False
            except:
                print("Invalid choice ???? Please Enter Numbers only..")
        for choice in range(1,len(DEPTS)+1):
            return DEPTS[choice-1]
        
def display_year_details():
    status = True
    while(status):
        s_num=1
        #print("YEAR DETAILS")
        for year in YEARS:   
            print(f"{s_num}.{year}")
            s_num += 1
        status = True
        while status:
            try:
                choice = int(input("\nSelect which year:->"))
                status = False
            except:
                print("Invalid choice ???? Please Enter Numbers only..")
        for choice in range(1,len(YEARS)+1):
            return YEARS[choice-1]
        
def display_sem_details(): 
    status = True
    while(status):
        s_num=1
        #print("SEM DETAILS")
        for sem in SEMS:   
            print(f"{s_num}.{sem}")
            s_num += 1
        status = True
        while status:
            try:
                choice = int(input("\nSelect which sem:->"))
                status = False
            except:
                print("Invalid choice ???? Please Enter Numbers only..")
        for choice in range(1,len(SEMS)+1):
            return SEMS[choice-1]  
        
        
        