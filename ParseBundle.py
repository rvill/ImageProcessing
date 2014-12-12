import numpy as np


#ref: https://mail.python.org/pipermail/tutor/2002-May/014665.html

arr = []
inp = open ("/home/rvill/Desktop/research/image-scraping/geosearch-flickr/flickrcrawler/github/ImageProcessing/img/tag/img-output/bundle/bundle.out","r")
#read line into array 

for line in inp.readlines()[2:]: #skip 1st 2 lines
    # add a new sublist
    arr.append([])
    # loop over the elemets, split by whitespace
    for i in line.split():
        # convert to integer and append to the last
        # element of the list
        arr[-1].append(float(i))
print arr[33]
print np.add(arr[1],arr[33])

"""n=3
data = np.genfromtxt('/home/rvill/Desktop/research/image-scraping/geosearch-flickr/flickrcrawler/github/ImageProcessing/img/tag/img-output/bundle/bundle.out',skiprows=n)"""

"""data = np.genfromtxt('/home/rvill/Desktop/research/image-scraping/geosearch-flickr/flickrcrawler/github/ImageProcessing/img/tag/img-output/bundle/bundle.out', invalid_raise=True)
avg = np.average(data)
print avg"""
