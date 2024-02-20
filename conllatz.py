def conllatz(var):
    array_var = []
    while (True):
        if(var != 1 ):
            if (var % 2 != 0):
                    var = var*3+1
            else : 
                    var = var/2
            array_var.append(var)
        else :
            break
    return array_var

#n => m
m = 1
n = 10
array_i = []
longest_cycle_length = 0
k = 0
for i in range (m,n):
    array_i.append(conllatz(i))
    print(array_i[k])
    if (len(array_i[k]) >= longest_cycle_length):
         longest_cycle_length = len(array_i[k]) + 1
    k += 1
print(m)
print(n)
print(longest_cycle_length)