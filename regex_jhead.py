#!/usr/bin/env python
#this code  use s regex to extract the image ids. 

import urllib
import  os,sys
import re
import  flickrapi


api_key = '005b8c46e4020bd2639342676d41cfcc'  
api_secret = '95940c26dc30095f'  

flickr = flickrapi.FlickrAPI(api_key,api_secret)

textfile = open('url.txt')
filetext = textfile.read()
textfile.close()

#1. find all 10-11 digits (picture ids)in text file using regular expressions
matches = re.findall('\d{10,11}',filetext)
      
#2. download images from flickrapi with found ids
for photo in matches:
     url = flickr.photos_getSizes(photo_id=photo).getiterator('size')[-1].attrib['source']

     filename = '%s.'%photo + url.split('.')[-1].split('?')[0]

     urllib.urlretrieve(url, filename)

     tags = flickr.photos_getExif(photo_id=photo).getiterator('exif')

     with open('tags.xml', 'w') as tags_file:
         tags_file.write("<?xml version='1.0' encoding='UTF-8'?>\n<rdf:RDF xmlns:rdf='http://www.w3.org/1999/02/22-rdf-syntax-ns#'>\n")
         for tag in tags:
             tags_file.write('<%s:%s>%s</%s:%s>\n'%(tag.attrib['tagspace'], tag.attrib['tag'], tag.getchildren()[0].text.strip().encode('utf-8'), tag.attrib['tagspace'], tag.attrib['tag']))
         tags_file.write('</rdf:RDF>\n')

     os.system('exiftool -overwrite_original -tagsfromfile tags.xml %s'%filename)

os.remove('tags.xml')


#3. jhead on each output













