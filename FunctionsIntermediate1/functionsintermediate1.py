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

x[1][0] = 15

print(x)

students[0]['last_name'] = 'Bryant'

print(students[0])

sports_directory['soccer'][0] = 'Andres'

print(sports_directory['soccer'])

z[0]['y'] = 30

print(z[0]['y'])



students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]




def iterateDictionary(some_list):
    strname = ''
    for x in range(0, len(some_list)):
        y = 0
        for key, value in some_list[x].items():
            strname += key + " - " + value
            if (y != 1):
                strname += ", "
                y = y + 1
        print(strname)
        strname = ''

    

iterateDictionary(students)



def iterateDictionary2(key_name, some_list):
    for x in range(0, len(some_list)):
        print(some_list[x][key_name])

iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)


dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(d):
    x = 0
    for key, values in d.items():
        print(key.upper())
        for value in values:
            print(value)



printInfo(dojo) 







