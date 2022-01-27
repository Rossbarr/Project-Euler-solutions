from re import I
import string

with open('problems 20-29/data/p022_names.txt', encoding='utf8') as f:
  names = f.readline().replace('"', '').split(",")

alphabet_string = string.ascii_uppercase

print(alphabet_string)

scores = []
for name in names:
  score = 0
  for letter in name:
    i = 1
    for score_letter in alphabet_string:
      if letter == score_letter:
        score += i
        break
      else:
        i += 1
  scores.append(score)

print(scores)

