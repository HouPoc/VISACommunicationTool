from io import *
import visa



# module read file mainly text file

infile = "myFile.txt"
retrievedFile = open(infile,  mode='r', encoding="utf-8")
if retrievedFile.mode == "r":
    retrievedFile = (open(infile, 'r') or StringIO("some initial text data"))
elif retrievedFile.mode == "rb":
    retrievedFile = (open(infile, "rb") or BytesIO(b"some initial binary data: \x00\x01"))
else:
    print("this file is not readable")
    exit(0)
for line in retrievedFile:
        outfile = line.readall()
        outfile.BufferedWriter()

        # module controller of the communication between application and
        # various buses ( e.g GPIB, RS232, USB, Ethernet)
        rm = visa.ResourceManager()
        rm.list_resources()
        ('ASRL1::INSTR', 'ASRL2::INSTR', 'GPIB0::12::INSTR')
        inst = rm.open_resource('GPIB0::12::INSTR')
        print(inst.query("*IDN?"))

        outfile.flush()
retrievedFile.isatty()
retrievedFile.close()





