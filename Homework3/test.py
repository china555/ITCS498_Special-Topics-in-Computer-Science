import csv

readfile = []
with open('hw1_std.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        readfile.append(row)

payload = []

# for i in range(2):
#     if(i>0):
#         payload.append(
#         {
#            readfile[0][1] : float(readfile[i][1]),
#            readfile[0][2] : readfile[i][2],
#            readfile[0][3] : float(readfile[i][3]),
#            readfile[0][4] : float(readfile[i][4]),
#            readfile[0][5] : float(readfile[i][5]),
#            readfile[0][6] : float(readfile[i][6]),
#            readfile[0][7] : float(readfile[i][7]),
#            readfile[0][8] : float(readfile[i][8]),
#            readfile[0][9] : float(readfile[i][9]),
#            readfile[0][10] : float(readfile[i][10]),
#            readfile[0][11] : float(readfile[i][11]),
#            readfile[0][12] : float(readfile[i][12]),
#            readfile[0][13] : float(readfile[i][13]),
#         })

for i in readfile[1:]:
    ai = {}
    count = 1
    for j in i[1:]:
        if j is '':
            ai[readfile[0][count]] = 0
            print(type(j))
        else:
            try:
                ai[readfile[0][count]] = int(j)
            except TypeError:
                ai[readfile[0][count]] = float(j)
            except:
                ai[readfile[0][count]] = j
        count = count + 1
    payload.append(ai)
print(payload[0:2])
