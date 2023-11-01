
print('Leap_Year_Checker')
 # Which year do you want to check?
year = int(input())

CheckA = year % 4
CheckB = year % 100
CheckC = year % 400

if CheckA == 0:
  if CheckB == 0:
    if CheckC == 0:
      print('Leap year')
    else:
      print('Not leap year')
  else:
    print('Leap year')
else:
  print ('Not leap year')