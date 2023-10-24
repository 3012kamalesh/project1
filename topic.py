##user_input=str(input("Enter the words"))
##words=user_input.split()
##a=""
##for i in words:
##    a=a+i[0].upper()
##print(a)        

##adding the two number:
def add(a,b):
    return a+b
##subtaract the two number:
def sub(a,b):
    return a-b
##multiply the two number:
def multi(a,b):
    return a*b
##divisible the two number:
def divide(a,b):
    if a==0 or b==0:
        print("please enter the valid no")
    else:
        print(a/b)
print("enter add the two number")
print("enter sub the two number")
print("enter multiply the two number")
print("enter divide the two number")
num=int(input("enter the number"))
num1=int(input("enter the number"))
c=input("enter the opition add, sub ,multiply ,division :")
if(c =="add"):
    print(add(num,num1))
elif(c =="sub"):
    print(sub(num,num1))
elif(c =="multiply"):
    print(multi(num,num1))
elif(c=="division"):
    divide(num,num1)
else:
    print("invalid no")

   















