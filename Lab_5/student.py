# Create a student dictionary
student = {
    'first_name': 'John',
    'last_name': 'Doe',
    'gender': 'Male',
    'age': 22,
    'marital_status': 'Single',
    'skills': ['Python', 'JavaScript'],
    'country': 'USA',
    'city': 'New York',
    'address': '123 Main St'
}

# I. Get the length of the student dictionary
student_length = len(student)
print("Length of the student dictionary:", student_length)

# II. Get the value of skills and check the data type
skills = student['skills']
print("Skills:", skills)
print("Data type of skills:", type(skills))  # It should be a list

# III. Modify the skills values by adding one or two skills
student['skills'].extend(['React', 'SQL'])
print("Updated skills:", student['skills'])

# IV. Get the dictionary keys as a list
keys = list(student.keys())
print("Dictionary keys:", keys)

# V. Get the dictionary values as a list
values = list(student.values())
print("Dictionary values:", values)

# VI. Change the dictionary to a list of tuples using items() method
student_items = list(student.items())
print("Dictionary as list of tuples:", student_items)

# VII. Delete one of the items in the dictionary (e.g., delete the 'city' key)
student.pop('city')
print("Dictionary after deleting 'city':", student)

# VIII. Delete the entire dictionary
del student

# Uncomment the line below to check if the dictionary is deleted (will raise an error)
# print(student)  # This will raise a NameError since the dictionary is deleted
