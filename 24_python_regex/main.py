import re

text = "The quick brown fox"
text += "jumps over 12 lazy dogs!"

x = re.findall(r"\d", text)

print(x)

y = re.findall(r"cat", text)
print(y)