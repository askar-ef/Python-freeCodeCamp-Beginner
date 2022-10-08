items = ["abraham", "Alibaba", "Chocho", "ray", "Stevi", "STevi"]

# mengurutkan tanpa merubah listnya
print(sorted(items, key= str.lower))

# mengubah urutan listnya
items.sort()
print(items)

items.sort(key=str.lower)
print(items)

