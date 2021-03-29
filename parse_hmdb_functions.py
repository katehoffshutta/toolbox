from lxml import etree
import sys

def clean(x):
    x = x.strip()
    x = x.strip("\n")
    return(x)

def populateMetabDict(xml):
    context = etree.iterparse(xml)
    metabDict = {}
    for event, element in context:

        # accession
        if(element.tag=="{http://www.hmdb.ca}accession" and element.getparent().tag=="{http://www.hmdb.ca}metabolite"):
            currHMDB = element.text
            metabDict[currHMDB]={}
        # Metabolite
        if(element.tag=="{http://www.hmdb.ca}name" and element.getparent().tag=="{http://www.hmdb.ca}metabolite"):
            metabDict[currHMDB]["Metabolite"]=element.text
        # synonyms
        if(element.tag=="{http://www.hmdb.ca}synonym" and element.getparent().tag=="{http://www.hmdb.ca}synonyms" and element.getparent().getparent().tag=="{http://www.hmdb.ca}metabolite"):
            if("synonyms" in metabDict[currHMDB].keys()):
                metabDict[currHMDB]["synonyms"].append(element.text)
            else:
                metabDict[currHMDB]["synonyms"]=[element.text]
        # direct_parent 
        if(element.tag=="{http://www.hmdb.ca}direct_parent"):
            metabDict[currHMDB]["direct_parent"]=element.text
        # kingdom
        if(element.tag=="{http://www.hmdb.ca}kingdom"):
            metabDict[currHMDB]["kingdom"]=element.text
        # super_class
        if(element.tag=="{http://www.hmdb.ca}super_class"):
            metabDict[currHMDB]["super_class"]=element.text
        # class
        if(element.tag=="{http://www.hmdb.ca}class"):
            metabDict[currHMDB]["class"]=element.text
        # sub_class
        if(element.tag=="{http://www.hmdb.ca}sub_class"):
            metabDict[currHMDB]["sub_class"]=element.text
        # diseases
        if(element.tag=="{http://www.hmdb.ca}name" and element.getparent().tag=="{http://www.hmdb.ca}disease"):
            disease = element.text
            if("diseases" in metabDict[currHMDB].keys()):
                metabDict[currHMDB]["diseases"].append(disease)
            else:
                metabDict[currHMDB]["diseases"]=[disease]
        # pathways
        if(element.tag=="{http://www.hmdb.ca}name" and element.getparent().tag=="{http://www.hmdb.ca}pathway"):
            pathway = element.text
            if("pathways" in metabDict[currHMDB].keys()):
                metabDict[currHMDB]["pathways"].append(pathway)
            else:
                metabDict[currHMDB]["pathways"]=[pathway]
        # kegg
        if(element.tag=="{http://www.hmdb.ca}kegg_map_id"):
            kegg = element.text
            if(kegg == None):
                continue
            elif("kegg_pathways" in metabDict[currHMDB].keys()):
                metabDict[currHMDB]["kegg_pathways"].append(kegg)
            else:
                metabDict[currHMDB]["kegg_pathways"]=[kegg]

    return(metabDict)

def writeTSV(metabDict):
    mx = metabDict.keys()
    attributes = ["Metabolite","direct_parent","kingdom","super_class","class","sub_class"]

    outfile = open("metabolites.tsv","w")
    outfile.write("HMDB.ID\t")
    for attr in attributes:
        outfile.write(attr)
        outfile.write("\t")
    outfile.write("diseases")
    outfile.write("\t")
    outfile.write("pathways")
    outfile.write("\t")
    outfile.write("kegg_pathways")
    outfile.write("\t")
    outfile.write("synonyms")
    outfile.write("\n")
    
    for hmdb in mx:
        if(hmdb == None):
            continue
        else:
            outfile.write(clean(hmdb))
            outfile.write("\t")
            for attr in attributes:
                if(attr in metabDict[hmdb].keys()):
                    if(metabDict[hmdb][attr]!=None):
                        outfile.write('"')
                        outfile.write(clean(metabDict[hmdb][attr]))
                        outfile.write('"')
                    else:
                        outfile.write("NA")
                    outfile.write("\t")
            if "diseases" in metabDict[hmdb].keys():
                outfile.write('"')
                for disease in metabDict[hmdb]["diseases"][:-1]:
                    outfile.write(clean(disease))
                    outfile.write(";")
                outfile.write(clean(metabDict[hmdb]["diseases"][-1]))
                outfile.write('"')
            else:
                outfile.write("NA")
            outfile.write("\t")
            if "pathways" in metabDict[hmdb].keys():
                outfile.write('"')
                for pathway in metabDict[hmdb]["pathways"][:-1]:
                    outfile.write(clean(pathway))
                    outfile.write(";")
                outfile.write(clean(metabDict[hmdb]["pathways"][-1]))
                outfile.write('"')
            else:
                outfile.write("NA")
            outfile.write("\t")
            if "kegg_pathways" in metabDict[hmdb].keys():
                outfile.write('"')
                for kegg in metabDict[hmdb]["kegg_pathways"][:-1]:
                    outfile.write(clean(kegg))
                    outfile.write(";")
                outfile.write(clean(metabDict[hmdb]["kegg_pathways"][-1]))
                outfile.write('"')
            else:
                outfile.write("NA")
            outfile.write("\t")
            if "synonyms" in metabDict[hmdb].keys():
                outfile.write('"')
                for synonym in metabDict[hmdb]["synonyms"][:-1]:
                    outfile.write(clean(synonym))
                    outfile.write(";")
                outfile.write(clean(metabDict[hmdb]["synonyms"][-1]))
                outfile.write('"')
            else:
                outfile.write("NA")
        outfile.write("\n")
    outfile.close()
    return

