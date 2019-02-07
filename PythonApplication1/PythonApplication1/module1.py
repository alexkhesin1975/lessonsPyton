'''
Python 3.6 (32-bit) interactive window [PTVS 15.9.18254.1-15.0]
Type $help for a list of commands.
l = (2,3)
type(l)
<class 'tuple'>
ls
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'ls' is not defined
dir
<built-in function dir>
e = {"name": "erez", "age": 29, "height": 190}
e
{'name': 'erez', 'age': 29, 'height': 190}
type(e)
<class 'dict'>
e[0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 0
e["name"]
'erez'
e["age"]
29
e["age"] = 50
e["age"]
50
e["weight"] = 75
e.values()
dict_values(['erez', 50, 190, 75])
e.keys()
dict_keys(['name', 'age', 'height', 'weight'])
e
{'name': 'erez', 'age': 50, 'height': 190, 'weight': 75}
e = {"Person1":["erez", 50, 190, 75], "Person2":["alex",22,200,85]}
e
{'Person1': ['erez', 50, 190, 75], 'Person2': ['alex', 22, 200, 85]}
e["Person1"]
['erez', 50, 190, 75]
e["Person1"][3]
75

e = {"erez" : {"age": 19, "height":100}, "alex": {"age":18, "height":200}}
e
{'erez': {'age': 19, 'height': 100}, 'alex': {'age': 18, 'height': 200}}
e["alex"]
{'age': 18, 'height': 200}
e["alex"]["age"]
18
'''