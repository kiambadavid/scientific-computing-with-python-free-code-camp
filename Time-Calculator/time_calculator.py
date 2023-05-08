def add_time(start_time, duration, day=None):
    start_time = start_time.split(" ")
    time = start_time[0]
    time = time.split(":")
    s_hours = time[0]
    s_minutes = time[1]

    ampm = start_time[1]
    if ampm == "PM":
        s_hours = int(s_hours) + 12

    duration = duration.split(":")
    d_hours = duration[0]
    d_minutes = duration[1]

    hours = int(s_hours) + int(d_hours)
    minutes = int(s_minutes) + int(d_minutes)
    if minutes >= 60:
        minutes = minutes - 60
        hours = hours + 1
    if minutes < 10:
        minutes = "0" + str(minutes)

    days_later = 0
    days_later_str = ""
    if hours == 12:
        ampm = "PM"
    elif 12 < hours < 24:
        hours = hours - 12
        ampm = "PM"
    elif hours >= 24:
        days_later = hours // 24
        if days_later == 1:
            days_later_str = " (next day)"
        elif days_later > 1:
            days_later_str = " (" + str(days_later) + " days later)"

        hours = hours % 24
        if hours == 0:
            hours = 12
            ampm = "AM"
        elif hours == 12:
            ampm = "PM"
        elif 12 < hours < 24:
            hours = hours - 12
            ampm = "PM"
        else:
            ampm = "AM"
    else:
        ampm = "AM"

        # output statement
    if day is None:
        time = str(hours) + ":" + str(minutes) + " " + ampm + days_later_str
    else:
        day = day[0].upper() + day[1:].lower()
        dict_day = {"Monday": 1, "Tuesday": 2, "Wednesday": 3, "Thursday": 4, "Friday": 5, "Saturday": 6, "Sunday": 7}
        day_start = dict_day[day]
        if days_later > 0:
            day_end = day_start + int(days_later)
        else:
            day_end = day_start
            days_later_str = ""
        if day_end > 7:
            day_end = day_end % 7
        for i in dict_day:
            if dict_day[i] == day_end:
                day_end = i
        time = str(hours) + ":" + str(minutes) + " " + ampm + ", " + str(day_end) + days_later_str
    return time
