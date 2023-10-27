with open("data.txt") as f:
    higher_score = int(f.read())
    print(type(higher_score))
score = 88
if 3 > higher_score:
   with open("data.txt", mode="w") as k:
       k.write(f"{score}")
