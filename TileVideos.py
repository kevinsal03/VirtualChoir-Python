import os

def makeRow(videosForRow, rowNumber):
    videosForRow = int(videosForRow)
    rowNumber = int(rowNumber)
    print("Videos in this row: " + str(videosForRow))
    ffmpegCmd = "ffmpeg "
    for x in range(videosForRow):
        ffmpegCmd = ffmpegCmd + "-i \"" + str(sources[0]) + "\" "
        sources.pop(0)
    outputName = os.path.join(sourcesDir, "output_row_" + str(rowNumber) + ".mp4")
    ffmpegCmd = ffmpegCmd + " -filter_complex hstack=inputs=" + str(videosForRow) + " -r 60 \"" + outputName + "\""
    print("FFMPEG Command: " + ffmpegCmd)
    os.system(ffmpegCmd)


print("Tile Videos by Kevin Salvatorelli")
print("Accepts any format FFMPEG can support.")
print("Files must already be synced!")
print()


sourcesDir = input("Enter source directory: ")


sources = []

for file in os.listdir(sourcesDir):
        print("Adding File: " + os.path.join(sourcesDir, file))
        sources.append(os.path.join(sourcesDir, file))

print()
print("Added " + str(len(sources)) + " files.")

print()

videosPerRow = int(input("How many videos per row? Recommended = 4: "))
totalRows = int(len(sources)/videosPerRow)
extraVideoRow = 0
if ((len(sources) - (totalRows * videosPerRow)) != 0):
    extraVideoRow = len(sources) - (totalRows * videosPerRow)
    totalRows = totalRows + 1

print("Total rows: " + str(totalRows))
if (extraVideoRow > 0):
    print("Extra row will have: " + str(extraVideoRow))

rowsLeft = totalRows
while(rowsLeft > 0):
    print("Building row: " + str(totalRows - rowsLeft))
    ffmpegCmd = "ffmpeg "
    if (extraVideoRow != 0):
        if (totalRows - rowsLeft == 1):
            makeRow(extraVideoRow, totalRows - rowsLeft)
        else:
            makeRow(videosPerRow, totalRows - rowsLeft)
    else:
        makeRow(videosPerRow, totalRows - rowsLeft)
    rowsLeft = rowsLeft - 1
