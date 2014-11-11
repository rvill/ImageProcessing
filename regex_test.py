#prints  each group as a separate line
import re

textfile=open('url.txt')
filetext = textfile.read()
textfile.close()
#find all 10-11 digits (picture ids) in textfile
matches = re.findall('\d{10,11}',filetext)
print matches

