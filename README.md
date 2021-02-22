# tv-rename

A command line Python tool to batch rename files in a folder to match Plex TV show naming convention.

Usage: `tv-rename.py [-h] [-d [DIRECTORY]] [-f [FIRST]] [-r] title season`

Positional arguments: 
Argument | Description
-------- | -----------
title | title of TV show
season | season number

Optional arguments: 
Argument | Description
-------- | -----------
-h, --help | show this help message and exit
-d [DIRECTORY], --directory [DIRECTORY] | the directory to read and rename files in
-f [FIRST], --first [FIRST] | episode number to start renaming from
  -r, --readonly | run the program in readonly mode (whatif mode)
