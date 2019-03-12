import sys
import os
import pipes
folderName = sys.argv[1]
movieFolder = '/media/nas/afschuld/Movies/'
if os.path.isdir(folderName):
    for filename in os.listdir(folderName):
        title = os.path.splitext(filename)[0]
        targetFolder =  movieFolder + folderName
        fullTarget = targetFolder + filename
        origin = folderName + filename
        cmd = 'mkdir ' + pipes.quote(targetFolder)
        print cmd
        os.system(cmd)
        cmd = 'ln ' + pipes.quote(origin) + ' ' + pipes.quote(fullTarget)
        print cmd
        os.system(cmd)
        cmd = 'chmod 775 ' + pipes.quote(fullTarget)
        print cmd
        os.system(cmd)
else:
    title = os.path.splitext(folderName)[0]
    targetFolder =  movieFolder + title
    fullTarget = targetFolder + folderName
    origin = folderName
    cmd = 'mkdir ' + pipes.quote(targetFolder)
    print cmd
    os.system(cmd)
    cmd = 'ln ' + pipes.quote(origin) + ' ' + pipes.quote(fullTarget)
    print cmd
    os.system(cmd)
    cmd = 'chmod 775 ' + pipes.quote(fullTarget)
    print cmd
    os.system(cmd)

