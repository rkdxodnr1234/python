num = input("몇 월인가요?")

if num in ["1","3","5","7","8","10","12"]:
  print(f"{num}월은 31일까지 있습니다")
elif num in ["4","6","9","11"]:
  print(f"{num}월은 30일까지 있습니다")
else:
  print(f"{num}은 28일까지 있습니다")