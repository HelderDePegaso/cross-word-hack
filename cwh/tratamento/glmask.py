import os
import json
import asyncio
import aiofiles
import argparse
from glmask_configurations import lpma 

openedMasks = ""
def prioritizeCombinations(arr):
    meio = len(arr) // 2
    primeira_metade = arr[:meio][::-1]
    segunda_metade = arr[meio:]
    high_priority = []
    medium_priority = []
    low_priority = []


    # Percorre a primeira metade de trás para frente
    for combination in primeira_metade:
        #avaliar_prioridade_curta(combination, alta, media, baixa)
        lpma(combination, high_priority, medium_priority, low_priority)

    # Percorre a segunda metade de frente para trás
    for combination in segunda_metade:
        lpma(combination, high_priority, medium_priority, low_priority)


    return {
        "high_priority": high_priority,
        "medium_priority": medium_priority,
        "low_priority": low_priority
    }

async def generate(mask, lang, path=None):
    if path is None:
        # It suposes the code to be running in the main directory
        path = "masks/linguistic-masks"

    prioritized = {
        "high_priority": [],
        "medium_priority": [],
        "low_priority": []
    }
    
    stats = {
        "high_priority": 0,
        "medium_priority": 0,
        "low_priority": 0
    }
    
    for m in mask:
        prioritizedCombinations = prioritizeCombinations(m)
        prioritized["high_priority"].extend(prioritizedCombinations["high_priority"])
        prioritized["medium_priority"].extend(prioritizedCombinations["medium_priority"])
        prioritized["low_priority"].extend(prioritizedCombinations["low_priority"])
    
    stats["high_priority"] = len(prioritized["high_priority"])
    stats["medium_priority"] = len(prioritized["medium_priority"])
    stats["low_priority"] = len(prioritized["low_priority"])
    
    opm = openedMasks.split("/")[-1].split("-")[1:]
    
    opm[-1] = opm[-1].split(".")[0]

    glowed = ""
    
    for i in range(len(opm)):
        if i <=    len(opm) - 1 and i > 0:
            glowed += "-"
        glowed +=  opm[i]

    
    general:str = "/" + lang + "-lpm-" + glowed
    folder = "{path}{general}".format(path=path, general=general)
    archive = "{path}{general}{general}.json".format(path=path, general=general)
    statFile = "{path}{general}{general}-stats.json".format(path=path, general=general)
    
    # lang + "-lpm-" + glowed + ".json"
    await saveAsFile(archive, json.dumps(prioritized, ensure_ascii=False, indent=4), folder)
    
    await saveAsFile(statFile, json.dumps(stats, ensure_ascii=False, indent=4), folder)
    
    


async def saveAsFile(archive, content, dirName):
    os.makedirs(dirName, exist_ok=True )
    async with aiofiles.open(archive, "w", encoding="utf-8") as f:
        print("Passou até aqui")
        await f.write(content)

def main():
    global openedMasks
    parser = argparse.ArgumentParser(description="Linguistic pattern mask algorithm genarator to prioritize relevant combination in a specific language")
    parser.add_argument("--mask", type=str, help="Specify the mask to use by a json arquive", required=True)
    parser.add_argument("--lang", type=str, help="Specify the language to use", required=True)
    parser.add_argument("--path", type=str, help="Specify the path to save the generated liguistic mask")

    args = parser.parse_args()
    
   
    if args.mask.endswith(".json"):
        print("Opening mask file...")
        print(openedMasks)
        openedMasks = args.mask
        print(openedMasks)
        with open(openedMasks, "r") as f:
            mask = json.load(f)
            asyncio.run(generate(mask, lang=args.lang, path=args.path))
    else:
        parser.error("Invalid mask file")
        

if __name__ == "__main__":
    
    main()
