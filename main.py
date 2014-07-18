#!/usr/bin/python 
import sys
print len(sys.argv)
if(len(sys.argv)==3):
	if(sys.argv[1]=="--directory" or sys.argv[1]=="-d"):
		folderpath=sys.argv[2]
		print "FOLDER TO BE ANALYZED: "+ folderpath

		from os import listdir
		from os.path import isfile, join, exists, basename
		from os import	 makedirs
		from mutagen.mp3 import MP3
		from mutagen.easyid3 import EasyID3
		import traceback
		from shutil import move
		import fnmatch
		import os

		mp3fileslist = []
		for root, dirnames, filenames in os.walk(folderpath):
			for filename in fnmatch.filter(filenames, '*.mp3'):
				mp3fileslist.append(os.path.join(root, filename))

		#mp3fileslist = [ f for f in listdir(folderpath) if isfile(join(folderpath,f)) and f.endswith(".mp3")]
		print "Total mp3 files: "+ str(len(mp3fileslist))
		for mp3 in mp3fileslist:
			try:
				srcfilename=mp3
				print "SRC: " +srcfilename
				audio = MP3(srcfilename, ID3=EasyID3)		
				print audio	
				if(audio.tags != None and len(audio.tags)>0):
					destFolder=join(folderpath , "tagged" , audio.tags["artist"][0])																		
					if not exists(destFolder):
						makedirs(destFolder) 
					destfilename= join(destFolder,basename(mp3))
					move(srcfilename, destfilename)
				else:
					print "IGNORED"
			except:
				pass
	else:
		print "Syntax Invalid. Use main.py --folder <folder_path>"
else:
	print "Syntax Invalid. Use main.py --folder <folder_path>"

