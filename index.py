import argparse 
import unicodedata
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
    
    if acceptableCharPattern(cp):
        charPos = getCharPos(cp)
        
        initialChar = findInitialChar(cp)
        finalChar = findFinalChar(cp)
        initialMask = None
        finalMask = None

        if initialChar != "":
            initialMask = initialMaskValue(len(initialChar))
        
        if finalChar != "" :
            finalMask = finalMaskValue(len(finalChar), len(cp)) 

        
        if initialMask and  not finalMask:
            selected =  withInitialOrFinalMaskValueSearch(cpLength = len(cp), initialMaskValue = initialMask, charsToUseLength = len(cu))

            print("selected: ", selected)
            
        elif not initialMask and finalMask:
            withInitialOrFinalMaskValueSearch(cpLength = len(cp), finalMaskValue = finalMask)

        elif initialMask and finalMask:
            withInitialOrFinalMaskValueSearch(cpLength = len(cp), initialMaskValue = initialMask, finalMaskValue = finalMask)

def withInitialOrFinalMaskValueSearch( cpLength: int ,   initialMaskValue: str = None, finalMaskValue: str = None, charsToUseLength: int = None):
    
    if not initialMaskValue and not finalMaskValue: 
        return None

    filtrated = {"high_priority": ListAsSet(), "medium_priority": ListAsSet(), "low_priority": ListAsSet()}
    
    
    maskSetList = list(ImportMaskArchive.importByLength(cpLength, globalLanguage))
    
   
    
    for mask in maskSetList:
        
        if initialMaskValue and not finalMaskValue:
            filtratedByStartOrEndMaskValue(initialMaskValue, None, mask , filtrated) 
        
        elif not initialMaskValue and finalMaskValue:
            filtratedByStartOrEndMaskValue(None, finalMaskValue, mask , filtrated) 

        elif initialMaskValue and finalMaskValue:
            filtratedByStartOrEndMaskValue(initialMaskValue, finalMaskValue, mask , filtrated) 


    print("Filtrated: ", filtrated)
    return filtrated



def filtratedByStartOrEndMaskValue(initialMaskValue: str, finalMaskValue: str, mask: dict, filtrated: dict ):
    

    for priority in filtrated.keys():
        for m in mask[priority]:
            if initialMaskValue and finalMaskValue:
                if m.startswith(initialMaskValue) and m.endswith(finalMaskValue):
                    filtrated[priority].append(m)
            elif initialMaskValue and not finalMaskValue:
                if m.startswith(initialMaskValue):
                    filtrated[priority].append(m)
            elif finalMaskValue:
                if m.endswith(finalMaskValue):
                    filtrated[priority].append(m)

    return filtrated




    

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



def getCharPos(charPattern: str) -> dict:
    charPositions = {}
    pos = []
    value = []

    for i, char in enumerate(charPattern):
        if char != "*":
            pos.append(i)
            value.append(char)

    charPositions["pos"] = pos
    charPositions["value"] = value
    
    return charPositions


def acceptableCharPattern(cp: str):
    
    if cp == "_.":
        return True

    totalAsteristic = 0
    cpArray = arrayFromString(cp)

    for char in cpArray:
        category = unicodedata.category(char)

        if char == "*":
            totalAsteristic += 1

        if char == "*" or category.startswith("L"):
            pass
        else:
            return False

    if totalAsteristic == 0:
        return False
        
    return True     


def verifyCompatibility(ogcsa, pttna):
  if len(ogcsa) != len(pttna) :
    return True
  
  for i in range(0, len(ogcsa)):
    s1 = ogcsa[i]
    s2 = pttna[i]

    if s2 == "*":
      continue

    if s1 != s2:
      return False

  

  
  
  return True

def findInitialChar(s):
    initialChar = ''
    for char in s:
        if char == '*':
            break
        
        initialChar += char

    return initialChar

def findFinalChar(s):
    finalChar = ''
    for char in reversed(s):
        if char == '*':
            break
        
        finalChar = char + finalChar
    return finalChar


def initialMaskValue(length):
    if length <= 1 :
        return None
    
    mask = ""
    for i in range(length):
        mask = mask + str(i) 
    return mask




def finalMaskValue(length, initialCharLength):
    if length <= 1 :
        return None
    
    mask = ""
    for i in reversed(range(initialCharLength)):
        if len (mask) == length:
            break
        mask = mask + str(i) 
    return mask

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
