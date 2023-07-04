import os
import sys
import subprocess

for file in os.listdir(sys.argv[1]):
	#build up args array
    fullpath = sys.argv[1] + '/' + file
    if os.path.isfile(fullpath):
        cmd = [0,0,0]
        cmd[0] = "stat" 
        cmd[1] = "--printf=\'%h\'"
        cmd[2] = fullpath
        #print(cmd)
        numLinks = subprocess.check_output(cmd).decode('utf-8')
        print(numLinks)
        if (numLinks == '\'1\''):
            print("deleting " + file)
            delcmd = "rm " + fullpath
            print(delcmd)
            os.system(delcmd)
        
    
