people = [
    {"name":"Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slyytherin"}
]

def f (person):
    return person["name"]

people.sort(key=f)
print(people)

#Alternatively
people.sort(key=lambda person: person["house"])
print(people)