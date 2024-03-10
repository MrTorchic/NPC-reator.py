#Fantasy name list generator

#Imports
import numpy
import linecache
import tkinter as tk
from tkinter import ttk
import os
from os import listdir
from os.path import isfile, join
from numpy.random import RandomState
from datetime import *
import subprocess
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
saveList=[
]


nameStr='init'
jobPath = 'src/Lists/Jobs/'
namePath = 'src/Lists/Names/'
jobFiles = [f for f in listdir(jobPath) if isfile(join(jobPath, f))]
nameFiles = [f for f in listdir(namePath) if isfile(join(namePath, f))]
#File Lists
def onExit():
	lineNum=0
	charNum=0
	endStr='end-1c'
	parta=f'{saveField.get(f"{lineNum+2}.{charNum}",tk.END)}'
	partb='./latest.txt'

	if parta!='': #If the file doesn't error out:
		subprocess.run(f'echo "{parta[1:]}" > latest.txt',shell=True,check=True)
		try:
			subprocess.run(f'mv ./out/*.txt ./out/old/out-{date.today()}-{numpy.random.randint(0,1000)}.txt', shell=True, check=True)
		except:
			print('bypassed room service... stage 1')
		try:
			subprocess.run(f'mv {partb} ./out/', shell=True, check=True)
		except:
			print('bypassed room service... stage 2')
	else:
		print('nothing to write')
	window.destroy()

def save():
	if savestateVal.get()==1:
		saveField.delete('2.0',tk.END)
	number=saveVal.get()
	output=outputField.get(f'{number+1}.0',f'{number+1}.50')
	saveField.insert(tk.END,f'\n{output}')

buildOutputhas_run = False
def buildOutput():
	global buildOutputhas_run
	if buildOutputhas_run:
		return
	if not buildOutputhas_run:
		quantity = numVal.get()
		for i in range(0,quantity+1):
			saveList.append(i+1)
		saveMenu=ttk.OptionMenu(window, saveVal, *saveList,style='TMenubutton')#.grid(row=0,column=12)
		saveMenu=saveMenu.grid(row=3,column=3,sticky='nw')
		saveField.insert('1.0','Save:')
		buildOutputhas_run=True

def main():
	quantity = numVal.get()
	amount = quantity
	buildOutput()
	outputField.delete('0.0',tk.END)
	with open(f'src/Lists/Names/{namefileVal.get()}') as e: #select randomJob
		line_countb = 0
		for line in e:
			line_countb += 1

	def seed():
		rand1=rng.integers(line_countb)
		numpy.random.seed()
		rand2=rng.integers(line_countb)
		numpy.random.seed()
		rand3=rng.integers(line_countb)
		randomGen(rand1,rand2,rand3)

	def randomGen(x,y,z):
		firstName = linecache.getline(f'src/Lists/Names/{namefileVal.get()}', x)
		lastName = linecache.getline(f'src/Lists/Names/{namefileVal.get()}', y)
		jobName =  linecache.getline(f'src/Lists/Jobs/{jobfileVal.get()}', z)
		nameStr=f'{ii+1} First:{firstName.rstrip()} Last:{lastName}'
		jobStr=f'Job:{jobName}'
		nameList.append(nameStr.strip())
		occupationList.append(jobStr.strip())

	if jobstateVal.get()!=1: #Merge
		num=0
		nameList.clear()
		outputField.insert('1.0','Generated:\n')

		for ii in range(0, quantity):
			seed()
			num=0
			if num<amount:
				num+=1
				outputField.insert(f'{ii+2}.0',f'{nameList[ii]}\n')

	elif jobstateVal.get()==1:
		num=0
		nameList.clear()
		outputField.insert('1.0','Generated:\n')
		for ii in range(0, quantity):
			seed()
			num=0
			if num<amount:
				num+=1
				outputField.insert(f'{ii+2}.0',f'{nameList[ii]} {occupationList[ii]}\n')

window = tk.Tk()
style = ttk.Style(window)
bgColor='#9932cc'
fgColor='#e6e6fa'
window.configure(bg=f'{bgColor}')
numVal = tk.IntVar()
numVal.set(5)
numLabel = ttk.Label(window,text='  Quantity:',style='TLabel')#.grid(row=0,column=11)
numMenu=ttk.OptionMenu(window, numVal, *numList,style='TMenubutton')#.grid(row=0,column=12)

jobstateVal= tk.IntVar()
jobfileVal = tk.StringVar()
jobfileVal.set(jobFiles[0])
jobLabel = ttk.Checkbutton(text=' Job List:',variable=jobstateVal)
jobMenu = ttk.OptionMenu(window, jobfileVal,*jobFiles,style='TMenubutton')#.grid(row=0,column=10)

namefileVal=tk.StringVar()
namefileVal.set(nameFiles[0])
nameLabel=ttk.Label(text='Name List:',style='TLabel')#.grid(row=0,column=6)
nameMenu=ttk.OptionMenu(window, namefileVal,*nameFiles,style='TMenubutton')#.grid(row=0,column=8)
savestateVal=tk.IntVar()
saveVal = tk.IntVar()
saveVal.set('')
saveLabel=tk.Checkbutton(text='Clear First?',variable=savestateVal)
saveButton = ttk.Button(window, text = 'Save', command=save,style='TButton')#.grid(row=0,column=3)
saveField=tk.Text(height=10,width=65, bg=f'{fgColor}')

outputField=tk.Text(height=10,width=65, bg=f'{fgColor}')


startButton = ttk.Button(window, text = 'Run', command=main,style='TButton')#.grid(row=0,column=3)


window.title('NPC-reator')


outputField.grid(row=0,column=1,sticky='e')
nameLabel.grid(row=4,column=2,sticky='ne')
nameMenu.grid(row=5,column=2,sticky='ne')
startButton.grid(row=1,column=2,sticky='e')
jobLabel.grid(row=6,column=2,sticky='ne')
jobMenu.grid(row=7,column=2,sticky='e')
numLabel.grid(row=2,column=2,sticky='e')
numMenu.grid(row=3, column=2,sticky='ne')

saveButton.grid(row=1,column=3,sticky='w')
saveField.grid(row=0,column=4,sticky='w')
saveLabel.grid(row=2,column=3,sticky='nw')






window.protocol("WM_DELETE_WINDOW", onExit)
window.mainloop()



