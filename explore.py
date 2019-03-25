from explorecourses import *
from explorecourses import filters
import pickle

def download_courses():
    connect = CourseConnection()
    year = '2018-2019'
    for school in connect.get_schools(year):
        for dept in school.departments:
            print(dept)
            courses = connect.get_courses_by_department(dept.code, year=year)
            pkl_out = open('courses/' + dept.code + '.pkl', 'wb')
            pickle.dump(courses, pkl_out)
            pkl_out.close()

def get_courses_arr(dept_code):
    return pickle.load(open('courses/' + dept_code + '.pkl', 'rb'))

if __name__ == '__main__':
    cs_classes = get_courses_arr('CS')
    for clas in cs_classes:
        print(clas.code)
