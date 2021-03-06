# These modules initialize the SPI connection and mounts the SPI filesystem.
import board 
import busio
import digitalio

# These modules give the device access to the SD card and SD card filesystem.
import adafruit_sdcard
import storage

# This creates the SPI bus and a digital output for the microSD card's CS line.
# The pin name should match our wiring.
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
# This is the chip select line on the M0 board...
cs = digitalio.DigitalInOut(board.D10)

# This creates the microSD card object and the filesystem object:
sdcard = adafruit_sdcard.SDCard(spi, cs)
# The microSD card object and the filesystem object are now 
# being passed through Vfsfat class.
vfs = storage.VfsFat(sdcard)

# We can now make the path /sd on the CircuitPython 
# filesystem read and write from the card:
storage.mount(vfs, "/sd")

# Creates a file and writes a line of text inside a text file along the path.
with open("/sd/test.txt", "w") as f:
    f.write("Hello world!\r\n")
 
# Opens the file that was written, declares object line that is an 
# array of lines generated by the readline function.
# The readline function returns the array of lines from the file object, f.readline
# Continues to print line array until it encounters
# an empty line array, a space character.
with open("/sd/test.txt", "r") as f:
    print("Printing lines in file:")
    line = f.readline()
    while line != '':
        print(line)
        line = f.readline()
        

with open("/sd/test.txt", "r") as f:
    lines = f.readlines()
    print("Printing lines in file:")
    for line in lines:
        print(line)
     
with open("/sd/test.txt", "a") as f:
    f.write("This is another line!\r\n")
    
