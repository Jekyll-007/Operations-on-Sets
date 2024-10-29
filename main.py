my_set={1,1,2,2,2,3,4,5,5,5,6,7,8,9,9}
print(my_set)
my_set.add(10)
print("updated set",my_set)
my_set2={1,2,11,12,13,14,15,11}
my_set3=my_set.intersection(my_set2)
print(my_set3)
my_set4=my_set.union(my_set2)
print(my_set4)