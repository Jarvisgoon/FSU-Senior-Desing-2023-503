# Send data over serial
import serial
outport = 'COM3' # Select the appropriate comm port

teensy = serial.Serial(outport, 9600)

while True:
    # Code to generate output
    command = input("Bit: ")
    
    # Code to normalize output
    cmdByte = bytes(command, 'utf-8')
    
    # send command
    try:
        teensy.write(cmdByte)
        teensy.flush()
    except:
        teensy.close()
        print("Data send failed")
        
    if command != '1' and command != '0':
        teensy.close()
        break
