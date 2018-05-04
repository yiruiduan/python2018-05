#Author:yiruidaun
def talk(self):
    print("%s is wangwangwang!!!!"%self.name)
class Dog(object):
    def __init__(self,name):
        self.name=name
    def eat(self,food):
        print("%s is eatting %s"%(self.name,food))


d=Dog("wangcai")
choice=input(">>:").strip()
print(d.name)
try:
    # attr=getattr(d,choice)
    # setattr(d,choice,"yiruiduan")
    delattr(d,choice)
except AttributeError:
    # setattr(d,choice,talk)        #动态添加方法
    # getattr(d,choice)(d)          #getattr获取的是一个方法，返回的就是这个方法的内存地址，
    setattr(d,choice,"hello")            #动态添加属性
    print(getattr(d,choice))   #getattr获取的是一个属性，返回的就是这个属性的值
    delattr(d,choice)

print(d.name)
print(getattr(d,choice))