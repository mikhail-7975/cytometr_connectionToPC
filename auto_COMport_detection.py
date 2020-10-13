import serial
import serial.tools.list_ports
import matplotlib.pyplot as plt
import time

porNameList = [i.device for i in serial.tools.list_ports.comports()]
print(porNameList)

port = serial.Serial(porNameList[0])

while(1):
    data = []
    while len(data) < 1002:
        port.write(b"req")
        #print("send request...")
        startTime = time.time()
        while not port.inWaiting():
            #print('.')
            if time.time() - startTime > 1:
                #print("much time not in waiting")
                break

        i = 0
        inp = 0
        startTime = time.time()
        while(inp != 254):
            while port.inWaiting():
                #print(ord(port.read()), i)
                inp = ord(port.read())
                data.append(inp)
                #print("reading", i)
                i += 1
            if time.time() - startTime > 1:
                #print("much time in trying to read")
                break

    port.write(b"ack")
    print(len(data), data)
    #plt.plot(data)
    plt.show()
    print(port)