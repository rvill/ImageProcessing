import flickrapi
import urllib
import string
import os
import time

api_key = 'key'
secret ='secret'

# read query
query_retrieve_num = 5
query_file = open('query_word.txt', 'r')
query_tags = string.split(query_file.read())
query_file.close()
for query_tag in query_tags:
    print query_tag
print len(query_tags)

# flickr api
flickr = flickrapi.FlickrAPI(api_key)
for query_tag in query_tags:
    path = 'img/tag/' + query_tag
    if not os.path.exists(path):
        os.mkdir(path)
    photos = flickr.walk(tags = query_tag, extras = 'tags, url_z, original,geo_context=2')
   # photos= flickr.photos_search(tags=query_tag, lat='42.374028', lon='-71.114655',radius='5')
    current_num = 0
    for photo in photos:
        time.sleep(1)
        url = photo.get('url_z')
        if url is not None:
            #add
           # f = open("/home/rvill/Desktop/research/image-scraping/geosearch-flickr/flickrcrawler-master/img/tag/output_tags.txt", "w")
            #f.write(query_tag + '\n')
            #f.write(str(current_num))
           # f.write(url + '\n')
             #need to encode characters, otherwise 'ascii' codec can't encode  
           # f.write(photo.get('tags').encode('ascii','ignore').decode('ascii'))
           # f.close()
    
            #end  add
            print query_tag, current_num, url
            print photo.get('tags')
            file_name = path + '/' + str(current_num) + '.jpg'
            urllib.urlretrieve(url, file_name)
            current_num += 1
            if current_num >= query_retrieve_num:
                break
        else:
            print 'url is None'

        
