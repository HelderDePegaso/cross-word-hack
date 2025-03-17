import argparse 
from extensionFunction import *

def simpleSearch(cu:str):
    cuArray  = arrayFromString(cu)
    for i in range(len(cuArray)):
        pass 

def withPatternSearch(cu:str, cp:str):
    pass

def processTask(charsToUse:str, charPattern:str = "_.", rbf: int = 1):
    _cu = stripSpaceIn(charsToUse.strip())
    _cp = stripSpaceIn(charPattern.strip())
    
    print(charsToUse, charPattern, rbf)

    if unacceptableString(_cu) or unacceptableString(_cp):
        pass

    if _cp == "_.":
        simpleSearch(_cu)
    else: 
        withPatternSearch(_cu, _cp)

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

def main() : 
    
    print("as")
    parser = argparse.ArgumentParser()

    parser.add_argument("--charsToUse", type=str, help = "Define the chars to use in the search")
    parser.add_argument("--charPattern", type=str, help = "Define a pattern for the search of the possible words")
    parser.add_argument("--rbf", type=int, help = "What words to prioritize ")
    
    args = parser.parse_args()
    
    
    activeArgs = {"cu" : True,"cp" : False,"rb" : False}

    if args.charsToUse : 
        if args.charsPattern and args.rbf:
            processTask(args.charsToUse, args.charPattern, args.rbf)
        
        elif args.charPattern and args.rbf == None:
            processTask(args.charsToUse, args.charPattern)

        elif not args.charPattern == None & args.rbf:
            processTask(charsToUse=args.charsToUse, rbf = args.rbf)

        else:
            processTask(args.charsToUse)

if __name__ == "__main__" :
    main()
