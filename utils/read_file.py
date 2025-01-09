
def read_file(path):

    subtitle_file = open(path,"r")

    text = subtitle_file.read() 

    subtitle_file.close()

    return text
