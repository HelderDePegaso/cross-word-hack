import os
import json
import unittest

class ImportMaskArchive:
    @staticmethod
    def path():
        return os.path.join("masks", "linguistic-masks")
    
    @staticmethod
    def pathLang(lang: str):
        """
        Return the path of the language folder.
        """
        path = os.path.join(ImportMaskArchive.path(), lang)
        print("The path is: ", path)
        if os.path.exists(path):
            return path
        else:
            raise FileNotFoundError("Language folder not found")

    @staticmethod
    def validateCharLength(charLength: int):
        if not isinstance(charLength, int) or charLength <= 0:
            raise ValueError("charLength must be a positive integer")
    
    @staticmethod
    def maskFilePath(language: str, maskName: str):
        """
        Return the full path of a mask file.
        """
        return os.path.join(ImportMaskArchive.pathLang(language), f"{language}-lpm-{maskName}", f"{language}-lpm-{maskName}.json")
    
    @staticmethod
    def enlistMasks(language: str):
        """
        Import all masks with names of a certain length from the top-level package.
        """
        try:
            path = ImportMaskArchive.pathLang(language)
            
            print("The language is: ", language)
            finalPath = os.path.join(path, f"{language}-lpm-stats.json")

            if not os.path.exists(finalPath):
                raise FileNotFoundError("The stat file {finalPath} does not exist".format(finalPath=finalPath))
            with open(os.path.join(path, f"{language}-lpm-stats.json"), 'r') as f:
                langMasksStats = json.load(f)
    
            if langMasksStats is None:
                raise FileNotFoundError("Language masks stats file not found")
            return langMasksStats.get("pt-lpm", {}).get("list", [])
        except Exception | FileNotFoundError as e:
            print(e)
            return None
    
    @staticmethod
    def fromTop(charLength: int, language):
        """
        Import all masks with names of a certain length from the top-level package.
        """
        try:
            ImportMaskArchive.validateCharLength(charLength)
            
            pathLang = ImportMaskArchive.pathLang(language)
            masksNames: list = ImportMaskArchive.enlistMasks(language)
            print("The list")
            print(masksNames)
            for maskName in masksNames:
                # Get the first character in maskName
                inxZ = int(maskName.split("-")[0])
                if inxZ <= charLength:
                    yield ImportMaskArchive.importOneByName(ImportMaskArchive.maskFilePath(language, maskName))
        
        except ValueError as e:
            print(e)
            return None
        
    @staticmethod
    def importAllFromTop(char_length: int, language: str):
        """
        Import all masks with names of a certain length from the top-level package.
        """
        try:
            print("The language is: ", language)
            return list(ImportMaskArchive.fromTop(char_length, language))
        except StopIteration:
            print("No more masks to import.")
            return None

    @staticmethod
    def importOneByLength(charLength: int, language: str):
        """
        Import the first mask with a name of a certain length from the top-level package.
        """
        try:
            ImportMaskArchive.validateCharLength(charLength)
            return {}
        except ValueError as e:
            print(e)
            return None
        
        masksNames: list = ImportMaskArchive.enlistMasks(language)
        for maskName in masksNames:
            # Get the first character in maskName
            inxZ = int(maskName.split("-")[0])
            if inxZ == charLength:
                return ImportMaskArchive.importOneByName(ImportMaskArchive.maskFilePath(language, maskName))

    @staticmethod
    def importOneByName(mask_name: str):
        print("The mask name is: ", mask_name)
        if not os.path.exists(mask_name):
            raise FileNotFoundError("Mask file not found")
        with open(mask_name, 'r') as f:
            print("The file is: ", f)
            package = json.load(f)
            
        return package








#print(ImportMaskArchive.importAllFromTop(5, "pt"))

#class TestImportMaskArchive(unittest.TestCase):
#    def test_importAllFromTop(self):
#        self.assertIsInstance(ImportMaskArchive.importAllFromTop(5, "pt"), list)

    #def test_importOneByLength(self):
    #    self.assertIsInstance(ImportMaskArchive.importOneByLength(5, "pt"), dict)
    #def test_importOneByName(self):
    #    mask_name = ImportMaskArchive.maskFilePath("pt", "5-test")
    #    self.assertIsInstance(ImportMaskArchive.importOneByName(mask_name), dict)
#
    #def test_fromTop(self):
    #    result = list(ImportMaskArchive.fromTop(5, "pt"))
    #    self.assertIsInstance(result, list)
    #    self.assertGreaterEqual(len(result), 0)
#
    #def test_enlistMasks(self):
    #    masks = ImportMaskArchive.enlistMasks("pt")
    #    self.assertIsInstance(masks, list)

if __name__ == "__main__":
    unittest.main()