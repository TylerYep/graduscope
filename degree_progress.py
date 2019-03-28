import const
import explore

class MajorRequirements():
    def __init__(self, init_config):
        '''
        Converts constant config into Python object
        '''
        self.init_dict = init_config
        for key in init_config:
            setattr(self, key, init_config[key])
        self.courses = []

    def load_courses(self, filename):
        with open(filename, 'r') as f:
            for line in f:      # TODO optimize lookups
                self.courses.append(explore.get_course(line))

    def complete_degree(self, filename=None):
        if filename is not None: self.load_courses(filename)
        print(self.get_total_units())
        print(self.get_dept_units())

    def get_total_units(self):
        return sum([c.units_max for c in self.courses])

    def get_dept_units(self):
        subtotals = dict()
        for dept in self.min_dept_units:
            for c in self.courses:
                print(c.subject)
            subtotals[dept] = sum([c.units_max for c in self.courses if c.subject == dept])
        print(subtotals)

    def __repr__(self):
        return self.degree_name


if __name__ == '__main__':
    mr = MajorRequirements(const.CS_MAJOR_REQS)
    mr.complete_degree('tyler_classes.txt')

