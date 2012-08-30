import os, subprocess, operator, random

ftype = '.mp3'
def split_mp3_file(fullpath,filename):
    digit_length = 2.5
    processes = []
    splits = [0,2.5,5,7.5,10,12.5]
    for i in xrange(len(splits)):
        outname = str(random.randint(0,1000000))+'.wav'
        options = ['sox',fullpath+filename+ftype,fullpath+filename[i]+'/'+outname,'trim']
        options.append(str(splits[i]))
        options.append(str(digit_length))
        processes.append(subprocess.Popen(options, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE))

    for i in xrange(len(processes)):
        processes[i].communicate()

    return 'done!'

filepath = '/home/vitor/Documents/Projetos/Crawler/Simples/audio_samples/'
# fname = '849694'

for fname in os.listdir(filepath):
    if fname.endswith(ftype):
        split_mp3_file(filepath,fname[:-4])
print 'done!'
# print split_mp3_file(filepath,fname)
# for i in xrange(61,100):
#     newname = raw_input()
#     os.rename(filepath+'som'+str(i)+ftype,filepath+newname+ftype)
#     print 'renamed: '+filepath+'som'+str(i)+' to '+newname
