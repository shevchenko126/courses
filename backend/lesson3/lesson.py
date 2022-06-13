from datetime import datetime
from test import print_name
import requests


today = datetime.today()
first_june = datetime(2022, 6, 1, 12, 0, 0)
print(first_june)
print(today)

time_delta = today - first_june
print(time_delta.seconds % 3600)


print_name("Gre")


# 3/0

test = [3, 6, 7, 9]
try:
    print(test[2]/0)
except ZeroDivisionError:
    try:
        print(test[8]/1)
    except IndexError:
        print(test[2]/1)
except IndexError:
    print(test[3]/1)


x = 0
try:
    x = test[8]/0
except (ZeroDivisionError, IndexError):
    x = test[3]/1
    print(test[3]/1)
finally:
    y = x +1

print(y)



x = 0
index = 4
try:
    if index < 5:
        raise ZeroDivisionError
    x = test[index]/1
except (ZeroDivisionError, IndexError):
    x = test[index-5]/1
    print(test[index -5]/1)
finally:
    y = x +1

print(y)



print_name("Gre", "Petro", "Andrew", Oleksii="Petrenko", Andrii="Ivanenko")