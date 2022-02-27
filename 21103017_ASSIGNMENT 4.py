#ASSIGNMENT 4
#ANUREET SANDHU, SID:21103017, BRANCH:CSE

#Q1
print("Q1")
print("Tower of Hanoi:")
count = 0
def tower(n, source, inter, dest):
    #source is the peg from where we are picking disks
    #inter is the intermediate peg
    #dest is the destination peg where we need to keep it.
    global count
    if(n==1):
        print("Move disk 1 from",source,"to",dest)
        count = count+1
    else:
        tower(n-1, source, dest, inter)
        print("Move disk",n, "from ",source,"to ",dest)
        tower(n-1,inter, source, dest)   #to move all 3 disks finally from intermediate to destination using source
        count = count + 1
n = int(input("Enter number of disks: "))
tower(n,"A",'B',"C")
# A, B, C are names of pegs

#printing the count
print("No. of Steps taken are:",count, "= 2^n - 1")


print()
#Q2
#(i) using recursion
print("Q2 using recursion")

def cal(i,j):
    if(j==0 or j==i):
        return 1
    else:
        return cal(i-1,j) + cal(i-1,j-1)
m = int(input("Enter number of rows to form pascal triangle: "))
a = [[] for i in range(m)]
for i in range(m):  
    for j in range(i+1):
        print(cal(i,j), end = " ")
    print()

#(ii) using for loop
print()
print("Q2 using for loop")
    
m =int(input("enter the no of rows required in Pascal's triangle:"))
a = [[] for i in range(m)]
# [[],[],[],[],[]]

for i in range(m):  
    for j in range(i+1):  
        if(j<i):
            if(j==0):
                a[i].append(1)
            else:
                a[i].append(a[i-1][j] + a[i-1][j-1])
        elif(j==i):
            a[i].append(1)

#print(a)

for i in a:
    for j in i:
        print(j, end = ' '),
    print()

#Q3#creating an empty list
print()
print("Q3")
emp = []

#defining function which calculates quotient and remainder
def qr(a,b):
    #b)checking whether all the values are zero or not
     if(a==0 or b==0):
         print("b) one of the values is zero")
         return False
     else:
         global q
         global r
         print("b) all the values are non zero")
         q = a//b
         r = a%b

a = int(input("Enter first integer value: "))
b = int(input("Enter second integer value: "))

#a)checking whether function is callable or not
print("a) function is callable:",end=" ")
print(callable(qr))

qr(a,b)

print("c) result=",q,",",r)

emp.extend([q,r,4,5,6])
print("c) result along with added values:",emp)

print("c) result after filtering  out values greater than 4:",end=" ")
for i in emp:
 if(i<4):
   print(i,end=" ")

print()

converted_set = set(emp)
print("d) converted set:",converted_set)

imm_set = frozenset(converted_set)
print("e) immutable  set:",imm_set)

max_value = max(converted_set)
print("f) maximum value=",max_value)
x=float(max_value)
hash_value=hash(x)
print(x)
print("f) hash value=",hash_value)

print()
#Q4
print("Q4")
class Student:
 def __init__(self, name, roll_no):
  self.name = name
  self.roll_no = roll_no
#object creation
student1 = Student("Anureet",21103017)
print(student1.name)
print(student1.roll_no)
print()
def __del__(self):
 print()
del student1
print("Object is destroyed")


#Q5
print()
print("Q5")
class Office:
 def __init__(self, name, salary):
    self.name = name
    self.salary = salary
emp1 = Office("mehak",40000)
emp2 = Office("ashok",50000)
emp3 = Office("viren",60000)
print("a)",end="")
print("salary  of Mehak:",emp1.salary)
emp1.salary = 70000
print(" salary of Mehak after updating:",emp1.salary)
print()
print("b)deleting the record of employee Viren")
del emp3



#Q6
print("Q6")
str1=input("Enter word uttered by George: ")
str2=input("Enter meaningful word uttered by Barbie: ")
l1 = []
for i in str1:
    l1.append(i)
l2 = []
for j in str2:
    l2.append(j)

l1 = sorted(l1)
l2 = sorted(l2)

# list -> if it is sorted -> == -> element wise check 
if(len(l1)==len(l2)):
    if(l1==l2):
        print("Friendship is real")
    else:
        print("Friendship is fake")
else:
    print("Friendship is fake")#words are of different length



    
