# 'r' reading only a file
# 'w' writing only a file
# 'a' append only a file
# 'r+' is for reading & writing
# 'w+' is for writing and reading(over rides existing file)



with open ('vanilla.txt',mode = 'w') as f:
    f.write("I have created this file")

with open('vanilla.txt',mode = 'r') as f:
    print(f.read())