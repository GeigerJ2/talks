import os,sys

def  foo( x,y):print( x+y )

class bar:
 def __init__(self,a=1,b=2):self.a=a;self.b=b
 def baz(self):return self.a*self.b

if __name__=='__main__':
 foo(1,2)
 b=bar(3 ,4)
 print(b.baz())
