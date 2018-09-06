import sys
import os
import pipes
foldername = sys.argv[1]
target = sys.argv[2]
for filename in os.listdir(foldername):
	title = os.path.splitext(filename)[0]
	fulltarget =  target + filename
	#cmd = 'mkdir ' + fulltarget
	#print cmd
	#os.system(cmd)
	cmd = 'ln ' + pipes.quote(filename) + ' ' + pipes.quote(fulltarget)
	print cmd
	os.system(cmd)
	cmd = 'chmod 775 ' + pipes.quote(fulltarget)
	print cmd
	os.system(cmd)


