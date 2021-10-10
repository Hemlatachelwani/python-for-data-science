names=["hema","kiru","tina"]
country=["india","us","uk"]
universs=["Marvel","sweden"]
index=0
for i in names:
   print(index,i)
   index+=1

#instead of above solution. we can use zip which can be used for as many lists as possible.
# we can use enumerate when
for nm in enumerate(names):
     print(nm)
for index,nm in enumerate(names,start=1):
     print(index,nm)
for nm in enumerate(names,start=1):
     print(index,nm)

for nm,c,u in zip(names,country,universs):
     print(f'{nm} lives in {c} - {u}')