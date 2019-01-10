
# Define a dictionary that contains information about several members of your family. Use the following example as a template.

my_family = {
    'father': {
        'name': 'Greg',
        'age': 56
    },
    'mother': {
        'name': 'Karen',
        'age': 54
    },
    'sister': {
        'name': 'Hannah',
        'age': 27
    },
    'brother': {
        'name': 'Eli',
        'age': 15
    }
}

# Using a dictionary comprehension, produce output that looks like the following example:
# Krista is my sister and is 42 years old

family_text = {f"{v['name']} is my {k} and is {v['age']} years old" for (k, v) in my_family.items() }

print(family_text)

