age=10.3
#print(a)
name="suma"
boolean=True
#print(name)

name="suma sree"
#print(name[50])
#print(len(name))

#a=eval(input("enter a number-->"))
#b=eval(input("enter b number-->"))
#print(a+b)
#print(complex(7,8))

a=5
b=10
c=8
#print('a+b=',a+b,'a-b=',a-b,'a/b=',a/b,'a*b=',a*b,'a%b=',a%b)
#print(a>=b)
#print(a<b)
#print(a<b and a>b)
#print(a>b and a<=c)
#print(bin(a))
#list=["apple","mango","orange"]
#print("berry" in list)
#print("mango" not in list)
str="tom"
name="Tom"
#print(str is name)
#print(str is not name)

'''if 3>2:
    print("this is if block")
    print("this is main")
marks=10
if marks>=25:
    print("pass")
else:
    print("fail")'''

'''
marks=eval(input("enter ur marks"))
if marks>=80:
     print("dis")
elif marks>=60 and marks<=79:
         print("1st class")
elif marks>=40 and marks<=59:
             print("2nd class")
elif marks>=25 and marks<=39:
                 print("3rd class")
elif marks>=1 and marks<=24:
                     print("faild")
else:
    print("ur absent")'''

#for i in range(5,15):
   # print(i)

#for i in range(0,100,2):
    #print(i)

'''list=["car","bike","scooty","lory","train","bus"]
for i in list:
    #print(i)
    for j in range(4):
        print(i,j)'''
'''
i=1
while(i<=4):
    print(i)
    i=i+1'''

'''for i in range(10):
    if i == 5:
        break
    print(i)'''
'''
for i in range(11):
    if i == 6:
        continue
    print(i)'''
    

'''name1="aarun"
name1="T"+name1[5:]
print("name1=",name1)


print("id of name_1 = ", id(name1))'''

'''
x=("red","blue","green")
y=list(x)
y[1]="kiwi"
x=tuple(y)
print(x)
print("id of x=",id(x))
print("id of y=",id(y))'''

'''
str="ramarao"
#str1=str+"rao"
#print(str1)
#print(str[0])
#print(str[-2])
#print(str[1:6])
#print(str[-7:-2])
#print(str[::-1])
#print(str[-4:-7:-1])

#print(str.capitalize())
#print(str.count('a'))
#print(str.index('m'))
#print(str.isalnum())
#print(str.isalpha())
#print(str.replace('r','j'))
#print(str.replace('a','r',2))
#str1="virat kohli"
#li=str1.split("virat")
#print(li)'''


list=["shaik","mansoor","damodar","mounika",34,55]
#print(list)
#print(list[0])
#print(list.sort)
#for i in list:
    #print(i)

#list.append("sree")
#list.clear()
#list1=list.copy()
#print(list.count("mounika"))
#list1=["aishwarya","divya","rk"]
#list.append(list1)
#list.extend(list1)
#print(list1.index("rk"))
#list.insert(4,"manasa")
#list.pop()
#list.remove("damodar")
#list.reverse()
#list.sort()
#print(list.index("mounika"))
#print(list)'''


'''
tuple=("tom","sam",2)
print(tuple.count("sam"))
print(tuple.index("tom"))
print(tuple)'''

'''
set={"apple","mango","orange","berry","mango","peach1"}
set1={"apple","orange","berry","tomato","onion","peach"}
set2={"apple","orange","berry","tomato","pumpkin"}
set3={"apple","mango"}
grp1={"ram","tom","bheem","nbk","virat"}
grp2={"ram","pk","mb","nbk","ntr"}
#set.add("cherry")
#set.clear()
#print(set1.difference(set))
#print(set1)
#set1.difference_update(set)
#print(grp2.difference(grp1))
#print(grp2.difference_update(grp1))
#print(grp2)
#print(set1)
#print(set)
#set.discard("apple")
grp3={}
grp3=set.intersection(set1)
#print(grp3)
#print(set.intersection(set1))
#print(set)
#print(set.intersection_update(set1))
#print(set.isdisjoint(grp1))
#print(set.clear())
#print(set.issubset(grp1))
#set.pop()
#set.remove("peach1")
#print(set.discard("apple"))
#print(set.union(set1,grp2))
#set.update(grp2)
print(set)'''


dict={"name":"tom","name":"bheem","age":45,"city":"hyd",24:56}
#print(dict["city"])
#dict["name"]="sam"
#dict.clear()
#dict1=dict.copy()
#print(dict.get("city"))
#list=dict.items()
#print(type(list))
#print(dict.keys())
#print(dict.pop("city"))
#print(dict.popitem())
#dict.setdefault("weight",100)
#dict.update({"email":"damos@gmail.com","phone":123456766454767879})
print(dict.values())
print(dict)
