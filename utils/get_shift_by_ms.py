
def get_shift_by_ms(change_ms, direction):
    
    normalized_direction = direction.lower()

    if(normalized_direction == 'forward'):
        return int(change_ms)
    elif(normalized_direction == 'backward'):
        return -int(change_ms)
    else:
        raise Exception("Direction should be either forward or backward")

