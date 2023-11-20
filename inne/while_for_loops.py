i = 1
while i < 5:
    print (i)
    i = i + 1
print ("The end")


name = "Zuza"
for x in name:
    print(x)

name_surname = ["Zuzanna", "Wojtowicz"]
for x in name_surname:
    print(x)


#Control flow

 #break
i = 1
while i < 5:
    print(i)
    if i == 3:
        break
    i = i + 1
print ("The end")

 #continue
word_list = ["wyrewolwerowny", "rewolwerowiec", "z", "rozentuzjazmowanego", "tłumu"]
for name in word_list:
    if name == "rozentuzjazmowanego":
        continue
    print(name)
print("The end")
