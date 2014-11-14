#!/bin/sh 

#python python_script.py

#execute: chmod u+x job.sh to make the script runnable
#run it ./job.sh

#Get flickr photos by tag, flickr returns medium sized photos. Output tags and urls to raw_output.txt
python FlickrCrawlerByTag.py > raw_output.txt

#open raw_output.txt and create a new file with  modified contents called raw_output.py 
python pre+append.py

#cleans up by using regular expression to just extract urls in text
python raw_output.py > url.txt

#Get original size image with flickr image ids. Reads url.txt as input.
python regex_jhead.py



