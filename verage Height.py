student_height = input ("input a list of student heights\n").split()

for n in range (0, len(student_height)):
    student_height[n] = int(student_height[n])
print (student_height)

# this line of code help to print the sum of student height from the input
# it help us to initalize the value we are going to print
sum_height = 0
for h in student_height: 
    sum_height += h #it will run in as much there is still value in the range part
# print (sum_height)

#this line of code help to print the number of student instead of using the len ()
number_of_student = 0
for n in student_height:
    number_of_student += 1 # this line of code will be icreasing by 1 thereby counting the number of range 
# print (number_of_student)

#this line of code help us to print out the average 
average_height = sum_height / number_of_student
print (average_height)

    
# print (sum_height (student_height))
# print (n + 1)
# print (sum_height(student_height)/ (n + 1))


