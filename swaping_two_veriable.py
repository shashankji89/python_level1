print("how to swap to veriable")
#the example is using third veriable
x=4
y=3
temp=x
print("the value of temp variable: ",temp)
x=y
print("the value of x is", x)
y=temp
print("the value of y is", y)

#now the example is without using third veriable
xx=12
yy=13
xx, yy=yy, xx
print("the value x is", xx)
print("the value y is", yy)