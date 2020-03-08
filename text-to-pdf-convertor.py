from tkinter import *
from tkinter import filedialog,messagebox,simpledialog
# pip install fpdf
from fpdf import FPDF

"""this project is created by Yogesh singh ,,
 Adimn of instagram page dynamic_codeing  """
def convert():
    # save FPDF() class into a variable pdf
    pdf = FPDF()
    # Add a page
    pdf.add_page()
    # set style and size of font that you want in the pdf
    pdf.set_font("Arial", size=15)
    # open the text file in read mode
    try:
        f = open(set_path.get(), "r")
        # insert the texts in pdf
        for x in f:
            text2 = x.encode('latin-1', 'replace').decode('latin-1')
            pdf.cell(200, 10, txt=text2, ln=1, align='L')

        name = simpledialog.askstring('Convertor Says ','Enter name of your PDF')
        if '.pdf' in name :
            pdf.output(name)
            messagebox.showinfo("Convertor Says", name + " IS Created")
        else:
            pdf_name = str(name) + '.pdf'
            pdf.output(pdf_name)
            messagebox.showinfo("Convertor Says", pdf_name + " IS Created")



    except Exception as e :
        messagebox.showerror("Convertor says ","Some thing went Wrong // \n please Try again")



def get_path():
    path = filedialog.askopenfilename()
    set_path.set('')
    set_path.set(path)


root = Tk()
root.title("Text to Pdf ")
root.geometry("310x150")
root.resizable(0,0)
root.configure(background="white")
set_path = StringVar()

title_label = Label(root,text="Text To PDF Convertor",font=('Arial',20,'bold'),bg="white")
title_label.grid(row=0,column=0)

path_of_text_entry = Entry(root,width=40,font=('Arial',10),bd=4,relief=GROOVE,textvariable=set_path)
path_of_text_entry.grid(row=1,column=0)

get_path_button = Button(root,text="Find TEXT file",font=('Arial',10,'bold'),command=get_path)
get_path_button.grid(row=2,column=0)

convert_button = Button(root,text="Convert Into PDF",font=('Arial',10,'bold'),command=convert)
convert_button.grid(row=4,column=0,ipadx=5,ipady=10)


root.mainloop()