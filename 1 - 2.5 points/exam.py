correct_f = int(input())
my_answers = input()
friends_answers = input()
diff = 0
eq = 0

for i in range(len(my_answers)):
    if my_answers[i] != friends_answers[i]:
        diff += 1
    else:
        eq += 1

if eq >= correct_f:
    maxr = correct_f + diff
elif eq < correct_f:
    maxr = eq + diff+eq-correct_f

print (maxr)
