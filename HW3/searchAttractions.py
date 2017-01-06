import argparse
import json
import pprint
import collections

attractionsDict = {}
attractionsList = []

def validateJsonLineFile(filePath):
    fileHandle = open(filePath)
    try:
        for objLine in fileHandle:
            obj = json.loads(objLine)
            for attraction in obj:
                attractionsDict[attraction] = obj[attraction]
                attractionsList.append(attraction.lower())
            #pprint.pprint(obj, indent=4)
    except ValueError:  # includes simplejson.decoder.JSONDecodeError
        print('Decoding JSON has failed. INVALID Json Lines file')
        return False
    print('Json Lines file is VALID')
    return True

def get_key(key):
    try:
        return int(key)
    except ValueError:
        return key

def main():
    parser = argparse.ArgumentParser(description="Search for Attractions")
    parser.add_argument("path", help="path to load attractions JsonLines File")
    args = parser.parse_args()
    filePath = args.path
    if validateJsonLineFile(filePath):
        attractions = set(attractionsList)
        place = input("Enter place of attraction : ")
        if place in attractions:
            sortedAttractions = (sorted(attractionsDict[place].items(), key=lambda t: get_key(t[0])))
            print("Rank    Attraction")
            #pprint.pprint(sortedAttractions)
            for rank,attraction in sortedAttractions:
                print("{}\t{}".format(rank,attraction['attraction']))
                print("\tURL: ", attraction['url'])
                print("\tNoOfReviews : ", attraction['noOfReviews'])
                print("\tAddress : ", attraction['address'])
                print("\tContact: ", attraction['contact'])
                print()
        else:
            print("Attraction {} NOT FOUND".format(place))
        

if __name__ == "__main__" : main()