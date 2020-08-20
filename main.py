from tkinter import *
from time import *
from tkinter import ttk
from tkinter import messagebox

global minutes
global seconds
global seconds_displayed
global minutes_displayed
global closing_count

minutes = 0
seconds = 0

closing_count = 0

global indicator
indicator = 0


class Stop_Watch:
    def __init__(self, master):
        self.root = master
        self.root.title("Sasatech Timer")
        self.root.iconbitmap('chronographwatch.ico')
        self.root.geometry("250x120+600+0")
        self.root.resizable(False, False)
        self.root.configure(background='sky blue')

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        # --labels--
        self.time_now = Label(self.root, text="Time Now:", bg='sky blue')
        self.time_now.grid(row=0, column=0)

        self.time_label = Label(self.root, font=("algerian", 10), bg='sky blue')
        self.time_label.grid(row=0, column=2)

        self.start_time_label = Label(self.root, text="Start Time:", bg='sky blue')
        self.start_time_label.grid(row=1, column=0)

        self.start_time = Label(self.root, font=("algerian", 10), bg='sky blue')
        self.start_time.grid(row=1, column=2)

        self.stop_time_label = Label(self.root, text="Stop Time:", bg='sky blue')
        self.stop_time_label.grid(row=2, column=0)

        self.stop_time = Label(self.root, font=("algerian", 10), bg='sky blue')
        self.stop_time.grid(row=2, column=2)

        self.time_spent_label = Label(self.root, text='Time Spent:', bg='sky blue')
        self.time_spent_label.grid(row=3, column=0)

        self.timer_label = Label(self.root, text='00:00', font=("algerian", 10), bg='sky blue')
        self.timer_label.grid(row=3, column=2)

        # --buttons--

        self.start_button = ttk.Button(self.root, text="START", command=self.time_at_start)
        self.start_button.grid(row=5, column=0)

        self.stop_button = ttk.Button(self.root, text="STOP", command=self.time_at_stop)
        self.stop_button.grid(row=5, column=1)

        self.reset_button = ttk.Button(self.root, text="RESET", command=self.time_reset)
        self.reset_button.grid(row=5, column=2)

    def on_closing(self):
        global closing_count


        # moving to the next page
        if closing_count == 0:
            root3 = Toplevel(self.root)
            newGUI = Close_window(root3)
            closing_count=3

        elif closing_count == 1:
            self.root.destroy()

        else:
            messagebox.showwarning('ERROR!', 'PLEASE ENSURE THAT YOU HAVE ENTERED THE PASSWORD TO CLOSE THE WINDOW')

    def time_time(self):
        self.current_time = strftime('%I:%M %p')
        self.time_label['text'] = self.current_time
        self.root.after(200, self.time_time)

    def time_at_start(self):
        global indicator
        if indicator == 0:
            self.time_start = strftime('%I:%M %p')
            self.start_time['text'] = self.time_start
            indicator = 1
            self.timer_on()

        elif indicator == 1:
            self.start_button['state'] = 'disabled'

        elif indicator == 2:
            messagebox.showwarning('ERROR!', 'PLEASE RESET THE TIMER!!')

    def time_at_stop(self):
        global indicator
        if indicator == 1:
            self.time_stop = strftime('%I:%M %p')
            self.stop_time['text'] = self.time_stop
            indicator = 2

        elif indicator == 2:
            self.stop_button['state'] = DISABLED
            messagebox.showwarning('STOP!', 'PLEASE RESET THE TIMER!')

        elif indicator == 0:
            messagebox.showwarning('STOP!', 'THE TIMER HAS NOT BEEN STARTED!!')

    def time_reset(self):
        global indicator
        global minutes
        global seconds

        if indicator == 2:
            root2 = Toplevel(self.root)
            newGUI = Confirmation(root2)


        elif indicator == 1:
            messagebox.showwarning('STOP!', 'THE TIMER CANNOT RESET WHILE IT IS STILL RUNNING!')

        elif indicator == 0:
            self.stop_time['text'] = " "
            self.start_time['text'] = " "
            self.timer_label['text'] = '00:00'
            self.start_button['state'] = NORMAL
            self.stop_button['state'] = NORMAL

        else:
            messagebox.showwarning('STOP!', 'THE TIMER HAS NOT STARTED YET!')

    def timer_on(self):
        global minutes
        global seconds
        global seconds_displayed
        global minutes_displayed

        if indicator == 1:
            if (seconds) < 59:
                seconds = seconds + 1


            elif (seconds) == 59:
                seconds = 0
                minutes += 1

            if minutes < 10:
                minutes_displayed = str(0) + str(minutes)

            else:
                minutes_displayed = str(minutes)

            if seconds < 10:
                seconds_displayed = str(0) + str(seconds)

            else:
                seconds_displayed = str(seconds)

            self.timer_label['text'] = f'{minutes_displayed}:{seconds_displayed}'
            self.root.after(1000, self.timer_on)
        elif indicator == 0:
            self.timer_label['text'] = '00:00'

        else:
            self.timer_label['text'] = f'{minutes_displayed}:{seconds_displayed}'


class Confirmation:
    def __init__(self, master):
        self.root = master
        self.root.title("Sasatech Timer")
        self.root.iconbitmap('chronographwatch.ico')
        self.root.geometry("250x100+600+0")
        self.root.resizable(False, False)
        self.root.configure(background='sky blue')

        # --labels--
        self.confirmation_label = Label(self.root, text='Please Enter Reset Password:', bg='sky blue')
        self.confirmation_label.grid(row=0, column=0, columnspan=2)

        # --entry--
        self.password_entry = Entry(self.root, show='*', width=30)
        self.password_entry.grid(row=1, column=0, columnspan=2, pady=5)

        # -- buttons--
        self.submit = ttk.Button(self.root, text='Submit', command=self.submit_password)
        self.submit.grid(row=2, column=0)

        self.quit = ttk.Button(self.root, text='Quit', command=self.destroy_page)
        self.quit.grid(row=2, column=1)

    def submit_password(self):
        self.password = self.password_entry.get()

        global indicator
        global minutes
        global seconds

        if self.password == 'Antoh' or self.password == 'Freddie':
            messagebox.showinfo('Success', 'Success')

            indicator = 0
            minutes = 0
            seconds = 0
            self.root.destroy()



        else:
            messagebox.showwarning('ERROR', 'WRONG PASSWORD!!')
            self.root.destroy()

    def destroy_page(self):
        self.root.destroy()


class Close_window:
    def __init__(self, master):
        self.root = master
        self.root.title("Sasatech Timer")
        self.root.iconbitmap('chronographwatch.ico')
        self.root.geometry("200x120+600+300")
        self.root.resizable(False, False)
        self.root.configure(background='sky blue')

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        # --labels--
        self.confirmation_label = Label(self.root, text='Please Enter Closing Password:', bg='sky blue')
        self.confirmation_label.grid(row=0, column=0, columnspan=2)

        # --entry--
        self.password_entry = Entry(self.root, show='*', width=30)
        self.password_entry.grid(row=1, column=0, columnspan=2, pady=5)

        # -- buttons--
        self.submit = ttk.Button(self.root, text='Submit', command=self.submit_password)
        self.submit.grid(row=2, column=0, sticky=W)

        self.quit = ttk.Button(self.root, text='Quit', command=self.destroy_page)
        self.quit.grid(row=2, column=1)

    def on_closing(self):
        self.root.destroy()
        global closing_count
        closing_count = 0

    def submit_password(self):

        self.password = self.password_entry.get()

        if self.password == 'Antoh' or self.password == 'Freddie':
            self.root.destroy()
            global closing_count
            closing_count = 1


        else:
            messagebox.showwarning('ERROR', 'WRONG PASSWORD!')
            self.root.destroy()
            closing_count = 0

    def destroy_page(self):
        self.root.destroy()
        global closing_count
        closing_count = 0



root = Tk()
stop_watch = Stop_Watch(root)
stop_watch
stop_watch.time_time()

root.mainloop()
