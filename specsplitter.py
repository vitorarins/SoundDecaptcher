import Image, os, subprocess, operator

filename = '/home/vitor/Documents/Projetos/Crawler/Simples/spectrograms/som65'
sample_rate = 11025.0
spectrogram = filename + ".png"
image = Image.open(spectrogram).convert("RGB")
image = remove_white_border(image)
image_index = {} #Reset the file nameing convention
debug_images = True

if debug_images:
    image.save(filename + "_noborder.png", "PNG")
images,column_xs = split_into_words(image, filename)
if len(images) > 6:
    while len(images) > 6:
        new_column_xs = []
        new_images = []
        lengths = {}
        for i in range(0, len(column_xs)):
            lengths[i] = column_xs[i][1] - column_xs[i][0]
        lengths = sorted(lengths.iteritems(), key=operator.itemgetter(1))
        lengths.reverse()
        indexes = []
        for i in range(0, 6):
            indexes.append(lengths[i][0])
        indexes.sort()
        for i in indexes:                
            new_images.append(images[i])
            new_column_xs.append(column_xs[i])
            
        column_xs = new_column_xs
        images = new_images
elif len(images) < 6:
    minimum_word_height = minimum_word_height
    while len(images) < 6:
        minimum_word_height -= 5
        images,column_xs = split_into_words(image, filename, minimum_word_height)

sizex,sizey = image.size
if debug_images:
    split_mp3_file(column_xs, sizex, filename, "before")

for i in range(0, len(images)):
    split_image = images[i]
    if debug_images:
        save_image(split_image, filename, "before")
    split_image, (left, right) = trim_image(split_image)
    column_xs[i] = [column_xs[i][0] + left, column_xs[i][0] + right]
    if "image" in split_components:
        save_image(split_image, filename)
if "audio" in split_components:
    split_mp3_file(column_xs, sizex, filename)
print len(images)

def get_duration(self, audiofile):
    """Gets the number of frames for the specified audio file"""
    p = subprocess.Popen(["sox", audiofile, "-c", "1", "-n", "stat"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output = p.communicate()[1]
    sampleLine = output.split("\n")[0]
    return float(sampleLine.split(":")[1].replace(" ", ""))


def split_mp3_file(self, column_xs, sizex, filename, suffix = ""):
    """Splits the corresponding wav file based on the columns found in the
    spectrogram.  The column x start and x end should be passed in a list
    of tuples in column_xs and they should not overlap. The width of the
    image should be passed in sizex, and optionally a naming suffix for
    the split up wav files can be passed in suffix."""
    fullfile = filename + ".mp3"
    soundsizex = get_duration(fullfile)
    sizex = float(sizex)
    pos = 0.0
    sound_columns = []
    processes = []
    for i in range(0,len(column_xs)):
            #Sox has the ability to split multiple parts at once, but it doesn't work (but I couldn't get it to work)
        options = ["sox", fullfile, filename + "_" + str(i) + suffix + ".wav", "trim"] 
        #The number of seconds to skip
        skip = float(column_xs[i][0]) * (soundsizex/sizex) * (1.0 / sample_rate)
        #The number of seconds to read
        length = float(column_xs[i][1] - column_xs[i][0] + 1.0) \
            * (soundsizex / sizex) * (1.0 / sample_rate) 

        options.append(str(skip))
        options.append(str(length))
        processes.append(subprocess.Popen(options, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE))
        sound_columns.append([skip, skip + length])

    for i in range(0, len(processes)):
        processes[i].communicate() #Wait for the last sox process to end
    print "Sound Column x-coordinates are: " + str(sound_columns)

