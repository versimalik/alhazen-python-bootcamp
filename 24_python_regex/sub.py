import re

text = "The quick brown fox"
text += "jumps over 12 lazy dogs!"

x = re.sub(r"\d", "-", text)

print(x)
