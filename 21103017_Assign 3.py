#ASSIGNMENT 3
#ANUREET SANDHU
#SID:21103017

#Q1
print("Q1")
string=input("Enter a string: ")
string=string.lower() 
occ={} 
if " " in string:
    words=string.split(" ") #Splits the words in the string into a list
    for i in words: 
        if i in occ: #Checks if the word is in the dictionary or not
            occ[i] += 1 #iterates the word if it is already present in the dictionary
        else:
            occ[i]=1 #adds the word to the dictionary
    print("Occurences of words in input string: ",occ)
else:
    letters=list(string) #stores the letters of a word in a list
    for i in letters: 
        if i in occ: #checks if the letter is in the dictionary
            occ[i] += 1 #iterates the letter  
        else:
            occ[i]=1 #adds the letter to the dictionary
    print("Ocuurences of characters in input string: ",occ)
print("\n")


#Q2
print("Q2")
day=int(input("Enter the day:"))
month=int(input("Enter month:"))
year=int(input("Enter the year:"))
if 1800<=year<=2025:#to check whether year is in range
 if 1<=month<=12:#to check whether month is in range
   if month in[1,3,5,7,8,10]:
     if 1<=day<31:
        print("Next date is:",day+1,"/",month,"/",year)
     elif day==31:
         print("Next date is:1/",month+1,"/",year)
     elif day<1 or day>31:#when day is out of range for months 1,3,5,7,8,10
        print("day out of range")
   if month in [4,6,9,11]:
     if 1<=day<30:
      print("Next date is:",day+1,"/",month,"/",year)
     elif day==30:
      print("Next date is:1/",month+1,"/",year)
     elif day<1 or day>30:#when day is out of range for months 4,6,9,11 
      print("day out of range")
   if month==2:
    #for leap years
    if year%4==0:
      if 1<=day<29:
        print("Next date is:",day+1,"/",month,"/",year)
      elif day==29:
        print("Next date is:1/",month+1,"/",year)
      elif day<1 or day>29 :#when day is out of range for february in a leap year
        print("day out of range")
    #for non leap years
    else:
       if 1<=day<28:
         print("Next date is:",day+1,"/",month,"/",year)
       elif day==28:
         print("Next date is:1/",month+1,"/",year)
       elif day<1 or day>28:#when day is out of range for february in a non leap year
         print("day out of range")
   if month==12:
     if 1<=day<31:
         print("Next date is:",day+1,"/",month,"/",year)
     elif day==31:
         print("Next date is:1/1/",year+1)
     elif day<1 or day>31:#when day is out of range for december
         print("day out of range")
 else:
     print("month out of range")
else:
    print("year out of range")

#Q3
print("Q3")
list=[2,5,6,23,34]
print("the list is",list)
output_list=[(i,i**2) for i in list]
print("output:",output_list)


#Q4
print("Q4")
#prompting user to enter a grade between 4 and 10
input_grade=int(input("Enter your grade lying between 4 and 10:"))
if input_grade==10:
    letter_grade="A+"
    performance="Outstanding"
elif input_grade==9:
    letter_grade="A"
    performance="Excellent"
elif input_grade==8:
    letter_grade="B+"
    performance="Very Good"
elif input_grade==7:
     letter_grade="B"
     performance="Good"
elif input_grade==6:
     letter_grade="C+"
     performance="Average"
elif input_grade==5:
     letter_grade="C"
     performance="Below Average"
elif input_grade==4:
     letter_grade="D"
     performance="Poor"
if 4<input_grade<10:
    print("Your grade is '",letter_grade,"' and ",performance," performance.")
else:
    print("Error: grade is not between 4 and 10")


#Q5
print("Q5")
string="ABCDEFGHIJK"
counter=1#for first row
while(counter<7):#no. of rows to be printed=6
    print(" "*(counter-1),string[0:11-((counter-1)*2)])#no. of gaps to be left in each row= counter-1
                                                       #in each row no. alphabets of the string to be left=2x(counter-1)
    counter=counter+1
    

#Q6
print("Q6")
dict1 = {}
while True:                     #loop for repeatedly asking user to enter name and SID
    name = input("Enter the name of the student: ")
    SID = int(input("Enter the SID of %s: " % name))
    dict1[SID] = name
    print("\nYou have entered %d value(s) till now" % len(dict1))
    while True:
        more_data = input("Do you want to enter more data? ")
        if more_data in ("N","n","No","no","NO"):
            more_data = 0
            break
        elif more_data in ("Y","y","Yes","yes","YES"):
            more_data = 1
            break
        else:
            print("\nPlease say yes or no")
            continue
    if more_data == 0:
        break
print("\na. Student Details:")          #Q6(a)printing student details stored in dictionary
for i in dict1:
    print("The SID of %s is %d" % (dict1[i],i))
dict2 = {}
for sorted_value in sorted(dict1.values()): 
    for key,value in dict1.items():
        if value == sorted_value:
            dict2[key] = value
print("\nb. Student Details (sorted with respect to names):") #Q6(b)sorting the dictionary using student names
for i in dict2:
    print("The SID of %s is %d" % (dict2[i],i))
dict3 = {}
for sorted_key in sorted(dict1):            #Q6(b)sorting the dictionary using SIDs
    for key,value in dict1.items():
        if key == sorted_key:
            dict3[key] = value
print("\nc. Student Details (sorted with respect to SIDs):")#Q6(c)
for i in dict3:
    print("The SID of %s is %d" % (dict3[i],i))
print("\nd. ", end="")                      #Q6(d)printing name of student by searching using SID
while True:
    search_SID = int(input("Enter the SID of the student: "))
    if search_SID in dict1:
        print("The name of student whose SID is %d is %s" % (search_SID,dict1[search_SID]))
        break
    else:
        print("The SID you entered isn't entered\nPlease enter a valid SID to be searched\nList of valid SIDs: %s\n" % list((dict1.keys())))
        continue

#Q7
print("Q7")
n=int(input("Enter the number of terms of the fibonacci sequence: "))
sum=0 #This will be required for the average of the series

a=0 #The first value of the fibonacci sequence
b=1 #A temporary variable which helps getting the sequence correct
for i in range(n):
    print(a)
    c=a+b
    sum+=a
    a=b
    b=c
avg=sum/n #Calculates the average of the series
print("The average of the above fibonacci series is: ",avg, "\n")


#Q8
print("Q8")
set1={1,2,3,4,5}
set2={2,4,6,8}
set3={1,5,9,13,17}
print(set1)
print(set2)
print(set3)
#a.
print("a. set of elements that are in set 1 and set 2 but not both:",set1^set2)
#b.
print("b. set of elements that are in only one of the three sets:",set1^set2^set3)
#c.
print("c. set of elements that are in exactly two of the sets set1, set2, set3:",set1&set2|set2&set3|set3&set1)
#d.
print("d. set of all  integers in the range 1 to 10 that are not in set1:",set(range(1,10))-set1)
#e.
print("e. set of all integers  in the range 1 to 10 that arenot in set1,set2 ans set3:",set(range(1,10))-set1-set2-set3)
