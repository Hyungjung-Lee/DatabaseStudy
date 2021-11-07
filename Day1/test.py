

print("="*50)
print("my program")
print("="*50)

odd = [1,2,3,4,5]

odd[4] = 6 

odd.append(10)

odd[odd.index(10)]

odd.insert(0,12)

odd.pop()

odd.pop(0)

odd += [4,5]

tup =  (1,2,3,4,5,10)

tup.index(10)

tup[1:]

dic = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}

dic.keys()
dic.values()

for k in dic.keys():
    print(k)

dic.items()

for k,i in dic.items():
    print(k,i)

dic.items()

dic.get('name','sex')

dic = {'name':['김득화','나아름','김현수'],'sex' : ['M','F','F']}


for i in dic.keys():


a = 'Hello'

set(a)

type(dic)

id(a)

a = [1,2,3,4,5]
b = a


b

a.append(6)


a ={'국어':80,'영어':75,'수학':55}

type(a.values())

import numpy as np 