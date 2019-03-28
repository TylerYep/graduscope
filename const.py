YEAR = '2018-2019'

CS_MAJOR_REQS = {
    'degree_code': 'CS',
    'degree_name': 'Computer Science',
    'total_units' : 180,
    'min_dept_units': {
        'Mathematics': 26,
        'Science': 11,
        'Engineering Fundamentals': 13
    },
    'required_course_counts': {
        'Technology in Society': 1,
        'Senior Project': 3
    },
    'required_courses': {
        'Mathematics': {
            'CS103',
            'CS109'
        },
        'Science': {
            'PHYSICS41',
            'PHYSICS43'
        },
        'Engineering Fundamentals': {
            (1, 'CS106A', 'CS106AJ', 'CS106AP', 'CS106B', 'CS106X'),
            (1, 'ENGR40A', 'ENGR40M')
        },
        'Core': {
            (1, 'CS107', 'CS107E'),
            'CS110',
            'CS161'
        }
    }
}

GENERAL_CS_ELECTIVES = (
    'CS108', 'CS124', 'CS131', 'CS140', 'CS141', 'CS142', 'CS143', 'CS144', 'CS145', 'CS148', 'CS149', 'CS151', 'CS154', 'CS155', 'CS157', 'CS166', 'CS168', 'CS190', 'CS195', 'CS205B', 'CS205L', 'CS210A', 'CS217', 'CS221', 'CS223A', 'CS224N', 'CS224S', 'CS224U', 'CS224W', 'CS225A', 'CS227B', 'CS228', 'CS229', 'CS229T', 'CS230', 'CS231A', 'CS231B', 'CS231M', 'CS231N', 'CS232', 'CS233', 'CS234', 'CS236', 'CS238', 'CS240', 'CS242', 'CS243', 'CS244', 'CS244B', 'CS245', 'CS246', 'CS248', 'CS251', 'CS252', 'CS254', 'CS255', 'CS261', 'CS262', 'CS263', 'CS264', 'CS265', 'CS266', 'CS267', 'CS269I', 'CS270', 'CS272', 'CS273A', 'CS273B', 'CS274', 'CS276', 'CS279', 'CS348B', 'CS348C', 'CS348K', 'CS352', 'CS369L', 'CME108', 'EE180', 'EE282', 'EE364A'
)

HCI_TRACK_REQS = {
    'required_courses': {
        'CS147',
        'CS247',
        (3, 'CS142', 'CS146', 'CS148', 'CS194H', 'CS206', 'CS210A', 'CS278', 'CS376', 'CS377A', 'CS377B', 'CS377C', 'CS448B', 'ME216M'),
        (2, *GENERAL_CS_ELECTIVES)
    }
}

WAYS_REQ_COUNTS = {
    'WAY-AII': 2,
    'WAY-AQR': 1,
    'WAY-CE': 1,
    'WAY-ED': 1,
    'WAY-ER': 1,
    'WAY-FR': 1,
    'WAY-SMA': 2,
    'WAY-SI': 2
}