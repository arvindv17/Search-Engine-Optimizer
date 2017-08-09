import requests

#from main import crawler
from bs4 import BeautifulSoup
import urllib
#from urllib import request,error
from urllib.error import HTTPError,URLError
from urllib.request import urlopen
import nltk

from nltk.stem.snowball import SnowballStemmer
from nltk.tokenize import RegexpTokenizer


"""
This class is defined as crawler. It contains the function to get the HTML code of the page and to Tokenize and clean the data 
get the most relevant data.
"""
class crawler:

    #Creating the constructor by passing the URL taken in the input field
    def __init__(self,url):
        self.url=url

    """
    Function 1: getHTML()
    Will take in the user html URL input, and will parse the HTML and give out the text by cleaning out the HTML code
    Packages used : BeautifulSoup
    """
    def getHtml(self):

        html = (self.url).read()
        print("Parsing the HTML that has been extracted from the url ")
        soup = BeautifulSoup(html, "html.parser")

        # Loop to kill all script and style elements
        for script in soup(["script", "style"]):
            script.extract()

            # Extract the text from the beautifulsoup object
            text = soup.get_text()

            # break into lines and remove leading and trailing space on each
            lines = (line.strip() for line in text.splitlines())

            # break multi-headlines into a line each
            chunks = (phrase.strip() for line in lines for phrase in line.split("  "))

            # drop blank lines
            text = '\n'.join(chunk for chunk in chunks if chunk).lower()
            #print(text)

        # Removing of the punctuation marks from the extracted text which has only the lines
        print("Removing all the punctuations")
        tokenizer = RegexpTokenizer(r'\w+')
        tokens = tokenizer.tokenize(soup.text)

        #Stemming of the text
        print("Stemming of the words")
        stemmer = SnowballStemmer("english")
        stemmed_tokens = [stemmer.stem(t) for t in tokens]



        """
        This is to identify the frequency distribution of each word. If a word has occurred multiple times, then
        it is highly probable that the word is relevant to identify the information in the data.
        
        In this case, it is highly important to identify the stop words like is, are, they and remove them from the entire
        stemmed text.
        """
        #fdist = nltk.FreqDist(stemmed_tokens)
        sorted(nltk.corpus.stopwords.words('english'))
        stemmed_tokens_no_stop = [stemmer.stem(t) for t in stemmed_tokens if
                                  t not in nltk.corpus.stopwords.words('english')]

        step_word_distribution = nltk.FreqDist(stemmed_tokens_no_stop)

        #Creating a dictionary of a list of the values that have just been extracted, which do not contain the stop words as well

        l = dict(list(step_word_distribution.items()))

        """
        This is to print out the values of the most relevant words that will help identify the context.
        This can be configured to identify any number of results.
        """
        print("The final output of the most frequent and relevnat terms are :")
        print(sorted(l, key=l.get, reverse=True)[:15])

def user_input():

    try:
        mainURL = urllib.request.urlopen(str(input("Enter the URL: ")))
    except HTTPError as e:
        print('The server could not fulfill the request')
        print('Error code: ', e.code)
        user_input=False

    except URLError as e:
        print('We failed to reach a server.')
        print('Reason: ', e.reason)
        user_input = False
    except NameError as e:
        print("Some error in the input URL that you are trying to enter.")
        print('Error: ', e)
        user_input = False
    except Exception as e:
        print('There is error in the URL you have entered :',e)
        user_input = False

    else:
        #user_input = True
        crawl = crawler(mainURL)
        crawl.getHtml()
        quit()

while user_input :
    user_input()
    val=str(input("Do you wish to retry?Press y/n   "))
    choice = {'y': 1, 'n': 2, 'Y': 3, 'N': 4}
    if(choice.keys() is val):
        user_input()
    else:
        print("Exiting......")
        quit()
