#sets do not care about the order of the objects

#empty set
s = set()

#add elements to set
s.add(1)
s.add(2)
s.add(3)
s.add(4)

print(s)

#a set never contains two or more identical objects
s.add(3)
print(s)

s.remove(2)
print(s)

print(f"The set has {len(s)} elements.")

