import json
import asyncio
import aiofiles
from extensionFunction import * 

array = [0, 1, 2, 3, 4, 5]

async def repeatFirst(array: list, base = ""):
    length = len(array)
    result = []
    result_part = []
    baseAsArray = []
    lastMask = generateLastMask(array)
    stopCondition = False

    lastElement: str = ""

    for i in range(length - 1):
        l = array[length - 1]
        lastElement += str(l)


    print(lastElement)
    
    while stopCondition != True:
        #input()
            
        baseAsArray = arrayFromString(base)
        baseIn = ""
        last = ""
        lbot = 0
        first = ""
        # Define the base for this iteration
        if len(baseAsArray) > 2:
            last = baseAsArray[len(baseAsArray) - 1]
            lbot = int(baseAsArray[len(baseAsArray) - 2])
            first = arrayToString(baseAsArray[0 : len(baseAsArray) - 2])
        # Iterate the elements in general
        for j in range(length):
            
            lbot = j
            baseIn = first + str(lbot)


            # Reproduce a new row of possibilities which come from the "base"
            row = repeat(baseIn, length)

            result.append(row)
            result_part.append(row)

            print("O Result part")
            print(result_part)
            # If 

            # If we in the end of the iteration
            if length - j == 1:
                # print("\n In if length - j == 1 ")
                base = row[len(row) - 1]

            if len(base) < length - 1:
                pass
            
        # endfor


        # Final size of the base
        lenBase = len(base)

        # base string as array
        baseToUse = arrayReverse(arrayFromString(base))  

        #       
        if lenBase <= length:
            #print("Forming newBase")
            #print(f"lenBase {lenBase}")
            #print(f"baseToUse {baseToUse}")
            newBase = ""

            # Loop from 0 to (lenBase - 1) to iterate the base elements
            for i in range(lenBase):
                print(f"The base {newBase}")
                #print("The i index ", i)

                # Get the characters from the end to the begin
                lastFromBase = baseToUse[i]
                #print("The lastFromBase ",  lastFromBase)
                
                
                if base == "0555":
                    print()
                
                
                
                # if the actual base is equal to the lastMask
                if base == lastMask:
                    stopCondition = True
                    await create_json_mask_file(len(result_part), result_part)
                    break

                # If all the elements in the base are equal to the last element in the array
                # of the main input 
                if isAllLastElement(baseToUse, array[length - 1]):
                    print("leveling up")
                    newBase = levelUp(len(baseToUse))
                    await create_json_mask_file(len(result_part), result_part)
                    result_part = []
                    break
            
                # if lastFromBase is equal to last element in the array of the main input, add 0 in its 
                # related position in the newBase 
                # else: add 1 in the lastFromBase, join the result in the newBase and return the newBase out of the loop
                if int(lastFromBase) == array[length - 1]: 
                    newBase = newBase + "0"
                    print("5 to 0")
                else: 
                    nmb = int(lastFromBase) + 1
                    if length - i - 1 >= 0 :
                        u = baseToUse[i + 1:]

                        if len(u) > 0:    
                            v = arrayReverse(u)
                            newBase = arrayToString(v) + str(nmb) +  newBase
                            print("From ", lastFromBase, " til ", nmb)
                        else: 
                            newBase = str(nmb) +  newBase
                    else:
                        newBase = nmb + newBase

                    break 
            # endfor
        else:
            print("Tragado no else")
            print("newBase: ", newBase)
            input()
        # endif

        base = newBase
        print("Base state: ", base)
        #break
        #exit()

        if base == "999999999":
            break
    # endwhile    

        
    
   
    print(result)
    print(base)

    

    

               

def repeat(leading, length): 
    row = []
    for i in range(length):
        join = leading + str(i)
        row.append(join)
        if i == length -1:
            break
    
    return row





def isAllLastElement(array, element):
    for i in range(len(array)):
        if int(array[i]) != element:
            return False

    return True


def levelUp(length):
    r = "0"
    for i in range(length):
        r += "0"
   
    return r

def generateLastMask(array):
    r = ""
    length = len(array)
    for i in range(length):
        r += str(array[length - 1])
        
    return r

def repeat2():
    pass

def arrayReverse(array):
    arrayReversed = []
    length = len(array)

    for i in range(length):
        if i == 0: continue
        arrayReversed.append(array[length - i])

    arrayReversed.append(array[0])

    return arrayReversed

def arraySlice(array, start, end):
    return array[start:end]


async def create_json_mask_file1(length, data):
    file_name = f"masks/mask-{length}.json"
    async with aiofiles.open(file_name, "w", encoding="utf-8") as file:
        await file.write(json.dumps(data, ensure_ascii=False, indent=4))
    print(f"File '{file_name}' created successfully!")



async def create_json_mask_file(length, data):
    file_name = f"masks/mask-{length}.json"

    if not data:
        print(f"⚠️ Atenção: Nenhum dado para salvar em {file_name}!")
        return

    async with aiofiles.open(file_name, "w", encoding="utf-8") as file:
        await file.write(json.dumps(data, ensure_ascii=False, indent=4))

    print(f"✅ Arquivo '{file_name}' criado com sucesso!")



asyncio.run(repeatFirst(array))





