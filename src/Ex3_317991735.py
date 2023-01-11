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



if __name__ == "__main__":
    print_pairs("ABCDEFG")

    lst = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
    for i in lst:
        assert is_prime(i)

    print(log10_list_comprehension([1,2,3,4,5,6,7]))
    print(log10_list_comprehension([]))

    lst = [1,2,3,4,5,6]
    log10_inplace(lst)
    print(lst)
    lst = []
    log10_inplace(lst)
    print(lst)
    
    print(most_common_value_in_dict({'1':2, 'a':3, 'x':3, 4:3, 2:2, 'y':1}))
    print(get_highest_average_column([[-42]]))

    assert get_longest_increasing_subsequence([[-4, 5, 3, 3.2], [5, 6.0, -2.4, 6], [7, 3, 2, -1]]) == 2
    assert get_longest_increasing_subsequence([[-4, 5, 5, 3.2], [5, 6.0, -2.4, 6], [7, 3, 2, -1]]) == 3
    assert get_longest_increasing_subsequence([[-4, 5, 6, 3.2], [5, 6.0, -2.4, 6], [7, 3, 2, -1]]) == 3
    assert get_longest_increasing_subsequence([[-4, 5, 6, 6], [5, 6.0, -2.4, 6], [7, 3, 2, -1]]) == 4
    assert get_longest_increasing_subsequence([[-4, 5, 6, 10], [5, 6.0, -2.4, 6], [7, 3, 2, -1]]) == 4
    assert get_longest_increasing_subsequence([[-4, -5, -6, -7], [4, 3, 2, 1], [4, 3, 2, 1]]) == 1
    assert get_longest_increasing_subsequence([[-42]]) == 1