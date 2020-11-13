import requests
from lxml import etree
import time
import threading, random
from multiprocessing import Pool
import json

class ADKCourses:
    # the adk courses
    # from https://www.handbook.unsw.edu.au/postgraduate/specialisations/2021/COMPCS
    course = ['COMP4121', 'COMP4161', 'COMP4418', 'COMP6445', 'COMP6447', 'COMP6448', 'COMP6449', 'COMP6452', 'COMP6714', 'COMP6721', 'COMP6733', 'COMP6741', 'COMP6752', 'COMP6771', 'COMP6845', 'COMP9153', 'COMP9242', 'COMP9243', 'COMP9312', 'COMP9315', 'COMP9318', 'COMP9319', 'COMP9323', 'COMP9334', 'COMP9336', 'COMP9337', 'COMP9417', 'COMP9418', 'COMP9434', 'COMP9444', 'COMP9491', 'COMP9517', 'COMP9844', 'COMP9900', 'COMP9991', 'COMP9992', 'COMP9993', 'GEOS9016', 'GMAT9200', 'GMAT9300', 'GMAT9600']

class CSECourse:
    # enter a code, you will get:
    #   1. course name
    #   2. course prequisite
    #   3. course handbook link
    #   4. course timetable link
    #   5. if is an ADK course
    #   6. UOC
    #   7. outline link
    #   8. description


    def __init__(self, course_code = 'COMP9336'):
        # handbook_api = "https://www.handbook.unsw.edu.au/api/content/render/false/query/+contentType:unsw_psubject%20+unsw_psubject.studyLevelURL:postgraduate%20+unsw_psubject.implementationYear:2021%20+unsw_psubject.code:comp9336%20+conHost:f59fc109-4aaa-40e0-bdcc-7039d31533f8%20+deleted:false%20+working:true%20+live:true%20+languageId:1%20/orderBy/modDate%20desc"

        handbook_api = f"https://www.handbook.unsw.edu.au/api/content/render/false/query/+contentType:unsw_psubject%20+unsw_psubject.studyLevelURL:postgraduate%20+unsw_psubject.implementationYear:2021%20+unsw_psubject.code:{course_code}"

        try:
            self.resp = json.loads(requests.get(handbook_api).content).get('contentlets')[0]

            data2 = json.loads(self.resp['data'])

            # add more content
            self.timetableURL = data2['timetableURL']
            self.prequisite = data2['enrolment_rules'][0]['description'] if len(data2['enrolment_rules']) else None
            self.code = data2['cl_code']
            self.title = data2['title']
            self.description = data2['description']
            self.uoc = data2['credit_points_header']
            self.handbookURL = data2['hb_entries'][0]['link_url']


        except IndexError:
            print(f"IndexError: Fail to access the data! {course_code} : {handbook_api}")

    def __repr__(self):
        return f"{self.code} {self.title}"


    def is_adk(self):
        return self.code in ADKCourses.course


    def get_prequisite(self):
        try:
            if self.prequisite:
                return self.prequisite.split(":")[-1].strip('<br/><br/>')
            return None
        except:
            return "Unknown"

    def get_timetable(self, year=2020):
        url = f"http://timetable.unsw.edu.au/{year}/{self.code}.html"
        # todo  get teaching period
        # todo get lecture capacity
        # todo  get course staff


# todo  write a testcase

class Timetable:
    def courses_list(self, year, term):
        # get all the courses
        pass
    def course_capacity(self):
        pass
     


