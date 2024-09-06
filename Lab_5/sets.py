# Given sets A and B
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

# I. Join A and B (Union of A and B)
A_union_B = A.union(B)
print("Union of A and B:", A_union_B)

# II. Find A intersection B
A_intersection_B = A.intersection(B)
print("Intersection of A and B:", A_intersection_B)

# III. Is A subset of B
is_A_subset_of_B = A.issubset(B)
print("Is A a subset of B?", is_A_subset_of_B)

# IV. Are A and B disjoint sets
are_A_and_B_disjoint = A.isdisjoint(B)
print("Are A and B disjoint sets?", are_A_and_B_disjoint)

# V. Join A with B and B with A
A_join_B = A.union(B)
B_join_A = B.union(A)
print("Join A with B:", A_join_B)
print("Join B with A:", B_join_A)

# VI. What is the symmetric difference between A and B
A_symmetric_difference_B = A.symmetric_difference(B)
print("Symmetric difference between A and B:", A_symmetric_difference_B)

# VII. Delete the sets completely
del A
del B

# Uncomment the lines below to check if the sets are deleted (this will raise an error)
# print(A)  # This will raise a NameError because A is deleted
# print(B)  # This will raise a NameError because B is deleted
