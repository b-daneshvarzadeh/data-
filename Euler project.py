Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> u =0
>>> k =0
>>> s1 =0
>>> s2 =0
>>> s3 =0
>>> thislist =[1, 2, 7]
>>> for i in range(1, 20):
	u =3 *i
	if u <20:
		s1 =s1 +u
		thislist.append(u)

	
>>> print(thislist)
[1, 2, 7, 3, 6, 9, 12, 15, 18]
>>> for i in range(1, 20):
	k =5 *i
	if k <20:
		if k in thislist:
			print(k)
		else:
			s2 =s2 +k

	
15
>>> s3 =s1 +s2
>>> print(s3)
78
>>> #sumation of multiple of 3 or 5 in range(1,20)
