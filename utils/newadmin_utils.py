from assets.data import LMS
from utils.display_utils import display_branch_details
def add_Admin():
    status = True
    while status:
        print("=="*60)
        print("ADMIN DETAILS")
        print("=="*60)
        name = input("Enter your name:->")
        password = input("Enter your Password:->")
        address = input("Enter your address:->")
        phoneno = input("Enter your phone no:->")
        Admin={"name":name ,"password":password ,"address":address ,"phoneno":phoneno }
        LMS["ADMINS"].append(Admin)
        print(f"\nTeacher {name} added successfully as admin\n")
        print(">>"*30)
        choice = input("Do you want to add one more more(Y/N):->").upper()
        print(">>"*30)
        if choice != "Y":
            status = False
            
