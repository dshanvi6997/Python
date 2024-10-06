# union and update

name = {'ram', 'sham', 'rohan', 'sham'}
name2 = {'rahim', 'shetty', 'rohan', 'ronak'}

# final_name = name.union(name2)
# print(final_name)

name.update(name2)
print(name)

# intersection and intersection_update()

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# cities3 = cities.intersection(cities2)
# print(cities3)


# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# cities.intersection_update(cities2)
# print(cities)

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# cities3 = cities.symmetric_difference(cities2)
# print(cities3)

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# cities.symmetric_difference_update(cities2))
# print(cities)

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Seoul", "Kabul", "Delhi"}
# cities3 = cities.difference(cities2)
# print(cities3)

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Seoul", "Kabul", "Delhi"}
# cities3 = cities2.difference(cities)
# print(cities3)

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Seoul", "Kabul", "Delhi"}

# Modifies 'cities' in place
# print(cities.difference_update(cities2))

# Now print the modified set
# print(cities)

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# cities3 = {"Toakyo", "Madarid", "Bearlin", "Delahi"}
# print(cities.isdisjoint(cities3))


# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Seoul", "Kabul"}
# print(cities.issuperset(cities2))
# cities3 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# print(cities.issuperset(cities3))

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Delhi", "Madrid"}
# print(cities2.issubset(cities))

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities.add("Helsinki")
# print(cities)

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Helsinki", "Warsaw", "Seoul"}
# tuples = (1,3,5,7)
# names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
# cities.update(tuples)
# cities.update(names)
# # cities.update(cities2)
# # print(cities)

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities.remove("Tokyo")
# print(cities)

# citiess = {"Madrid", "Berlin", "Delhi"}
# citiess.remove("Tokyo")
# print(citiess)

# cities = {"Madrid", "Berlin", "Delhi"}
# cities.discard("Tokyo")
# print(cities)

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# item = cities.pop()
# print(cities)
# print(item)


# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# del cities
# print(cities)

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities.clear()
# print(cities)

# info = {"Carla", 19, False, 5.9}
# if "Carla" in info:
#     print("Carla is present.")
# else:
#     print("Carla is absent.")

# list = [4,2,5,3,6,1,2,1,3,2,8,9,7]
# if 9 in list:
#     print("7 is present.")
# else:
#     print("7 is absent.")

# tuples = ('apple', 'orange', 'green')
# if 'orange' in tuples:
#     print("orange is present.")
# else:
#     print("orange is absent.")
