#!/usr/bin/python

import fileinput
import re

num = 0		#section number

for line in fileinput.input():
	#print (line, end='')
	if re.search('^## ', line):		#prelim search
		mat = re.search('(^## )([0-9\.]*)(.*)', line)
		if mat:
			num = num + 1		#1.0, 2.0
			subnum = 0		#sub section number

			print (f'## {num}.{subnum} {mat.group(3)}')

	elif re.search('^### ', line):		#prelim search
		mat = re.search('(^### )([0-9\.]*)(.*)', line)
		if mat:
			subnum = subnum + 1	#1.1, 1.2

			print (f'### {num}.{subnum} {mat.group(3)}')
	else:					#not a header line
		print (line, end='')

