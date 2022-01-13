#assignment 1
#question 1
a=int(input("enter first number here:"))
b=int(input("enter second number here:"))
c=int(input("enter third number here:"))
avg=(a+b+c)/3
print("average is:",avg)

#question 2
standard_deduction=10000
depend_deduction=3000
gross=input("enter your gross income")
No_of_dependents=input("Enter your number of dependents")
taxable_income=int(gross)-int(standard_deduction)-(int(depend_deduction)*int(No_of_dependents))
tax=(float(taxable_income)*0.2)
print("Your income tax is :")
print(float(tax))

#question 3
SID=input("Enter your SID here")
Name=input("Enter your name here")
Gender=input("Enter your gender here")
#use gender values:'F','M','U'
Course=input("Enter your course name here")
CGPA=float(input("Enter your CGPA here"))
Student=[SID,Name,Gender,Course,CGPA]
print(Student)

#question 4
marks=[]
for i in range(5): #for loop to take input 5 times
    marks.append(input("Enter marks of students"))
marks.sort()
print(marks)

#question 5
colour=['Red','Green','White','Black','Pink','Yellow']
colour.remove(colour[3])
print("Part a question : ",colour)
colour=['Red','Green','White','Black','Pink','Yellow']
colour[3:5]=['Purple']
print("Part b of question :",colour)
