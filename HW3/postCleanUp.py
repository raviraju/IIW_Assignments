import json_lines, json
import argparse 
#import pprint

def main():
    
    parser = argparse.ArgumentParser(description="Cleanup Json Lines file from scrapinghub")
    parser.add_argument("path", help="path to file to cleanup")
    args = parser.parse_args()
    filePath = args.path
    
    with open('extractions.json', 'w') as outfile:
        with open(filePath, encoding='utf8') as infile:
            for item in json_lines.reader(infile):
                if 'things_to_do_in' in item.keys():
                    thing = item['things_to_do_in'][0]
                    if not thing:#None
                        continue
                    attractionPlace = thing.lower()
                    
                    url = item.get('url',None)
                    if not url:#None
                        continue
                    
                    processedDict = {}
                    processedDict['attraction_in'] = attractionPlace
                    processedDict['url'] = url
                    
                    placeList = item.get('place',None) #item['place'][0]
                    if placeList:
                        place = placeList[0]
                        processedDict['attraction'] = place
                        
                    rankingList = item.get('ranking',None)
                    if rankingList:
                        ranking = rankingList[0].strip('#') #int(rankingList[0].strip('#'))
                        processedDict['rank'] = ranking
                            
                    reviewCountList = item.get('reviewCount',None)
                    if reviewCountList:
                        reviewCount = reviewCountList[0].strip(' Reviews')
                        processedDict['noOfReviews'] = reviewCount
                    
                    addressList = item.get('address',None)
                    if addressList:
                        address = addressList[0]
                        processedDict['address'] = address
                        
                    contactList = item.get('contact',None)
                    if contactList:
                        contact = contactList[0]
                        processedDict['contact'] = contact
                    
                    json.dump(processedDict, outfile)
                    print(file=outfile)
    print("Done CleanUp.Output found in extractions.json")
if __name__ == "__main__" : main()