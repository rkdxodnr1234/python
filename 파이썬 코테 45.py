"""
7자리 수가 1,2 이면 1900년대, 3,4이면 2000년대 
1,3이면 남자 2,4면 여자
첫 두자리 수 추출해서 year로 저장

"""
num = input("주민등록번호 입력:")
gender_code = num[7]

if gender_code in["1" , "2"]:
  year = "19"+num[:2]
else :
  year = "20"+num[:2]

if gender_code in ["1", "3"] :
  gender = "남자"
else :
  gender = "여자"

print(f"{gender}{year}년 출생")