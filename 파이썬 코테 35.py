a = int(input("정수 한 개를 입력하시오"))

if a < 0 and a % 2 == 1 :
  print('음수이자 홀수')

if a < 0 and a % 2 == 0 :
  print('음수이자 짝수')

if a > 0 and a % 2 == 1 :
  print('양수이자 홀수')
  
if a > 0 and a % 2 == 0 :
  print('양수이자 짝수')