

from assets.data import LMS
from config import *

# def check_name_password(credentials):
#     admin = credentials[0]
#     name = credentials[1]
#     password = credentials[2]
#     if (admin["name"] == name) and (admin["password"] == password):
#         return True
#     else:
#         return False
    
# def admin_login():
#      print("\n****Well come you logined as ADMIN****")
#      name = input("\nplease enter your name:->")
#      password = input("\nplease enter your password:->")
   
    
#      all_admins = list(zip(LMS["ADMINS"],[name]*len(LMS["ADMINS"]),\
#                           [password]*len(LMS["ADMINS"])))
#      output = list(filter(check_name_password,all_admins))
        
#      if output:
#         status = True
#         print("\n****ADMIN login is successful****")
#      else:
#         status = False
#         print("\n!!!! Login is unsuccessful !!!!")
#      return status
 
def admin_login():
    name = input("Please enter your name:-> ")
    password = input("Please enter your password:-> ")

    for admin in LMS["ADMIN"]:
        if admin["name"].strip().lower() == name.strip().lower() and \
           admin["password"] == password:
            print("Admin login successful!")
            return True

    print("!!!! ADMIN login unsuccessful !!!!")
    return False

def student_login():
    print("\n******** Welcome to STUDENT login ********")
    name = input("Enter your name: ")
    password = input("Enter your password: ")
    for branch in LMS["STUDENTS"]:
        for year in LMS["STUDENTS"][branch]:
            for sem in LMS["STUDENTS"][branch][year]:
                for student in LMS["STUDENTS"][branch][year][sem]:
                    if student["name"] == name and student["password"] == password:
                        print("Student login successful!")
                        return True
    print("???????? Login failed ????????.")
    return False


def teacher_login():
    print("\n ******** Welcome to TEACHER login ********")
    name = input("Enter your name: ")
    password = input("Enter your password: ")
    for branch in LMS["TEACHERS"]:
                for teacher in LMS["TEACHERS"][branch]:
                    if teacher["name"] == name and teacher["password"] == password:
                        print("Teacher login successful!")
                        return True
    print("!!!!!!!! Login failed !!!!!!!!!.")
    return False

def login(type_of_login):
    if type_of_login == "ADMIN":
        login_status=admin_login()
    elif type_of_login == "STUDENT":
        login_status=student_login()
    elif type_of_login == "TEACHER":
        login_status=teacher_login()
    else:
        login_status = False   
    return login_status