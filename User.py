#under heavy work warning

#intro
"""
    to create User custom config file in a binary
"""
    
import pickle

class user_add:
    def __init__(self,user_name,user_password):
        self.user_name=user_name 
        self.user_password=user_password

'''
p1 = user_add("John", 36)

print(p1.user_name)
print(p1.user_password)
'''
my = MyClass("someone")
pickle.dump(my, open("myobject", "wb"))
me = pickle.load(open("myobject", "rb"))
me.display()
