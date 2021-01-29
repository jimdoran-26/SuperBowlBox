import random
import sys

###FUNCTIONS DESIGNED TO MAKE PRINTING OF FINAL TABLE EASIER
def print_row():
    final=''
    for i in range(10):
        final+= '     |       ' + str(a[i])
    return final

def print_block(z):
    final=''
    for n in range(10):
        if n!=9:
            final+= final_names[z][b[n]] + store[0:(len(store)-1-len(final_names[z][b[n]]))]+ '|'
        else:
            final+= final_names[z][b[n]]
    return final

###GENERATE THE LIST OF NAMES ALONG WITH CORRESPONDING NUMBER OF BOXES THEY ARE BUYING
names={}
total =0

def print_line():
    return ('   --|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------')

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

a,b,c=list(range(10)),list(range(10)),list(range(10))
random.shuffle(a),random.shuffle(b)

active=0
bucs='BUCCANEERS'
j=0
store = '              '

###PRINT THE FINAL BOX
print('                                                                     CHIEFS                                                                    ')
print(print_row())
print(print_line())

for i in c:
    if 1<i<7:
        print(bucs[j]+'  '+str(a[i])+' ' + '|' + '  ' + print_block(i))
        j+=1
        print(bucs[j]+ print_line()[1:])
        j+=1
    else:
        print('   '+str(a[i])+' ' + '|' + '  ' + print_block(i))
        print(print_line())