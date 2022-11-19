'''set1={"A","B","C","D"}
set2={"A","B","C","D","E","F"}
#print(set)

#set.add("cherry")
#print(set)

#set.clear()
#print(list)


print("before", set1)
print(set1.difference(set2))
print("after", set1)'''


set={"apple","mango","orange","berry","mango","peach1"}
set1={"apple","orange","berry","tomato","onion","peach"}
set2={"apple","orange","berry","tomato","pumpkin"}
set3={"apple","mango"}
grp1={"ram","tom","nbk","virat"}
grp2={"ram","pk","mb","nbk","ntr"}

#print(type(set))

#set.add("cherry")
#print(set)


#set.clear()
#print(set)

#print(set1.difference(set))
#print(grp2.difference_update(grp1))
#print(grp2)
#set1.difference_update(set)
#print(set1)

#set.discard("apple")
#print(set)

#grp3=set.intersection(set1)
#print(grp3)
#print(set.intersection(set1,set2))
#print(set)
#print(set.intersection_update(set1))
#print(set2)

#print(set.isdisjoint(grp1))

#set.clear()

#print(set.issubset(grp1))

#set.pop()
#print(set)
#set.remove("peach1")
#print(set)

#print(set.union(set1,grp2))
#print(set)

set.update(grp2,set1)
print(set)
