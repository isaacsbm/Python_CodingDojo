# 1 Update Values in Dictionaries and Lists
x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0]=15
students[1]['last_name']='Bryant'
z[0]['y']=30

# 2 Iterate Through a List of Dictionaries
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
for each_student in range(len(students)):
    first_name=students[each_student]['first_name']
    last_name=students[each_student]['last_name']
    full_name="First_Name - "+ first_name+ ", Last_Name - " + last_name
    print(full_name)

# 3 Get Values from a List of Dictionaries

def iterate_dictionary(key_name,some_list):
    for dictionary in some_list:
        if key_name in dictionary:
            print(dictionary[key_name])

#4 Iterate Through a Dictionary with List Values
def print_info (dict):
    for some_key in dict:
        print(f"{some_key}-{len(dict[some_key])}")
        for some_value in dict[some_key]:
            print(some_value)