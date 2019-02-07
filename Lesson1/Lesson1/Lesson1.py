import sys
sys.path.append('../')
import module1 
import socket

def arr(x): #recieve array reference
    x[0] = 33

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.bind(("127.0.0.1", 12345))

print("Server is listening...")
c.listen(1)
csock, caddr = c.accept()
print("client connected", caddr)
csock.sendall("Hello dear client")
message = csock.recv(10)
print("Got message from client:")

'''
p = [1,5,"alex"] #array
a = p # reference to same array
#a = list(p) #copy of array
arr(p)
print(p)
print(a)
'''

'''
def func1(x):
    print("func1!!!", x)
    return 5, 6, "erez"

    
#a = int(input("please enter number:"))
#print(type(a))
a,b,c = func1("str")
print(a)
print(b)
print(c)
module1.func2()
'''




# comment
'''
if False:
    print("hello ")
    print("dodo")
elif a == 5:
     print("4")
else:
    print("5")
'''
'''
for i in range(3, 10, 2): #start from 3 untill 10 ( not included) in step of 2
    print(i)

a = "erez"
x = ""
for c in a:
    #print(c, " ") #for each character in "a" print character and next line
    x = x + c + " "
print (x)

print (type(c))
a = 1
while a < 10:
    print(a)
    a = a + 1
'''
