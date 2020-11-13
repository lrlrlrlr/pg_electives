import requests
from lxml import etree
import time
import threading, random
from multiprocessing import Pool
from ultilities import CSECourse
import logging

logging.basicConfig(filename="condition.log",level=logging.INFO)

def conditions(course):
    url = f"https://www.handbook.unsw.edu.au/postgraduate/courses/2021/{course}"
    r = requests.get(url)
    if r.status_code == 200:
        selector = etree.HTML(r.content)
        # contents = selector.xpath('/html/body/div[1]/div[2]/div[2]/div/div/div[2]/div[3]/div/div[1]/div')
        contents = selector.xpath('/html/body/div[3]/div[3]/div[2]/div/div[2]/div[3]/div[2]/div[1]/div[2]/div[2]/div')
        if len(contents) == 1:
            if contents[0].text.strip():
                # remove "Prerequisite:" and other blank
                return contents[0].text.split(":")[-1].strip()
        return "None"
    else:
        return f"Error, code {r.status_code}"

def count(n):
    time.sleep(random.randrange(1,5))
    print(n)

def mul_thread(func, args, n=1):
    p = Pool(n)
    for arg in args:
        result = p.apply_async(func, args=(arg,)).get()
        print(result)
    p.close()
    p.join()



if __name__ == '__main__':
    # course = input("pls input the course code: ")
    # print(conditions(course))

    course_lst ='''
    BINF9010 
    COMP6441
    COMP9020 
    COMP9021 
    COMP9032 
    COMP9311 
    COMP9414 
    COMP9814
    COMP9511 
    GSOE9210 
    GSOE9220 
    GSOE9820 
    BINF6111
    BINF6112
    COMP4121 
    COMP6451
    COMP6324
    COMP9024 
    COMP9044
    COMP9101 
    COMP9801 
    COMP9222 
    COMP9321
    COMP9322
    COMP9331 
    COMP4161
    COMP9415 
    COMP9447 
    BINF9020
    COMP4141
    COMP4418 
    COMP6445 
    COMP6447  
    COMP6721
    COMP6448  
    COMP6452
    COMP6714
    COMP6841
    COMP9102
    COMP9154
    COMP9164
    COMP6733
    COMP9201
    COMP9283
    COMP9211
    COMP9313
    COMP6741 
    COMP6752
    COMP6771
    COMP9332
    COMP9333
    COMP6845 
    COMP9153
    COMP9242 
    COMP9243 
    COMP9315
    COMP9318
    COMP9319
    COMP6443
    COMP9323 
    COMP9334 
    COMP9336
    COMP9337
    COMP6843 
    COMP9417
    COMP9418 
    COMP9434
    COMP9444
    COMP9517
    COMP9596
    COMP9900
    COMP9945
    BIOT7160 
    MBAX9117 
    GEOS9016 
    GMAT9106 
    GMAT9200 
    GMAT9201 
    GMAT9205 
    GMAT9210 
    GMAT9211 
    GMAT9300 
    GMAT9600 
    GMAT9606 
    GSOE9010 
    GSOE9011 
    GSOE9758 
    INFS5885 
    INFS5905 
    INFS5991 
    TABL5521 
    MATH5836 
    MATH5845 
    MATH5846 
    MATH5855 
    MATH5856 
    MATH5905 
    MATH5960 
    TELE9751 
    TELE9752 
    TELE9753 
    TELE9754 
    MARK5826
    MARK5827
    MARK5828
    '''
    course_lst = course_lst.split('\n')
    course_lst = [c.strip() for c in course_lst if c]

    # SINGLE THREAD
    for course in course_lst:
        # print(course, end="    ")
        c = CSECourse(course)
        # print(c.get_prequisite())
        logging.info(f"{course}    {c.get_prequisite()}")
        time.sleep(0.5)


    # 
    #


    # MUL_THREAD
    # mul_thread(conditions, course_lst, 2)

    # conditions(course_lst)


