from functools import reduce
n_list=[10,20,30,40,50]

result = reduce(lambda x , y : x*y, n_list) #((((10*20)*30)*40)*50)로 처리
print(result)
result_2 = reduce(lambda x, y: x+y,n_list) # ((((10+20)+30)+40)+50)
print(result_2)