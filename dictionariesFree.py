cat = {
    "name": "Blekcil", "color": "Black and White", "fur": "Short"
}

cat["name"] = "Cimot"

print(cat["name"]) # panggil name
print(cat.get("color")) # panggil color

catCopy = cat.copy()

cat.popitem() # hapus item terakhir
cat.pop("name") # menghapus nama
print(cat)

cat["food"] = "Whiskas"

print("color" in cat)

print(list(cat.keys())) # nunjukin keys nya ada apa aja
print(list(cat.values())) # nunjukkin value nya ada apa aja
print(list(cat.items())) # nunjukkin keduanya 
# gausa pake func list tetep bisa

del cat["color"] # hapus dengan del

print(cat)
print(catCopy)