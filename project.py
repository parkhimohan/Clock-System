import tkinter as tk
import math
import datetime
import time
import os
from tkinter import messagebox
import webbrowser
import subprocess
#########################################################################################################################################
######code for stop watch################################################################################################################
#########################################################################################################################################
def update_timeText():
    if (state == True):
        global timer
        # Every time this function is called, 
        # we will increment 1 centisecond (1/100 of a second)
        timer[2] += 1
        
        # Every 100 centisecond is equal to 1 second
        if (timer[2] >= 100):
            timer[2] = 0
            timer[1] += 1
        # Every 60 seconds is equal to 1 min
        if (timer[1] >= 60):
            timer[0] += 1
            timer[1] = 0
        # We create our time string here
        timeString = pattern.format(timer[0], timer[1], timer[2])
        # Update the timeText Label box with the current time
        timeText.configure(text=timeString)
        # Call the update_timeText() function after 1 centisecond
    root1.after(10, update_timeText)

# To start the kitchen timer
def start():
    global state
    state = True

# To pause the kitchen timer
def pause():
    global state
    state = False

# To reset the timer to 00:00:00
def reset():
    global timer
    timer = [0, 0, 0]
    timeText.configure(text='00:00:00')

#To print lap time
def lap():
	tText = tk.Label(root1, text=str(timer[0])+':'+str(timer[1])+':'+str(timer[2]), font=("Helvetica", 10))
	tText.pack()  
   
def split():
	global timer
	tText = tk.Label(root1, text=str(timer[0])+':'+str(timer[1])+':'+str(timer[2]), font=("Helvetica", 10))
	tText.pack()
	timer=[0,0,0]
# To exist our program
def exit():
    root1.destroy()

# Simple status flag
# False mean the timer is not running
# True means the timer is running (counting)
def stopwatch():
	global state
	state = False
	global root1
	root1 = tk.Tk()
	root1.wm_title('Stop Watch')
	global timer
	# Our time structure [min, sec, centsec]
	timer = [0, 0, 0]
	global pattern
	# The format is padding all the 
	pattern = '{0:02d}:{1:02d}:{2:02d}'
	global timeText
	# Create a timeText Label (a text box)
	timeText = tk.Label(root1, text="00:00:00", font=("Helvetica", 150))
	timeText.pack()

	startButton = tk.Button(root1, text='Start', command=start)
	startButton.configure(foreground="blue")
	startButton.pack()

	pauseButton = tk.Button(root1, text='Pause', command=pause)
	pauseButton.configure(foreground="blue")
	pauseButton.pack()

	resetButton = tk.Button(root1, text='Reset', command=reset)
	resetButton.configure(foreground="blue")
	resetButton.pack()

	quitButton = tk.Button(root1, text='Quit', command=exit)
	quitButton.configure(foreground="blue")
	quitButton.pack()

	lapButton = tk.Button(root1, text='lap', command=lap)
	lapButton.configure(foreground="blue")
	lapButton.pack()

	splitButton = tk.Button(root1, text='split', command=split)
	splitButton.configure(foreground="blue")
	splitButton.pack()
	
	update_timeText()
	root1.mainloop()
#########################################################################################################################################
######code for analog clock################################################################################################################
#########################################################################################################################################
def update_time():
	if (anastate == True):
		#taking current time from computer 
		t=str(datetime.datetime.now())
		time=t.split()
		var1=time[1].split(':')
		#storing hours
		hr=int(var1[0])
		#storing minutes
		minute=int(var1[1])
		#storing seconds
		sec=math.floor(float(var1[2]))
		second=int(sec)
		#displaying clock base
		coord=175,160,425,410						# outer white circle
		arc=c.create_oval(coord,fill="white")
		coord1=180,165,420,405						# inner black circle
		arc=c.create_oval(coord1,fill="black")
		mainpoint=297,282,303,288					# middle point
		arc=c.create_oval(mainpoint,fill="grey")
		point1=345,200,351,206						#1
		arc=c.create_oval(point1,fill="grey")
		point2=378,233,384,239						#2
		arc=c.create_oval(point2,fill="grey")
		point3=394,282,400,288						#3
		arc=c.create_oval(point3,fill="grey")
		point4=378,331,384,337						#4
		arc=c.create_oval(point4,fill="grey")
		point5=345,364,351,370						#5
		arc=c.create_oval(point5,fill="grey")
		point6=297,379,303,385						#6		
		arc=c.create_oval(point6,fill="grey")
		point7=249,364,255,370						#7
		arc=c.create_oval(point7,fill="grey")
		point8=216,331,222,337						#8
		arc=c.create_oval(point8,fill="grey")
		point9=200,282,206,288						#9
		arc=c.create_oval(point9,fill="grey")
		point10=216,233,222,239						#10
		arc=c.create_oval(point10,fill="grey")
		point11=249,200,255,206						#11
		arc=c.create_oval(point11,fill="grey")
		point12=297,185,303,191						#12			
		arc=c.create_oval(point12,fill="grey")
		#if 24 hr clock it converts it into 12 hr
		if hr>=12:
			hr=hr-12
		#to set the position of hour needle
		x3=300+50*(math.cos(math.radians(((hr*30)+(minute//10)*6)-90)))
		y3=285+50*(math.sin(math.radians(((hr*30)+(minute//10)*6)-90)))
		coord3=x3,y3,300,285
		line=c.create_line(coord3,fill="green",width=5)		# hour hand
		#to set the position of minute needle
		x2=300+75*(math.cos(math.radians((minute*6)-90)))
		y2=285+75*(math.sin(math.radians((minute*6)-90)))
		coord2=x2,y2,300,285
		line=c.create_line(coord2,fill="red",width=3)		# minute hand
		x1=300+85*(math.cos(math.radians((second*6)-90)))
		y1=285+85*(math.sin(math.radians((second*6)-90)))
		#to set the position of seconds needle
		coord1=x1,y1,300,285
		line=c.create_line(coord1,fill="blue",width=1)		# seconds hand
		c.pack()
		#calling functon after every second
		top.after(1000,update_time)
def analog():
	global anastate
	anastate=True
	global top
	top=tk.Tk()
	top.title('Analog Clock')
	global c
	#setting the canvas size
	c=tk.Canvas(top,bg="black",height=600,width=600)
	update_time()
	top.mainloop()
#########################################################################################################################################
######code for digital clock################################################################################################################
#########################################################################################################################################
def digi():
	global digital
	digital = tk.Tk()
	global time1
	time1 = ''
	global clock
	clock = tk.Label(digital, font=('times', 100, 'bold'), bg='white')
	clock.pack(fill=tk.BOTH, expand=1)
	scroll()
	digital.mainloop(  )
def scroll():
    global time1
    # get the current local time from the PC
    time2 = time.strftime('%H:%M:%S')
    # if time string has changed, update it
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)
    # calls itself every 200 milliseconds
    # to update the time display as needed
    # could use >200 ms, but display gets jerky
    digital.title('Digital clock')
    clock.after(200, scroll)
#########################################################################################################################################
######code for alarm################################################################################################################
#########################################################################################################################################
def SubmitButton():

  AlarmTime= entry1.get()
  Message1()
  #label2.config(text ="The Alarm will Ring at {} ".format(AlarmTime))  #delayed in execution
  CurrentTime = time.strftime("%H:%M")
  print("the alarm time is: {}".format(AlarmTime))
  #label2.config(text="")
  while AlarmTime != CurrentTime:
    #label2.config(text ="The Alarm will Ring at {} ".format(AlarmTime))
    CurrentTime = time.strftime("%H:%M")
    time.sleep(1)
  if AlarmTime == CurrentTime:
     #print("now Alarm Music Playing")
     #os.system("start voltage.mp3")
     webbrowser.open("/home/parkhi/Desktop/voltage.mp3")
     label2.config(text = "Alarm music playing.....")
     messagebox.showinfo(title= 'Reminder', message= "{}".format(entry2.get()))
def Message1():
    AlarmTimeLable= entry1.get()
    #label2.config(text="the Alarm time is Counting...")
    #label2.config(text= "the Alarm will ring at {}".format(AlarmTimeLable))
    messagebox.showinfo(title = 'Alarm clock', message = 'Alarm will Ring at {}'.format(AlarmTimeLable))  
def alarm():
	global root 
	root = tk.Tk()
	root.title("Alarm clock")  
	frame1 = tk.Frame(root)
	frame1.pack()
	frame1.config(height = 100, width = 100)

	global label1
	label1= tk.Label(frame1,text = "Enter the Alarm time :")
	label1.pack()

	global entry1
	entry1 = tk.Entry(frame1, width = 30)
	entry1.pack()
	entry1.insert(3,"example - 13:15")

	labelAlarmMessage= tk.Label(frame1, text="Alarm Message:")
	labelAlarmMessage.pack()

	global entry2
	entry2= tk.Entry(frame1, width=30)
	entry2.pack()

	button1= tk.Button(frame1, text= "submit", command=SubmitButton)
	button1.pack()
	global label2
	#this Label2 will show the Last Alarm Time
	label2= tk.Label(frame1)
	label2.pack()

		
	#label2.config(text="hello")

	root.mainloop()
#########################################################################################################################################
######code for timer##############################################################################################################
#########################################################################################################################################
def update_timertime():
    if (timerstate == True):
        global timer
        # Every time this function is called, 
        # we will increment 1 centisecond (1/100 of a second)
        timer[1] -= 1
        if timer[1]==0 and timer[0]==0:
        	subprocess.call(['xdg-open','/home/parkhi/Desktop/voltage.mp3'])
        	exittimer()
        # Every 60 seconds is equal to 1 min
        if (timer[1] == 0):
            timer[0] -= 1
            timer[1] = 60
        # We create our time string here
        timeString = pattern.format(timer[0], timer[1])
        # Update the timeText Label box with the current time
        timeText.configure(text=timeString)
        # Call the update_timertime() function after 1 centisecond
    timerroot.after(1000, update_timertime)

# To start the kitchen timer
def timerstart():
    global timerstate
    timerstate = True


def exittimer():
	global timerstate
	timestate=False
	timerroot.destroy()

# Simple status flag
# False mean the timer is not running
# True means the timer is running (counting)
def funtimer():
	timermin=int(input("Enter no.of min: "))
	timersec=int(input("Enter no.of sec: "))
	global timerstate
	timerstate = False
	global timerroot
	timerroot = tk.Tk()
	timerroot.wm_title('Timer')
	global timer
	# Our time structure [min, sec, centsec]
	timer = [timermin, timersec]
	global pattern
	# The format is padding all the 
	pattern = '{0:02d}:{1:02d}'
	global timeText
	# Create a timeText Label (a text box)
	timeText = tk.Label(timerroot, text=str(timermin)+':'+str(timersec), font=("Helvetica", 150))
	timeText.pack()

	startButton = tk.Button(timerroot, text='Start', command=timerstart)
	startButton.pack()


	quitButton = tk.Button(timerroot, text='Quit', command=exittimer)
	quitButton.pack()

	update_timertime()
	timerroot.mainloop()
#########################################################################################################################################
def end():
		menu.destroy()


def main():
	global menu
	menu = tk.Tk()
	menu.wm_title('Clock System')

	headingLabel = tk.Label(menu, text='Clock System', font=("Helvetica", 45))
	headingLabel.configure(foreground="blue")

	headingLabel.pack()

	alarmClockButton = tk.Button(menu, text='Alarm Clock', command=alarm)
	alarmClockButton.configure(foreground="red", bg="pink")
	alarmClockButton.pack()

	stopWatchButton = tk.Button(menu, text='Stop Watch', command=stopwatch)
	stopWatchButton.configure(foreground="red", bg="pink")
	stopWatchButton.pack()

	timerButton = tk.Button(menu, text='     Timer     ', command=funtimer)
	timerButton.configure(foreground="red", bg="pink")
	timerButton.pack()

	analogClockButton = tk.Button(menu, text='Analog Clock', command=analog)
	analogClockButton.configure(foreground="red", bg="pink")
	analogClockButton.pack()

	digitalClockButton = tk.Button(menu, text='Digital Clock', command=digi)
	digitalClockButton.configure(foreground="red", bg="pink")
	digitalClockButton.pack()

	exitButton = tk.Button(menu, text='       Exit      ', command=end)
	exitButton.configure(foreground="red", bg="pink")
	exitButton.pack()

	menu.mainloop()
main()
	
