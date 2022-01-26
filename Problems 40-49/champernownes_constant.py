champ = str()
i = 0

while (len(champ) < 1000000):
    i += 1
    champ += str(i)

print(
    int(champ[1-1]) 
    * int(champ[10-1]) 
    * int(champ[100-1]) 
    * int(champ[1000-1])
    * int(champ[10000-1])
    * int(champ[100000-1])
    * int(champ[1000000-1])
    )
