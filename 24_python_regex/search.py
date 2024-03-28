import re

text = "The quick brown fox"
text += "jumps over 12 lazy dogs!"

y = re.search(r"fox", text)
if y:
    print("pola ditemukan")