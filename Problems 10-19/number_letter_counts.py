"""
Not a very elegant solution, but it gives the right answer, lol

TO-DO: clean up and make more efficient
"""

def singles(n) -> str:
  if n < 5:
    if n < 3:
      if n == 0:
        return ""
      elif n == 1:
        return "one"
      else:
        return "two"
    else:
      if n == 3:
        return "three"
      else:
        return "four"
  else:
    if n < 7:
      if n == 5:
        return "five"
      else:
        return "six"
    else:
      if n == 7:
        return "seven"
      elif n == 8:
        return "eight"
      elif n == 9:
        return "nine"

def teens(n) -> str:
    if n == 10:
      return "ten"
    elif n == 11:
      return "eleven"
    elif n == 12:
      return "twelve"
    elif n == 13:
      return "thirteen"
    elif n == 15:
      return "fifteen"
    elif n == 18:
      return "eighteen"
    else:
      return singles(n % 10) + "teen "

def doubles(n) -> str:
  x = int(n/10)
  y = n % 10
  if x:
    if x == 1:
      return teens(n)
    elif x == 2:
      return "twenty " + singles(y)
    elif x == 3:
      return "thirty " + singles(y)
    elif x == 4:
      return "forty " + singles(y)
    elif x == 5:
      return "fifty " + singles(y)
    elif x == 8:
      return "eighty " + singles(y)
    else:
      return singles(x) + "ty " + singles(y)
  elif y:
    return singles(y)
  else:
    return ""

def triples(n) -> str:
  x = int(n/100)
  y = n % 100
  if x and y:
    return singles(x) + " hundred and " + doubles(y)
  elif x:
    return singles(x) + " hundred"
  else:
    return doubles(y)

def number_letter_counts(n) -> str:
  word = triples(n) 
  return word

print(number_letter_counts(342))
print(number_letter_counts(115))
print(len(number_letter_counts(342).replace(" ", "")))
print(len(number_letter_counts(115).replace(" ", "")))


numbers = range(1, 1000, 1)
total = 0
for n in numbers:
  word = number_letter_counts(n)
  total += len(word.replace(" ", ""))

print(total + len("onethousand"))