#Fantasy name list generator

#Imports
import numpy
import linecache
import tkinter as tk
from tkinter import ttk
from os import listdir
from os.path import isfile, join
from numpy.random import RandomState


#Variables
	#List location default
rng = numpy.random.default_rng()
numList = [
5,
10,
20,
40,
80,
160
]
amount=0

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
#File Lists
def randName(name, quantity):
	print(f'Generating... \n{name} x {quantity}')
	with open(f'Lists/Names/{name}') as f:
		line_count = 0
		for line in f:
			line_count += 1
		for i in range(0, quantity):
			#get the contents of the line
			firstName = linecache.getline(f'Lists/Names/{name}', rng.integers(line_count))
			lastName = linecache.getline(f'Lists/Names/{name}', rng.integers(line_count))
			#append line
			nameList.append(f'First Name: {firstName.rstrip()} Last: {lastName}')
		else:
			print(f"loop 1 success")
			print(f'{nameList}\n')

def randJob(jobName, quantity):
	print(f'Generating... \n{jobName} x {quantity}')
	with open(f'Lists/Jobs/{jobName}') as f:
		line_counta = 0
		for line in f:
			line_counta += 1
		for i in range(0, quantity):
			print(i)
			#randomly pick a
			x = rng.integers(line_counta)
			#get the random job
			randJob = linecache.getline(f'Lists/Jobs/{jobName}', x)
			#append randJob to $occupationList
			occupationList.append(f'Occupation: {randJob.rstrip()}')
		else:
			#confirms when process is finished
			print('loop 2 success')




def main():
	num = 0
	output.delete(0.0, 'end')
	numpy.random.seed()
	amount=numVal.get()
	if jobStatus.get()==0: #Jobs Disabled
		randName(nameSelect.get(),amount)
		for i in nameList:
			if num<amount:
				num+=1
			else:
				num=0
			output.insert(f'{num}.0',i)
		else:
			print('main loop finished')
	elif jobStatus.get()==1: #Jobs Enabled
		randName(nameSelect.get(),amount)
		randJob(jobSelect.get(),amount)
		for i in range(0,amount):
			mergedList.append(f'{nameList[i].rstrip()} {occupationList[i].rstrip()}\n')
		else:
			print(mergedList)
		for i in mergedList:
			num = 0
			if num<amount:
				num+=1
			else:
				num=0
			output.insert(f'{num}.0',i)
		else:
			print('main loop finished')
		print('1')

#Init Window
window = tk.Tk()
#Init & Define Main Label
label = ttk.Label(text='NPC-reator')
#Init & Define Output Field


output = tk.Text(height=10,width=100)
nameSelect = tk.StringVar()
#Init Job Var
jobSelect = tk.StringVar()
#Set Default Job File
jobSelect.set('N/A')
#Set Default Name File
nameSelect.set('N/A')
#Init & Define Job Selector
jobEntry = tk.OptionMenu(window, jobSelect,*jobFiles)
#Init & Define Name Selector
nameEntry = tk.OptionMenu(window, nameSelect,*nameFiles)
#
numLabel = tk.Label(text='Quantity:')
#
numVal = tk.IntVar()
numVal.set(10)
#
numEntry = tk.OptionMenu(window, numVal, *numList)
#
#
nameLabel= tk.Label(text='Name List:')
#
jobStatus= tk.IntVar()
#
jobToggle= tk.Checkbutton(text='Job List:',variable=jobStatus)
#
start = ttk.Button(text='Start',command=lambda:[delete_text(), main()])

#Assign to grid
	#Main Label
label.grid(row=0,column=0)
	#Start Button
start.grid(row=0,column=2)
	#Jobs
jobEntry.grid(row=2,column=5)
jobToggle.grid(row=2,column=4)
	#Names
nameEntry.grid(row=1,column=5)
nameLabel.grid(row=1,column=4)
	#Output Field
output.grid(row=0,column=1)
def delete_text():
	output.delete("1.0", tk.END)
	print('deleted')
	#Quantity Label & Settings
numLabel.grid(row=3,column=4)
numEntry.grid(row=3,column=5)
window.mainloop()


