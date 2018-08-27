'''
Q.1- Name and handle the exception occured in the following program:
a=3
if a<4:
    a=a/(a-3)
    print(a)

'''

#Zero Division Error
a=3
try:
    if a<4:
        a=a/(a-3)
        print(a)
except ZeroDivisionError:
    print('You can\'t Divide by Zero')
    


'''
Q.2- Name and handle the exception occurred in the following program: 
l=[1,2,3] 
print(l[3])
'''
#INDEX ERROR(Index out of range)
l=[1,2,3]
try:
    print(l[3])
except IndexError:
    print('Index out of range')    



'''
Q.3- What will be the output of the following code:
# Program to depict Raising Exception
     
try:
    raise NameError("Hi there")  # Raise Error
except NameError:
    print("An exception")
    raise  # To determine whether the exception was raised or not
'''
OUTPUT:-
An exception
Traceback (most recent call last):
  File "C:/Users/Apurva Gupta/Desktop/a.py", line 2, in <module>
    raise NameError("Hi there")  # Raise Error
NameError: Hi there

#it will be calling its constructor with no arguments as exception class is passed



'''
Q.4- What will be the output of the following code: 

     # Function which returns a/b
def AbyB(a , b):
    try:
        c = ((a+b) / (a-b))
    except ZeroDivisionError:
            print("a/b result in 0")
    else:
            print(c)
    
# Driver program to test above function
AbyB(2.0, 3.0)
AbyB(3.0, 3.0)
'''
OUTPUT:-
-5.0
a/b result in 0

#as AbyB(2.0, 3.0) this will not raise the error so it will go in 'else'
#but AbyB(3.0, 3.0) this will raise an error and exception code will execute


'''    
Q.5- Write a program to show and handle following exceptions: 
1. Import Error 
2. Value Error 
3. Index Error 
'''
#1. Import Error
try:
  from importing import file
  print(file)
except ImportError:
  print("IMPORT ERROR")

#2. Value Error
try:
  n=int(input("Enter Value: "))
  print(n)
except ValueError:
  print("VALUE ERROR")
 
#3. Index Error 
List=['a',1,2]
try:
  print(List[5])
except IndexError:
  print("INDEX ERROR (index out of range)")
