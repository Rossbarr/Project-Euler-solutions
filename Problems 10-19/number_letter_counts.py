"""
Not a very elegant solution, but it gives the right answer, lol

TO-DO: clean up and make more efficient
"""

def singles(n) -> str:
  num_letters = 0;
  if n == 0:
    num_letters = 0;
  elif n == 1 or n == 2 or n == 6:
    num_letters = 3;
  elif n == 4 or n == 5 or n == 9:
    num_letters = 4;
  elif n == 3 or n == 7 or n == 8:
    num_letters = 5;

  return num_letters

def teens(n) -> str:
    if n == 10:
      return 3
    elif n == 11 or n == 12:
      return 6
    elif n == 15:
      return 7
    elif n == 13 or n == 18:
      return 8
    else:
      return singles(n % 10) + 4 # plus 4 for "-teen"

def doubles(n) -> str:
  x = int(n/10)
  y = n % 10
  if x:
    if x == 1:
      return teens(n)
    elif x == 2:
      return 6 + singles(y)
    elif x == 3:
      return 6 + singles(y)
    elif x == 4:
      return 5 + singles(y)
    elif x == 5:
      return 5 + singles(y)
    elif x == 8:
      return 6 + singles(y)
    else:
      return singles(x) + 2 + singles(y)
  elif y:
    return singles(y)
  else:
    return 0

def triples(n) -> str:
  x = int(n/100)
  y = n % 100
  if x and y:
    return singles(x) + 10 + doubles(y)
  elif x:
    return singles(x) + 7
  else:
    return doubles(y)

def number_letter_counts(n) -> str:
  word = triples(n) 
  return word

print(number_letter_counts(342))
print(number_letter_counts(115))


numbers = range(1, 1000, 1)
total = 0
for n in numbers:
  total += number_letter_counts(n)

print(total + len("onethousand"))