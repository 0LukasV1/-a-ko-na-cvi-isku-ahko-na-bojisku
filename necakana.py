data = {}

def create_intervals(data):
    tu = []
    lis2 = list(data)
    print(lis2)
    pocitadlo = 1
    if len(lis2) == 0 or lis2 == None:
        return []
    
    start = minule = lis2[0]
    for i in lis2[1:]:
        if i == int(minule) + 1:
            minule = i
        elif i < int(minule) + 1:
            return tu
        else:
            tu.append((start, minule))
            start = minule = i
    tu.append((start, minule))
    return tu
    

print(create_intervals(data))





