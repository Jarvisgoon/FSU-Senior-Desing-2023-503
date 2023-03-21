# Send data over serial
import serial
outport = 'COM3' # Select the appropriate comm port

teensy = serial.Serial(outport, 9600)

while True:
    # Code to generate output
    command = input("Bit: ")
    command2 = input("Bit2: ")
    
    # Code to normalize output
    cmdByte = bytes(command, 'utf-8')
    cmd2Byte = bytes(command2, 'utf-8')
    
    # send command
    try:
        teensy.write(cmdByte)
        teensy.write(cmd2Byte)
        teensy.flush()
    except:
        teensy.close()
        print("Data send failed")
        break
        
    if (command != '1' and command != '0') or (command2 != '1' and command2 != '0'):
        teensy.close()
        break
