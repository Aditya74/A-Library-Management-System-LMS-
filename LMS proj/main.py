'''
This file is the starting file for Innomatics LMS projects
And it contains business logic of LMS

Author:aadhimarumalla@gmail.com
Copy Rights:2025@Innomatics
'''
import sys #root path of the file is import the file by path
from libs import json
sys.path.append(r"C:\Users\HOME\LMS")
from assets.data import LMS
from assets.data import write_out
#from assets.data import initialize_data #* is used for import all the data can be imported
#from commons.login import student_login
from utils.admin_utils import process_request
#from assets.data import initialize_sample_students
from utils.display_utils import (
    display_login_options,
    display_student_options,
    display_teacher_options,
)
def main():
    '''
    Main function is a starting point for LMS.
    '''
    print("=="*60)
    print("WELCOME TO LMS")
    print("=="*60)
    #Initializing our data.add. 

    # initialize_data()
    # login_status,turn_off,selected=display_login_options()
    # if turn_off:
    #     print("Turning of the software")
    #     return #Successful Return Gracefull Return
        
    # if login_status:
    #     #initialize_sample_students()
    #     if selected == "ADMIN":
    #         process_request()
    #         # choice = display_admin_options()
    #         # process_request(choice)
    #     elif selected == "STUDENT":
    #         display_student_options()
    #     elif selected == "TEACHER":
    #         display_teacher_options()   
             
    #     status = True
    #     while status:
    #         login_status,turn_off,selected=display_login_options()
    #         if turn_off:
    #             print("Turning of the software")
    #             status = False 
    # else:
    #     print("!!! Unsuccessful login! invilid usear details. LMS exiting try again with correct details.!!!")
        

    #initialize_data()  # Initialize LMS data first

    try:
        while True:
            login_status, turn_off, selected = display_login_options()
            
            if turn_off:
                print("Turning off the software")
                write_out()
                break

            if login_status:
                if selected == "ADMIN":
                    process_request()  # admin menu
                elif selected == "STUDENT":
                    display_student_options()  # <-- student menu shown here
                elif selected == "TEACHER":
                    display_teacher_options()# teacher menu
            else:
                print("!!! Unsuccessful login! Invalid user details !!!")    
                
    finally:
        write_out()
            
if __name__ == "__main__":
    main()


