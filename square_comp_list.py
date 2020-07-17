n_list = [10,20,30,40,50]
num_list = list(range(1,30))
square_arr = [i**2 for i in n_list]
print(square_arr)

##짝수만 제곱

square_even = [i**2 for i in range(2,21,2)] # range 뒤에 숫자 간격 입력 가능
#print(square_even)
square_LCM = [i**2 for i in num_list if i%2==0 and i%3==0] # in 조건에서 if 로 선별할 수 있어
print(square_LCM)