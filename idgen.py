
try:
    import argparse
    import wordlist
    import random
    import time
    import datetime
except Exception as e:
    raise ModuleNotFoundError(e)


class Genarate(object):
    
    def __init__(self, BirthDay, BirthMonth, BirthYear, Gender, resident, lockNew):
        
        #print(str(type(BirthDay).__name__))
        if not str(type(BirthDay).__name__) == 'int':
            raise TypeError("The input is in '" + str(type(BirthDay).__name__) + "'. The input for the birthday must be 'int'.")

        if not str(type(BirthMonth).__name__) == 'int':
            raise TypeError("The input is in '" + str(type(BirthMonth).__name__) + "'. The input for the birth month must be 'int'.")

        if not str(type(BirthYear).__name__) == 'int':
            raise TypeError("The input is in '" + str(type(BirthYear).__name__) + "'. The input for the birth year must be 'int'.")

        if not str(type(Gender).__name__) == 'str':
            raise TypeError("The input is in '" + str(type(Gender).__name__) + "'. The input for the birth year must be 'str'.")
        self.lockNew = lockNew
        self.birth_day = BirthDay
        self.birth_month = BirthMonth
        self.birth_year = BirthYear
        self.gender = Gender.upper()
        self.year_data = {
            'L': [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
            'H': [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        }
        
        # print(self.year_data['H'][2])
        # අදිකවර්ෂ හා අදිකනොවන වර්ෂ හදිනා ගැනීම. Tn = a+(n-1)d ,ආදර්ශ අදිකවර්ෂය(a) = 2020, පොදු අන්තරය(d) = 4
        # ඉහත සුත්‍රය වෙනස් කල විට n = (Tn-a)/d +1
        # සුලුවී ලැබෙන සංක්‍යාව පුර්ණ සංක්‍යාවක් නම් Tn අදික වර්ෂයක් වේ.
        n = ((self.birth_year - 2020)/4) + 1
        n = str(n); n = n.split('.'); n = int(n[1])
        
        if not n > 0:
            self.Hyear = True       # this section is working
           
        else:
            self.Hyear = False

        # මාසයට හිමි අංකයේ වලංගු බව‍ පර්ක්ෂා කිරීම
        if (self.birth_month <= 12) and (self.birth_month > 0): #13>12
            # මාසයට හිමි දින ගණන පරික්ෂා ව
            mon = self.birth_month
            bd = self.birth_day
            if self.Hyear == True:
                #print(self.year_data['H'][mon -1] >= bd)
                if not self.year_data['H'][mon -1] >= bd or bd < 1:       # this section is working
                    raise Exception(str(self.birth_day) + ' Invalid date entered. Month ' + str(self.birth_month))
                
            elif self.Hyear == False:
                #print(self.year_data['L'][mon -1] >= bd)
                if not self.year_data['L'][mon -1] >= bd or bd < 1:
                    raise Exception(str(self.birth_day) + ' Invalid date entered. Month ' + str(self.birth_month))

        else:
            raise Exception(str(self.birth_month) + ' is not valid. There are between 1 and 12 months a year.')
        # Identification of the Identity Card Number(old, new)
        if self.birth_year < 1910:
            raise Exception('Birth year out of range.')

        if not self.lockNew == True:
            if self.birth_year < 2000:
                self.birth_year = self.birth_year - 1900
        else:
            pass

        #dates for month
        rrt = 0
        for i in range(0, self.birth_month -1):
            if self.Hyear == True:
                rrt = rrt + self.year_data['H'][i]
            else:
                rrt = rrt + self.year_data['L'][i]
        
        tc = int(str(self.birth_year) + str('%03d' % (rrt + self.birth_day)))
        if self.gender == 'FEMALE':
            tc = int(str(self.birth_year) + str('%03d' % (rrt + self.birth_day + 500)))
        self.tc = tc
    # random section
        self.charactors = '0123456789'

    def randomSingle(self):
        
        generator = wordlist.Generator(self.charactors)
        data = []
        start_time = time.process_time_ns()
        for each in generator.generate(5, 5):           # 
            #print('2000138' + each)
            data.append(str(self.tc) + each)
        rand = []
        for i in range(0, 1):
            rand.append(data[random.randrange(len(data))])
        end_time = time.process_time_ns()
        print('Time:', end_time-start_time, 'ns.')
        data.clear()
        return rand

    def randomCount(self, count):

        generator = wordlist.Generator(self.charactors)
        data = []
        start_time = time.process_time_ns()
        for each in generator.generate(5, 5):           # 
            #print('2000138' + each)
            data.append(str(self.tc) + each)
        rand = []
        for i in range(0, count):
            rand.append(data[random.randrange(len(data))])
        end_time = time.process_time_ns()
        print('Time:', end_time-start_time, 'ns.')
        data.clear()
        return rand

    def randomRange(self, rengeStart, rangeEnd):
        pass

    # bruteforce section
    def bruteforceAll(self, structure):
        
        structure = structure.upper()
        if not (structure == 'ACS' or structure == 'DES' or structure == 'SHUFFEL'):
            raise Exception('Undefined data stucture.')

        generator = wordlist.Generator(self.charactors)
        data = []
        start_time = time.process_time_ns()
        for each in generator.generate(5, 5):           # 
            #print('2000138' + each)
            data.append(str(self.tc) + each)
        cou = len(data)
        if structure == 'DES':
            data.reverse()
        if structure == 'SHUFFEL':
            random.shuffle(data)
        end_time = time.process_time_ns()
        now = datetime.datetime.now()
        print('[', now, ']', 'T.Pas:', end_time-start_time, 'ns.-bfaC|stuct: ', structure,
         '| gen:', cou, '| birthd:', self.birth_day, '/', self.birth_month, '/',
          self.birth_year, '| gend:',
          self.gender)
        return data

    def bruteforceallCustom(self, structure, pattern):
        
        if not len(pattern) == 5:
            if len(pattern) < 5:
                raise Exception('The pattern is too short. Patterns length should be 5.')
            elif len(pattern) > 5:
                raise Exception('The pattern is too long. Patterns length should be 5.')
        else:
            a = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '@']
            
            for char in pattern:

                if not (char == a[0] or char == a[1] or char == a[2] or 
                char == a[3] or char == a[4] or char == a[5] or char == a[6] or
                char == a[7] or char == a[8] or char == a[9] or char == a[10]):
                    raise Exception('Invalid charactor detected ', char, 
                '| valid charactors : 0,1,2,3,4,5,6,7,8,9,@')
                
        structure = structure.upper()
        if not (structure == 'ACS' or structure == 'DES' or structure == 'SHUFFEL'):
            raise Exception('Undefined data stucture.')

        generator = wordlist.Generator(self.charactors)
        data = []
        start_time = time.process_time_ns()
        for each in generator.generate_with_pattern(pattern):
            data.append(str(self.tc) + each)
        cou = len(data)

        if structure == 'DES':
            data.reverse()
        if structure == 'SHUFFEL':
            random.shuffle(data)
        end_time = time.process_time_ns()
        now = datetime.datetime.now()

        print('[', now, ']', 'T.Pas:', end_time-start_time, 'ns.-bfaC|stuct:', structure,
         '|gen:', cou, '|birthd:', self.birth_day, '/', self.birth_month, '/',
          self.birth_year, '| gend:',
          self.gender)
        return data

#x = Genarate(1, 12, 2020, 'male', 'permanant', True)
#r = x.bruteforceAll('acs')
#print(r)

