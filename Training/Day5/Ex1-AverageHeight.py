# Instructions
# You are going to write a program that calculates the average student height from a List of heights.
#
# e.g. student_heights = [180, 124, 165, 173, 189, 169, 146]
#
# The average height can be calculated by adding all the heights together and dividing by the total number of heights.
#
# e.g.
#
# 180 + 124 + 165 + 173 + 189 + 169 + 146 = 1146
#
# There are a total of 7 heights in student_heights
#
# 1146 ÷ 7 = 163.71428571428572
#
# Average height rounded to the nearest whole number = 164
#
# Important You should not use the sum() or len() functions in your answer. You should try to replicate
# their functionality using what you have learnt about for loops.
#
# Example Input
# 156 178 165 171 187

# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
avg_of_heights = 0
counter = 0

for height in student_heights:
    counter += 1
    avg_of_heights += height

print(int(round(avg_of_heights / counter, 0)))
