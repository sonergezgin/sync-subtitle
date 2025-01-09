

time_types = ["hour","minute","second"]

def convert_string_time_to_ms_time(time_str):

    time_str = time_str.strip()

    splitted_time = time_str.split(":")

    result = 0

    for index, each_time_piece in enumerate(splitted_time):
        
        
        current_time_type = time_types[index]

        if(current_time_type == "hour"):
            ms = convert_hour_to_ms(each_time_piece)

        elif(current_time_type == "minute"):
            ms = convert_minute_to_ms(each_time_piece)

        elif(current_time_type == "second"):
            ms = convert_second_to_ms(each_time_piece)

        else:
            print("something went wrong")
            break

        result += ms

    return result


def convert_hour_to_ms(hour_str):

    hour_int = int(hour_str)
    return hour_int * 60 * 60 * 1000

def convert_minute_to_ms(minute_str):

    minute_int = int(minute_str)
    return minute_int * 60 * 1000

def convert_second_to_ms(second_str):

    second, ms = second_str.split(",")

    second_int = int(second)
    ms_int = int(ms)

    return second_int * 1000 + ms_int
    