# a,b,c=(12,45,89,2)
# print(a)
# print(b)
# print(c)
# ##  error - a,b,c=(12,45,89,2)
# ## ValueError: too many values to unpack (expected 3)

# a,b,c=(12,4)
# print(a)
# print(b)
# print(c)
#  a,b,c=(12,4)
# ValueError: not enough values to unpack (expected 3, got 2)

# u can store var no. of args via * 
a,b,*c,d=(12,45,89,2,90,7)
print(a)
print(b)
print(c)
print(d)
##  op- 12,
# 45,
# [89,2,90]
# 7

# if u dont want to store those values in variable. use _
a,b,*_,d=(12,45,89,2,90,7)
print(a)
print(b)
# print(c)
print(d)
# op - 12
# 45
# 7

