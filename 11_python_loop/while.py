number =  7

while number < 10:
  print("i like python!")
  number += 1

#while break
number = 1
while number <= 10:
  print(number)
  if number == 5:
    break
  number += 2

#while continue
number = 0
while number <= 10:
  number += 1
  if number == 3:
    continue
  print(number)

#while else
i = 1
while i <= 10:
  print(i)
  i += 1
else:
  print("all numbers are printed")


#while pass
number = 1
while number < 8:
  pass
