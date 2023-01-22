#############################################
#                   Task 1
#############################################
def range_dict(a, b):
    d = {}
    for x in range(a, b + 1):
        d[str(x)] = [x]
    return d

#############################################
#                   Task 2
#############################################
def list_to_last_letter_map(lst):
    d = {}
    for word in lst:
        if word[0] in d.keys():
            d[word[0]] += [word[1:]]
        else:
            d[word[0]] = [word[1:]]
    return d

#############################################
#                   Task 3
#############################################
def swap_student_courses(name_to_courses):
    d = {}
    for k, v in name_to_courses.items():
        for course in v:
            if not course in d.keys():
                d[course] = [k]
            else:
                d[course] += [k]
    return d

# students_d = {"Yuval": ["Math", "Computer Science", 
# "Statistics"], "Gal": ["Algebra", "Statistics", "Physics"], "Noam": 
# ["Statistics", "Math", "Programming"]}
# print(swap_student_courses(students_d))

#############################################
#                   Task 4
#############################################
import re
def regex_a(txt):
    match = re.search("Product review: \d+", txt) 
    return match

def regex_b(txt):
    match = re.search("Product review: \d", txt) 
    return match

def regex_c(txt):
    match = re.search("Product review: \s*\d{1,5}", txt) 
    return match

def regex_d(txt):
    match = re.search("Product review: \d{3,5}\.", txt) 
    return match
#############################################
#                   Challenge
#############################################
