import requests

def Download(links):
    try:
        _1st = requests.get(links[0])
        _2nd = requests.get(links[1])
        _3rd = requests.get(links[2])
        _4th = requests.get(links[3])
        _5th = requests.get(links[4])  
    except Exception as e:
        raise Exception(e)
    ret = [_1st.content, _2nd.content, _3rd.content, _4th, _5th.content]
    return ret

class Recognition(object):
    def __init__(self):
        self.number0 = open('0.bytecode', 'r')
        self.number1 = open('1.bytecode', 'r')
        self.number2 = open('2.bytecode', 'r')
        self.number3 = open('3.bytecode', 'r')
        self.number4 = open('4.bytecode', 'r')
        self.number5 = open('5.bytecode', 'r')
        self.number6 = open('6.bytecode', 'r')
        self.number7 = open('7.bytecode', 'r')
        self.number8 = open('8.bytecode', 'r')
        self.number9 = open('9.bytecode', 'r')
        
    def recognition(self, link1, link2, link3, link4, link5):
        #send liks download methode
        links = [link1, link2, link3, link4, link5]
        self.reseve = Download(links)
        # create numberdata array
        numArray = [self.number0.readlines(),
        self.number1.readlines(),
        self.number2.readlines(),
        self.number3.readlines(),
        self.number4.readlines(),
        self.number5.readlines(),
        self.number6.readlines(),
        self.number7.readlines(),
        self.number8.readlines(),
        self.number9.readlines()]
        #find 1st number
        reg_zed_numbers = []
        for i in range(len(self.reseve)):
            _str = self.reseve[i]
            for data in range(len(numArray)):
                if _str == numArray[data]:
                    reg_zed_numbers.append(i)
        print(str(numArray[0]))
        return reg_zed_numbers
# testing
obj = Recognition().recognition('https://eservices.elections.gov.lk/ShowImage.ashx?id=SuO3D',
                                'https://eservices.elections.gov.lk/ShowImage.ashx?id=SuO',
                                'https://eservices.elections.gov.lk/ShowImage.ashx?id=S',
                                'https://eservices.elections.gov.lk/ShowImage.ashx?id=SuO3DiEtF',
                                'https://eservices.elections.gov.lk/ShowImage.ashx?id=SuO')
print(obj)