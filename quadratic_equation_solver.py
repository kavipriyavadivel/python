import cmath
def getRoots(a,b,c):
    dis=b**2 - (4*a*c)
    root1=((-b)+cmath.sqrt(dis))/2*a
    root2=((-b)-cmath.sqrt(dis))/2*a
    return root1,root2#(-0.5 + 0.86602...i)

a=int(input())
b=int(input())
c=int(input())
root1,root2=getRoots(a,b,c)
if root1.imag != 0:
    print(f"Root1: {(root1.real,root1.imag)}")
else:
    print(f"Root1: {root1.real}")
if root2.imag != 0:
    print(f"Root2: {(root2.real,root2.imag)}")
else:
    print(f"Root2: {root2.real}")