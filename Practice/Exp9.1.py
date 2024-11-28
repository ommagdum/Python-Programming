'''Write a program that perform file handling operations 1)
open 2) read 3) write 4) close 5) append'''

f = open("file.txt",'r')
print(f.read())

f = open("file.txt",'w')
f.write("TY B.Tech")
f.close

f = open("file.txt",'a')
f.write("\nEnd OF File")

