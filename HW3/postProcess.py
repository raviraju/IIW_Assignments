import json_lines, json
import argparse 
#import pprint

def main():
	
	parser = argparse.ArgumentParser(description="post process Json Lines file from scrapinghub")
	parser.add_argument("path", help="path to file to parse")
	args = parser.parse_args()
	filePath = args.path
	
	attractions = {}
	unknown_place = ['PlaceUnknown']
	unknown_ranking = ['RankUnknown']
	unknown_reviewCount = ['ReviewsUnknown']
	unknown_address = ['AddressUnknown']
	unknown_contact = ['ContactUnknown']

	with open('attractions.jl', 'w') as outfile:
		with open(filePath, encoding='utf8') as infile:
			for item in json_lines.reader(infile):
				#print(item.keys(), type(item))
				if 'things_to_do_in' in item.keys():
					thing = item['things_to_do_in'][0]
					if not thing:#None
						continue
					attractionPlace = thing.lower()
					
					placeList = item.get('place',unknown_place) #item['place'][0]
					place = placeList[0]
					rankingList = item.get('ranking',unknown_ranking)
					ranking = rankingList[0].strip('#') #int(rankingList[0].strip('#'))	
					reviewCountList = item.get('reviewCount',unknown_reviewCount)
					reviewCount = reviewCountList[0].strip(' Reviews')
					
					addressList = item.get('address',unknown_address)
					address = addressList[0]
					contactList = item.get('contact',unknown_contact)
					contact = contactList[0]
					
					url = item.get('url','url not found')
	
					#address
					if attractionPlace in attractions.keys():
						attractions[attractionPlace][ranking] = {}
						attractions[attractionPlace][ranking]['attraction'] = place
						attractions[attractionPlace][ranking]['url'] = url
						attractions[attractionPlace][ranking]['noOfReviews'] = reviewCount
						attractions[attractionPlace][ranking]['address'] = address
						attractions[attractionPlace][ranking]['contact'] = contact
					else:
						place_info = {}
						place_info[ranking] = {}
						place_info[ranking]['attraction'] = place
						place_info[ranking]['url'] = url
						place_info[ranking]['noOfReviews'] = reviewCount
						place_info[ranking]['address'] = address
						place_info[ranking]['contact'] = contact
						attractions[attractionPlace] = place_info
		#pprint.pprint(attractions, indent=4)
		for attraction,detail in attractions.items():
			tmpDict = {}
			tmpDict[attraction] = detail
			json.dump(tmpDict, outfile)
			print(file=outfile)

if __name__ == "__main__" : main()