import os

print("Scale Videos by Kevin Salvatorelli")
print("Accepts any format FFMPEG can support.")
print()


sourcesDir = input("Enter source directory: ")

sources = []

for file in os.listdir(sourcesDir):
        print("Adding File: " + os.path.join(sourcesDir, file))
        sources.append(os.path.join(sourcesDir, file))

print()
print("Added " + str(len(sources)) + " files.")

print()

horizRes = int(input("Horizontal Resolution? Recommended = 480: "))
vertRes = horizRes * 0.5625

for x in range(len(sources)):
    fileName = str(sources[x])
    outFileName = fileName[0:fileName.find('.')] + "_SCALED" + fileName[fileName.find('.'):]
    print("Current File: " + str(x))
    filter = "scale={}:{}:force_original_aspect_ratio=decrease,pad={}:{}:(ow-iw)/2:(oh-ih)/2,setsar=1".format(horizRes, vertRes, horizRes, vertRes)
    ffmpegCmd = 'ffmpeg -i "{}" -filter:v {} -r 60 "{}"'.format(fileName, filter, outFileName)
    print("FFMPEG Command: " + ffmpegCmd)
    os.system(ffmpegCmd)

print("All videos scaled!")