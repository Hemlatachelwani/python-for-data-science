import re

str="Hi! My name is hemlata!!"
pattern="is"  # Sub string

srch_op=re.search(pattern,str)
match_op=re.match(pattern,str)
print(srch_op)
print(match_op)