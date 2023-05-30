# # from timer_function import print_module


# # def print_test():
# #     print("123")
    

import tkinter as tk

def key_pressed(event):
    global index
    text.tag_remove('current', '1.0', tk.END)
    # text.tag_add('current', f'1.{index}', f'1.{index+1}')
    text.tag_add('current', '1.0', f'1.{index+1}')
    text.tag_configure('current', foreground='red')
    index += 1

root = tk.Tk()

text = tk.Text(root, height=10, width=30)
text.pack()

text.insert(tk.END, 'This is a test. This is a test.')

index = 0

text.bind('<Key>', key_pressed)
text.focus_set()

root.mainloop()


