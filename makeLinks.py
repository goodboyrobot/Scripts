import os
import sys
#import datetime from datetime

NumFilesLinked = 0
NumFilesSkipped = 0

def LinkMedia(filename,sourcedir):
	global NumFilesLinked
	global NumFilesSkipped
	#print 'further examining %s' % (filename)
	ext = os.path.splitext(filename)[1]
	if 'Battlestar' in filename:
		return
	if 'Sample' in filename:
		return
	if (ext == '.mkv'):
		target = '/media/MediaTransfer/Movies/' + filename 
		#print 'checking to see if %s exists' % (target)
		if (os.path.isfile(target)):
			#print 'File %s already exists' % (filename)
			NumFilesSkipped = NumFilesSkipped + 1
		else:
			print 'Linking %s with sourcedir %s' % (filename,sourcedir)
			cmd = 'ln ' + sourcedir + '/' + filename +' '+ target
			os.system(cmd)
			cmd = 'chmod 775 ' + target
			os.system(cmd)
			NumFilesLinked = NumFilesLinked + 1


for filename in os.listdir(sys.argv[1]):
	#print 'examining %s' % (filename)
	source = sys.argv[1] + filename	
	if (os.path.isdir(source)):	
		#print 'source = %s' % (source)
		for subfile in os.listdir(source):
			#print 'subfile = %s' % (subfile)
			LinkMedia(subfile,source)
	else:
		LinkMedia(filename,sys.argv[1])

print 'Script finished, new files linked: %d, files already linked %d' % (NumFilesLinked,NumFilesSkipped)
