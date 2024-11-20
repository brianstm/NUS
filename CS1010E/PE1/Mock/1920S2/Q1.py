bouquet = ("R", "P", "W", "W", "P", "R", "R", "R")

def rotate(bouquet, step):
    bouquet = list(bouquet)
    for _ in range(step):
        tmp = bouquet[0]
        bouquet.pop(0)
        bouquet.append(tmp)

    return tuple(bouquet)


def flower_I(bouquet, k):
    bouquet = list(bouquet)
    result = ""
    current_index = 0
    
    for _ in range(len(bouquet)):  
        current_index = (current_index + k - 1) % len(bouquet)
        selected_flower = bouquet.pop(current_index)
        result += selected_flower        
    
    return result


def flower_R(bouquet, k):
    bouquet = list(bouquet)
    if len(bouquet) == 1:
        return bouquet[0]
    
    current_index = (k - 1) % len(bouquet)
    selected_flower = bouquet.pop(current_index)
    next_flower = flower_I(bouquet, k)
    result = selected_flower + next_flower
    return result


print(rotate(bouquet,2))
print(flower_I(bouquet, 8))
print(flower_R(bouquet, 8))

