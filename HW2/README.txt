nltk library was used to segment texts
	sudo python3 -m pip install -U nltk
	sudo python3 -m nltk.downloader all
	
Standford-CoreNLP was used for POS and NER tagging
	Install : https://github.com/hhsecond/corenlp_pywrap
	Extract and run server : 
	ravirajukrishna@ubuntu:~/Desktop/stanford-corenlp-full-2015-12-09$ java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer
	-- listing properties --
	Starting server on port 9000 with timeout of 5000 milliseconds.
	StanfordCoreNLPServer listening at /0:0:0:0:0:0:0:0:9000
	[/0:0:0:0:0:0:0:1:34326] Interactive connection

source/extractText.py 
	used to tag tokens from sources, tagged results shall be written to file : training
	ravirajukrishna@ubuntu:~/Desktop/IIW_HomeWorks$ python3 extractText.py
	
	Labels : 
		d : date,  m : month,   y : year , p : place, n : noAffected ,i : irrelevant
		c : cause(EarthQuake/OilSpill/FireAccident/typhoon)
		e : effect(Kills/Injures/Devastates/Destroy)
	Token, POS_TAG, NER_TAG, Capitalization(0/1), Numeral(0/1, Sequence_Code(B-X/I-X/O), Label(d/m/y/p/c/e/n/i)
		Last JJ MISC 0 0 O irrelevant
		Updated VBN MISC 0 0 O irrelevant
		: : O 0 0 O irrelevant
		Monday NNP DATE 1 0 B-X date
		, , DATE 0 0 O irrelevant
		September NNP DATE 1 0 I-X month
		19 CD DATE 0 1 I-X irrelevant
		, , DATE 0 0 O irrelevant
		2016 CD DATE 0 1 I-X year

		M4 NN O 0 0 O irrelevant
		.6 CD NUMBER 0 0 O irrelevant
		moderate JJ O 0 0 O irrelevant
		aftershock NN O 0 0 O cause
		in IN O 0 0 B-X irrelevant
		Sindhupalchowk NNP LOCATION 1 0 I-X place
		, , O 0 0 O irrelevant
		Nepal NNP LOCATION 1 0 I-X place


other_files/template_file
	Configure template file for crf module
	# Unigram
	# Token Sequence
	U00:%x[-2,0]
	U01:%x[-1,0]
	U02:%x[0,0]
	U03:%x[1,0]
	U04:%x[2,0]
	U05:%x[-1,0]/%x[0,0]
	U06:%x[0,0]/%x[1,0]

	#POS
	U10:%x[-2,1]
	U11:%x[-1,1]
	U12:%x[0,1]
	U13:%x[1,1]
	U14:%x[2,1]
	U15:%x[-2,1]/%x[-1,1]
	U16:%x[-1,1]/%x[0,1]
	U17:%x[0,1]/%x[1,1]
	U18:%x[1,1]/%x[2,1]

	U20:%x[-2,1]/%x[-1,1]/%x[0,1]
	U21:%x[-1,1]/%x[0,1]/%x[1,1]
	U22:%x[0,1]/%x[1,1]/%x[2,1]

	# Token and POS
	U30:%x[0,0]/%x[0,1]
	#NER
	U31:%x[0,2]
	#Captilize
	U32:%x[0,3]
	#Numeral
	U33:%x[0,4]

	#BIO
	U40:%x[-2,5]
	U41:%x[-1,5]
	U42:%x[0,5]
	U43:%x[1,5]
	U44:%x[2,5]

	# Bigram
	B

other_files/model_file
	Run crf_learn to train crf classifier: https://taku910.github.io/crfpp/
	ravirajukrishna@ubuntu:~/Desktop/IIW_HomeWorks$ crf_learn template_file training model_file
	CRF++: Yet Another CRF Tool Kit
	Copyright (C) 2005-2013 Taku Kudo, All rights reserved.

	reading training data: 100.. 
	Done!0.02 s

	Number of sentences: 110
	Number of features:  57960
	Number of thread(s): 4
	Freq:                1
	eta:                 0.00010
	C:                   1.00000
	shrinking size:      20
	iter=0 terr=0.90168 serr=0.82727 act=57960 obj=2347.68950 diff=1.00000
	iter=1 terr=0.29495 serr=1.00000 act=57960 obj=1150.48870 diff=0.50995
	iter=2 terr=0.29495 serr=1.00000 act=57960 obj=1014.44491 diff=0.11825
	iter=3 terr=0.23118 serr=0.83636 act=57960 obj=802.74979 diff=0.20868
	iter=4 terr=0.14880 serr=0.70000 act=57960 obj=541.03481 diff=0.32602
	iter=5 terr=0.09300 serr=0.52727 act=57960 obj=382.71573 diff=0.29262
	iter=6 terr=0.05934 serr=0.43636 act=57960 obj=299.98616 diff=0.21616
	iter=7 terr=0.05403 serr=0.39091 act=57960 obj=255.84516 diff=0.14714
	iter=8 terr=0.04960 serr=0.38182 act=57960 obj=228.51594 diff=0.10682
	iter=9 terr=0.04163 serr=0.32727 act=57960 obj=204.09372 diff=0.10687
	iter=10 terr=0.02657 serr=0.23636 act=57960 obj=174.44643 diff=0.14526
	iter=11 terr=0.00974 serr=0.10000 act=57960 obj=151.19425 diff=0.13329
	iter=12 terr=0.00797 serr=0.08182 act=57960 obj=134.60191 diff=0.10974
	iter=13 terr=0.00531 serr=0.05455 act=57960 obj=130.34941 diff=0.03159
	iter=14 terr=0.00443 serr=0.04545 act=57960 obj=125.64616 diff=0.03608
	iter=15 terr=0.00354 serr=0.03636 act=57960 obj=124.37878 diff=0.01009
	iter=16 terr=0.00443 serr=0.04545 act=57960 obj=121.60175 diff=0.02233
	iter=17 terr=0.00443 serr=0.04545 act=57960 obj=120.60339 diff=0.00821
	iter=18 terr=0.00443 serr=0.04545 act=57960 obj=118.98925 diff=0.01338
	iter=19 terr=0.00354 serr=0.03636 act=57960 obj=117.43824 diff=0.01303
	iter=20 terr=0.00354 serr=0.03636 act=57960 obj=118.27507 diff=0.00713
	iter=21 terr=0.00354 serr=0.03636 act=57960 obj=116.91548 diff=0.01150
	iter=22 terr=0.00354 serr=0.03636 act=57960 obj=116.17585 diff=0.00633
	iter=23 terr=0.00354 serr=0.03636 act=57960 obj=115.91188 diff=0.00227
	iter=24 terr=0.00354 serr=0.03636 act=57960 obj=115.43115 diff=0.00415
	iter=25 terr=0.00354 serr=0.03636 act=57960 obj=115.28243 diff=0.00129
	iter=26 terr=0.00354 serr=0.03636 act=57960 obj=115.12517 diff=0.00136
	iter=27 terr=0.00354 serr=0.03636 act=57960 obj=115.04233 diff=0.00072
	iter=28 terr=0.00354 serr=0.03636 act=57960 obj=114.99056 diff=0.00045
	iter=29 terr=0.00266 serr=0.02727 act=57960 obj=114.98123 diff=0.00008
	iter=30 terr=0.00266 serr=0.02727 act=57960 obj=114.92356 diff=0.00050
	iter=31 terr=0.00266 serr=0.02727 act=57960 obj=114.90616 diff=0.00015
	iter=32 terr=0.00266 serr=0.02727 act=57960 obj=114.89064 diff=0.00014
	iter=33 terr=0.00266 serr=0.02727 act=57960 obj=114.87406 diff=0.00014
	iter=34 terr=0.00266 serr=0.02727 act=57960 obj=114.86368 diff=0.00009
	iter=35 terr=0.00266 serr=0.02727 act=57960 obj=114.85204 diff=0.00010
	iter=36 terr=0.00266 serr=0.02727 act=57960 obj=114.84466 diff=0.00006
	iter=37 terr=0.00266 serr=0.02727 act=57960 obj=114.84285 diff=0.00002
	iter=38 terr=0.00266 serr=0.02727 act=57960 obj=114.83883 diff=0.00004

	Done!0.81 s

	ravirajukrishna@ubuntu:~/Desktop/IIW_HomeWorks$

other_files/low_quality_testing
	testing file for low_quality sources
other_files/high_quality_testing
	testing file for high_quality sources

other_files/combined_quality_test_output.txt
other_files/low_quality_test_output.txt
other_files/high_quality_test_output.txt
Test CRF classifier on test data
	ravirajukrishna@ubuntu:~/Desktop/IIW_HomeWorks$ crf_test -m model_file testing > combined_quality_test_output.txt
	ravirajukrishna@ubuntu:~/Desktop/IIW_HomeWorks$ crf_test -m model_file low_quality_testing > low_quality_test_output.txt
	ravirajukrishna@ubuntu:~/Desktop/IIW_HomeWorks$ crf_test -m model_file high_quality_testing > high_quality_test_output.txt
	ravirajukrishna@ubuntu:~/Desktop/IIW_HomeWorks$

source/generate_report.py
	Compute Precision,Recall,F1-Scores
	ravirajukrishna@ubuntu:~/Desktop/IIW_HomeWorks$ python generate_report.py combined_quality_test_output.txt 
	('y_true_dict : ', {'cause': 17, 'effect': 10, 'month': 4, 'place': 16, 'year': 7, 'irrelevant': 234, 'noAffected': 12})
	('y_pred_dict : ', {'cause': 14, 'effect': 2, 'month': 4, 'place': 15, 'year': 6, 'irrelevant': 251, 'noAffected': 8})
	('tp_dict : ', {'cause': 10, 'effect': 1, 'month': 4, 'place': 15, 'year': 6, 'irrelevant': 231, 'noAffected': 7})
	('fp_dict : ', {'cause': 4, 'effect': 1, 'month': 0, 'place': 0, 'year': 0, 'irrelevant': 20, 'noAffected': 1})

	('recall_dict : ', {'cause': 0.59, 'effect': 0.1, 'month': 1.0, 'place': 0.94, 'year': 0.86, 'irrelevant': 0.99, 'noAffected': 0.58})
	('precision_dict : ', {'cause': 0.71, 'effect': 0.5, 'month': 1.0, 'place': 1.0, 'year': 1.0, 'irrelevant': 0.92, 'noAffected': 0.88})
	('f1_score : ', {'cause': 0.64, 'effect': 0.17, 'month': 1.0, 'place': 0.97, 'year': 0.92, 'irrelevant': 0.95, 'noAffected': 0.7})
	('weighted_avg of f1-scores for all classes: ', 0.9)
				 precision    recall  f1-score   support

		  cause       0.71      0.59      0.65        17
		 effect       0.50      0.10      0.17        10
	 irrelevant       0.92      0.99      0.95       234
		  month       1.00      1.00      1.00         4
	 noAffected       0.88      0.58      0.70        12
		  place       1.00      0.94      0.97        16
		   year       1.00      0.86      0.92         7

	avg / total       0.90      0.91      0.90       300

	ravirajukrishna@ubuntu:~/Desktop/IIW_HomeWorks$ python generate_report.py high_quality_test_output.txt 
	('y_true_dict : ', {'cause': 9, 'effect': 5, 'month': 2, 'place': 10, 'year': 3, 'irrelevant': 148, 'noAffected': 6})
	('y_pred_dict : ', {'cause': 6, 'effect': 1, 'month': 2, 'place': 10, 'year': 2, 'irrelevant': 157, 'noAffected': 5})
	('tp_dict : ', {'cause': 5, 'effect': 1, 'month': 2, 'place': 10, 'year': 2, 'irrelevant': 147, 'noAffected': 5})
	('fp_dict : ', {'cause': 1, 'effect': 0, 'month': 0, 'place': 0, 'year': 0, 'irrelevant': 10, 'noAffected': 0})

	('recall_dict : ', {'cause': 0.56, 'effect': 0.2, 'month': 1.0, 'place': 1.0, 'year': 0.67, 'irrelevant': 0.99, 'noAffected': 0.83})
	('precision_dict : ', {'cause': 0.83, 'effect': 1.0, 'month': 1.0, 'place': 1.0, 'year': 1.0, 'irrelevant': 0.94, 'noAffected': 1.0})
	('f1_score : ', {'cause': 0.67, 'effect': 0.33, 'month': 1.0, 'place': 1.0, 'year': 0.8, 'irrelevant': 0.96, 'noAffected': 0.91})
	('weighted_avg of f1-scores for all classes: ', 0.93)
				 precision    recall  f1-score   support

		  cause       0.83      0.56      0.67         9
		 effect       1.00      0.20      0.33         5
	 irrelevant       0.94      0.99      0.96       148
		  month       1.00      1.00      1.00         2
	 noAffected       1.00      0.83      0.91         6
		  place       1.00      1.00      1.00        10
		   year       1.00      0.67      0.80         3

	avg / total       0.94      0.94      0.93       183

	ravirajukrishna@ubuntu:~/Desktop/IIW_HomeWorks$ python generate_report.py low_quality_test_output.txt 
	('y_true_dict : ', {'cause': 8, 'effect': 5, 'month': 2, 'place': 6, 'year': 4, 'irrelevant': 86, 'noAffected': 6})
	('y_pred_dict : ', {'cause': 8, 'effect': 1, 'month': 2, 'place': 5, 'year': 4, 'irrelevant': 94, 'noAffected': 3})
	('tp_dict : ', {'cause': 5, 'effect': 0, 'month': 2, 'place': 5, 'year': 4, 'irrelevant': 84, 'noAffected': 2})
	('fp_dict : ', {'cause': 3, 'effect': 1, 'month': 0, 'place': 0, 'year': 0, 'irrelevant': 10, 'noAffected': 1})
	NOTE:
	('Unable to compute f1_score for : ', 'effect')
	('recall_dict[keyClass] : ', 0.0)
	('precision_dict[keyClass] : ', 0.0)

	('recall_dict : ', {'cause': 0.63, 'effect': 0.0, 'month': 1.0, 'place': 0.83, 'year': 1.0, 'irrelevant': 0.98, 'noAffected': 0.33})
	('precision_dict : ', {'cause': 0.63, 'effect': 0.0, 'month': 1.0, 'place': 1.0, 'year': 1.0, 'irrelevant': 0.89, 'noAffected': 0.67})
	('f1_score : ', {'cause': 0.63, 'effect': 0.0, 'month': 1.0, 'place': 0.91, 'year': 1.0, 'irrelevant': 0.93, 'noAffected': 0.44})
	('weighted_avg of f1-scores for all classes: ', 0.85)
				 precision    recall  f1-score   support

		  cause       0.62      0.62      0.62         8
		 effect       0.00      0.00      0.00         5
	 irrelevant       0.89      0.98      0.93        86
		  month       1.00      1.00      1.00         2
	 noAffected       0.67      0.33      0.44         6
		  place       1.00      0.83      0.91         6
		   year       1.00      1.00      1.00         4

	avg / total       0.84      0.87      0.85       117

	ravirajukrishna@ubuntu:~/Desktop/IIW_HomeWorks$ 

