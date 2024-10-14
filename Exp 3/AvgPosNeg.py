'''Write a python program to read the numbers until -1 is encountered. Find the average of positive numbers and negative numbers entered by the user'''

numList = []
while(True):
    num = int(input("Enter A Number : "))
    if(num==-1):
        break
    numList.append(num)

avgPos = 0
posCount = 0
avgNeg = 0
negCount = 0

for i in numList:
    if(i > 0):
            avgPos += i
            posCount += 1
    elif(i < 0):
            avgNeg += i
            negCount += 1
if posCount > 0 :
    print(f"Average Of Positive Numbers = {avgPos/posCount}")
else:
    print(f"No Positive Numbers Found")

if negCount > 0:
    print(f"Average Of Negative Numbers = {avgNeg/negCount}")
else:
    print(f"No Negative Numbers Found")