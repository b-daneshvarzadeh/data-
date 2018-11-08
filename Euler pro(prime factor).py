Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # THE LARGEST PRIME FACTOR
>>> def checkprime(checknum):
	for i in range(2, checknum):
		if checknum %i !=0:
			return(checknum)
		return(1)

	
>>> answer =0
>>> mylist =[1, 2]
>>> x =600851475143
>>> y =x //2
>>> print(y)
300425737571
>>> for k in range(2, 300425737571):
	answer =checkprime(k)
	if answer !=1:
		if x %answer ==0:
			mylist.append(answer)

			
Traceback (most recent call last):
  File "<pyshell#18>", line 4, in <module>
    if x %answer ==0:
TypeError: unsupported operand type(s) for %: 'int' and 'NoneType'
>>> print(mylist[-1])
2
>>> #I DONT UNDRESTEND THIS ERROR
