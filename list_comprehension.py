names = ['James',"John","Marthin","Jwings","Ghost"]
J_names = []
for name in names:
    if 'J' in name:
        J_names.append(name)
print(J_names)

J_name = [name for name in names if 'J' in name]
print(J_name)

animals = ['lion','tiger','monkey','elephant','frog']
filtered_animals = [i.title() for i in animals ]
print(filtered_animals)
