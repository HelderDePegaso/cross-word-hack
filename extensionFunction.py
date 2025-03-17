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
