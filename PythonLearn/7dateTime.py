import datetime

current_datetime = datetime.datetime.now()

# print(current_datetime)
""""""

year = current_datetime.year
month = current_datetime.month
day = current_datetime.day
hour = current_datetime.hour
minute = current_datetime.minute
second = current_datetime.second

# print(f"Year: {year}, Month: {month}, Day: {day}")
# print(f"Hour: {hour}, Minute: {minute}, Second: {second}")

""""""
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
# print(formatted_datetime)

""""""
date_string = "2023-09-10 15:30:00"
parsed_datetime = datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
# print(parsed_datetime)

""""""
from datetime import timedelta

time_difference = parsed_datetime - current_datetime
# print(time_difference)

""""""

three_days_later = current_datetime + timedelta(days=3)
# print(three_days_later)




#exercise

ccurent_time = datetime.datetime.now()

ccurent_year = ccurent_time.year
ccurent_month = ccurent_time.month
ccurent_day = ccurent_time.day
ccurent_hour = ccurent_time.hour
ccurent_minute = ccurent_time.minute
ccurent_second = ccurent_time.second

# print(f"year{ccurent_year}")

# print(ccurent_time)

fccurent_time = "2023/09/12 03:10:00"
format_curr_time = datetime.datetime.strptime(fccurent_time,"%Y/%m/%d %H:%M:%S")

# print(f"{format_curr_time}")


ttime_dif = ccurent_time - format_curr_time

# print(f"{ttime_dif}")


deltime = ccurent_time - timedelta(weeks=3)

# print(f"{deltime}")