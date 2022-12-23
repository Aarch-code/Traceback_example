def a():
    print('start of a()')
    b()

def b():
    print('start of b()')
    c()

def c():
    print('start of c()')
    42/0                      #here if you change 0 to any other number you won't get an error

a()

Output:
  
start of a()
start of b()
start of c()
Traceback (most recent call last):
  File "C:/Users/Lenovo/Desktop/abctraceback.py", line 13, in <module>
    a()
  File "C:/Users/Lenovo/Desktop/abctraceback.py", line 3, in a
    b()
  File "C:/Users/Lenovo/Desktop/abctraceback.py", line 7, in b
    c()
  File "C:/Users/Lenovo/Desktop/abctraceback.py", line 11, in c
    42/0
ZeroDivisionError: division by zero
