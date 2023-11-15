# Practice Question : Q5
'''Write a Python program that uses the elif statement to determine the season based on the
month provided as input.'''

month = input("Input the month:")

if month in ('January','February','March'):
    season = 'winter'
elif month in ('April','May','June'):
    season = 'spring'
elif month in ('July','August','September'):
    season = 'summer'
elif month == 'November':
    season = 'autumn'
elif month == 'December':
    season = 'winter'

print(f"On {month} season is {season}.")
