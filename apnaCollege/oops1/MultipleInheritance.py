class A:
    varA="class A "
class B:
    varB="class B"
class C(A,B):
    varC="class C"

c1=C()
print(c1.varC)
print(c1.varB)
print(c1.varA)