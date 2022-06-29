import os
a = os.getcwd()
b = os.path.join(a,"币制对照表")
c = os.path.dirname(os.path.realpath(__file__))
print(a)
print(b)
print(c)