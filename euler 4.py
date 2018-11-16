Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> x =0
>>> st1 =0
>>> for i in reversed(range(900, 1000)):
	for j in reversed(range(900, 1000)):
		x =i *j
		st1 =str(x)
		if st1[0] ==st1[5] and st1[1] ==st1[4]  and st1[2] ==st1[3]:
			print(st1)

			
906609
886688
888888
861168
888888
861168
886688
824428
906609
819918
824428
819918
>>> 
