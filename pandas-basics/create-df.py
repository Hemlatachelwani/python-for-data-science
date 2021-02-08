import pandas as pd

myd={ 'cars': ["Bmw","polado"],
       'tyre':[4,888]}
df=pd.DataFrame(myd)
print(df)
print(pd.__version__)

Output:
     cars  tyre
0     Bmw     4
1  polado   888
0.24.2 <- Version of pandas

P.S.: 
If myd={ 'cars': ["Bmw","polado"],
       'tyre':[4,888,6]}
Then got the error 
raise ValueError('arrays must all be same length')
ValueError: arrays must all be same length
