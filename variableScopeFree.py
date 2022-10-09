age = 8

def test():
    print(age)

print(age) #8
test() #8



def test():
    age = 8
    print(age)

print(age) #error karena age=8 berada di dalam fungsi
test() #8