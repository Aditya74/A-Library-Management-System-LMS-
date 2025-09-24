
from assets.data import LMS
from utils.display_utils import(
    display_branch_details,
    display_year_details,
    display_sem_details  
)


def add_student():
    status = True
    while status:
        print("=="*60)
        print("STUDENT DETAILS")
        print("=="*60)
        print("\nBRANCH DETAILS")
        branch = display_branch_details()
        print("\nYEAR DETAILS")
        year = display_year_details()
        print("\nSEM DETAILS")
        sem = display_sem_details()
        name = input("Enter student name: ")
        password = input("Enter password: ")
        roll_no = input("Enter Roll no: ")
        address = input("Enter Address: ")
        phone_no = input("Enter phone no: ")

        student = {
            "name": name,
            "password": password,
            "roll_no": roll_no,
            "address": address,
            "phone_no": phone_no
        }

        LMS["STUDENTS"][branch][year][sem].append(student)
        print(f"\nStudent {name} added successfully to {branch} - {year} - {sem}\n")
        print(">>"*30)
        choice = input("Do you want to add one more student(Y/N):->").upper()
        print(">>"*30)
        if choice != "Y":
            status = False
