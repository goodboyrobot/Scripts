import os
import sys
import subprocess

for file in os.listdir(sys.argv[1]):
	#build up args array
	cmd = [0,0,0]
	cmd[0] = "stat" 
	cmd[1] = "--printf=\'%h\'"
	cmd[2] = sys.argv[1] + file
	#print cmd
	numLinks = subprocess.check_output(cmd)
	#print numLinks
	if (numLinks == '\'1\''):
		print "deleting " + file
		delcmd = "rm " + cmd[2]
		#print delcmd
		os.system(delcmd)

