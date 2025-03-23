import argparse 
from ImportMaskArchive import ImportMaskArchive
from extensionFunction import *
from extensionObjects import ListAsSet
from datetime import datetime



globalLanguage = ""

def simpleSearch(cu:str):
    global globalLanguage
    language = globalLanguage
    _return = {"high_priority" : ListAsSet(), "medium_priority" : ListAsSet(), "low_priority" : ListAsSet()}
    cuArray  = arrayFromString(cu)

    masksList = ImportMaskArchive.importAllFromTop(len(cuArray), language)

    for mask in masksList:
        fillInMask(mask["high_priority"], cuArray, _return["high_priority"])
        fillInMask(mask["medium_priority"], cuArray, _return["medium_priority"])
        fillInMask(mask["low_priority"], cuArray, _return["low_priority"]) 
    
    return _return


def withPatternSearch(cu:str, cp:str):
    pass




def fillInMask(maskPriorityPart:list, cuArray:list, returnPriorityPart:list):
    print("The cuArray : ", cuArray)
    for mask in maskPriorityPart:
        toUnmask = []
        maskAsArray = arrayFromString(mask)
        for i in range(len(maskAsArray)):
            point = int(maskAsArray[i])


            # To prevent index out of range
            if point > len(cuArray) - 1:
                continue
            
            char = cuArray[point]

            # To avoid repeating a char when it is not necessary
            if toUnmask.count(char) < cuArray.count(char): 
                toUnmask.append(char)
        
        
        if len(toUnmask) > 0 and len(toUnmask) == len(maskAsArray):
            unmasked = arrayToString(toUnmask)
            returnPriorityPart.append(unmasked)

def processTask(charsToUse:str, charPattern:str = "_.", rbf: int = 1):
    print("Processing task...")
    print(charsToUse, charPattern, rbf)
    _cu = stripSpaceIn(charsToUse.strip())
    _cp = stripSpaceIn(charPattern.strip())
    
    print(charsToUse, charPattern, rbf)

    if unacceptableString(_cu) or unacceptableString(_cp):
        pass

    if _cp == "_.":
        h = simpleSearch(_cu)
        print("Eu recebi : ", h)
    else: 
        withPatternSearch(_cu, _cp)
        

def main() : 
    
    print("as")
    parser = argparse.ArgumentParser()

    parser.add_argument("--charsToUse", type=str, help = "Define the chars to use in the search" , required=True)
    parser.add_argument("--lang", type=str, help = "Define the language to use", required=True)
    parser.add_argument("--charPattern", type=str, help = "Define a pattern for the search of the possible words")
    parser.add_argument("--rbf", type=int, help = "What words to prioritize ")
    
    args = parser.parse_args()
    
    
    activeArgs = {"cu" : True,"cp" : False,"rb" : False}

    global globalLanguage 
    globalLanguage = args.lang

    if args.charsToUse : 
        if args.charPattern and args.rbf:
            processTask(args.charsToUse, args.charPattern, args.rbf)
        
        elif args.charPattern and args.rbf == None:
            processTask(args.charsToUse, args.charPattern)

        elif not args.charPattern == None and args.rbf:
            processTask(charsToUse=args.charsToUse, rbf = args.rbf)

        else:
            processTask(args.charsToUse)

if __name__ == "__main__" :
    main()
