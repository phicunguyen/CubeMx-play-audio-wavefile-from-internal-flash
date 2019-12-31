# CubeMx-play-audio-wavefile-from-internal-flash
This example play 4 seconds of  the audio (wave file) that store in an array embedded with the code.

    
    Using the st-util to program stm32f04VGTx_wavefile_from_flash.hex to your stm32f407-disc.
    Plug the headphone to the phone jack.
    You should hear the audio play about 4s then a small click sound that when it start play the audio over again.
    
The audio.py is used to convert the audio.wav to an array of bytes that going to be stored in the flash. it generates a audio_data.c
  
    samplefreq  = 44100   #sample freq      
    bitdepth    = 16      #bit depth
    channels    = 2       #number of channesl
    duration    = 3       #how long to play
    #Total number of bytes of the audio data
    size        = (samplefreq * bitdepth * channels * duration) / 8
    
    const uint8_t audio_data[] = { 
        0x52, 0x49, 0x46, 0x46, 0x30, 0x13, 0x08, 0x00, 0x57, 0x41, 0x56, 0x45, 0x66, 0x6d, 0x74, 0x20,
        ...
        0x75, 0x01, 0xcf, 0x01, 0xb1, 0x00, 0x3e, 0x01, 0x0d, 0xff, 0xca, 0xff, 0x98, 0xfc, 0x81, 0xfd, 
    };
    
    
This code was based on  the this https://www.youtube.com/watch?v=6g2jSqvmpt4 and stm32f407 Audio_playback_and_record.
Both code were play audio from a sdcard but I don't have one therefore I changed the code to play from flash instead.
