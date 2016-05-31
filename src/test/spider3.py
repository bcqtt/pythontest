'''
Created on 2016年5月30日

@author: gionee
'''
from _collections import deque

queue = deque(["美女","帅哥","二次元"])
queue.append("电影")
queue.append("新闻")
print(queue.pop())

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)

print('apple' in basket)
print('aaa' in basket)


a = set('abracadabra')
b = set('alacazam')
print(a)
print(b)
print(a|b)
print(a-b)
print(b-a)
print(a&b)
print(a^b)