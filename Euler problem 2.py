Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> u =1
>>> v =1
>>> w =0
>>> sum1 =0
>>> while w <4000000:
	w =u +v
	if w %2 ==0 and w <4000000:
		sum1 =sum1 +w
	u =v
	v =w

	
>>> print(sum1)
4613732
>>> print(w)
5702887
>>> #problem2 (fibonacci sequence)
