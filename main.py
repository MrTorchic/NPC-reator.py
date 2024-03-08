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
def main():
	quantity = numVal.get()
	amount = quantity
	nameList.clear()
	occupationList.clear()
	with open(f'Lists/Names/{namefileVal.get()}') as f:
		line_count = 0
		for line in f:
			line_count += 1
		for i in range(0, quantity):
			rand1=rng.integers(line_count)
			rand2=rng.integers(line_count)
			firstName = linecache.getline(f'Lists/Names/{namefileVal.get()}', rand1)
			lastName = linecache.getline(f'Lists/Names/{namefileVal.get()}', rand2)
			nameStr=f'First: {firstName.rstrip()} | Last: {lastName.rstrip()}'+'\n'
			nameList.append(f'{nameStr}')
	if jobState.get()==0: #Occupation not enable, make and append nameList
		numpy.random.seed()
		output.delete(0.0, tk.END)
		num=0
		for i in nameList:
			output.insert(f'{num}.0',i)
			for i in nameList:
				if num<amount:
					num+=1
				else:
					num=0
	with open(f'Lists/Jobs/{jobfileVal.get()}') as g: #select randomJob
		line_counta = 0
		for line in g:
			line_counta += 1
		for i in range(0, quantity):
			rand3 = rng.integers(line_counta)
			randomJob = linecache.getline(f'Lists/Jobs/{jobfileVal.get()}', rand3)
			occupationList.append(f'Occupation: {randomJob}')
	if jobState.get()==1: #Merge
		num=0
		numpy.random.seed()
		output.delete(0.0, tk.END)
		mergedList.clear()
		for ii in range(0, quantity):
			print(mergedList)
			mergedList.append(f'{nameList[ii].rstrip()} | {occupationList[ii].rstrip()}')
			output.insert(f'{ii}.0',f'{mergedList[ii]}\n')

#Init Window
window = tk.Tk()
ttk.Style().theme_use('clam')
window.configure(bg='#9932cc')
window.title('NPC-reator')
#Name
namefileVal=tk.StringVar()
namefileVal.set('devNames.txt')
nameMenu=tk.OptionMenu(window, namefileVal,*nameFiles)
nameMenu.configure(background="#dda0dd")
nameMenu.grid(row=0,column=8)
nameLabel=tk.Label(text='Name List:',bg='#dda0dd').grid(row=0,column=6)
#Job
jobfileVal = tk.StringVar()
jobfileVal.set('devOccupations.txt')
#
jobMenu = tk.OptionMenu(window, jobfileVal,*jobFiles)
jobMenu.configure(background="#dda0dd")
jobMenu.grid(row=0,column=10)
#
jobState= tk.IntVar()
jobToggle= tk.Checkbutton(text='Job List:',variable=jobState,bg='#dda0dd').grid(row=0,column=9)
#Num
numLabel = tk.Label(window,text='Quantity:',bg='#dda0dd').grid(row=0,column=11)
numVal = tk.IntVar()
numVal.set(5)
numEntry = tk.OptionMenu(window, numVal, *numList)
numEntry.configure(background="#dda0dd")
numEntry.grid(row=0,column=12)
#Other
start = tk.Button(window, text = 'Run', bg='#dda0dd', command=main).grid(row=0,column=3)
output=tk.Text(height=25,width=75, bg='#dda0dd')
output.grid(row=0,column=1)
label = tk.Label(text='NPC-reator',bg='#dda0dd').grid(row=0,column=0)
window.mainloop()


