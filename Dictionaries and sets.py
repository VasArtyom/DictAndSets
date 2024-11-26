
my_dict = {"A" : 11, "B" : 22}
print(my_dict)
print(my_dict["B"])
my_dict.update({"C" : 33, "D" : 44})
del my_dict["A"]
print(my_dict)

my_set = {1, (1.1, 2.2), 2, True, 2, "BOB", 3, True, 3, 1, "BOB", (1.1, 2.2)}
print(my_set)
my_set.add(5)
my_set.add("18")
my_set.remove(1)
print(my_set)