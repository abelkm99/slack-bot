from datetime import datetime, time, timedelta, date
date_format = "%Y-%m-%dT%H:%M:%S"


def parse_date_time(date_string):
    return datetime.strptime(date_string, date_format)


def get_day_range(start_date, end_date):
    start_of_day = datetime.combine(start_date, time.min)
    end_of_day = datetime.combine(end_date, time.max)
    return start_of_day, end_of_day

def convert_seconds(seconds):
  # Use time.gmtime() to convert seconds to a struct_time object
  t = time.gmtime(seconds)
  # Use time.strftime() to format the struct_time object as HH:MM:SS 
  return time.strftime("%H:%M:%S", t)
