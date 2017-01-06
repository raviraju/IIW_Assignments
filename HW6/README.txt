JsonLine file produced by Portia :
	items_www.tripadvisor.com_9 (8).jl

JsonLine file was stored as text file with .log extension, as Trifacta-Wrangler doesnt accept .jl format
	items_www.tripadvisor.com_text.log

Scripts used in Trifacta-Wrangler :
	aggregation_no_of_attractions_per_country.wrangle
	aggregtion_no_of_attractions_per_location.wrangle  
	merging_all_results.wrangle

Data cleaned result using Trifacta-Wrangler:
	ravi_raju_hw6_data.jl

To tranform jsonLines to Json output required by assignment : shall produce output.json, renamed as ravi_raju_hw6_data.json
    python3 .\convertJsonLines_Json.py .\ravi_raju_hw6_data.jl

Report :
	ravi_raju_hw6.pdf
