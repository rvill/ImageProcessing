import re


result =  re.search(r'^(https://)?(farm4\.)?(staticflickr\.com/)?(\d+)?(\D+)(\d+)',open('url.txt', 'r').read())

print result

