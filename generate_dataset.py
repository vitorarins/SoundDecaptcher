import wave
from wave import Wave_read

filename = '/home/vitor/Documents/Projetos/Crawler/Simples/modified_samples/8/818169.wav'
outfile = 'soundbytes.txt'
wavobj = wave.open(filename,'rb')

frames = wavobj.getnframes()
print frames
print wavobj.getsampwidth()
# with open(outfile,'wb') as f:
#     print f.encoding
#     f.write(wavobj.readframes(frames))
wavobj.close()
print 'done!'
