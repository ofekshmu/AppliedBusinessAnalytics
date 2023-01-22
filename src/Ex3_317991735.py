#############################################
#                   Task 1
#############################################
def print_pairs(text):
    st = ""
    for i in range(len(text)-1):
        st += f"{text[i]}{text[i+1]} "
    print(st[:-1])

#############################################
#                   Task 2
#############################################
def is_prime(n):
    for num in range(2,n):
        if n % num == 0:
            return False
    return True

#############################################
#                   Task 3
#############################################
import math

def log10_list_comprehension(l):
    return [math.log10(e) for e in l]

#############################################
#                   Task 4
#############################################
def log10_inplace(l):
    for i in range(len(l)):
        l[i] = math.log10(l[i])

#############################################
#                   Task 5
#############################################
def most_common_value_in_dict(d):
    value_counts = {}
    for value in d.values():
        if value in value_counts:
            value_counts[value] += 1
        else:
            value_counts[value] = 1
    return max(value_counts.items(), key=lambda x: x[1])[0]


#############################################
#                   Task 6
#############################################
def get_highest_average_column(mat):
    index = 1
    max_avg = 0
    initial_avg = True
    for j in range(len(mat[0])):
        avg = 0
        for i in range(len(mat)):
            avg += mat[i][j]
        if max_avg <= avg or initial_avg:
            initial_avg = False
            max_avg = avg
            index = j + 1
    return index

#############################################
#                   Task 7
#############################################

def get_longest_increasing_subsequence(mat):
    if len(mat[0]) == 1:
        return 1
    
    count = 1
    max_count = 1
    for i in range(len(mat)):
        for j in range(len(mat[0]) - 1):
            if mat[i][j] <= mat[i][j + 1]:
                count += 1
            else:
                count = 0
            if count > max_count:
                max_count = count
        count = 1
    return max_count
