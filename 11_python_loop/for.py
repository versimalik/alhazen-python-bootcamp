names = ["Andy", "Abby", "Benny"]
for name in names:
  print(name)

for i in range(10):
  print("i like python!")

#for break
for i in range(1,10):
  print(i)
  if i == 3:
    break


#for continue
for i in range(1,10):
  if i == 3:
    continue
  print(i)

#for else
name = "Jaka"
for letter in name:
  print(letter)
else:
  print(f"{name} latters are printed")


#for pass
for i in range(10):
  pass