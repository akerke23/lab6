"""
#1 есеп  

list = ["Myrzaly", "Akerke", "Sabitkyzy"]
tuple = ("Kazakhstan", "Almaty")
set = {"Satbayev University", "Software Engineering", "Computer Science"}
dict = {"IIN": "020323601354", "Phone number": "87078335178"}
print("Лист: ", list)
print()
print("Кортеж: ", tuple)
print()
print("Коллекция: ", set)
print()
print("Словарь: ", dict)
print()



#2 есеп 

list = ["Myrzaly", "Akerke", "Sabitkyzy"]
tuple = ("Kazakhstan", "Almaty")
set = {"Satbayev University", "Software Engineering", "Computer Science"}
dict = {"IIN": "020323601354", "Phone number": "87078335178"}

print("\n", "Лист")
print("\n", list)

list.append("kazakh") 
print("\n", list)

x = "23.03.2002"
list.insert(3, x) 
print("\n", list)

list.pop(4) 
print("\n", list)

#-----------------------------------------------------------------------------

print("\n", "Кортеж")
print("\n", tuple)

tuple2 = ("Kazakhstan", "Astana")
tuple3 = tuple + tuple2
print("\n", tuple3)
print("\n", tuple3.count("Kazakhstan"))

print("\n", tuple3.index("Astana"))

#-----------------------------------------------------------------------------

print("\n", "Коллекция")
print("\n", set)

set.add("GPA: 3.5")
print("\n", set)

set.remove("Software Engineering")
print("\n", set)

print("\n", len(set))

set2= {"Satbayev University", "cybersecurity", "Information Security System"}
print("\n", set2)
print("\n", set.difference(set2))

#-----------------------------------------------------------------------------

print("\n", "Словарь")
print("\n", dict)

dict["Home number"] = "274-34-23"
print("\n", dict)

dict.pop("IIN")
print("\n", dict)

v = dict.get("Phone number")
print("\n", v)

k = dict.keys()
print("\n", k)


#5 есеп Словарь синонимов

dict = {}
n = int(input())
for i in range(n):
    firstword, secondword = input().split()
    dict[firstword] = secondword
    dict[secondword] = firstword
print(dict[input()])

"""

#6 есеп Выборы в США ( поменяйте все на выброры в Казахстане) 

total_votes = {}
for _ in range(int(input())):
    name, votes = input().split()
    total_votes[name] = total_votes.get(name, 0) + int(votes)
for name, votes in sorted(total_votes.items()):
    print("Результат: ", name, votes)

