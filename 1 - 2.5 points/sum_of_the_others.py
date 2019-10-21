test = True

while test == True:
    try:
        list_of_n = input().split(' ')
        negative, positive = [0, 0]

        for item in list_of_n:
            if int(item) > 0:
                positive += int(item)
            else:
                negative += int(item)

        print (int((positive + negative)/2))
    except EOFError:
        test = False
