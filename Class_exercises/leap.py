def leap_year(year):
    if year % 100 == 0  and year %400 != 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False
    
print(leap_year(1997))
print(leap_year(1996))
print(leap_year(2021))
print(leap_year(2020))