def adult(n):
    if n >=20:
        return n
    else :
        return None

# print(adult(18))

ages = [34,25,17,13,54]
print('성인 리스트')
for i in filter(adult ,ages): #ages 대신 filter이용
    print(i) #filter는 adult의 return이 boolean 또는 변수n 자체 일때 성립, 이외에 개판

print(list(filter(lambda n:n>=20, ages))) #object를 리스트로

for i in filter(lambda n:n>=20, ages): #object를 for 마다 프린트로
    print(i)
