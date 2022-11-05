#dictionary of month numbers to days
days_in_month = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 31,
    10: 30,
    11: 30,
    12: 31
}

#reference date to calculate forward from
ref_year = 1900
ref_month = 1
ref_day = 1 #this is a monday

#date to start counting matches from
starting_year = 1901
starting_month = 1
starting_day = 1

#date to end counting at
ending_year = 2000
ending_month = 12
ending_day = 31

#working variables
year = ref_year
month = ref_month
day = ref_day
total_days = 1 #include the first day, every 7th day is a sunday
total_sundays = 0

#assume you're starting at the first of the month
def increment_month(y,m):
    global month
    global year
    global total_days

#    print(y)
#    print(m)
    #check for february leap year
    if(m == 2 and y % 4 == 0):
        m_length = 29
    else:
        if(m % 400 == 0):
            m_length = 29
        else:
            m_length = days_in_month.get(month)
    
    #print(m_length)
    #increment month and year
    if(m == 12):
        month = 1
        year += 1
    else:
        month += 1

    #add to total number of days
    total_days += m_length
    return

#look for sundays before ending year
while(year <= ending_year):
    #don't count sundays until starting year
    if(year >= starting_year):
        #check if day is a sunday
        if(total_days % 7 == 0):
            total_sundays += 1
#            print("Year: " + str(year) + " Month: " + str(month) + " Days in Month: " + str(days_in_month.get(month)) + " Day of Week: " + str(total_days % 7) + " Total Days: " + str(total_days))
#            print(total_sundays)
#            print()

    increment_month(year, month)

print(total_sundays)