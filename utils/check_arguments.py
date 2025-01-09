import os

def check_arguments(args):

    number_of_arguments = len(args)
    if(number_of_arguments != 4):
        print("Either subtitle filename path, miliseconds or direction parameter missing.")
        print("Please specify subtitle filename path, miliseconds and direction respectively.")
        return -1

    path = args[1] 
    
    does_file_exist = os.path.isfile(path)

    if(not does_file_exist):
        print("No file is found.")
        print("Please make sure you specify the path correctly")
        return -1
    
    subtitle_filename = os.path.basename(path)
    is_srt_file = subtitle_filename.endswith(".srt")

    if(not is_srt_file):
       print("Subtitle file name should be in .srt format")
       print("Please specify a file with an extension of .srt")
       return -1

    
    ms_change = args[2]

    is_correct_type = ms_change.isnumeric()
    is_above_zero =  int(ms_change) > 0

    if(not is_correct_type or not is_above_zero):
        print("Miliseconds should be numeric and above zero")
        print("Please specify miliseconds in a correct format")
        return -1


    direction = args[3]

    is_correct_direction = (direction.lower() == 'forward') or (direction.lower() == 'backward')
    if(not is_correct_direction):
        print("Shift direction should be either forward or backward")
        print("Please specify direction in a correct format") 
        return -1

    return [path, ms_change, direction]

