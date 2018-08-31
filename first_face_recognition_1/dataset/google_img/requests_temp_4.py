from bs4 import BeautifulSoup
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from user_agent import generate_user_agent
from urllib.parse import urljoin
import json
import re,time,os,csv
from random import *

cwd = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))+'/'
last_value=''	#last value initialization
last_list=[]	#last list  initialization
domain = 'http://lyricsming.com'
headers = {
            "user-agent": generate_user_agent(device_type="desktop", os=('mac', 'linux')),
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "accept-charset": "ISO-8859-1,utf-8;q=0.7,*;q=0.3",
            "accept-encoding": "gzip,deflate,sdch",
            "accept-language": "en-US,en;q=0.8",
          }

 
#----------------------------------------------#Getting Link---------------------------------------------------------------------#
def get_url(page_link):
    print('URL: ',page_link)
    time.sleep(randint(1,5))
    t0 = time.time()
    try:
        #page_response = requests_retry_session().get(page_link, timeout=5, headers=headers)
        page_response = requests.get(page_link, timeout=10, headers=headers)
        print('code:: ',page_response.status_code)
        if page_response.status_code == 200:
            return page_response
        else:
            print(page_response.status_code)
            return "Not_Found"
    except Exception as x:
        print('It failed :(', x.__class__.__name__)
        time.sleep(5)
        return get_url(page_link)
    else:
        print('It eventually worked', response.status_code)
    finally:
        t1 = time.time()
        
#-------------------------------------------------#List URL------------------------------------------------------------------#   
def parse_link(page_response,title,sliced_song_src):		
    pass

#-------------------------------------------------------------------------------------------------------------------#   
def parse_data(content,dir_cont,rel_date,mov_singer,output_dic):
    pass
#--------------------------------------------Opening Csv File------------------------------------------------------------------------#
def create_csv():
    with open(cwd+'Output.csv', 'a') as csvfile:
        fieldnames = ['file_no','movie_name','title', 'artist' , 'director_name', 'music_director_name', 'release_date','orignal_lyrics','translated_lyrics']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if(not os.path.isfile(cwd+'Identification.txt')):
            writer.writeheader()
#---------------------------------------------Writing in Csv--------------------------------------------------------#
def csv_writer(output_dic):
    with open(cwd+'Output.csv', 'a') as csvfile:
	    fieldnames = ['movie_name', 'title', 'artist', 'music_director_name',
	                  'lyricist', 'orignal_lyrics', 'devnagiri_lyrics', 'song_url']
	    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	    writer.writerow(output_dic)
#-----------------------------------------------Main File--------------------------------------------------------------------#
def start(file_no,title):			
    pass
#-------------------------------------------------------------------------------------------------------------------#
if(__name__ == '__main__'):
    sty = "-"*15
    if(os.path.isfile(cwd+'Identification.txt')):	#Check Identification
        with open(cwd+'Identification.txt') as idf:
            last_list = idf.readlines()
            last_value = last_list[-1].strip()
            print('Last Value: ',last_value)
    with open(cwd+'input.txt') as f:
        readline_list = f.readlines()
    if(last_value):
        readline_list = readline_list[len(last_list):]
    else:
    print('{}>Crawling Initiate<{}'.format(sty, sty))
    for line in readline_list:
        if(line.strip()):
            file_no, title = line.strip().split(',')  # spliting
            print('{}>{}\t{}<{}'.format((sty), (file_no), (title), (sty)))
            start(file_no, title)
            with open(cwd+'Identification.txt', 'a') as ida:
                ida.write('{},{}\n'.format(file_no,title))

#-------------------------------------------------------------------------------------------------------------------#
