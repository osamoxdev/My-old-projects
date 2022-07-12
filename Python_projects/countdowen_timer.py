# Count dowen timer (simple)

# import time


# def countdown(s):

#     while s :
#         mins, secs = divmod(s, 60)

#         timer = "{:02d}:{:02d}".format(mins, secs)

#         print(timer, end= '\r')

#         time.sleep(1)

#         s -= 1
#     print('NOW!')

# s = input('Enter the time in seconds : ')

# countdown(int(s))

import tkinter as tk    
import time
import threading

from plyer import notification

class Timer :

    def __init__(self) :
        

        self.root = tk.Tk()
        self.root.title('Countdown Timer')
        self.root.geometry('460x220')

        self.time_entery = tk.Entry(self.root, font=('Helvetica',30)) # font=()
        self.time_entery.grid(row=0, column=0, columnspan=2, padx=5,pady=5)

        self.start_butten = tk.Button(self.root, font=('Helvetica', 30), text='Start', command=self.start_thread)
        self.start_butten.grid(row=1, column=0, padx=5, pady=5)

        self.stop_butten = tk.Button(self.root, font=('Helvetica',30), text='Stop', command=self.stop)
        self.stop_butten.grid(row=1, column=1, padx=5, pady=5)

        self.time_lable = tk.Label(self.root, font=('Helvetica', 30), text= 'Time: 00:00:00')
        self.time_lable.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

    
        self.stop_loop = False
        
        self.root.mainloop()


        
    def start_thread(self):

        t = threading.Thread(target=self.start)

        t.start()

    def start(self):

        self.stop_loop = False

        hour, min, sec = 0, 0, 0
        string_split = self.time_entery.get().split(':')

        if len(string_split) == 3 :

            hour = int(string_split[0])
            min = int(string_split[1])
            sec = int(string_split[2])

        elif len(string_split) == 2 :
            min = int(string_split[0])
            sec = int(string_split[1])

        elif len(string_split) == 1 :
            sec = int(string_split[0])

        else : 
            print('Invalid Time format!')
            return#


        full_sec = hour * 3600 + min *60 + sec

        while full_sec > 0 and not self.stop_loop :

            full_sec -= 1

            min, sec = divmod(full_sec, 60)
            hour, min = divmod(min, 60)
            
            self.time_lable.config(text=f'Time: {hour:02d}:{min:02d}:{sec:02d}')
            self.root.update()


            time.sleep(1)

        if not self.stop_loop :

            title = 'Countdown Timer'
            message = 'Full Time!'

            notification.notify(title=title, message=message, timeout=8)

    def stop(self):

        self.stop_loop = True
        self.time_lable.config(text='Time: 00:00:00')

Timer()