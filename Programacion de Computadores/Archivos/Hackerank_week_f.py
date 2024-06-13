import random

num_al = (random.randint(1,100))

print(num_al)
if num_al % 2 != 0 or num_al >= 6 and num_al < 20:
    print("Weird")
elif num_al % 2 == 0 and num_al >= 2 or num_al % 2 == 0 and num_al =< 5 or num_al % 2 == 0 and num_al >= 20:
    print("Not Weird")
