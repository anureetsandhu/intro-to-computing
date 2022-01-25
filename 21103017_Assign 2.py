#ASSIGNMENT 2
#ANUREET SANDHU
#21103017
#CSE

#Q1
  #given input string is "Python is a case sensitive language"
input_string=input("Enter string for question 1:")
#a.
  #using inbuilt function len() to find length of input string
print("length of string is:",len(input_string))
#b.
  #using slice function to reverse input string
print("reverse of string is:",input_string[::-1])
#c.
  #using slice function to create new string "a case sensitive" from input string
  #in input_string index of a is 10 and index of e is 25
new_string=input_string[10:26]
print(new_string)
#d.
  #using inbuilt function replace() to replace "a case sensitive" with "object oriented"
print(input_string.replace("a case sensitive","object oriented"))
#e.
  #using find() function to find index of "a" in input string
print(input_string.find('a'))
#f.
  #using replace() function to remove the white spaces from input string
print(input_string.replace(" ",""))


                  
      
#Q2
name="Anureet Sandhu"
SID=21103017
dept="CSE"
CGPA=9
#printing the output using formatted strings
print(f'''Hey,{name} Here!
My SID is {SID}
I am from {dept} department and my CGPA is {CGPA}''')




#Q3
a=56
b=10
#a.
print(a&b)
#b
print(a|b)
#c
print(a^b)
#d.
print(a<<2)

print(b<<2)
#e.
print(a>>2)

print(b>>4)



#Q4
#take input of a list of 3 numbers

n1=float(input("Enter the first number:"))
n2=float(input("Enter the second number:"))
n3=float(input("Enter the third number:"))
if (n2>=n1 and n2>=n3):
    print("The largest among these three numbers is:",n1)
elif(n2>=n1 and n2>=n3):
    print("The largest among these three numbers is:",n2)
else:
    print("The largest among these three numbers is:",n3)




#Q5
entry=input("Enter something:")
if 'name' in entry:
 print("yes")

else:
 print("no") 


#Q6
#first we get the user to enter the lengths of the three sides
side_1=int(input("enter length of first side:"))
side_2=int(input("enter length of second side:"))
side_3=int(input("enter length of third side:"))
#use given condition to find out whether a triangle can be formed
if side_1+side_2>side_3 and side_1 + side_3>side_2 and side_2+ side_3> side_1:
 print("Yes")
else:
    print("No")



