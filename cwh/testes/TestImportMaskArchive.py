import os
import sys



from cwh import ImportMaskArchive

import unittest

class TestImportMaskArchive(unittest.TestCase):
    def test_importAllFromTop(self):
        self.assertIsInstance(ImportMaskArchive.importAllFromTop(5, "pt"), list)

    def test_importOneByLength(self):
        self.assertIsInstance(ImportMaskArchive.importOneByLength(5, "pt"), dict)
    def test_importOneByName(self):
        mask_name = ImportMaskArchive.maskFilePath("pt", "5-test")
        self.assertIsInstance(ImportMaskArchive.importOneByName(mask_name), dict)

    def test_fromTop(self):
        result = list(ImportMaskArchive.fromTop(5, "pt"))
        self.assertIsInstance(result, list)
        self.assertGreaterEqual(len(result), 0)

    def test_enlistMasks(self):
        masks = ImportMaskArchive.enlistMasks("pt")
        self.assertIsInstance(masks, list)

if __name__ == "__main__":
    unittest.main()