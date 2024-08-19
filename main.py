import keyboard
from tkinter import *
from tkinter import ttk
from auto_clicker import Autoclicker

def start():
  mouse_button = mouse_button_cbox.get()
  cps = cps_entry.get()
  default_cps = 1
  if (cps == ""):
    cps_entry.insert(0, default_cps)
    cps = default_cps
  root.iconphoto(False, PhotoImage(file='assets/icon-on.ico'))
  start_btn.config(state=DISABLED)
  stop_btn.config(state=NORMAL)
  autoclicker.start(cps, mouse_button)

def stop():
  root.iconphoto(False, PhotoImage(file='assets/icon.ico'))
  start_btn.config(state=NORMAL)
  stop_btn.config(state=DISABLED)   
  autoclicker.stop()

def toggle_auto_clicker():
  state = str(start_btn['state'])
  if (state == "normal"):
    start()
  else:
    stop()

def select_hotkey():
  select_key_label.config(text="Press key...")
  select_key_label.config(foreground="#454445")
  root.bind("<Key>", select_hotkey_func)
  keyboard.unhook_all()

def select_hotkey_func(e):
  select_key_label.config(text=str.upper(e.keysym))
  select_key_label.config(foreground="blue")
  root.unbind("<Key>")
  keyboard.on_press_key(select_key_label['text'], lambda _:toggle_auto_clicker())

def validate_cps_entry(P):
  return str.isdigit(P) or P==""

if __name__ == "__main__":

  MOUSE_BUTTONS = ("left", "middle", "right")
  root = Tk()
  autoclicker = Autoclicker()
  
  # window config
  root.title("Autoclicker")
  root.iconphoto(False, PhotoImage(file='assets/icon.ico'))
  root.resizable(False, False)
  root.config(padx = 10, pady = 5)

  # cps validation command
  validate_cps_entry_cmd = (root.register(validate_cps_entry), '%P')
 
  # create widgets
  mouse_button_label = ttk.Label(text="BUTTON:")
  cps_label = ttk.Label(text="CPS:")
  hotkey_label = ttk.Label(text="HOTKEY:")
  select_key_label = ttk.Label(text="")
  cps_entry = ttk.Entry(width=10, validate="all", validatecommand=validate_cps_entry_cmd)
  hotkey_btn = ttk.Button(text="Select", command=select_hotkey)
  mouse_button_cbox = ttk.Combobox(values=MOUSE_BUTTONS, state="readonly", width=10)
  start_btn = ttk.Button(text="Start", command=start,)
  stop_btn = ttk.Button(text="Stop", command=stop, state=DISABLED, )
  mouse_button_cbox.current(0)

  # draw widgets
  mouse_button_label.grid(row=0, column=0)
  cps_label.grid(row=0, column=2)
  hotkey_label.grid(row=0, column=1)
  select_key_label.grid(row=2, column=1)
  mouse_button_cbox.grid(row=1, column=0)
  hotkey_btn.grid(row=1, column=1)
  cps_entry.grid(row=1, column=2)
  start_btn.grid(row=1, column=3)
  stop_btn.grid(row=1, column=4)
  
  root.mainloop()