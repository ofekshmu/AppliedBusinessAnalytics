#############################################
#                   Task 1
#############################################
email = "ofek.shmuel1@gmail.com"
print(email)

#############################################
#                   Task 2
#############################################
x = input()
print(len(x))

#############################################
#                   Task 3
#############################################
st = input()
print(st[:3].lower())

#############################################
#                   Task 4
#############################################
st = input()
print(st[-2::-2])

#############################################
#                   Task 5
#############################################
st = input()
print(len(st.replace(" ", "")))

#############################################
#                   Task 6
#############################################
i = int(input())
print(i*"I will submit my assignment on time\n")

#############################################
#                   Task 7
#############################################
text = input("Please insert some text: ")
start = int(input())
end = int(input())
copies = int(input())
print(copies*text[start:end + 1])

#############################################
#                   Challenge
#############################################
text = input("Please insert some text: ")
start = int(input())
end = int(input())
copies = int(input())
if start < 0 or end < 0 or end >= len(text) or copies < 0:
    print("Error: illegal input!")
else:
    print(copies*text[start:end + 1])
