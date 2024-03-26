names = ['andi', 'benny', 'chika', 'doni', 'evi']
my_name = "bennedict"

# for i in range(len(names)):
#     names[i] = names[i].capitalize()
# print(names)

def cap_name(name):
    return name.capitalize()

proper_name = map(cap_name,my_name)

print(proper_name)
print(list(proper_name))