# hasilnya akan True jika memiliki nilai, tapi jika tidak punya nilai (empty) maka False.
# hasilnya akan "yes"
done = True
done = 1
done = -1
# hasilnya akan "no"
done = False
done = ""
done = 0

if done:
    print("yes")
else:
    print("no")

# ingat, tetap string dan bukan booelan
done = "beau"
print(type(done) == bool)

# any dan all
# konsepnya seperti or dan and
tujuan = True
kendaraan = False
perjalanan = any ([tujuan, kendaraan])
print("any", perjalanan)
perjalanan = all([tujuan, kendaraan])
print("all", perjalanan)

