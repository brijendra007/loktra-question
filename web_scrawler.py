import requests
import sys
import re
from bs4 import BeautifulSoup

def text_scrapper(keyword,page_number=None):
    if page_number !=None:#its for Query 2
        url='http://www.shopping.com/products~PG-'+str(page_number)+'?KW='+str(keyword)
        source_code=requests.get(url);
        plain_text=source_code.text
        soup = BeautifulSoup(plain_text)
        for producttitle in soup.findAll('span',{'id':re.compile('nameQA.*')}):
           print producttitle.get('title')
        results=soup.find('span',{'class':'numTotalResults'}).text
        print results   
    else:  #its for Query 1  
        url='http://www.shopping.com/products?KW=' + str(keyword)
        source_code=requests.get(url);
        plain_text=source_code.text
        soup = BeautifulSoup(plain_text)
        results=soup.find('span',{'class':'numTotalResults'}).text
        print results

if __name__ == "__main__":           
    length=len(sys.argv)
    if length < 2 or length > 3:
        print "please provide the specific argument"        
    elif length == 2:
        keyword=sys.argv[1]
        text_scrapper(keyword)
    else:
        page_number=sys.argv[1]
        keyword=sys.argv[2]
        text_scrapper(keyword,page_number)
        
        
        
        
        