
from assets.data import LMS
from utils.display_utils import display_branch_details

        
def add_Teacher():
    status = True
    while status:
        print("=="*60)
        print("TEACHER DETAILS")
        print("=="*60)
        print("BRANCH DETAILS")
        branch = display_branch_details()
        name = input("Enter teacher name: ")
        password = input("Enter password: ")
        emp_id = input("Enter Employee ID: ")
        phone_no = input("Enter phone no: ")

        teacher = {
            "name": name,
            "password": password,
            "emp_id": emp_id,
            "phone_no": phone_no
        }

        LMS["TEACHERS"][branch].append(teacher)
        print(f"\nTeacher {name} added successfully to {branch} branch\n")
        print(">>"*30)
        choice = input("Do you want to add one more Teacher(Y/N):->").upper()
        print(">>"*30)
        if choice != "Y":
            status = False
            
            
        