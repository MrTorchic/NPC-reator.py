#Fantasy name list generator

#Imports
import numpy
import linecache

from tkinter import *
from tkinter import ttk
#Variables
	#List location default
listName = 'devNames.txt'
listJob = 'devOccupations.txt'
amount = 10

	#The Final Name List (DOO DOO DOO DOO)
nameList = [	
]
	#The Final Occupation List (... doesn't roll of the tongue as well)
occupationList = [
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
			nameList.append(f'{firstName.rstrip()} {lastName}')
		else:
			print('loop 1 success')

		
		


def randJob(jobName, quantity):
	print(f'Generating... \n{jobName} x {quantity}')
	with open(f'Lists/{jobName}') as f:
		line_counta = 0
		for line in f:
			line_counta += 1
		for i in range(0, quantity):
			#randomly pick a seed
			x = numpy.random.randint(line_counta)
			#get the random job
			randJob = linecache.getline(f'Lists/{jobName}', x)
			#append randJob to $occupationList
			occupationList.append(f'{randJob.rstrip()}')
		else:
			#confirms when process is finished
			print('loop 2 success')

			
randName(listName, amount)
randJob(listJob, amount)

