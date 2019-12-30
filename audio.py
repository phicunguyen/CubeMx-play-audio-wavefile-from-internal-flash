import os
import sys

def file_read(file):
    buffer = []
    file = os.path.normcase(os.path.normpath(file))
    if not os.path.isfile(file):
        print "Input file not found!"
        sys.exit(1)
    else:
        file = open(file, "rb")
        buffer = file.read()
        file.close()
    return buffer 

outputfile = ""
if __name__ == "__main__":
    samplefreq  = 44100         #
    bitdepth    = 16
    channels    = 2
    duration    = 3
    
    #Total number of bytes of the audio data
    size        = (samplefreq * bitdepth * channels * duration) / 8

    sys.stdout.write("%d (%x)\n" % (size, size))

    #read the audio.wav and store in a buffer
    aud_buf = bytearray(file_read("audio.wav"))

    #store the size of the audio
    aud_buf[7] = (size >> 24) & 0xff
    aud_buf[6] = (size >> 16) & 0xff
    aud_buf[5] = (size >> 8) & 0xff
    aud_buf[4] = size & 0xff

    #generage an array of audio data
    f_aud = open("audio_data.c", "w")
    f_aud.write("#include \"main.h\"\n")
    f_aud.write("const uint8_t audio_data[] = { \n")
    for i in range(size):
        if (i % 16 == 0 and i != 0):
            #sys.stdout.write("\n")
            f_aud.write("\n")
        #sys.stdout.write("0x%02x, " % aud_buf[i])
        f_aud.write("0x%02x, " % aud_buf[i])
        
    f_aud.write("\n};\n")
    f_aud.close()
    print("done")
