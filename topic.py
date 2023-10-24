user_input=str(input("Enter the words"))
words=user_input.split()
a=""
for i in words:
    a=a+i[0].upper()
print(a)        
