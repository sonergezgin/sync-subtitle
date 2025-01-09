from conversions.ms_to_string import *
from conversions.string_to_ms import * 

def sync(subtitle, ms_change):


    lines = subtitle.split("\n")
    
    modified_subtitle_file = open("./output/modified_subtitle_file.srt","w")

    for each in lines:
        
        splitted_line = each.split("-->")
        is_time_line = len(splitted_line) == 2

        if not is_time_line:
            modified_subtitle_file.write(each + "\n")
            continue

        # destructure it
        start_time = splitted_line[0]
        finish_time = splitted_line[1]

        ms_start_time = convert_string_time_to_ms_time(start_time)
        ms_finish_time = convert_string_time_to_ms_time(finish_time) 

        new_ms_start_time = ms_start_time + ms_change
        new_ms_finish_time = ms_finish_time + ms_change

        new_start_string_time = convert_ms_time_to_string_time(new_ms_start_time)
        new_finish_string_time = convert_ms_time_to_string_time(new_ms_finish_time)

        modified_subtitle_file.write(new_start_string_time + " --> " +  new_finish_string_time + "\n")

    
    modified_subtitle_file.close()

    print("All done.")
