NOTE : The file data.zip which contains all the raw webpages (at least 500) you scraped
	Since Portia cloud based service was used to crawl and scrape web pages, web-pages werent downloaded.
	However the url of web-pages which were scrolled is reported as part of extractions.json

Portia was used to scrape Attractions found in www.tripadvisor.com : https://portia-beta.scrapinghub.com/#/projects/104977
1. Select Website like to scrape
	https://www.tripadvisor.com/Attraction_Review-g1776497-d5496345-Reviews-Sri_Ranganathaswamy_Temple-Srirangapatna_Karnataka.html
   Create a Spider
2. Set Start Page :
	https://www.tripadvisor.com/Attraction_Review-g1776497-d5496345-Reviews-Sri_Ranganathaswamy_Temple-Srirangapatna_Karnataka.html
3. Link Crawling : Configure url patterns
	/Attraction_Review-.*html$
4. Create a sample using : 
	https://www.tripadvisor.com/Attraction_Review-g1776497-d5496345-Reviews-Sri_Ranganathaswamy_Temple-Srirangapatna_Karnataka.html
5. Annotate relevant fields and upload the project to scraping hub : https://app.scrapinghub.com/p/104977/jobs
	Schedule the job and run the spider
6. Download the items as JSON Lines format:
	items_www.tripadvisor.com.jl:(an instance)
		{"ranking":["#1"],"reviewCount":["110 Reviews"],"url":"https://www.tripadvisor.com/Attraction_Review-g1776497-d5496345-Reviews-Sri_Ranganathaswamy_Temple-Srirangapatna_Karnataka.html","_type":"item","_cached_page_id":"f1b17f12b271f090607ff7b6e95e4c1a06353518","contact":["8197443378"],"things_to_do_in":["Srirangapatna"],"address":["Temple Road , Srirangapatna , India"],"_template":"f1b17f12b271f090607ff7b6e95e4c1a06353518","place":["Sri Ranganathaswamy Temple"]}
7. postCleanUp.py : 
	Script to cleanup irrelevant default fields (_type,_cached_page_id,_template) added to extractions
	Script also performs string processing and field name changes
	
	PS C:\Users\Ravi\Desktop\USC\Courses_Sem3\Info_Integrate_Web\homework\hw3\ravi_raju_hw5> python3 .\postCleanUp.py .\items_www.tripadvisor.com.jl
	Done CleanUp.Output found in extractions.json

	extractions.json:(an instance)
		{"attraction_in": "srirangapatna", "contact": "8197443378", "rank": "1", "attraction": "Sri Ranganathaswamy Temple", "address": "Temple Road , Srirangapatna , India", "noOfReviews": "110", "url": "https://www.tripadvisor.com/Attraction_Review-g1776497-d5496345-Reviews-Sri_Ranganathaswamy_Temple-Srirangapatna_Karnataka.html"}
8. validateJsonLines.py
	Validate extractions.json :
	PS C:\Users\Ravi\Desktop\USC\Courses_Sem3\Info_Integrate_Web\homework\hw3\ravi_raju_hw5> python3 .\validateJsonLines.py .\extractions.json
	Json Lines file is VALID
	PS C:\Users\Ravi\Desktop\USC\Courses_Sem3\Info_Integrate_Web\homework\hw3\ravi_raju_hw5>
	
	
For sake of Class Project:
The data source attractions reviews at www.tripadvisor.com was used to aid in collecting dataset for classProject
1. postProcess.py
	Script to group attraction reviews by the place of interest, it produces output in attractions.jl
	PS C:\Users\Ravi\Desktop\USC\Courses_Sem3\Info_Integrate_Web\homework\hw3\ravi_raju_hw5> python3 .\postProcess.py .\items_www.tripadvisor.com.jl
2. searchAttractions.py
	Script to enlist attractions at given place of interest ordered by ranking 
	
	PS C:\Users\Ravi\Desktop\USC\Courses_Sem3\Info_Integrate_Web\homework\hw3\ravi_raju_hw5> python3 .\searchAttractions.py .\attractions.jl
	Json Lines file is VALID
	Enter place of attraction : santa cruz
	Rank    Attraction
	2       Madeiralimo
			URL:  https://www.tripadvisor.com/Attraction_Review-g1053631-d4832373-Reviews-Madeiralimo-Santa_Cruz_Madeira_Madeira_Islands.html
			NoOfReviews :  38
			Address :  Santa Cruz , Madeira 9000-019 , Portugal
			Contact:  +351 291 092 320

	3       Sao Salvador Church
			URL:  https://www.tripadvisor.com/Attraction_Review-g1053631-d10354293-Reviews-Sao_Salvador_Church-Santa_Cruz_Madeira_Madeira_Islands.html
			NoOfReviews :  9
			Address :  Rua Irma Wilson, 1 , Santa Cruz , Madeira 9100-161 , Portugal
			Contact:  +351 291 524 145

	4       Focus Natura
			URL:  https://www.tripadvisor.com/Attraction_Review-g1053631-d5123379-Reviews-Focus_Natura-Santa_Cruz_Madeira_Madeira_Islands.html
			NoOfReviews :  9
			Address :  Edificio Frente Mar Foz da Ribeira da Boaventura , Santa Cruz , Madeira 9100-115 , Portugal
			Contact:  916 409 780

	5       Municipal Market of Santa Cruz
			URL:  https://www.tripadvisor.com/Attraction_Review-g1053631-d10354399-Reviews-Municipal_Market_of_Santa_Cruz-Santa_Cruz_Madeira_Madeira_Islands.html
			NoOfReviews :  8
			Address :  Rua da Praia , Santa Cruz , Madeira, Portugal
			Contact:  +351 291 520 100

	7       3S Santa Cruz Surf School
			URL:  https://www.tripadvisor.com/Attraction_Review-g1053631-d4023441-Reviews-3S_Santa_Cruz_Surf_School-Santa_Cruz_Madeira_Madeira_Islands.html
			NoOfReviews :  2
			Address :  Santa Cruz , Santa Cruz , Madeira, Portugal
			Contact:  ContactUnknown

	PS C:\Users\Ravi\Desktop\USC\Courses_Sem3\Info_Integrate_Web\homework\hw3\ravi_raju_hw5>