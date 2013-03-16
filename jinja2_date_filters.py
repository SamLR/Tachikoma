"""
Some custom filters for Jinja2 for dealing with dates
"""

def get_month_str(month_n):
  """
  Returns the name of the n-th month in the standard Gregorian Calendar 
  assuming January=1 and December=12.
  """
  months=("January", "Feburary", "March", "April", "May", "June", \
          "July", "August", "September", "October", "November", "December")
  month_n = int(month_n)
  if month_n not in range(1,13): raise ValueError("Month must be in 1..12")
  return months[month_n - 1]
  
def get_day_str(day_n):
  """
  Converts a datetime day of the week to its name.
  Monday=0, Sunday=6
  """
  days=("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
  day_n = int(day_n)
  # if day_n not in range(7): raise DateStrException("Day must be in 0..6")
  if day_n not in range(7): raise ValueError("Day must be in 0..6")
  return days[day_n]
  
def test_get_month_str():
  expect1="January"
  result1 = get_month_str(1)
  assert expect1==result1
  print( "get_month_str(1)=",result1)
  expect2="December"
  result2 = get_month_str(12)
  assert expect2==result2
  print( "get_month_str(12)=",result1)
  try:
    get_month_str(0)
  except ValueError as e:
    print(e)
  try:
    get_month_str(13)
  except ValueError as e:
    print(e)
    
def test_get_day_str():
  expect1="Monday"
  result1=get_day_str(0)
  assert expect1==result1
  print("get_day_str(0)=",result1)
  expect2="Sunday"
  result2=get_day_str(6)
  assert expect2==result2
  print("get_day_str(6)=",result2)
  try:
    get_day_str(7)
  except ValueError as e:
    print(e)
  
if __name__=="__main__":
  test_get_month_str()
  test_get_day_str()
  print("Passed all tests!")