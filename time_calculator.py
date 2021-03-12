def add_time(start, duration, day = 'default'):
    
    start_period = start.split()
    
    start_hour, start_minutes = start_period[0].split(':')

    add_hour, add_minutes = duration.split(':')

    # Calculate minutes
    end_minutes = int(start_minutes) + int(add_minutes)
    final_minutes = end_minutes%60
    if final_minutes < 10:
        final_minutes ="0"+str(final_minutes)
    else:
        final_minutes = str(final_minutes)
    convert_to_hours = int(end_minutes/60)

    # Calculate hours
    end_hour = 0
    final_hour = 0
    
    if start_period[1] == 'PM':
        end_hour = int(start_hour) + 12 + int(add_hour) + convert_to_hours
    else:
        end_hour = int(start_hour) + int(add_hour) + convert_to_hours
    
    if end_hour%12 ==0:
        final_hour = 12
    else:
        final_hour = end_hour % 12
    
    # Calculate period
    num_of_12h_period = int(end_hour / 12)
    period = ["AM" , "PM"]
    end_period = ""

    if num_of_12h_period%2 ==0:
        end_period = period[0]
    else:
        end_period = period[1]
       
    # Calculate number of days later
    no_of_days = int(end_hour/24)
    if no_of_days < 1:
        no_of_days = ""
    elif no_of_days == 1:
        no_of_days = ' (next day)'
    elif no_of_days > 1:
        no_of_days = ' ('+ str(no_of_days) +' days later)'
       
    if day == 'default':
        return (str(final_hour) + ':' + (final_minutes) + " " + (end_period) + (no_of_days) )

    start_count = 0
    final_count = 0
    final_day = 0
        
    if day != 'default':
        start_day = day.capitalize()
        
        day_of_week = {'Monday':1, 'Tuesday':2, 'Wednesday':3, 'Thursday':4, 'Friday':5, 'Saturday':6, 'Sunday':7}
        start_count = day_of_week.get(start_day)
        add_days = int(end_hour/24)%7
        final_count = start_count + add_days

        if add_days == 0:
            final_count = start_count
        elif final_count > 7:
            final_count = final_count%7
        
        
        day_of_week_count = {1:'Monday', 2:'Tuesday',3:'Wednesday',4:'Thursday',5:'Friday', 6:'Saturday', 7:'Sunday'}

        final_day = day_of_week_count.get(final_count)

        return (str(final_hour) + ':' + (final_minutes) + " " + (end_period) +", " + (final_day) + (no_of_days) )
