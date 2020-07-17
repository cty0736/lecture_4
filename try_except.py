try:
    a,b = input('두 수를 입력하세요').split()
    result = (int(a)/int(b))
    print(result)

# except :
#     print('try again') # 오류나면 여길 진행

except Exception as e:
    print('에러 형태는 {}'.format(e)) # 전반적인 오류 조건 다 가능

# except ZeroDivisionError as z:
#     print('에러 형태는 {}'.format(z)) # 특정 오류 조건에서 수행 가능
# except TypeError as t:
#     print('에러 형태는 {}'.format(t)) # 특정 오류 조건에서 수행 가능
# except ValueError as v:
#     print('에러 형태는 {}'.format(v))  # 특정 오류 조건에서 수행 가능      
        