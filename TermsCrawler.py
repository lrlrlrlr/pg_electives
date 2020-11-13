# get all the course available in PG Electives
def all_pg_courses(
        pgurl="https://www.engineering.unsw.edu.au/study-with-us/current-students/academic-information/electives/pg-electives") -> list:
    pass


# get all the courses in a spec term/sem.
def courses(term, year) -> list:
    pass


# course_detail
def course_details(course_code)->dict:




    return {"code":course_code,
     "timetable_url":timetable_url,
     "course_name":course_name,
     "level":level,
     "capacity": capacity,
     "prof": prof
     }
    pass

# capacity = [{"period": "T1", "capacity": "100/200"},
#             {"period": "T2", "capacity": "50/150"}]

# if this course code is adk
def is_ADK(course_code) -> bool:
    pass
