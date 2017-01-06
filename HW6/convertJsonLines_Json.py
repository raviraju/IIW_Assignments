import json_lines, json
from pprint import pprint 
import argparse

allAttractionsDict = {}

def main():
    parser = argparse.ArgumentParser(description="convert Json Lines file to Json")
    parser.add_argument("jsonLinesFile", help="jsonLines File (.jl) extension")
    args = parser.parse_args()
    jsonLinesFile = args.jsonLinesFile
    attractions = {}
    with open('output.json', 'w', encoding="utf8") as outfile:
        with open(jsonLinesFile, encoding='utf8') as infile:
            for item in json_lines.reader(infile):
                tempDict = {}
                attractionPlace = 'unknown'
                #print(item.keys(), type(item))
                attractionPlace = item['attraction_in'].lower()
                attraction = item['attraction']
                for key in item.keys():
                    if key not in ('attraction_in','attraction'):
                        tempDict[key] = item[key]
                if attractionPlace in allAttractionsDict.keys():
                    allAttractionsDict[attractionPlace][attraction] = tempDict
                else:
                    allAttractionsDict[attractionPlace] = {attraction : tempDict}
        #pprint(allAttractionsDict, indent=4)
        #for attraction_in in allAttractionsDict.keys():
        #    print(attraction_in)
        #    attractions = set(allAttractionsDict[attraction_in].keys())
        #    print(attractions)
        json.dump(allAttractionsDict, outfile, indent=4)
if __name__ == "__main__" : main()