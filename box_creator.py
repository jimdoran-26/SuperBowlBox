from random import sample
import sys

###FUNCTIONS TO MAKE PRINTING OF FINAL TABLE EASIER
#Print top row of the final table row
def print_top_row():
    final=''
    for i in range(10):
        final+= '     |       ' + str(random_a[i])
    return final

#Print a single row of final table with names and separators between names
def print_row(z):
    final=''
    for n in range(10):
        if n!=9:
            final+= final_names[z][random_b[n]] + store[0:(len(store)-1-len(final_names[z][random_b[n]]))]+ '|'
        else:
            final+= final_names[z][random_b[n]]
    return final

#Print a line with the horizontal outline and box separators
def print_line():
    return ('   --|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------')


###GENERATE THE LIST OF NAMES ALONG WITH CORRESPONDING NUMBER OF BOXES THEY ARE BUYING
#variables
names={}
total =0
name=' '
boxes=1
vals={}

##Ask user repeatedly for name & corresponding # of boxes
#if boxes reaches 100, program will print final box
#if boxes is greater than 100, will let the user know and not print final box
#if boxes are less than 100 simply leave name & boxes blank when prompted, will print final box with NULL in empty spaces
while(name!='' and boxes != 0):
    try:
        name = input('Person Name: ')
        boxes = int(input('# Boxes: '))
    except:
        name='NULL'
        boxes=0

    total += boxes
    vals[name[0:10]]=boxes

    if total==100:
        break
    elif(total>100):
        print('CANNOT BE MORE THAN 100 BOXES BOUGHT')
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
total_names=sample(total_names,len(total_names))
final_names = [total_names[i*10:(i+1)*10] for i in range((100+10-1)//10)]

random_a,random_b,c=sample(range(10),10),sample(range(10),10),list(range(10))


#Variables to help output NFC team name vertically along outsice of box & help with spacing
bucs='BUCCANEERS'
j=0
store = '              '

###PRINT THE FINAL BOX
print('                                                                     CHIEFS                                                                    ')
print(print_top_row())
print(print_line())

for i in c:
    if 1<i<7:
        print(bucs[j]+'  '+str(random_b[i])+' ' + '|' + '' + print_row(i))
        j+=1
        print(bucs[j]+ print_line()[1:])
        j+=1
    else:
        print('   '+str(random_b[i])+' ' + '|' + '' + print_row(i))
        print(print_line())