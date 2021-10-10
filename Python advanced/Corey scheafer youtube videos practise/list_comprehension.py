# if __name__ == '__main__':
#     x = int(input())
#     y = int(input())
#     z = int(input())
#     n = int(input())
#     newlist=i for i in range(0,x+1) for j in range(0,y+1) for z in range(0,z+1) if i+j+k !=n
#     print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)