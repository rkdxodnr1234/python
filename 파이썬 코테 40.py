name = input("이름을 입력하세요:")
high = float(input("키를 입력하세요"))

if name.startswith("m") or (150 <= high < 170) :
  print("탈 수 있어요")
else :
  print("탈 수 없어요")