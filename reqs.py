import const

class BachelorsDegree:
    def __init__(self, gen_reqs=None, majors=None, minors=None):
        ''' gen_reqs, majors, & minors are lists of Reqs, MajorReqs, & MinorReqs respectively. '''
        self.general_reqs = [] if gen_reqs is None else gen_reqs
        self.majors = [] if majors is None else majors
        self.minors = [] if minors is None else minors

class MastersDegree:
    def __init__(self):
        ''' Same as BachelorsDegree. '''
        pass

class StanfordCourse:
    def __init__(self, id, title, units, grading='Letter',
                 ways=None, special_role=None, prereqs=None):
        ''' Represents a Stanford Course. '''
        self.id = id
        self.title = title
        self.units = units
        self.grading = grading
        self.ways = [] if ways is None else ways
        self.special_role = dict() if special_role is None else special_role
        self.prereqs = set() if prereqs is None else prereqs

class MajorReqs(Reqs):
    def __init__(self, name, year='', req_txt=''):
        ''' '''
        super().__init__(req_txt)

class MinorReqs(Reqs):
    def __init__(self, req_txt):
        ''' '''
        super().__init__(req_txt)

class WaysReqs(Reqs):
    def __init__(self, req_txt):
        ''' '''
        super().__init__(req_txt)

    def get_ways_reqs(self):
        for way, count in const.WAYS:
            # self.required_courses
            pass

class Reqs:
    def __init__(self, req_txt):
        ''' '''
        self.req_txt = req_txt
        self.required_courses = dict()

    def create_requirements(self):
        '''
        Returns dict of string: (set{classes}, count of each needed)
            'math & science' : 3
        '''
        with open(req_txt, 'r') as f:
            pass
