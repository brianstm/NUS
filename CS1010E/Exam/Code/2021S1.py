print(10+6//4+3//2)
print(([1,2,3]*2)[::2])
print('abcdef'[(1,'d',4)[2]])
# print([a,b,c][int('1')]) # name 'a' is not defined
print({'a':(1,2,3),'b':'qsr',2:[6]}['abc'[1]][0])
print([i**2 for i in range(1,10)][3])
print(len([[1,2,3],[4,5,6],[7,8,9],[10,11,12]]))
print(tuple(map(lambda x:x[0]+x[1],((1,2),(3,4)))))
print(list(tuple(set('abcabc')))) # set removes duplicates
print((lambda x,y,z:x(y)+x(z))((lambda x:x*2),4,5))