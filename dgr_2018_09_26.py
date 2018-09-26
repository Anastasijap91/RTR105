Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> input
<built-in function input>
>>> input ("Cienamajs lietotaj, lūdzu , ievadi skaitli :")
Cienamajs lietotaj, lūdzu , ievadi skaitli :100
100
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', '__doc__': None, '__package__': None}
>>> mans_mainigais = input ("Cienamais lietotajs, lūdzu , ievadi skaitli :")
Cienamais lietotajs, lūdzu , ievadi skaitli :100
>>> vars ()
{'__builtins__': <module '__builtin__' (built-in)>, 'mans_mainigais': 100, '__package__': None, '__name__': '__main__', '__doc__': None}
>>> mans_mainigais
100
>>> mans_mainigais = input (" Cienamais lietotajs, lūdzo , ievadi skaitli :")
 Cienamais lietotajs, lūdzo , ievadi skaitli :200
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, 'mans_mainigais': 200, '__package__': None, '__name__': '__main__', '__doc__': None}
>>> 
=============== RESTART: /home/user/rtr105/test_1_20180926.py ===============
 Cienamais lietotajs, lūdzo , ievadi skaitli :85
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__file__': '/home/user/rtr105/test_1_20180926.py', '__package__': None, '__name__': '__main__', '__doc__': None}
>>> 
=============== RESTART: /home/user/rtr105/test_1_20180926.py ===============
 Cienamais lietotajs, lūdzo , ievadi skaitli :4

Traceback (most recent call last):
  File "/home/user/rtr105/test_1_20180926.py", line 2, in <module>
    x = mans_mainigais * mans_mainigais
NameError: name 'mans_mainigais' is not defined
>>> 
>>> 
=============== RESTART: /home/user/rtr105/test_1_20180926.py ===============
 Cienamais lietotajs, lūdzo , ievadi skaitli :4
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__file__': '/home/user/rtr105/test_1_20180926.py', 'mans_mainigais': 4, '__package__': None, 'x': 16, '__name__': '__main__', '__doc__': None}
>>> x
16
>>> 
=============== RESTART: /home/user/rtr105/test_1_20180926.py ===============
 Cienamais lietotajs, lūdzo , ievadi skaitli :12
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__file__': '/home/user/rtr105/test_1_20180926.py', 'mans_mainigais': 12, '__package__': None, 'x': 144, '__name__': '__main__', '__doc__': None}
>>> x
144
>>> 
=============== RESTART: /home/user/rtr105/test_1_20180926.py ===============
 Cienamais lietotajs, lūdzo , ievadi skaitli :

Traceback (most recent call last):
  File "/home/user/rtr105/test_1_20180926.py", line 1, in <module>
    mans_mainigais = input (" Cienamais lietotajs, lūdzo , ievadi skaitli :")
  File "<string>", line 0
    
    ^
SyntaxError: unexpected EOF while parsing
>>> <type `int`>
SyntaxError: invalid syntax
>>> <type `int``>
SyntaxError: invalid syntax
>>> 
=============== RESTART: /home/user/rtr105/test_1_20180926.py ===============
 Cienamais lietotajs, lūdzo , ievadi skaitli :1.1
Lietotāj,tu esi ievadījis vērtību: 1.1000
Kā arī tagad atmiņā ir arī x= 1.210
>>> 
=============== RESTART: /home/user/rtr105/test_1_20180926.py ===============
 Cienamais lietotajs, lūdzo , ievadi skaitli :1.1
Lietotāj,tu esi ievadījis vērtību:     1.1000
Kā arī tagad atmiņā ir arī x=           1.210
>>> type(mans_mainigas)

Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    type(mans_mainigas)
NameError: name 'mans_mainigas' is not defined
>>> type(mans_mainigais)
<type 'float'>
>>> <type `int`>
SyntaxError: invalid syntax
>>> type(mains_mainigais)

Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    type(mains_mainigais)
NameError: name 'mains_mainigais' is not defined
>>> 
=============== RESTART: /home/user/rtr105/test_1_20180926.py ===============
 Cienamais lietotajs, lūdzo , ievadi skaitli :aaaaaaaa

Traceback (most recent call last):
  File "/home/user/rtr105/test_1_20180926.py", line 1, in <module>
    mans_mainigais = input (" Cienamais lietotajs, lūdzo , ievadi skaitli :")
  File "<string>", line 1, in <module>
NameError: name 'aaaaaaaa' is not defined
>>> 
=============== RESTART: /home/user/rtr105/test_1_20180926.py ===============
 Cienamais lietotajs, lūdzo , ievadi tekstu:Cccccccc
Lietotāj,tu esi ievadījis vērtību: Cccccccc
>>> 
=============== RESTART: /home/user/rtr105/test_1_20180926.py ===============
 Cienamais lietotajs, lūdzo , ievadi tekstu:ccc
Lietotāj,tu esi ievadījis vērtību: ccc
>>> sss

Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    sss
NameError: name 'sss' is not defined
>>> ccc

Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    ccc
NameError: name 'ccc' is not defined
>>> Cccc

Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    Cccc
NameError: name 'Cccc' is not defined
>>> 
=============== RESTART: /home/user/rtr105/test_1_20180926.py ===============
 Cienamais lietotajs, lūdzo , ievadi tekstu:
=============== RESTART: /home/user/rtr105/test_1_20180926.py ===============
 Cienamais lietotajs, lūdzo , ievadi tekstu:

