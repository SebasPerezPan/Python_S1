
# Online Python - IDE, Editor, Compiler, Interpreter

def proc(a, b):
    for i in range(100):
        a[i] = i
        b[i] = i*2


a = [0]*100
b = [0]*100

proc(a,b)

print(a)
print(b)