count = 0
imp = False
min_count = 99999999999999
number_of = input()
helium = input()
helium_list = helium.split(' ')
helium_list = list(map(int, helium_list))
helium_list = sorted(helium_list)

for item in helium_list:
    count += 1
    if item > count:
        imp = True
        break
    div = item/count
    if div < min_count:
        min_count = div 
    
if imp:
    print ("impossible")
else:
    print (min_count)
