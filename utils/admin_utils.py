from utils.student_utils import add_student
from utils.Teacher_utils import add_Teacher
from utils.books_utils import add_books
from utils.newadmin_utils import add_Admin
from utils.display_utils import (
    display_admin_options,
)

def process_request():
    status=True
    while status:
        choice = display_admin_options()  # get new choice each time
        if choice == "1":
            add_student()
        elif choice == "2":
            add_Teacher()
        elif choice == "3":
            add_books()
        elif choice == "4":
            add_Admin()
        elif choice == "5":
            print("\nLogging out...\n")
            status = False
        else:
            print("\nInvalid choice, please try again.\n")    