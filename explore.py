from explorecourses import *
from explorecourses import filters
import pickle
import re

def download_courses():
    connect = CourseConnection()
    for school in connect.get_schools(const.YEAR):
        for dept in school.departments:
            print(dept)
            courses = connect.get_courses_by_department(dept.code, year=year)
            pkl_out = open('courses/' + dept.code + '.pkl', 'wb')
            pickle.dump(courses, pkl_out)
            pkl_out.close()


def get_courses_arr(dept_code):
    return pickle.load(open('courses/' + dept_code + '.pkl', 'rb'))


def get_course(course_code):
    course_code = course_code.replace(' ', '').strip()
    dept_code = re.match('[a-zA-Z]+', course_code).group()
    all_courses = get_courses_arr(dept_code)
    found_course = [c for c in all_courses if dept_code + c.code == course_code]
    return found_course[0]


if __name__ == '__main__':
    print(get_course('CS106B'))
