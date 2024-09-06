# Given sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# I. Find the length of the set it_companies
it_companies_length = len(it_companies)
print("Length of it_companies set:", it_companies_length)

# II. Add 'Twitter' to it_companies
it_companies.add('Twitter')
print("IT companies after adding 'Twitter':", it_companies)

# III. Insert multiple IT companies at once to the set it_companies
it_companies.update({'Netflix', 'Tesla', 'Adobe'})
print("IT companies after adding multiple companies:", it_companies)

# IV. Remove one of the companies from the set it_companies
it_companies.remove('Oracle')  # You can replace 'Oracle' with any other company in the set
print("IT companies after removing 'Oracle':", it_companies)

# V. Difference between remove and discard
# Explanation:
"""
- `remove()` will raise a KeyError if the item to remove is not present in the set.
- `discard()` will not raise any error, even if the item is not present in the set.
Example:
"""
it_companies.discard('Yahoo')  # Does nothing because 'Yahoo' is not in the set, no error
print("IT companies after discarding 'Yahoo' (which is not present):", it_companies)

# Uncomment to see the KeyError
# it_companies.remove('Yahoo')  # This would raise a KeyError because 'Yahoo' is not in the set
