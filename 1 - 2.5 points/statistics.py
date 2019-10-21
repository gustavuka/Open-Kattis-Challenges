count = 0
hello = True
while hello == True:
    try:
        data_int = []
        count +=1
        data = input().split(' ')
        for item in data:
            data_int.append(int(item))
        minimo = min(data_int[1:])
        maximo = max(data_int[1:])
        ranger = abs(maximo - minimo)
        print ("Case " + str(count) + ": " + " " + str(minimo) + " " + str(maximo) + " " + str(ranger))
    except EOFError:
        hello = False
