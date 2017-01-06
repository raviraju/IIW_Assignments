import urllib.request
from urllib.error import HTTPError
from bs4 import BeautifulSoup

from nltk import sent_tokenize#, word_tokenize, pos_tag

from corenlp_pywrap import pywrap

#import corenlp_pywrap as cp
#import logging
#cp.pywrap.root.setLevel(logging.DEBUG)

outfile = open('training', 'w')
no_of_sentence_units = 0

full_annotator_list = ["tokenize", "cleanxml", "ssplit", "pos", "lemma", "ner", "regexner", "truecase", "parse", "depparse", "dcoref", "relation", "natlog", "quote"]
ner_annotator_list = ["pos", "ner"]
cn = pywrap.CoreNLP(url='http://localhost:9000', annotator_list=ner_annotator_list)

LABEL = { 'd' : 'date', 'm' : 'month', 'y' : 'year',
          'p' : 'place',
          'c' : 'cause',     #(EarthQuake/OilSpill/FireAccident/typhoon)
          'e' : 'effect',    #(Kills/Injures/Devastates/Destroy)
          'n' : 'noAffected',
          'i' : 'irrelevant'
        }

def parseSource(src):
    print("*********************Parsing src : ", src)
    page = urllib.request.urlopen(src).read()
    soup = BeautifulSoup(page , "html.parser")
    
    #get rid of script and style elements
    for script in soup(["script", "style"]):
        script.extract()
    
    text = soup.get_text()
    
    #break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    for chunk in chunks:
        if chunk:
            sentences = sent_tokenize(chunk)
            for sent in sentences:
                print(sent)
                #stopChoice = input("Do u want to stop (y/n)?")
                #if stopChoice == "y":
                    #return
                choice = input("Do u want to consider the sentence for training data unit (y/n)?")
                if choice == "y":
                    print('''
							Labels : 
							d : date,          m : month,   y : year 
							p : place
							c : cause(EarthQuake/OilSpill/FireAccident/typhoon)
							e : effect(Kills/Injures/Devastates/Destroy)
							n : noAffected      i : irrelevant ''')
                    #tokens = word_tokenize(sent) using nltk
                    #tagged_tokens = pos_tag(tokens)
                    #print(tagged_tokens)
                    try:
                        #token_dict = cn.arrange(str(sent.encode('utf-8')))
                        token_dict = cn.arrange(sent)
                        indexes = token_dict['index']
                        for i in indexes:
                            j = int(i) -1
                            word = token_dict['originalText'][j]
                            
                            labelChoice = input("labelling : \n\"{}\" \nEnter your choice : ".format(word))
                            label = LABEL.get(labelChoice,'irrelevant')#default : irrelevant
                            
                            capCode = "0"
                            capChoice = input("Capitalized (y/n) ?")
                            if capChoice == "y":
                                capCode = "1"
                                
                            numCode = "0"
                            numChoice = input("Numeral (y/n) ?")
                            if numChoice == "y":
                                numCode = "1"
                            
                            seqCode = "O"
                            seqChoice = input("B-X (b), I-X(i), O(o)")
                            if seqChoice == "b":
                                seqCode = "B-X"
                            elif seqChoice == "i":
                                seqCode = "I-X"
                            else:
                                seqCode = "O"
                            resultString = "{} {} {} {} {} {} {}".format(word, token_dict['pos'][j], token_dict['ner'][j], capCode, numCode, seqCode, label)
                            print(resultString)
                            print(resultString, file=outfile)
                        print("", file=outfile)
                        #print(token_dict)
                        global no_of_sentence_units
                        no_of_sentence_units += 1
                        print('****************************************** No of sentences tagged : ', no_of_sentence_units)
                    except UnicodeEncodeError as e:
                        print("ignore sentence : ", sent)
                        print(e)

def main():
    sources = ["http://www.disaster-report.com/",
               "http://www.worldvision.org/disaster-response-news-stories/worst-natural-disasters-2015",
               "https://www.theguardian.com/world/2016/jul/27/flooding-in-india-affects-16m-people-and-submerges-national-park",
               "http://www.cnn.com/2016/04/04/asia/pakistan-floods/index.html",
               "http://www.rollingstone.com/culture/pictures/5-recent-underreported-environmental-disasters-20140407/elk-river-chemical-spill-0660454",
               "http://www.usnews.com/news/national/articles/2007/10/29/a-timeline-of-natural-disasters-in-california",
               "http://beforeitsnews.com/environment/2016/02/recent-natural-disasters-in-united-states-2016-2-2547510.html"
              ]
    source_1 = ["http://beforeitsnews.com/environment/2016/02/recent-natural-disasters-in-united-states-2016-2-2547510.html"]
    
    
    try:
        for src in sources:
            parseSource(src)
    except HTTPError as e:
        print("unable to parse src : {} due to {}".format(src,e))
        
if __name__=="__main__" : main()
