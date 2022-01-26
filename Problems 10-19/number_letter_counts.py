def number_letter_counts(n) -> str:
  word = triples(n) + doubles(n % 100) + singles(n % 10)
  return len(word)

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

def doubles(n) -> str:
  n = int(n/10)
  if n:
    if n <= 3:
      if n == 1:
        pass
      elif n == 2:
        return "twenty"
      else:
        return "thirty"
    else:
      return singles(n) + "y "

def triples(n) -> str:
  n = int(n/100)
  if n and (n % 100):
    return singles(n) + " hundred and "
  else:
    return singles(n) + " hundred"
