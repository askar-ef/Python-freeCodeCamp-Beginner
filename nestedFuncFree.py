# cara panjang
def talk(phrase):
    def say(word):
        print(word)

    words = phrase.split(" ")
    for word in words:
        say(word)

talk("i am going to buy the milk")

# cara lebih pendek
def talk(phrase):
    words = phrase.split(" ")
    for word in words:
        print(word)

talk("i am going to buy the milk")

# contoh lain
def counter():
    count = 0

    def increment ():
        nonlocal count
        count = count + 1
        return count
    
    return increment

increment = counter()

print(increment())
print(increment())
print(increment())

