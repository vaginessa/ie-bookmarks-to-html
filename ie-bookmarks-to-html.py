# This file will convert IE's .url files into standard html format,
# it uses the desired infolder as a command line argument.
import os
from sys import argv
script, path = argv

html = False
doc = """<!DOCTYPE NETSCAPE-Bookmark-file-1>
<META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=UTF-8">
<TITLE>Bookmarks</TITLE>
<H1>Bookmarks</H1>
<DL><p>"""

# Finds all files within sub-folders.
configfiles = [os.path.join(dirpath, f)
    for dirpath, dirnames, files in os.walk(path)
    for f in files if f.endswith('.url')]

i=0
while i<len(configfiles): #for every file...
	f = open(configfiles[i])

	##write url to outfile
	with open('outfile.html', 'a') as outfile:

		## Appends html doctype & headers
		if not html: 
			outfile.write(doc)
			html = True

		outlist = []
		icon = ""

		for line in f:
			if "IconFile" in line:
				icon = line[9:]
			if "[InternetShortcut]\r\n" in line:
				url = next(f)
				outlist.append(url.strip("\r\n"))

			title = str(f)

			while "/" in title:
				start = title.find("/")
				title = title[start+1:]
			else:
				end = title.find(".url")
				title = title[:end]

		for item in outlist:
			outfile.write("<dt><a href='" + item + "' " + "icon='" + icon + "'>" + title + "</a>\n")

	f.close()
	i += 1

with open('outfile.html', 'a') as outfile:
	outfile.write("</dt></p>")
	
print "Done.\nYou had " + str(len(configfiles)) + " bookmarks!"








