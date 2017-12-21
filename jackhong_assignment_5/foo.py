import numpy as np

def foo(a,b=3):
    return np.sqrt(a + b)

def bar(c=1.2, d=np.pi):
    print("d={}".format(d))
    return d**3

def foobar(x):
    x += 1
    return x

m = foo(1)
n = foo(3)
o = foo(a=-1.23)
p = foo(1,b=42)

q = bar()
r = bar(d=-np.pi)

s = foo
t = bar
u = s(1,2)
v = bar(c=foo)
