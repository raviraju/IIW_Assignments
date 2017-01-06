source1/
   items_www.tripadvisor.com_txt.log : Contains TripAdvisor Review Details for Attraction in California
   Trifacta Wrangler was used for data cleaning with the combination of following wrangle scripts
	enroute_items_www.tripadvisor.com_txt.wrangle & enroute_items_w_aggregation_txt.wrangle
   to generate Source1 for Record Linkage: info_tripAdvisor.csv


source2/
	extractCities.py : leverages GoogleScraper and StanfordCoreNLPServer to fetch Location Mentions in blogs for combinations of 			   			   pair of locations specified in california.json
			   These mentions are stored in ca_output/
	ca_output/ : a few sample files which contains the NER mentions, blogLinks extracted using Standford CRF
		anaheim_and_avalon.json
		anaheim_and_bakersfield.json

	To further cleanup the mentions extracted in ca_output getCityTowns.py is used
	getCityTowns.py : uses List_of_cities_and_towns_in_California_wiki.txt 
                          and geopy module to eliminate cities/towns mentions, invalid location mentions(whose lat,long cant be 			  			  resolved),and mentions which are too-far from either src/destination
			  Cleaned up location mentions with additional metadata(address, locType, longitude, latitude) in addition to blogLinks
			  are produced in processed_output/
	processed_output/ : a few sample files which contains the blog location mentions with enriched metadata
		anaheim_and_avalon.json
		anaheim_and_bakersfield.json

	convertJson_Csv.py : to convert json files from processed locations to summarized csv : csvResults.csv

	csvResults.csv was in turn post-processed using TextWrangler(extractPinCode.wrangle) to fetch pinCode, results found in info_blogs.csv

dataset1.csv : copy of source1/info_tripAdvisor.csv
dataset2.csv : copy of source2/info_blogs.csv
final_resulst.csv : results of record linkage