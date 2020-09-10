from tkinter import *
import create_data, face_recognize, test

window = Tk(); #created the window object...it is called window
window.title("Attendance Assistant")
window.geometry("720x400")
window.configure(background = "light grey")
logo_img = PhotoImage(file = "logo.png",width = 110)

logo = Label(window,image = logo_img,bg = "light grey")
logo.place(x = 600, y = 300)

text_entry = Entry()
top = 10
#functions that work when buttons are clicked
def CreateData():
    global text_entry
    global top
    top = Toplevel()
    top.configure(background = "light grey")
    top.geometry("720x480")
    top.title("New Face")
    # logo = Label(new_frame, image = logo_img).grid(row = 2, column = 2)
    # title = Label(new_frame,text="ATTENDANCE ASSISTANT" ,fg="black"  ,width=40  ,height=1,font=('Poor Richard', 35, 'bold') ).grid(row = 0, column = 0, columnspan = 2)
    instruction = Label(top,text="Enter Student Roll Number",fg = "black",bg = "light grey",font=('Poor Richard', 35, 'bold'))
    instruction.place(x = 100,y = 10)
    text_entry = Entry(top,bg = "white",width = 50, fg = "black")
    text_entry.place(x = 150, y = 100)
    submit_button = Button(top,text = "Submit",command = Run_Create_data,fg = "white", bg = "black",width = 25 , activebackground = "grey",font = ("Poor Richard",20,'bold'))
    submit_button.place(x = 150, y = 150)
def Run_Create_data():
    name = (text_entry.get())
    create_data.Create(name)
    top.destroy()   

def FaceDetect():
    global top
    top = Toplevel()
    top.configure(background = "light grey")
    top.geometry("720x480")
    top.title("Face Detection")
    instruction = Label(top, text = "Press Q to stop scanning for faces and close the window to continue with the program.",bg="light grey"  ,fg="black",height=1,font=('Poor Richard', 14, 'bold')).place(x = 20, y = 220)
    submit_button = Button(top,text = "Start Scanning",command = Run_Face_Detect,fg = "white", bg = "black",width = 25 , activebackground = "grey",font = ("Poor Richard",20,'bold'))
    submit_button.place(x = 150, y = 150)
def Run_Face_Detect():
    face_recognize.face_detect()
    top.destroy()   

def GenerateLOG():
    global top
    top = Toplevel()
    top.grid()
    top.configure(background = "light grey")
    top.geometry("720x480")
    top.title("Generating...")
    test.log_file_generator()
    message = Label(top,text = "Log File has been generated!\nPlease check the directory.").grid()
    okay_button = Button(top,text= "Ok",command = top.destroy()).grid()

title = Label(window,text="ATTENDANCE ASSISTANT" ,bg="light grey"  ,fg="black",height=1,font=('Poor Richard', 35, 'bold') )
title.place(x = 100, y = 10)
# lbl1 = Label(window, text="Enter Your College ID",width=20  ,height=2  ,fg="black"  ,bg="light grey" ,font=('Poor Richard', 25, ' bold ') ).grid(row = 2,column = 0,padx = 20,pady = 30)
# lbl2 = Label(window, text="Enter Your Name",width=20  ,fg="black"  ,bg="light grey"    ,height=2 ,font=('Poor Richard', 25, ' bold ')).grid(row = 2,column = 1,padx = 20,pady = 30) 

create_dat_button = Button(window, text = "Add New Face", command = CreateData, fg = "white", bg = "black",width = 25,height = 1, activebackground = "grey",font = ("Poor Richard",20,'bold'))
create_dat_button.place(x = 180, y = 80)
face_detect_button = Button(window,text = "Detect Face", command = FaceDetect, fg = "white", bg = "black",width = 25 ,height = 1, activebackground = "grey",font = ("Poor Richard",20,'bold'))
face_detect_button.place(x = 180,y = 140)
gen_output_button = Button(window,text = "Generate Log File",command = GenerateLOG, fg = "white", bg = "black",width = 25 ,height = 1, activebackground = "grey",font = ("Poor Richard",20,'bold'))
gen_output_button.place(x = 180, y = 200)
quit_wala_button = Button(window,text = "Quit",command = window.destroy,fg = "white", bg = "black",width = 25,height = 1, activebackground = "grey",font = ("Poor Richard",20,'bold'))
quit_wala_button.place(x = 180, y = 260)
window.mainloop()