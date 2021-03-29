import unittest
import parse_hmdb_functions as phf

class TestHMDBReader(unittest.TestCase):
    
    def test_read(self):
        xml = "unit_test.xml"
        metabDict = phf.populateMetabDict(xml)
        
        trueKeys = set()
        trueKeys.add("HMDB3141592")
        self.assertEqual(trueKeys, metabDict.keys())

        self.assertEqual(metabDict["HMDB3141592"]["Metabolite"],"Pumpkin-Pi-With-Whipped-Cream")
        self.assertEqual(metabDict["HMDB3141592"]["direct_parent"],"Pies and derivatives")
        self.assertEqual(metabDict["HMDB3141592"]["kingdom"],"Desserts")
        self.assertEqual(metabDict["HMDB3141592"]["super_class"],"Holiday desserts")
        self.assertEqual(metabDict["HMDB3141592"]["class"],"Thanksgiving desserts")
        self.assertEqual(metabDict["HMDB3141592"]["sub_class"],"Pastry-related Thanksgiving desserts")

        self.assertEqual(len(metabDict["HMDB3141592"]["diseases"]),2)
        self.assertEqual(metabDict["HMDB3141592"]["diseases"][0],"Oversatiety")
        self.assertEqual(metabDict["HMDB3141592"]["diseases"][1],"Sleepiness")

        self.assertEqual(len(metabDict["HMDB3141592"]["pathways"]),2)
        self.assertEqual(metabDict["HMDB3141592"]["pathways"][0],"Delicious Things Metabolism")
        self.assertEqual(metabDict["HMDB3141592"]["pathways"][1],"Turkey Digestion Catalysts")
        
        self.assertEqual(len(metabDict["HMDB3141592"]["kegg_pathways"]),2)
        self.assertEqual(metabDict["HMDB3141592"]["kegg_pathways"][0],"map00000")
        self.assertEqual(metabDict["HMDB3141592"]["kegg_pathways"][1],"map99999")

        self.assertEqual(len(metabDict["HMDB3141592"]["synonyms"]),3)
        self.assertEqual(metabDict["HMDB3141592"]["synonyms"][0],"1,2'-Gourd-based Dessert")
        self.assertEqual(metabDict["HMDB3141592"]["synonyms"][1],"C00:0 Orange Lactase Agitator")
        self.assertEqual(metabDict["HMDB3141592"]["synonyms"][2],"C. moschata (Long Island Cheese Pumpkin) Mousse in Shell with β-Creme")

        phf.writeTSV(metabDict)
        return

if __name__ == '__main__':
    unittest.main()
