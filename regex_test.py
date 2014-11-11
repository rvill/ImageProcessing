#prints  each group as a separate line
import re

file = open('url.txt')
text = file.read()
matchstr = re.findall(r'https://farm4.staticflickr.com?.\d+.d+',text)
for image_ids in text:
    print image_ids

