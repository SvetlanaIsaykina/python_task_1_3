procentage = list(range(1,101))
i = 1
while i < 101:
  if 11 <= i <= 14:
    print(i, "процентов")
  elif i%10 == 1:
    print(i, "процент")
  elif 2 <= i%10 <= 4:
    print(i, "процента")
  else:
    print(i, "процентов")
  i = i + 1
