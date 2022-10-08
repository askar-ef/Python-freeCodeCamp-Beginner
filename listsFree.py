oneList = ["Choy", 12, "Reamur", 4.3, True]

oneList[-1]=False
print(oneList[-1])

print(oneList)

# cara add di list
oneList.insert(2, "indeks 2") # add dengan menentukan indeksnya juga
print(oneList)
oneList[3:3] = ["indeks ke 3"]
print(oneList)

oneList.append("Oh no")
oneList.extend(["pizza", 12, 10])
oneList.extend("pizza")
oneList += ["iritasu"]

# menghapus di list
oneList.remove("Choy")
oneList.pop() # menghapus item terakhir pada list
print(oneList) 

Listing = (enumerate(oneList))

print(list(Listing))