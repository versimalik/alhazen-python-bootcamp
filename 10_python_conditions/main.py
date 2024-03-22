#PROJECT
# Case = score range
# create an input to take a score in integer data type
score = int(input("Masukkan score: "))
print(score)
# check the score in range, with 'and' operator
# 85-100 = grade is A
# 70-85 = grade is B
# 50-70 = grade is C
# less then 50 = grade is D
# Print grade for every specific range conditions
if score >= 85 and score <= 100:
  print("grade A")
elif score >= 70 and score <=85:
  print("grade B")
elif score >= 50 and score <=70:
  print("grade C")
elif score < 50:
  print("grade D")