height = float(input("키를 입력하세요: "))
gender = input("성별을 입력하세요:")

if 150 <= height < 170 and gender == "여자" or height % 5 == 0 :
    print("탈 수 있어요")
else:
    print("탈 수 없어요")
