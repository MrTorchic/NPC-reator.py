#Fantasy name list generator

#Imports
import numpy
import linecache
import tkinter as tk
from tkinter import ttk
from os import listdir
from os.path import isfile, join
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
	#A Merged List of the Two (if needed)
mergedList = [
]
jobPath = 'Lists/Jobs/'
namePath = 'Lists/Names/'
jobFiles = [f for f in listdir(jobPath) if isfile(join(jobPath, f))]
nameFiles = [f for f in listdir(namePath) if isfile(join(namePath, f))]
print(f'{jobFiles}\n{namePath}')
#File Lists
def randName(name, quantity):
	print(f'Generating... \n{name} x {quantity}')
	with open(f'Lists/Names/{name}') as f:
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
	with open(f'Lists/Jobs/{jobName}') as f:
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

def main(nameFile, jobFile, x):
	for i in range(0,x):
		if jobFile != 'None':
			print('both')
		else:
			print('only name')


window = tk.Tk()
start = ttk.Button(text='Start',command=main)
label = ttk.Label(text='NPC-reator')
output = tk.Text(height=10,width=60)
nameSelect = tk.StringVar()
jobSelect = tk.StringVar()
jobSelect.set('None')
nameSelect.set('devNames.txt')
job = tk.OptionMenu(window, jobSelect,*jobFiles)
name = tk.OptionMenu(window, nameSelect,*nameFiles)

label.grid(row=0,column=0)
output.grid(row=0,column=1)
start.grid(row=0,column=2)
job.grid(row=1,column=1)
name.grid(row=1,column=2)
window.mainloop()
randName(listName, amount)
randJob(listJob, amount)

