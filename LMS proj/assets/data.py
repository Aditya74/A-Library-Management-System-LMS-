from config import * #(DEPTS,YEARS,SEMS)specific data can be used if \
                        # is for total data can be imported total data from the data 
                        # #(.. is indicates previous directory)
from libs import json
                        
# LMS={} #global score

with open(r"C:\Users\HOME\LMS\assets\LMS.json") as f:
    LMS = json.load(f)
    
def write_out():
    with open(r"C:\Users\HOME\LMS\assets\LMS.json","w") as f:
        json.dump(LMS,f,indent=4)

# def initialize_data():
#         LMS["ADMINS"] = [{"name":"MEHER","password":"meher123"}]
#         LMS["STUDENTS"] ={}#{"name":"MEHER","rollnumber":"111"}
#         LMS["TEACHERS"] = {}
#         LMS["BOOKS"] = {}
        #LMS={} #local scope
        #LMS["ADMINS"] = [{"name":"MEHER","password":"meher123"}]
        # LMS["STUDENTS"] = {"name":"MEHER","rollnumber":"111"}
        # LMS["TEACHERS"] = {}
        # LMS["BOOKS"] = { "Python Basics": {"count": 5},"Data Science": {"count": 3}}  
        
           
        # for dept in DEPTS:
        #     LMS["STUDENTS"][dept] = {}
        #     for year in YEARS:
        #         LMS["STUDENTS"][dept][year] = {}
        #         for sem in SEMS:
        #             LMS["STUDENTS"][dept][year][sem] = []
                    
        # for dept in DEPTS:
        #     LMS["TEACHERS"][dept] = []
           
        # for dept in DEPTS:
        #     LMS["BOOKS"][dept] = {}
        #     for year in YEARS:
        #         LMS["BOOKS"][dept][year] = {}
        #         for sem in SEMS:
        #             LMS["BOOKS"][dept][year][sem] = []
                    
        
