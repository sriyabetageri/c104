import csv
from collections import Counter

with open("height-weight.csv", newline="")as f:
    reader=csv.reader(f)
    file_data = list(reader)

file_data.pop(0)

newData = []
for i in range(len(file_data)):
    n = file_data[i][1]
    newData.append(float(n))

#mean
a = len(newData)
total = 0
for x in newData:
    total += x
    
mean = total/a
print("mean: "+str(mean))    

#median
newData.sort()
if a%2 == 0:
    m1 = float(newData[a//2])
    m2 = float(newData[a//2-1])
    median = (m1+m2)/2
else:
    meadian = newData[a//2]
print("median: "+str(median))


#mode

data = Counter(newData)
mode_dataForRange = {
                        "50-60": 0,
                        "60-70": 0,
                        "70-80": 0
                    }
for height, occurance in data.items():

    if 50<float(height)<60:
        mode_dataForRange["50-60"]+= occurance

    if 60<float(height)<70:
        mode_dataForRange["60-70"]+= occurance

    if 70<float(height)<80:
        mode_dataForRange["70-80"]+= occurance

modeRange, modeOccurance = 0,0
for range, occurance in mode_dataForRange.items():
    if occurance> modeOccurance:
        modeRange,modeOccurance = [int(range.split("-")[0]),int(range.split("-")[1])],occurance
mode = float((modeRange[0]+modeRange[1])/2)

print(f"mode: {mode:2f} " )
