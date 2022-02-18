'''
course_search is a Python script using a terminal based menu to help
students search for courses they might want to take at Brandeis
'''

from schedule import Schedule

schedule = Schedule()
schedule.load_courses()
schedule = schedule.enrolled(range(5,1000)) # eliminate courses with no students

TOP_LEVEL_MENU = '''
quit
reset
term  (filter by term)
course (filter by coursenum, e.g. COSI 103a)
instructor (filter by instructor)
subject (filter by subject, e.g. COSI, or LALS)
title  (filter by phrase in title)
description (filter by phrase in description)
timeofday (filter by day and time, e.g. meets at 11 on Wed)
'''

terms = {c['term'] for c in schedule.courses}
subjects = {c['subject'] for c in schedule.courses}

def topmenu():
    '''
    topmenu is the top level loop of the course search app
    '''
    global schedule
    while True:
        command = input(">> (h for help) ")
        if command=='quit':
            return
        elif command in ['h','help']:
            print(TOP_LEVEL_MENU)
            print('-'*40+'\n\n')
            continue
        elif command in ['r','reset']:
            schedule.load_courses()
            schedule = schedule.enrolled(range(5,1000))
            continue
        elif command in ['t', 'term']:
            term = input("enter a term:"+str(terms)+":")
            schedule = schedule.term([term]).sort('subject')
        elif command in ['s','subject']:
            subject = input("enter a subject:"+str(subjects)+":")
            schedule = schedule.subject([subject])
        elif command in ['c', 'course']:                # Junhao Wang
            courses = input("enter a course number:")
            course = courses.split()
            schedule = schedule.subject([course[0]])
            schedule = schedule.coursenum(course[1])
        elif command in ['i', 'instructor']:            # Junhao Wang
            instructor = input("enter a instructor's email or lastname:")
            if "@" in instructor:
                schedule = schedule.email([instructor])
            else:
                schedule = schedule.lastname([instructor])
        elif command in ['ti', 'title']:                # Junhao Wang
            title = input("enter a title:")
            schedule = schedule.title(title)
        elif command in ['d', 'description']:           # Junhao Wang
            description = input("enter a description:")
            schedule = schedule.description(description)
        elif command in ['time', 'timeofday']:          # Junhao Wang
            timeofdays = input("enter a time of day: such as '1100 on w' m for Mon, tu for Tue, " + 
            "w for Wed, th for Thur, f for Fri, sa for Sat, su for Sun: ")
            timeofday =timeofdays.split()
            schedule = schedule.time(int(timeofday[0]))
            schedule = schedule.day(timeofday[2])
        elif command in ['w', 'waiting']:
            schedule = schedule.waiting(0)
        elif command in ['reci','recitation']:   #Tingwie Liu
            schdeule=schedule.recitation()
        else:
            print('command',command,'is not supported')
            continue

        print("courses has",len(schedule.courses),'elements',end="\n\n")
        print('here are the first 10')
        for course in schedule.courses[:10]:
            print_course(course)
        print('\n'*3)

<<<<<<< HEAD
=======

>>>>>>> e05afbb92d8cae1a6109417cdc91a2431db400fd
def print_course(course):
    '''
    print_course prints a brief description of the course
    '''
    print(course['subject'],course['coursenum'],course['section'],
          course['name'],course['term'],course['instructor'])

if __name__ == '__main__':
    topmenu()

