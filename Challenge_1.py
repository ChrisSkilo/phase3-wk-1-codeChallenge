def convert_to_24_hour_time(hour, minute, period):
    if period == "am" and hour == 12:
        return f"00{minute:02d}"
    elif period == "pm" and hour == 12:
        return f"12{minute:02d}"
    elif period == "pm":
        return f"{hour + 12:02d}{minute:02d}"
    else:
        return f"{hour:02d}{minute:02d}"

print(convert_to_24_hour_time(12, 15, "am"))
print(convert_to_24_hour_time(8, 30, "am")) 
print(convert_to_24_hour_time(8, 30, "pm")) 