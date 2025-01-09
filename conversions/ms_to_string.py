from math import floor

def convert_ms_to_hour(ms):

    hour = (ms / 1000) / ( 60 * 60) 
    
    hour_part = str(floor(hour))

    is_zero_necessary = len(hour_part) == 1
    if(is_zero_necessary):
        hour_part = "0" + hour_part
    
    return hour_part 

def convert_ms_to_minute(ms):

    minute = (((ms / 1000) / ( 60 * 60)) % 60) * 60
    minute_part = str(floor(minute % 60))

    is_zero_necessary = len(minute_part) == 1
    if(is_zero_necessary):
        minute_part = "0" + minute_part
    
    return  minute_part 

def convert_ms_to_second(ms):

    second = (ms / 1000) % 360

    second_part = str(round(second % 60, 3))
    
    complete, fraction = second_part.split(".")
    
    is_zero_necessary_for_complete = len(complete) == 1
    if(is_zero_necessary_for_complete):
        complete = "0" + complete

    is_zero_necessary_for_fraction = len(fraction) < 3
    if(is_zero_necessary_for_fraction):
        fraction = fraction + "0" * (3 - len(fraction))
     
    
    second_part = (complete + "," +  fraction)

    return second_part 



def convert_ms_time_to_string_time(ms_time):

    str_hour = convert_ms_to_hour(ms_time)    
    str_minute = convert_ms_to_minute(ms_time)
    str_second = convert_ms_to_second(ms_time)
    
    return str_hour + ":" + str_minute + ":" + str_second

