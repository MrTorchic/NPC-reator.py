#Fantasy name list generator

#Imports
import numpy
import linecache

from tkinter import *
from tkinter import ttk
#Variables
	#List location default
listName = 'dev.txt'

	#The Final List Down (DOO DOO DOO DOO)
nameList = [	
]


def randName(name, quantity):
	print(f'Generating... \n{name} x {quantity}')
	with open(f'Lists/{listName}') as f:
		line_count = 0
		for line in f:
			line_count += 1
		for i in range(0, quantity):
			
			#randomly pick a seed
			x = numpy.random.randint(line_count)
			y = numpy.random.randint(line_count)
			
			#get the contents of the line
			firstName = linecache.getline(f'Lists/{listName}', x)
			lastName = linecache.getline(f'Lists/{listName}', y)
			
			#print line
			print(f'{i+1}:\n    First: {firstName}\n    Last: {lastName}')
			nameList.append(f'{i+1} - {firstName} {lastName}')
		
		else:
			#confirms when process is finished
			print('Completed!')
			
		
		
randName(listName, 1)
