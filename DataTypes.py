def data_type(y=None):
    
    if type(y) == str:
        return len(y)
    elif y == None:
        return "no value"
    elif type(y) == bool:
        return y
    elif type(y) == list:
        if len(y) >= 3:
            return y[2]
        else:
            return None
    elif type(y) == int:
        if  y < 100:
            return "less than 100"
        elif y > 100:
            return "more than 100" 
        else:
            return "equal to 100"

