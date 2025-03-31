year = int(input("Year: "))

years_past_leap = year%4

years_to_next_leap = 4-years_past_leap

next_leap = year+years_to_next_leap

if(next_leap%100==0):

if(next_leap%400!=0):

next_leap+=4

print(f"the next leap year after {year} is {next_leap}")