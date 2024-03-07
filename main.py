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
100,
120,
140,
160,
180,
200,
400,
800,
1000
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
	nameList.clear()
	print(quantity)
	with open(f'Lists/Names/{name}') as f:
		line_count = 0
		print(quantity)
		for line in f:
			line_count += 1
		for i in range(0, quantity):
			#get the contents of the line
			x=rng.integers(line_count)
			y=rng.integers(line_count)
			firstName = linecache.getline(f'Lists/Names/{name}', x)
			lastName = linecache.getline(f'Lists/Names/{name}', y)

			print(i)
			nameStr=f'{firstName.rstrip()} {lastName.rstrip()}'
			#append line
			nameList.append(f'{nameStr}\n')
			print(nameList)
		else:
			print(f"loop 1 success")




def randJob(jobName, quantity):
	occupationList.clear()
	print(quantity)
	with open(f'Lists/Jobs/{jobName}') as f:
		line_counta = 0
		for line in f:
			line_counta += 1
		for i in range(0, quantity):
			#randomly pick a
			x = rng.integers(line_counta)
			#get the random job
			jobNamea = linecache.getline(f'Lists/Jobs/{jobName}', x)

			#append randJob to $occupationList
			occupationList.append(f'Occupation: {jobNamea}')
		else:
			#confirms when process is finished
			print('loop 2 success')


def merge(x):
	mergedList.clear()
	for i in range(0,x):
		print(i)
		mergedList.append(f'{nameList[i].rstrip()} - {occupationList[i]}')

def main():
	#make sure the num is reset
	#clear output field

	#rand seed
	#set the amout variable
	amount=numVal.get()
	if jobStatus.get()==0: #Jobs Disabled
		num=0
		numpy.random.seed()
		output.delete(0.0, tk.END)
		randName(nameSelect.get(),amount)
		for i in nameList:
			output.insert(f'{num}.0',i)
			for i in nameList:
				if num<amount:
					num+=1
				else:
					num=0
	elif jobStatus.get()==1: #Jobs Enabled
		num=0
		numpy.random.seed()
		output.delete(0.0, tk.END)
		randName(nameSelect.get(),amount)
		randJob(jobSelect.get(),amount)
		merge(amount)
		for i in mergedList:
			a = f'{num}.0'
			b = f'{i}'
			output.insert(a,b)
			for i in mergedList:
				if num<amount:
					num+=1
				else:
					num=0
		else:
			print('main loop finished')
			print('1')



#Init Window
window = tk.Tk()
ttk.Style().theme_use('clam')
window.configure(bg='#9932cc')
#Name
nameSelect=tk.StringVar()
nameSelect.set('N/A')
nameEntry=tk.OptionMenu(window, nameSelect,*nameFiles)
nameEntry.configure(background="#dda0dd")
nameEntry.grid(row=0,column=8)
nameLabel=tk.Label(text='Name List:',bg='#dda0dd').grid(row=0,column=6)
#Job
jobSelect = tk.StringVar()
jobSelect.set('N/A')
jobEntry = tk.OptionMenu(window, jobSelect,*jobFiles)
jobEntry.configure(background="#dda0dd")
jobEntry.grid(row=0,column=10)
jobStatus= tk.IntVar()
jobToggle= tk.Checkbutton(text='Job List:',variable=jobStatus,bg='#dda0dd').grid(row=0,column=9)
#Num
numLabel = tk.Label(window,text='Quantity:',bg='#dda0dd').grid(row=0,column=11)
numVal = tk.IntVar()
numVal.set(5)
numEntry = tk.OptionMenu(window, numVal, *numList)
numEntry.configure(background="#dda0dd")
numEntry.grid(row=0,column=12)
#Other
start = tk.Button(window, text = 'Run', bg='#dda0dd', command=main).grid(row=0,column=3)
output=tk.Text(height=25,width=50, bg='#e6e6fa')
output.grid(row=0,column=1)
label = tk.Label(text='NPC-reator',bg='#dda0dd').grid(row=0,column=0)
window.mainloop()


