import re
#1.write text file
#file = open("newfile.txt","w")

#1b.read text file
file=open('url.txt', 'r')
#print  file.read()
pattern = re.compile('\d+')
for line in file:
    find =re.findall(pattern,line)
    for ids  in find:
        print ids
        #print ids

    #z=p.findall(line)
   
#print z[2]
      
#file.write("hello rvill in the new  file\n")

#file.write("and another line\n")
file.close()

#2. regex extract url ids


#3. jhead on each output






