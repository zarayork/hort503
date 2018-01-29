# create a mapping of state to abbreviation
states = {
    'Washington': 'WA',
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'WA': 'Seattle',
    'FL': 'Jacksonville'
}

#Add counties.
counties = {
    'WA': 'Snohomish',
    'WA': 'King',
    'WA': 'Whatcom',
    'WA': 'Whitman',
    'WA': 'Spokane',
    'WA': 'Chelan',
    'WA': 'Skagit'
}

cities['Snohomish'] = 'Startup',
cities['Snohomish'] = 'Sultan'
cities['Snohomish'] = 'Monroe'
cities['King'] = 'Seattle' 'Skykomish'
cities['Whitman'] = 'Pullman' 'Colfax'
cities['Spokane'] = 'Spokane' 'Cheney'
cities['Chelan'] = 'Leavenworth' 'Peshastin' 'Cashmere' 'Wenatchee'
cities['Skagit'] = 'Mt Vernon'
cities['Whatcom'] = 'Bellingham'

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print('-' * 10)
print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])

# print some states
print('-' * 10)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

# do it by using the state then cities dict
print('-' * 10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

# print every state abbreviation
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

# print every city in state
print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

# now do both at the same time
print('-')
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and county {counties[abbrev]} has city {cities[abbrev]}")


print('-' * 10)
# safely get a abbreviation by state that might not be there
state = states.get('Texas')

if not state:
    print("Sorry, no Texas.")

# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print(f"The city for the state 'TX' is: {city}")
