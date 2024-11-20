def magicPotionTreatment(h1, h2):
    potion = ''
    while True:
        if h1 % 2 != 0:
            potion += 'A'
            h1 += 1
        if h1 > h2:
            potion += 'B'
            h1 /= 2
        if h1 < h2:
            potion += 'A'
            h1 += 1
        if h1 == h2:
            break
    return potion


print(magicPotionTreatment(4, 3))
print(magicPotionTreatment(9, 2))
print(magicPotionTreatment(123, 5))
