#!/usr/bin/python

import os
import sys
from syslog import syslog
#import datetime from datetime


def LinkMedia(filename,sourcedir):
#print 'further e:xamining %s' % (filename' % (subfile)

	ext = os.path.splitext(filename)[1]
	if 'Battlestar' in filename:
		return
	if 'Sample' in filename:
		return
	if 'sample' in filename:
		return
	if 'Prince' in filename:
		return
	if 'Genius' in filename:
		return
	if (ext == '.mkv'):
		target = '/media/MediaTransfer/Movies/' + filename
		syslog('checking to see if %s exists' % (target))
		if (os.path.isfile(target)):
			syslog('File %s already exists' % (filename))
		else:
			target = '\"' + target + '\"'
			syslog('Linking %s with sourcedir %s' % (filename,sourcedir))
			cmd = 'ln ' + sourcedir + '/' + filename +' '+ target
			os.system(cmd)
			cmd = 'chmod 775 ' + target
			os.system(cmd)

source = sys.argv[3] + '/' + sys.argv[2]
syslog('examining %s' % (source))
if (os.path.isdir(source)):	
	syslog('source = %s' % (source))
	for subfile in os.listdir(source):
		syslog('subfile = %s' % (subfile))
		LinkMedia(subfile,source)
else:
	LinkMedia(sys.argv[2],sys.argv[3])
