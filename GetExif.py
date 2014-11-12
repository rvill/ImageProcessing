#!/usr/bin/env python

#This code gets full resolution image from flickr image ids, and so bypassing the flickr api limit of medium-sized images only. 

import urllib
import os
import argparse
 
import flickrapi
 
api_key = '005b8c46e4020bd2639342676d41cfcc'
api_secret = '95940c26dc30095f'

parser = argparse.ArgumentParser()
parser.add_argument('--auth', action='store_true')
parser.add_argument('photos', nargs='+')
args = parser.parse_args()

flickr = flickrapi.FlickrAPI(api_key, api_secret)

if args.__dict__['auth']:
    (token, frob) = flickr.get_token_part_one(perms='write')
    if not token: raw_input("Press ENTER after you authorized this program")
    flickr.get_token_part_two((token, frob))

for photo in args.__dict__['photos']:
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


