import os

while (True):
    fileName = input("Enter file location: ").strip().replace('"', '')
    outFileName = fileName[0:fileName.find('.')] + "_SYNCED" + fileName[fileName.find('.'):]
    print("Output file: " + outFileName)

    startTimestamp = input("Enter delay timestamp: ")
    startTime = float(startTimestamp[startTimestamp.find(':') + 1:])
    print("Start Time: " + str(startTime))

    delayTime = 60 - startTime
    print("Delaying Video by: " + str(startTime))

    os.system('ffmpeg -itsoffset "{}" -i "{}" -an "{}"'.format(delayTime, fileName, outFileName))
    print("")
    print("Enter next file or Control + C to quit.")

