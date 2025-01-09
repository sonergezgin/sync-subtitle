import sys

from sync import sync

from utils.check_arguments import check_arguments
from utils.read_file import read_file
from utils.get_shift_by_ms import get_shift_by_ms
"""
command line arguments should be in the format of 
python3 main.py [path] [ms] [forward | backward] 

example
python3 main.py './example/When Harry Met Sally.srt' 2000 forward

"""
def main():
    result = check_arguments(sys.argv)
    if(result == -1):
        return
    
    [path, ms, direction] = result
    
    file_content = read_file(path)
    
    normalized_ms = get_shift_by_ms(ms, direction)

    sync(file_content, normalized_ms)

    
if __name__ == "__main__":
    main()
    

