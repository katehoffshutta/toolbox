import parse_hmdb_functions as phf
import sys

xml = sys.argv[1]
metabDict = phf.populateMetabDict(xml)
phf.writeTSV(metabDict)
