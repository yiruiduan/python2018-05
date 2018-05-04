#Author:yiruidaun
# import importlib
# mod_name="hello.aa"
# mod=__import__(mod_name)
# Name=mod.aa.C()
# print(Name.name)
# # Name=mod.aa.C()
# # print(Name.name)
# # instance=getattr(mod.aa,"C")
# # obj=instance()
# # print(obj.name)
# mod1=importlib.import_module(mod_name)
# print(mod1.C().name)
# class CALL:
#     def __call__(self, *args, **kwargs):
#         print("call")
# nihao=CALL()()







class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)

class MyList(list):
    __metaclass__ = ListMetaclass