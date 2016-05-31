'''
Created on 2016年5月27日

@author: gionee
'''
from test.Cat import Cat

class Employee:
    
    __name = ''
    __age = 0
    __email = ''
   
    def __init__(self,n,a,e):
        self.__name = n
        self.__age = a
        self.__email = e
    
    def getName(self):
        return self.__name
    
    def doSome(self):
        cat = Cat()
        cat.doSome()
    
emp = Employee("小明",6,"abc@123.com")
print(emp.getName())
emp.doSome()
