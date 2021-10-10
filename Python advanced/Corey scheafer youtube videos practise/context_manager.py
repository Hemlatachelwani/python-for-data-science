with open('f_strings.py','r') as f:
    file_contents=f.read()

words=file_contents.split(' ')
print(len(words))

# when u have to read files, rather than read n write each n every time. u can use this.

