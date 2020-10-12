import serial
import serial.tools.list_ports

porNameList = [i.device for i in serial.tools.list_ports.comports()]
print(porNameList)

port = serial.Serial(porNameList[0])
print(port)