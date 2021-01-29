import random
import sys

###GENERATE THE LIST OF NAMES ALONG WITH CORRESPONDING NUMBER OF BOXES THEY ARE BUYING
names={}
total =0

try:
    name = input('Person Name: ')
    boxes = int(input('# Boxes: '))
except:
    name = 'NULL'
    boxes = 0

total+=boxes
vals ={name:boxes}

while(name!='' and boxes != 0):
    try:
        name = input('Person Name: ')
        boxes = int(input('# Boxes: '))
        total += boxes
    except:
        name='NULL'
        boxes=0

    vals[name[0:10]]=boxes

    if total==100:
        break
    elif(total>100):
        print('CANNOT BE MORE THAN 100 BOXES')
        sys.exit()

###IF THERE ARE NOT ENOUGH BOXES BOUGHT WILL FILL THE REMAINDER WITH 'NULL' AND PROCEED WITH PROGRAM
if total != 100:
    vals['NULL']=100-total
    print('There are '+str(100-total) + ' boxes that did not get bought')

###CREATE A LIST OF THE TOTAL NUMBER OF NAMES ENTERED INTO THE BOX, MAKING SURE EACH NAME IS IN THE CORRECT NUMBER OF TIMES
total_names=[]
for key,value in vals.items():
    for v in range(value):
        total_names.append(key)

###SHUFFLE THE LIST SO THAT IT IS RANDOM ORDER
random.shuffle(total_names)
final_names = [total_names[i*10:(i+1)*10] for i in range((100+10-1)//10)]

###PRINT THE FINAL BOX
a,b,c=list(range(10)),list(range(10)),list(range(10))
random.shuffle(a),random.shuffle(b)

active=0
bucs='BUCCANEERS'
j=0
store = '              '

print('                                                                     CHIEFS                                                                    ')
print('     |    ' + str(a[0]) + '        |      ' + str(a[1]) + '      |      ' + str(a[2]) + '      |      ' + str(a[3]) + '      |      ' + str(a[4]) + '      |      ' + str(a[5]) + '      |      ' + str(a[6]) + '      |      ' + str(a[7]) + '      |      ' + str(a[8]) + '      |      ' + str(a[9]) + '           ')
print('   --|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|---------')


for i in c:
    if 1<i<7:
        print(bucs[j]+'  '+str(a[i])+' ' + '|' + final_names[i][b[0]]+store[0:(len(store)-1-len(final_names[i][b[0]]))] + '|' + final_names[i][b[1]]+store[0:(len(store)-1-len(final_names[i][b[1]]))] + '|' + final_names[i][b[2]]+store[0:(len(store)-1-len(final_names[i][b[2]]))] + '|' + final_names[i][b[3]]+store[0:(len(store)-1-len(final_names[i][b[3]]))] + '|' + final_names[i][b[4]]+store[0:(len(store)-1-len(final_names[i][b[4]]))] + '|' + final_names[i][b[5]]+store[0:(len(store)-1-len(final_names[i][b[5]]))] + '|' + final_names[i][b[6]]+store[0:(len(store)-1-len(final_names[i][b[6]]))] + '|' + final_names[i][b[7]]+store[0:(len(store)-1-len(final_names[i][b[7]]))] + '|' + final_names[i][b[8]]+store[0:(len(store)-1-len(final_names[i][b[8]]))] + '|' + final_names[i][b[9]])
        j+=1
        print(bucs[j]+ '  --|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|---------')
        j+=1
    else:
        print('   '+str(a[i])+' ' + '|' + final_names[i][b[0]]+store[0:(len(store)-1-len(final_names[i][b[0]]))] + '|' + final_names[i][b[1]]+store[0:(len(store)-1-len(final_names[i][b[1]]))] + '|' + final_names[i][b[2]]+store[0:(len(store)-1-len(final_names[i][b[2]]))] + '|' + final_names[i][b[3]]+store[0:(len(store)-1-len(final_names[i][b[3]]))] + '|' + final_names[i][b[4]]+store[0:(len(store)-1-len(final_names[i][b[4]]))] + '|' + final_names[i][b[5]]+store[0:(len(store)-1-len(final_names[i][b[5]]))] + '|' + final_names[i][b[6]]+store[0:(len(store)-1-len(final_names[i][b[6]]))] + '|' + final_names[i][b[7]]+store[0:(len(store)-1-len(final_names[i][b[7]]))] + '|' + final_names[i][b[8]]+store[0:(len(store)-1-len(final_names[i][b[8]]))] + '|' + final_names[i][b[9]])
        print('   --|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|---------')