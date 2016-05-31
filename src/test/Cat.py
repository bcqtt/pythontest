'''
Created on 2016年5月27日

@author: gionee
'''
class Cat:
    name = None
    age = None
    
    def __init__(self):
        self.name = "小猫咪"
        self.age = 1
    
    def doSome(self):
        print("!!!!!")
        
cat = Cat()
cat.doSome()
print("%s 现在  %d 岁。" % (cat.name, cat.age))




    