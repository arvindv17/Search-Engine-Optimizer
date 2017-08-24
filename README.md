# Search-Engine-Optimizer
This project is aimed at creating a simple WebCrawler in Python. From the raw HTML data extracted after crawling through the webpage, the relevant texts are extracted and resturned as a list.

# Description
A web crawler is an automated script to crawl (browse) through pages in the World Wide Web. This is one of the ways used by search engines to keep track of the pages that have been visited and have been optimized.
One of the key challenges that is faced by a web crawl a particular web page and identify its relevancy. Big and powerful search engines perform web crawling where they go around the web searching for pages and the ones are visited are marked as ‘visited’. To optimize their search, they have also started classifying the pages based on the content, to easily identify and filter out results based on key search terms.

# Objective
To take any URL, scrape it and give the most relevant details to classify it and enable in search optimization.

# Architecture
The requirements of the development of this project were to take a user URL input, and provide the most relevant text in those URL. The relevant text are to be returned as a list.

For this phase, we have used Python and its rich libraries to perform the crawling and the cleaning functions.

URL is taken from the user as an input. This URL is converted to the corresponding raw HTML. Relevancy has been identified as the most frequently occurring terms(other than the stop words) in the context. Once these values have been identified, the top values are returned in a list to mark the relevancy.

# Approach
A generic URL is taken as a user input. The resultant is the most relavant key words which are scraped from the web data. The relavant key words are the cleaned words using NLTK package, and the most frequently occurring words.

# Steps
1.	Take a user Input as a URL
2.	Verify if that is a valid URL or not.
3.	Use the python library BeautifulSoup to crawl the data from the webpage. BeautifulSoup returns a soup, which contains all the HTML tags and the raw HTML of the page.
4.	Clean the raw HTML tags and take only the content.
5.	Split the raw HTML input into lines
6.	Using NLTK library, clean the punctuation marks and the stop words. Also stem the words to get the correct values.
7.	Get the most frequently mentioned words in the text.
Note:- This has been configured as 15 for the current code. This can be changed based on the number of results that are needed.
8.	The highest mentioned words in the texts are rated as the most relevant for search optimization.

Note:- The number of words returned is a custom slice of the list. It has been put as 15, it can be changed accordingly.


# Links
1. [Scripts](https://github.com/arvindv17/Search-Engine-Optimizer/tree/master/Scripts)
2. [Documents](https://github.com/arvindv17/Search-Engine-Optimizer/tree/master/Documents)
