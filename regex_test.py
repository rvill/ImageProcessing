import re

#file=open('url.txt','r')

#for line in  file:
url='https://farm4.staticflickr.com/3943/15386021170_c2607cb639_z.jpg'

result=re.search(r'^(https://)?(farm4\.)?(staticflickr\.com/)?(\d+)?(\D+)(\d+)',url).group(6)

print result

#file.close()
