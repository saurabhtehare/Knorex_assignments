# defining  the states and phone prefix
states = ['Alabama,205',
'Alaska,907',
'Arizona,480',
'Arkansas,479',
'California,209',
'Colorado,303',
'Connecticut,203',
'Delaware,302',
'District of Columbia,202',
'Florida,239']

# usorted list of phone numbers
phone_nos = ['205-187-3946',
'205-255-6983',
'479-172-2272',
'239-911-4469',
'205-938-8632',
'480-364-9536',
'205-662-8389',
'479-742-6763',
'479-896-3819',
'480-468-6769',
'907-314-9167',
'205-374-9162',
'479-142-6152',
'907-146-9975',
'479-117-4115',
'907-683-7493',
'239-499-7963',
'239-486-9335',
'480-132-7865',
'907-316-9144'
]


# creating a dictionary to map prefix to state names
state_prefix = {}
for i in states:
    state, prefix = i.split(",")
    state_prefix[prefix] = state # mapping prefix to that state

# group phone number by state, so creating dictionary
state_phones = {}
for phone in phone_nos:
    prefix = phone.split("-")[0]
    state = state_prefix.get(prefix)
    if state:
        state_phones.setdefault(state, []).append(phone) # adding phone number to the state's list

# sorting the states alphabetically
sorted_states = sorted(state_phones.keys())
# list for final sorted o/p
sorted_output = []
# for state and sorted phone number
state_phone_mapping = []



for state in sorted_states:
    sorted_numbers = sorted(state_phones[state]) # sorting phone number within the states
    sorted_output.extend(sorted_numbers) # adding sorted phone numbers to final output
    for phone in sorted_numbers: # map each phone number to its states
        state_phone_mapping.append((state,phone))


# column headers
print("{:<30} {:20}".format("STATES","SORTED OUTPUT"))
print("-"*50)

# printing each state and its sorted phone numbers
for state, phone in state_phone_mapping:
    print(f"{state:<30} {phone:<20}")