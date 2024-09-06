# Given person dictionary
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# I. Check if the person dictionary has a 'skills' key, if so print the middle skill
if 'skills' in person:
    skills = person['skills']
    middle_skill = skills[len(skills) // 2]  # Find the middle skill
    print("Middle skill:", middle_skill)

# II. Check if the person dictionary has 'skills' key, if so check if the person has 'Python' skill
if 'skills' in person:
    has_python = 'Python' in person['skills']
    print("Has Python skill:", has_python)

# III. Determine if the person is a front end, back end, or fullstack developer
if 'skills' in person:
    skills = person['skills']
    
    if 'JavaScript' in skills and 'React' in skills and len(skills) == 2:
        print('He is a front end developer')
    elif 'Node' in skills and 'Python' in skills and 'MongoDB' in skills:
        print('He is a backend developer')
    elif 'React' in skills and 'Node' in skills and 'MongoDB' in skills:
        print('He is a fullstack developer')
    else:
        print('Unknown title')

# IV. Check if the person is married and lives in Finland
if person['is_marred'] and person['country'] == 'Finland':
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married.")
