# MRO: Method Resolution Order

#   object
#     |
#     A
#    / \
#   /   \
#  B     C
#   \   /
#    \ /
#     D

class A:
    num = 10

class B(A):
    pass

class C(A):
    num = 1

class D(B, C):
    pass

print(D.num)
print(D.mro()) # the order that is gonna back

#          object
#        /   |   \
#       /    |    \
#      X     Y     Z
#       \   / \   /|
#         A     B  |
#          \   /   |
#            M ----

class X: pass
class Y: pass
class Z: pass
class A(X, Y): pass
class B(Y, Z): pass
class M(B, A, Z): pass

print(M.__mro__) # the algorithm used for MRO is Depth First Search (DFS)