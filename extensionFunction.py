def arrayFromString(string: str ): 
    array = []
    for s in string:
        array.append(s)

    return array


def arrayToString(array):
        r = ""
        for i in range(len(array)):
            r += str(array[i])
            
        
        return r


def arrayTil(array, stopIndex):
        r = ""
        for i in range(len(array)):
            r += str(array[i])
            if i == stopIndex:
                break
        
        return r

def unacceptableString(string:str):
        if string == "" or len(string) < 2:
            return True
        else:
            return False
        
def stripSpaceIn(string:str):
    if not string.__contains__(" "):
        return string
    
    returned: str = ""
    for r in string:
        returned += r
    returned
