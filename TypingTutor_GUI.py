import time
import os
import tkinter as tk
root = tk.Tk()
root.geometry("400x600")
top = tk.Frame(root)
bottom = tk.Frame(root)
top.pack(side=tk.TOP)
bottom.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

if os.path.isfile('statistics.txt'):
    os.remove('statistics.txt')
write = open('statistics.txt', 'w')

try:
	with open('sentences.txt', 'r') as f:
		current_line = ''

		def statistics():
			st = open('statistics.txt', 'r+')
			S = st.readlines()
			statisticsLABEL.config(text=S)
			st.close()


		def clear(content):
			content.set("")


		def close_window():
			root.destroy()


		def next_line():
			global current_line
			current_line = next(f)
			label.config(text=current_line.strip('\n'))
			global start1
			start1 = time.time()
			global k
			k=0


		label = tk.Label(root, text='')
		label.pack(in_= top)
		l = label.cget("text")

		instruction = tk.Label(root, text='Type here:')
		instruction.pack(in_=top)
		content = tk.StringVar()
		e = tk.Entry(root, textvariable = content,  font = "Helvetica 20 bold")
		e.pack(in_= top)


		z = e.get()
		start0 = time.time()


		it = 0
		error = 0



		def pressed(keyevent):
			global k
			k += 1

			word_count = len(label.cget("text").split())
			stop1 = time.time()
			timetaken1 = stop1 - start0
			speed1 = (word_count / timetaken1)
			speedPerpressing.config(text=("Speed-> " + "{:.2f}".format(speed1)))


			if e.get() == label.cget("text")[:k]:
				print(e.get(), type(e.get()), label.cget("text")[:k], type(label.cget("text")[:k]), e.get() == label.cget("text")[:k])
				print("correct")
				bool.config(text="correct letter")


			else:
				k -=1
				print(e.get(), type(e.get()), label.cget("text")[:k], type(label.cget("text")[:k]), e.get() == label.cget("text")[:k])
				print("incorrect")
				bool.config(text="incorrect letter")
				global error
				error += 1
				print(error)
				totalerrors.config(text="total mistakes: {}".format(error))


			# if len(e.get()) == 1 and len(label.cget("text")) > 1 and str(tuple(label.cget("text"))[0]) == keyevent.char:  #this to start time after typing the first letter
			# 	global start1
			# 	start1 = time.time()

			if label.cget("text") == e.get():
				evaluation.config(text = "Match")
				stop2 = time.time()
				timetaken2 = stop2 - start1
				speed2 = (word_count / timetaken2)
				finalspeed.config(text="You took {:.2f}".format(timetaken2) + " seconds , " + "Typing speed: {:.2f} ,".format(speed2) + " mistakes: {}".format(error))
				st1 = open('statistics.txt', 'a')
				global it
				it += 1
				st1.write("Line {}: {}".format(it,(finalspeed.cget("text"))) + '\n')
				st1.close()

			if label.cget("text") != e.get():
				evaluation.config(text="you're still in process")
				finalspeed.config(text="Results......")


		speedPerpressing = tk.Label( root, text='')
		speedPerpressing.pack(in_= top)

		bool = tk.Label(root, text='')
		bool.pack(in_=top)

		totalerrors = tk.Label(root, text='')
		totalerrors.pack(in_=top)

		evaluation = tk.Label( root, text='')
		evaluation.pack(in_= top)

		finalspeed = tk.Label(root, width=50, height=1, bg = "white", text='')
		finalspeed.pack(in_= top)


		nxtbtn = tk.Button(root, width=18, height=3, text="Click for next line", command=next_line)
		nxtbtn.pack(in_= top, side= tk.LEFT, padx=15, pady=10, ipadx = 15)

		clearBtn = tk.Button(root, width=20, height=3, text="Clear input",command=lambda: clear(content))
		clearBtn.pack(in_= top, side= tk.LEFT, padx=20, pady=10, ipadx = 20)

		closeWindow = tk.Button(root, width=18, height=3, text="CLOSE", command= close_window)
		closeWindow.pack(in_= bottom, side= tk.LEFT, padx=20, pady=10, ipadx = 10)

		printStatistics = tk.Button(root, width=18, height=3, text="My Statistics", command=statistics)
		printStatistics.pack(in_= bottom, side= tk.LEFT, padx=20, pady=10, ipadx=13)

		statisticsLABEL = tk.Label(root, text='')
		statisticsLABEL.pack()

		next_line()
		e.bind('<KeyRelease>', pressed)
		root.mainloop()


except IOError as ex:
	NoFile = tk.Label(root, text="No such file exists!(")
	NoFile.pack()

root.mainloop()


#these next lines are not important but only for comparing between the input and each lines from the file
# print(str(tuple(e.get())[-1]), type(str(tuple(e.get())[-1])), str(tuple(label.cget("text"))[-1]), type(str(tuple(label.cget("text"))[-1])), str(tuple(e.get())[-1]) == str(tuple(label.cget("text"))[-1]))
# if str(tuple(e.get())[-1]) == str(tuple(label.cget("text"))[-1]):
#
# print(e.get(), type(e.get()), label.cget("text"), type(label.cget("text")), e.get() == label.cget("text"))
# if e.get() == label.cget("text"):
#
# print(len(e.get()), type(len(e.get())), len(label.cget("text")), type(len(label.cget("text"))), len(e.get()) == len(label.cget("text")))
# if len(e.get()) == len(label.cget("text")):
