grade_points = {
    "A" : 5.0,
    "B" : 4.0,
    "C" : 3.0,
    "D" : 2.0,
    "F" : 0.0

}

grades = []
for i in range(1,7): #So it runs 6 times#
    grade = input(f"Enter your grade for subject {i}: ").upper() #Turns even "a" to "A"#
    while grade not in grade_points : 
        print ("Invalid Grade. Please enter A, B, C, or F")
        grade = input(f"Enter your grade for subject {i}: ").upper()
    grades.append(grade_points[grade])    

gpa = sum(grades)/len(grades)    
print("Your CGPA is :", round (gpa,2))
#To print out the classes#
if gpa >= 4.50:
    print("Woah! You'rea first class student")
elif gpa >= 3.50:
    print("You're on a Second class Upper")
elif gpa >=2.40:
    print("You're on a second  class Lower")
elif gpa >= 1.50:
    print("You're on a third class")
else:
    print("You need to work harder")