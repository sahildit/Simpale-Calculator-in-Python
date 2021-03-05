def add(a,b):
	result=a+b
	print(result)

def sub(a,b):
	result=a-b
	print(result)

def mul(a,b):
	result=a*b
	print(result)

def div(a,b):
	result=a/b
	print(result)

a=int(input("enter the first number: "))
b=int(input("enter the second number: "))
operator=input("enter the operator:")

if operator=="+":
	add(a,b)
elif operator=="-":
	sub(a,b)
elif operator=="*":
	mul(a,b)
elif operator=="/":
	div(a,b)
else:
	print("invalid operator")

