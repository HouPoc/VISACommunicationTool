from io import *
import visa

class dataCommReceivedtxt:
    def __init__(self):
        print('text to read and send')

    def __del__(self):
        print('text successfully transmitted ')

# method reading text file
    def datareceivedtext(self,systemfile):
        self.systemfile = systemfile
        tfile = ''
        for line in open('systemfile').readlines():
            tfile = line.rstrip()
        return tfile

        bfile = ''
        for lineb in open('systemfile').StringIO():
            bfile = lineb.rstrip()

        return bfile

class dataCommReceivedbyte:
    def __init__(self):
        print('bytes ready to be send')

    def __del__(self):
        print('bytes successfully received')

# method reading byte file
    def datareceivedbytes(self, systemfilebyte):
        self.systemfilebyte = systemfilebyte
        byfile = ''
        for linebyte in BytesIO(b'systemfilebyte'):
            byfile = linebyte.rstrip()
        return byfile


class displayIntrumentData:

    def __init__(self):
        print('connected from the measuring instrument ')

    def __del__(self):
        print('data successfully read from the instrument')

    # ('ASRL1::INSTR', 'ASRL2::INSTR', 'GPIB0::12::INSTR')
    # module controller of the communication between application and
    # various buses ( e.g GPIB, RS232, USB, Ethernet)
    visa.log_to_screen()
    rm = visa.ResourceManager('C:\WINDOWS\system32\\visa32.dll')
    rm.list_resources()
    for itrm in rm.list_resources():
        if itrm == 'ASRL1::INSTR':
            my_instrument = rm.open_resource('ASRL1::INSTR')
        elif itrm == 'ASRL2::INSTR':
            my_instrument = rm.open_resource('ASRL2::INSTR')
        elif itrm == 'GPIB0::12::INSTR':
            my_instrument = rm.open_resource('GPIB0::12::INSTR')
        else:
            my_instrument = rm.open_resource(' ')

        intval = my_instrument.query("*IDN?")
        values = my_instrument.query_ascii_values('CURV?', container= numpy.array)


# data to be read and written on the buffer
filread = dataCommReceivedtxt()
filread.datareceivedtext('systemfile')
filread.__del__()


filreadbyte = dataCommReceivedbyte()
filreadbyte.datareceivedbytes('systemfilebyte')
filreadbyte.__del__()


fildevice = displayIntrumentData()
fildevice.__del__()



