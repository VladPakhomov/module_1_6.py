my_dict = {'Kolya' : 1948,'Alla' :1951,'Sveta' : 1975,'Kirill' : 1977 }
print(my_dict)
print(my_dict['Alla'])
my_dict['Sasha'] = 1979
print(my_dict)
my_dict.update({'Max':1980,'Ivan':1981})
del my_dict['Kolya']
print(my_dict.get('Kolya'))
print(my_dict)
a = my_dict.pop('Sveta')
print(my_dict)
print(a)
my_set = {12.35,'string',1,2,3,4,4,1,2}
print(my_set)
my_set.add(8)
my_set.add(23.45)
my_set.remove('string')
print(my_set)



