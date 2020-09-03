'''
# Tn = a+(n-1)*d
# 2024 = 2020+(n-1)*4
# 2024/2020/4 = n-1
x= ((2020-2020)/4) +1

x = str(x)
x = x.split('.')

print(x)
x = int(x[1])
if not x > 0:
    print('teue')
else:
    print('false')
'''
'''

generator = wordlist.Generator('0123456789')
data = []
for each in generator.generate(5, 5):
    #print('2000138' + each)
    data.append('2003362' + each)
#print(data)
for i in data:
    if i == '200336201057':
        print(i)
        
'''
'''
pattern = "12468@x!@#$%^&*()_+8ty"

avlchar = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '@']
for char in pattern:
    if not (char == '0' or char == '1' or char == '2' or char == '3' or char == '4' or char == '5' or char == '6' or char == '7' or char == '8' or char == '9' or char == '@'):
        print('detected', char)

'''
'''
pattern = "12468@"
a = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '@']
for char in pattern:

    if not (char == a[0] or char == a[1] or char == a[2] or 
        char == a[3] or char == a[4] or char == a[5] or char == a[6] or
        char == a[7] or char == a[8] or char == a[9] or char == a[10]):
        print('detected', char)

a = 0
print (str('%03d' % a))
'''
'''
import idgen
x = idgen.Genarate(2, 2, 2000, 'female', 'permanant', False).bruteforceAll('acs')
for i in x:
    if i == '200053302775':
        print(i, 'founded')
'''
import capchaRecog
# ShowImage.ashx?id=1
#x = capchaRecog.Recognition('https://eservices.elections.gov.lk/ShowImage.ashx?id=vx50R')
#y = capchaRecog.Recognition('https://eservices.elections.gov.lk/ShowImage.ashx?id=1qjQw')
#capchaRecog.Recognition('https://eservices.elections.gov.lk/ShowImage.ashx?id=p')
#if x == y:
   #print('test success')

numbers = [

    'https://eservices.elections.gov.lk/ShowImage.ashx?id=', #0-
    'https://eservices.elections.gov.lk/ShowImage.ashx?id=p',#1-
    'https://eservices.elections.gov.lk/ShowImage.ashx?id=En',#2-
    'https://eservices.elections.gov.lk/ShowImage.ashx?id=pLE',#3-
    'https://eservices.elections.gov.lk/ShowImage.ashx?id=SvtO',#4-
    'https://eservices.elections.gov.lk/ShowImage.ashx?id=pLEGr',#5-
    'https://eservices.elections.gov.lk/ShowImage.ashx?id=1bWIOb',#6-
    'https://eservices.elections.gov.lk/ShowImage.ashx?id=ke6WmQ9',#7
    'https://eservices.elections.gov.lk/ShowImage.ashx?id=EnU1j0Zz',#8-
    'https://eservices.elections.gov.lk/ShowImage.ashx?id=pLEGrI6Bi'#9-

]
