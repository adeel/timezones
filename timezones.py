import pytz

def localize(date, time_zone):
    "Convert the date to the local time zone (from UTC)."

    return date.replace(second=0, microsecond=0,
        tzinfo=pytz.utc).astimezone(pytz.timezone(time_zone))

def to_utc(date, time_zone):
    "Change a datetime corresponding to the time_zone to UTC time."

    return pytz.timezone(time_zone).localize(date.replace(
        second=0, microsecond=0)).astimezone(pytz.utc)