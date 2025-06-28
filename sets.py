#Sets
'''
my_sets = {1, 2, 3, 4, 5}

print(my_sets)

my_sets.add(6)

print(my_sets)
my_sets.remove(2)
print(my_sets)  

'''

set1 = {1, 2, 3}
set2 = {3,4 , 5}

#Union
union_sets = set1.union(set2)
print(union_sets)

#Intersection
inter_sets = set1.intersection(set2)
print(inter_sets)

#Difference
diff_sets = set1.difference(set2)
print(diff_sets)    