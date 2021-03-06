from tkinter import *
import numpy as np
import os as os

window = Tk()
window.title("ELASTICITY")
window.geometry("1300x600")

#In this section, elastic stiffness matrix of 6x6 and elastic compliance matrix
# which is the inverse of the elastic stiffness matrix are created.
# In addition, the formulas of these modules have been integrated.
def calculate():
    matris = np.array([[float(input1.get()), float(input2.get()), float(input3.get()), float(input4.get()), float(input5.get()), float(input6.get())],
    [float(input7.get()), float(input8.get()), float(input9.get()), float(input10.get()), float(input11.get()), float(input12.get())],
    [float(input13.get()), float(input14.get()), float(input15.get()), float(input16.get()), float(input17.get()), float(input18.get())],
    [float(input19.get()), float(input20.get()), float(input21.get()), float(input22.get()), float(input23.get()), float(input24.get())],
    [float(input25.get()), float(input26.get()), float(input27.get()), float(input28.get()), float(input29.get()), float(input30.get())],
    [float(input31.get()), float(input32.get()), float(input33.get()), float(input34.get()), float(input35.get()), float(input36.get())]])
    invmatris = np.linalg.inv(matris)
    t1.insert(INSERT, str(matris))
    t2.insert(INSERT, invmatris)
    voightbulkmodulus =float(((matris[0][0]+matris[1][1]+matris[2][2]+2*(matris[0][1]+matris[0][2]+matris[1][2]))/9))
    voightbulkmodulus = round(voightbulkmodulus, 5)
    vbm['text'] = str(voightbulkmodulus)
    reussbulkmodulus = float(1/(invmatris[0][0]+invmatris[1][1]+invmatris[2][2]+2*(invmatris[0][1]+invmatris[1][2]+invmatris[0][2])))
    reussbulkmodulus = round(reussbulkmodulus, 5)
    rbm['text'] = str(reussbulkmodulus)
    vrhbulkmodulus = float(((((matris[0][0]+matris[1][1]+matris[2][2]+2*(matris[0][1]+matris[0][2]+matris[1][2]))/9))+(1/(invmatris[0][0]+invmatris[1][1]+invmatris[2][2]+2*(invmatris[0][1]+invmatris[1][2]+invmatris[0][2]))))/2)
    vrhbulkmodulus = round(vrhbulkmodulus, 5)
    vrhb['text'] = str(vrhbulkmodulus)
    voightshearmodulus = float((matris[0][0]+matris[1][1]+matris[2][2]-(matris[0][1]+matris[0][2]+matris[1][2])+3*(matris[3][3]+matris[4][4]+matris[5][5]))/15)
    voightshearmodulus = round(voightshearmodulus, 5)
    vsm['text'] = str(voightshearmodulus)
    reussshearmodulus = float(15/(4*(invmatris[0][0]+invmatris[1][1]+invmatris[2][2])-4*(invmatris[0][1]+invmatris[1][2]+invmatris[0][2])+3*(invmatris[3][3]+invmatris[4][4]+invmatris[5][5])))
    reussshearmodulus = round(reussshearmodulus)
    rsm['text'] = str(reussshearmodulus)
    vrhshearmodulus = float((((matris[0][0]+matris[1][1]+matris[2][2]-(matris[0][1]+matris[0][2]+matris[1][2])+3*(matris[3][3]+matris[4][4]+matris[5][5]))/15)+(15/(4*(invmatris[0][0]+invmatris[1][1]+invmatris[2][2])-4*(invmatris[0][1]+invmatris[1][2]+invmatris[0][2])+3*(invmatris[3][3]+invmatris[4][4]+invmatris[5][5]))))/2)
    vrhshearmodulus = round(vrhshearmodulus, 5)
    vrhs['text'] = str(vrhshearmodulus)
    youngmodulus = float((9*((((matris[0][0]+matris[1][1]+matris[2][2]-(matris[0][1]+matris[0][2]+matris[1][2])+3*(matris[3][3]+matris[4][4]+matris[5][5]))/15)+(15/(4*(invmatris[0][0]+invmatris[1][1]+invmatris[2][2])-4*(invmatris[0][1]+invmatris[1][2]+invmatris[0][2])+3*(invmatris[3][3]+invmatris[4][4]+invmatris[5][5]))))/2)*(((((matris[0][0]+matris[1][1]+matris[2][2]+2*(matris[0][1]+matris[0][2]+matris[1][2]))/9))+(1/(invmatris[0][0]+invmatris[1][1]+invmatris[2][2]+2*(invmatris[0][1]+invmatris[1][2]+invmatris[0][2]))))/2))/(((((matris[0][0]+matris[1][1]+matris[2][2]-(matris[0][1]+matris[0][2]+matris[1][2])+3*(matris[3][3]+matris[4][4]+matris[5][5]))/15)+(15/(4*(invmatris[0][0]+invmatris[1][1]+invmatris[2][2])-4*(invmatris[0][1]+invmatris[1][2]+invmatris[0][2])+3*(invmatris[3][3]+invmatris[4][4]+invmatris[5][5]))))/2)+3*((((((matris[0][0]+matris[1][1]+matris[2][2]+2*(matris[0][1]+matris[0][2]+matris[1][2]))/9))+(1/(invmatris[0][0]+invmatris[1][1]+invmatris[2][2]+2*(invmatris[0][1]+invmatris[1][2]+invmatris[0][2]))))/2))))
    youngmodulus = round(youngmodulus, 5)
    ym['text'] = str(youngmodulus)
    poissonratio = float(((3*(((((matris[0][0]+matris[1][1]+matris[2][2]+2*(matris[0][1]+matris[0][2]+matris[1][2]))/9))+(1/(invmatris[0][0]+invmatris[1][1]+invmatris[2][2]+2*(invmatris[0][1]+invmatris[1][2]+invmatris[0][2]))))/2))-((9*((((matris[0][0]+matris[1][1]+matris[2][2]-(matris[0][1]+matris[0][2]+matris[1][2])+3*(matris[3][3]+matris[4][4]+matris[5][5]))/15)+(15/(4*(invmatris[0][0]+invmatris[1][1]+invmatris[2][2])-4*(invmatris[0][1]+invmatris[1][2]+invmatris[0][2])+3*(invmatris[3][3]+invmatris[4][4]+invmatris[5][5]))))/2)*(((((matris[0][0]+matris[1][1]+matris[2][2]+2*(matris[0][1]+matris[0][2]+matris[1][2]))/9))+(1/(invmatris[0][0]+invmatris[1][1]+invmatris[2][2]+2*(invmatris[0][1]+invmatris[1][2]+invmatris[0][2]))))/2))/(((((matris[0][0]+matris[1][1]+matris[2][2]-(matris[0][1]+matris[0][2]+matris[1][2])+3*(matris[3][3]+matris[4][4]+matris[5][5]))/15)+(15/(4*(invmatris[0][0]+invmatris[1][1]+invmatris[2][2])-4*(invmatris[0][1]+invmatris[1][2]+invmatris[0][2])+3*(invmatris[3][3]+invmatris[4][4]+invmatris[5][5]))))/2)+3*((((((matris[0][0]+matris[1][1]+matris[2][2]+2*(matris[0][1]+matris[0][2]+matris[1][2]))/9))+(1/(invmatris[0][0]+invmatris[1][1]+invmatris[2][2]+2*(invmatris[0][1]+invmatris[1][2]+invmatris[0][2]))))/2)))))/(6*(((((matris[0][0]+matris[1][1]+matris[2][2]+2*(matris[0][1]+matris[0][2]+matris[1][2]))/9))+(1/(invmatris[0][0]+invmatris[1][1]+invmatris[2][2]+2*(invmatris[0][1]+invmatris[1][2]+invmatris[0][2]))))/2)))
    poissonratio = round(poissonratio, 5)
    pr['text'] = str(poissonratio)
    flexibilitycoefficient = float((((((matris[0][0]+matris[1][1]+matris[2][2]+2*(matris[0][1]+matris[0][2]+matris[1][2]))/9))+(1/(invmatris[0][0]+invmatris[1][1]+invmatris[2][2]+2*(invmatris[0][1]+invmatris[1][2]+invmatris[0][2]))))/2)/((((matris[0][0]+matris[1][1]+matris[2][2]-(matris[0][1]+matris[0][2]+matris[1][2])+3*(matris[3][3]+matris[4][4]+matris[5][5]))/15)+(15/(4*(invmatris[0][0]+invmatris[1][1]+invmatris[2][2])-4*(invmatris[0][1]+invmatris[1][2]+invmatris[0][2])+3*(invmatris[3][3]+invmatris[4][4]+invmatris[5][5]))))/2))
    flexibilitycoefficient = round(flexibilitycoefficient, 5)
    fc['text'] = str(flexibilitycoefficient)

# Frames and text fields have been created for visuality in this section.
mycolor = 'dark khaki'
frame1 = Frame(bg=mycolor, width=240, height=800)
frame1.place(x=0, y=0)
frame2 = Frame(bg=mycolor, width=1300, height=350)
frame2.place(x=245, y=0)
frame3 = Frame(bg=mycolor, width=1300, height=500)
frame3.place(x=245, y=355)
t1 = Text(width=110, height=6, bg="LightGoldenrod4", font="Courier 10 ", fg='black')
t1.place(x=300, y=50)
t2 = Text(width=110, height=6, bg="LightGoldenrod4", font="Courier 10 ", fg='black')
t2.place(x=300, y=240)

# Here, data entry part of elastic stiffness matrix with 36 components is created.
input1 = Entry(font="Courier 12", width=5, bg="LightGoldenrod4")
input1.place(x=40, y=50)
input2 = Entry(font="Courier 12", width=5, bg="LightGoldenrod4")
input2.place(x=40, y=80)
input3 = Entry(font="Courier 12", width=5, bg="LightGoldenrod4")
input3.place(x=40, y=110)
input4 = Entry(font="Courier 12", width=5, bg="LightGoldenrod4")
input4.place(x=40, y=140)
input5 = Entry(font="Courier 12", width=5, bg="LightGoldenrod4")
input5.place(x=40, y=170)
input6 = Entry(font="Courier 12", width=5, bg="LightGoldenrod4")
input6.place(x=40, y=200)
input7 = Entry(font="Courier 12", width=5, bg="LightGoldenrod4")
input7.place(x=40, y=230)
input8 = Entry(font="Courier 12", width=5, bg="LightGoldenrod4")
input8.place(x=40, y=260)
input9 = Entry(font="Courier 12", width=5, bg="LightGoldenrod4")
input9.place(x=40, y=290)
input10 = Entry(font="Courier 12", width=5, bg="LightGoldenrod4")
input10.place(x=40, y=320)
input11 = Entry(font="Courier 12", width=5, bg="LightGoldenrod4")
input11.place(x=40, y=350)
input12 = Entry(font="Courier 12", width=5, bg="LightGoldenrod4")
input12.place(x=40, y=380)
input13 = Entry(font="Courier 12", width=5, bg="LightGoldenrod4")
input13.place(x=40, y=410)
input14 = Entry(font="Courier 12", width=5, bg="LightGoldenrod4")
input14.place(x=40, y=440)
input15 = Entry(font="Courier 12", width=5, bg="LightGoldenrod4")
input15.place(x=40, y=470)
input16 = Entry(font="Courier 12", width=5, bg="LightGoldenrod4")
input16.place(x=40, y=500)
input17 = Entry(font="Courier 12", width=5, bg="LightGoldenrod4")
input17.place(x=40, y=530)
input18 = Entry(font="Courier 12", width=5, bg="LightGoldenrod4")
input18.place(x=40, y=560)
input19 = Entry(font="Courier 12", width=5, bg="LightGoldenrod4")
input19.place(x=140, y=50)
input20 = Entry(font="Courier 12", width=5, bg="LightGoldenrod4")
input20.place(x=140, y=80)
input21 = Entry(font="Courier 12", width=5, bg="LightGoldenrod4")
input21.place(x=140, y=110)
input22 = Entry(font="Courier 12", width=5, bg="LightGoldenrod4")
input22.place(x=140, y=140)
input23 = Entry(font="Courier 12", width=5, bg="LightGoldenrod4")
input23.place(x=140, y=170)
input24 = Entry(font="Courier 12", width=5, bg="LightGoldenrod4")
input24.place(x=140, y=200)
input25 = Entry(font="Courier 12", width=5, bg="LightGoldenrod4")
input25.place(x=140, y=230)
input26 = Entry(font="Courier 12", width=5, bg="LightGoldenrod4")
input26.place(x=140, y=260)
input27 = Entry(font="Courier 12", width=5, bg="LightGoldenrod4")
input27.place(x=140, y=290)
input28 = Entry(font="Courier 12", width=5, bg="LightGoldenrod4")
input28.place(x=140, y=320)
input29 = Entry(font="Courier 12", width=5, bg="LightGoldenrod4")
input29.place(x=140, y=350)
input30 = Entry(font="Courier 12", width=5, bg="LightGoldenrod4")
input30.place(x=140, y=380)
input31 = Entry(font="Courier 12", width=5, bg="LightGoldenrod4")
input31.place(x=140, y=410)
input32 = Entry(font="Courier 12", width=5, bg="LightGoldenrod4")
input32.place(x=140, y=440)
input33 = Entry(font="Courier 12", width=5, bg="LightGoldenrod4")
input33.place(x=140, y=470)
input34 = Entry(font="Courier 12", width=5, bg="LightGoldenrod4")
input34.place(x=140, y=500)
input35 = Entry(font="Courier 12", width=5, bg="LightGoldenrod4")
input35.place(x=140, y=530)
input36 = Entry(font="Courier 12", width=5, bg="LightGoldenrod4")
input36.place(x=140, y=560)

# Buttons
calculatebutton = Button(text="CALCULATE", font="Arial 10 bold", bg="LightGoldenrod4", fg='darkblue', command=calculate)
calculatebutton.place(x=1090, y=480)

infobutton = Button(text="info", font="Arial 10 bold", bg="LightGoldenrod4", fg='darkgreen',command=lambda:infoopen())
infobutton.place(x=1185, y=480)

resethbutton = Button(text="RESET", font="Arial 10 bold", bg="LightGoldenrod4", fg='darkred',command=lambda:refresh(window))
resethbutton.place(x=1226, y=480)

# Labels
label= Label(window, text="C11", font="Courier 10 bold", fg='black', bg=mycolor)
label.place(x=8, y=50)
label= Label(window, text="C12", font="Courier 10 bold", fg='black', bg=mycolor)
label.place(x=8, y=80)
label= Label(window, text="C13", font="Courier 10 bold", fg='black', bg=mycolor)
label.place(x=8, y=110)
label= Label(window, text="C14", font="Courier 10 bold", fg='black', bg=mycolor)
label.place(x=8, y=140)
label= Label(window, text="C15", font="Courier 10 bold", fg='black', bg=mycolor)
label.place(x=8, y=170)
label= Label(window, text="C16", font="Courier 10 bold", fg='black', bg=mycolor)
label.place(x=8, y=200)
label= Label(window, text="C21", font="Courier 10 bold", fg='black', bg=mycolor)
label.place(x=8, y=230)
label= Label(window, text="C22", font="Courier 10 bold", fg='black', bg=mycolor)
label.place(x=8, y=260)
label= Label(window, text="C23", font="Courier 10 bold", fg='black', bg=mycolor)
label.place(x=8, y=290)
label= Label(window, text="C24", font="Courier 10 bold", fg='black', bg=mycolor)
label.place(x=8, y=320)
label= Label(window, text="C25", font="Courier 10 bold", fg='black', bg=mycolor)
label.place(x=8, y=350)
label= Label(window, text="C26", font="Courier 10 bold", fg='black', bg=mycolor)
label.place(x=8, y=380)
label= Label(window, text="C31", font="Courier 10 bold", fg='black', bg=mycolor)
label.place(x=8, y=410)
label= Label(window, text="C32", font="Courier 10 bold", fg='black', bg=mycolor)
label.place(x=8, y=440)
label= Label(window, text="C33", font="Courier 10 bold", fg='black', bg=mycolor)
label.place(x=8, y=470)
label= Label(window, text="C34", font="Courier 10 bold", fg='black', bg=mycolor)
label.place(x=8, y=500)
label= Label(window, text="C35", font="Courier 10 bold", fg='black', bg=mycolor)
label.place(x=8, y=530)
label= Label(window, text="C36", font="Courier 10 bold", fg='black', bg=mycolor)
label.place(x=8, y=560)

label= Label(window, text="C41", font="Courier 10 bold", fg='black', bg=mycolor)
label.place(x=108, y=50)
label= Label(window, text="C42", font="Courier 10 bold", fg='black', bg=mycolor)
label.place(x=108, y=80)
label= Label(window, text="C43", font="Courier 10 bold", fg='black', bg=mycolor)
label.place(x=108, y=110)
label= Label(window, text="C44", font="Courier 10 bold", fg='black', bg=mycolor)
label.place(x=108, y=140)
label= Label(window, text="C45", font="Courier 10 bold", fg='black', bg=mycolor)
label.place(x=108, y=170)
label= Label(window, text="C46", font="Courier 10 bold", fg='black', bg=mycolor)
label.place(x=108, y=200)
label= Label(window, text="C51", font="Courier 10 bold", fg='black', bg=mycolor)
label.place(x=108, y=230)
label= Label(window, text="C52", font="Courier 10 bold", fg='black', bg=mycolor)
label.place(x=108, y=260)
label= Label(window, text="C53", font="Courier 10 bold", fg='black', bg=mycolor)
label.place(x=108, y=290)
label= Label(window, text="C54", font="Courier 10 bold", fg='black', bg=mycolor)
label.place(x=108, y=320)
label= Label(window, text="C55", font="Courier 10 bold", fg='black', bg=mycolor)
label.place(x=108, y=350)
label= Label(window, text="C56", font="Courier 10 bold", fg='black', bg=mycolor)
label.place(x=108, y=380)
label= Label(window, text="C61", font="Courier 10 bold", fg='black', bg=mycolor)
label.place(x=108, y=410)
label= Label(window, text="C62", font="Courier 10 bold", fg='black', bg=mycolor)
label.place(x=108, y=440)
label= Label(window, text="C63", font="Courier 10 bold", fg='black', bg=mycolor)
label.place(x=108, y=470)
label= Label(window, text="C64", font="Courier 10 bold", fg='black', bg=mycolor)
label.place(x=108, y=500)
label= Label(window, text="C65", font="Courier 10 bold", fg='black', bg=mycolor)
label.place(x=108, y=530)
label= Label(window, text="C66", font="Courier 10 bold", fg='black', bg=mycolor)
label.place(x=108, y=560)

# Result Tags
labelvbm= Label(window, text="Voight Bulk Modulus(GPa)", font="Courier 10 bold", fg='black', bg=mycolor)
labelvbm.place(x=300, y=360)
vbm = Label(text= "0.0", font="Courier 10", fg='black', bg=mycolor)
vbm.place(x=550, y=360)

labelrbm= Label(window, text="Reuss Bulk Modulus(GPa)", font="Courier 10 bold", fg='black', bg=mycolor)
labelrbm.place(x=300, y=390)
rbm = Label(text= "0.0", font="Courier 10", fg='black', bg=mycolor)
rbm.place(x=550, y=390)

labelvrh= Label(window, text="Bulk Modulus VRH Average(GPa)", font="Courier 10 bold", fg='black', bg=mycolor)
labelvrh.place(x=300, y=420)
vrhb = Label(text= "0.0", font="Courier 10", fg='black', bg=mycolor)
vrhb.place(x=550, y=420)

labelvsm= Label(window, text="Voight Shear Modulus(GPa)", font="Courier 10 bold", fg='black', bg=mycolor)
labelvsm.place(x=300, y=450)
vsm = Label(text= "0.0", font="Courier 10", fg='black', bg=mycolor)
vsm.place(x=550, y=450)

labelrsm= Label(window, text="Reuss Shear Modulus(GPa)", font="Courier 10 bold", fg='black', bg=mycolor)
labelrsm.place(x=300, y=480)
rsm = Label(text= "0.0", font="Courier 10", fg='black', bg=mycolor)
rsm.place(x=550, y=480)

labelvrhs= Label(window, text="Shear Modulus VRH Average(GPa)", font="Courier 10 bold", fg='black', bg=mycolor)
labelvrhs.place(x=700, y=360)
vrhs = Label(text= "0.0", font="Courier 10", fg='black', bg=mycolor)
vrhs.place(x=960, y=360)

labelym= Label(window, text="Young Modulus(GPa)", font="Courier 10 bold", fg='black', bg=mycolor)
labelym.place(x=700, y=390)
ym = Label(text= "0.0", font="Courier 10", fg='black', bg=mycolor)
ym.place(x=960, y=390)

labelpr= Label(window, text="Poisson Ratio", font="Courier 10 bold", fg='black', bg=mycolor)
labelpr.place(x=700, y=420)
pr = Label(text= "0.0", font="Courier 10", fg='black', bg=mycolor)
pr.place(x=960, y=420)

labelfc= Label(window, text="Flexibility Coefficient", font="Courier 10 bold", fg='black', bg=mycolor)
labelfc.place(x=700, y=450)
fc = Label(text= "0.0", font="Courier 10", fg='black', bg=mycolor)
fc.place(x=960, y=450)

# Other Tags
label1 = Label(window, text="Elastic Stiffness Tensor \nComponents(GPa)", bg=mycolor, font="Courier 11 bold", fg="black")
label1.place(x=8, y=5)

label2 = Label(window, text="Elastic Stiffness Tensor (GPa)", bg=mycolor, font="Courier 11 bold", fg="black")
label2.place(x=300, y=5)

label3 = Label(window, text="Elastic Compliance Modulus (1/GPa)", bg=mycolor, font="Courier 11 bold", fg="black")
label3.place(x=300, y=200)

label4 = Label(window, text="Cij", bg=mycolor, font="Courier 11 bold", fg="black")
label4.place(x=250, y=90)

label5 = Label(window, text="Sij", bg=mycolor, font="Courier 11 bold", fg="black")
label5.place(x=250, y=280)

# Button for information and communication
def infoopen():
    my_w_child = Toplevel()
    my_w_child.geometry("300x100")  # Size of the window
    my_w_child.title("info")
    my_w_childlabel1 = Label(my_w_child, text="Mehmet Erzen & Harun Akku??  \nmerzennn@gmail.com\nphysicisthakkus@gmail.com", font="Courier 11 bold",
                   fg="black")
    my_w_childlabel1.place(x=8, y=5)

# Button to reset the program
def refresh(self):
    self.destroy()
    os.system('python Elasticity.py')

window.mainloop()


