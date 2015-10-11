from collections import Counter
str = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
str = str.replace(",", "")
str = str.split()
for num in str:
  print(len(num))
