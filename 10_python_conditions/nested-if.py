#NESTED IF STATEMENT

age = 18
driver_license = False

if age > 17:
  print("User is tenager")
  if driver_license == True:
    print("And driving is allowed")
  else:
    print("But driving is not allowed")
else:
  print("User is not yet a tenager")
  print("so driving is not allowed")