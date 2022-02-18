'''
schedule maintains a list of courses with features for operating on that list
by filtering, mapping, printing, etc.
'''

import json

class Schedule():
    '''
    Schedule represent a list of Brandeis classes with operations for filtering
    '''
    def __init__(self,courses=()):
        ''' courses is a tuple of the courses being offered '''
        self.courses = courses

    def load_courses(self):
        ''' load_courses reads the course data from the courses.json file'''
        print('getting archived regdata from file')
        with open("courses20-21.json","r",encoding='utf-8') as jsonfile:
            courses = json.load(jsonfile)
        for course in courses:
            course['instructor'] = tuple(course['instructor'])
            course['coinstructors'] = [tuple(f) for f in course['coinstructors']]
        self.courses = tuple(courses)  # making it a tuple means it is immutable

    def lastname(self,names):
        ''' lastname returns the courses by a particular instructor last name'''
        return Schedule([course for course in self.courses if course['instructor'][1] in names])

    def email(self,emails):
        ''' email returns the courses by a particular instructor email'''
        return Schedule([course for course in self.courses if course['instructor'][2] in emails])

    def term(self,terms):
        ''' email returns the courses in a list of term'''
        return Schedule([course for course in self.courses if course['term'] in terms])

    def enrolled(self,vals):
        ''' enrolled filters for enrollment numbers in the list of vals'''
        return Schedule([course for course in self.courses if course['enrolled'] in vals])

    def subject(self,subjects):
        ''' subject filters the courses by subject '''
        return Schedule([course for course in self.courses if course['subject'] in subjects])

    def sort(self,field):
        '''sort'''
        if field=='subject':
            return Schedule(sorted(self.courses, key= lambda course: course['subject']))
        print("can't sort by "+str(field)+" yet")
        return self

    def title(self,phrase):
        '''filters courses containing the phrase in their title   Tingwie Liu'''
        return Schedule([course for course in self.courses if phrase in course['name']])

    def description(self,phrase):
        '''filters courses containing the phrase in the description   Tingwei Liu'''
        return Schedule([course for course in self.courses if phrase in course['description']])

    def recitation(self):
        '''filters courses have a reicitation.    Tingwei Liu'''
        return Schedule([course for course in self.courses
                         for j in course['times'] if 'Recitation' in j.values()])

    def coursenum(self,coursenums):
        '''filters courses by course number   Junhao Wang'''
        return Schedule([course for course in self.courses if course['coursenum'] in coursenums])

    def time(self,times):
        '''filters courses by course time     Junhao Wang'''
        return Schedule([course for course in self.courses
                        if len(course['times']) != 0 and course['times'][0]['start']==times*100])

    def day(self,days):
        '''filters courses by day             Junhao Wang'''
        return Schedule([course for course in self.courses
                        if len(course['times']) != 0 and  days in course['times'][0]['days']])

    def waiting(self, wait_num):
        '''filter course by waiting number'''
        return Schedule([course for course in self.courses if course["waiting"] > wait_num])
