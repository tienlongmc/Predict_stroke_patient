import tkinter
from tkinter import ttk#GUI
from tkinter import messagebox
from tkinter import *
#Thêm các thư viện để xử lí
import  tkinter as tk
from tkinter import messagebox
import numpy as np #numpy để tính toán giá trị cho ma trận và mảng
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
import pandas as pd
from scipy.sparse import coo_matrix
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

from sklearn.metrics import accuracy_score
import scipy.io as sio
import os
import openpyxl

window = tkinter.Tk()
window.title("Dự đoán nguy cơ bị đột quỵ")
#window.geometry("1000x900")
frame = tkinter.Frame(window)
frame.pack(padx=20, pady=10)

user_info_frame = tkinter.LabelFrame(frame, text="Thông tin")
user_info_frame.grid(row=0, column=0, padx=20, pady=10)
Name = StringVar()

first_name_label = tkinter.Label(user_info_frame, text="Tên")
first_name_label.grid(row=0, column=0)
#Khai báo các biến thông tin nhập giá trị input
Glu_level = DoubleVar()
Bmi = DoubleVar()

last_name_label = tkinter.Label(user_info_frame, text="Chỉ số BMI")
last_name_label.grid(row=0, column=1)
bmi_spinbox = tkinter.Spinbox(user_info_frame, from_=0.0, to=500, increment=0.5, textvariable=Bmi)

title_label = tkinter.Label(user_info_frame, text="Lượng đường trong máu")
#title_combobox = ttk.Combobox(user_info_frame, values=["", "Mr.", "Ms.", "Dr."])
title_label.grid(row=0, column=2)
duong_spinbox = tkinter.Spinbox(user_info_frame, from_=0.0, to=500, increment=0.5, textvariable=Glu_level)

first_name_entry = tkinter.Entry(user_info_frame, textvariable=Name)
first_name_entry.grid(row=1, column=0)
bmi_spinbox.grid(row=1, column=1)
duong_spinbox.grid(row=1, column=2)

Age = IntVar()
age_label = tkinter.Label(user_info_frame, text="Tuổi")
age_spinbox = tkinter.Spinbox(user_info_frame, from_=0, to=110, textvariable=Age)
age_label.grid(row=2, column=0)
age_spinbox.grid(row=3, column=0)

Sex=IntVar()
nationality_label = tkinter.Label(user_info_frame, text="Giới tính")
nationality_label.grid(row=2, column=1)
nam = ttk.Radiobutton(user_info_frame, text="Nam", variable=Sex, value=0)
nam.grid(row=3, column=1)
nu = ttk.Radiobutton(user_info_frame, text="Nữ", variable=Sex, value=1)
nu.grid(row=3, column=2)

#nationality_combobox = ttk.Combobox(user_info_frame, values=["Africa", "Antarctica", "Asia"])
#nationality_combobox.grid(row=3, column=1)
Age=IntVar()
age_label = tkinter.Label(user_info_frame, text="Tuổi")
age_spinbox = tkinter.Spinbox(user_info_frame, from_=0, to=110, textvariable=Age)
age_label.grid(row=2, column=0)
age_spinbox.grid(row=3, column=0)

Sex=IntVar()
nationality_label = tkinter.Label(user_info_frame, text="Giới tính")
nationality_label.grid(row=2, column=1)
nam = ttk.Radiobutton(user_info_frame, text="Nam", variable=Sex, value=0)
nam.grid(row=3, column=1)
nu = ttk.Radiobutton(user_info_frame, text="Nữ", variable=Sex, value=1)
nu.grid(row=3, column=2)

#nationality_combobox = ttk.Combobox(user_info_frame, values=["Africa", "Antarctica", "Asia"])
#nationality_combobox.grid(row=3, column=1)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

courses_frame=tkinter.LabelFrame(frame, text="Tình trạng")
courses_frame.grid(row=1, column=0, sticky="news", padx=20, pady=30)
Hypertension=IntVar()

huyetap_label = tkinter.Label(courses_frame, text="Có bị cao huyết áp?")
huyetap_label.grid(row=1, column=0)
co = ttk.Radiobutton(courses_frame, text="có", variable=Hypertension, value=1)
co.grid(row=2, column=0)
khong = ttk.Radiobutton(courses_frame, text="không", variable=Hypertension, value=0)
khong.grid(row=2, column=1)
Heart=IntVar()

tim1_label = tkinter.Label(courses_frame, text="Chọn câu trả lời")
tim1_label.grid(row=0, column=3)
tim2_label = tkinter.Label(courses_frame, text="Có bị bệnh tim?")
tim2_label.grid(row=1, column=5)
coo = ttk.Radiobutton(courses_frame, text="có", variable=Heart, value=1)
coo.grid(row=2, column=4)
khongg = ttk.Radiobutton(courses_frame, text="không", variable=Heart, value=0)
khongg.grid(row=2, column=5)
Smokes=IntVar()
thuoc_label = tkinter.Label(courses_frame, text="Có hút thuốc?")
thuoc_label.grid(row=3, column=0)
thuocc = ttk.Radiobutton(courses_frame, text="có", variable=Smokes, value=1)
thuocc.grid(row=4, column=0)
thuock = ttk.Radiobutton(courses_frame, text="không", variable=Smokes, value=0)
thuock.grid(row=4, column=1)

marry=IntVar()
keth_label = tkinter.Label(courses_frame, text="Tình trạng hôn nhân?")
keth_label.grid(row=3, column=5)
kethco = ttk.Radiobutton(courses_frame, text="có", variable=marry, value=1)
kethco.grid(row=4, column=4)
kethk = ttk.Radiobutton(courses_frame, text="không", variable=marry, value=0)
kethk.grid(row=4, column=5)

#Truyền data vào 2 biến từ 2 tập dữ liệu với input là Train_x.txt và nhận cho tập dữ
file_x='Train_x.txt'
data=pd.read_csv(file_x,sep='\t')
#Chuyển data vừa đưa vào về dạng numpy.array
X = data.values
file_y='Train_y.txt'
data=pd.read_csv(file_y,sep='\t')
y=data.values.ravel()
print("hahaha" ,y.shape)

# y=y.reshape(299)
print(y)

file_x='Test_x.txt'
data=pd.read_csv(file_x,sep='\t')
#Chuyển data vừa đưa vào về dạng numpy.array
test_x = data.values

file_y='Test_y.txt'
data=pd.read_csv(file_y,sep='\t')
test_y=data.values
# test_y=test_y.reshape(29)
#Sử dụng thư viện trong sklearn để training cho tập vì dụ huấn luyện
pd= LogisticRegression(solver='lbfgs', max_iter=1000)
pd.fit(X,y)

# def getvalue():
#     Name = txt.get()
# Hàm predict để đưa dữ liệu vào
def predict():
    Sepb = float(Sex.get())
    Ages = float(Age.get())
    Hypertensions = float(Hypertension.get())
    Hearts = float(Heart.get())
    Glu_levels = float(Glu_level.get())
    Bmis = float(Bmi.get())
    Smokess = float(Smokes.get())
    #Hàm pd.predict để đưa ra nhận cho tập dữ liệu,giá trị trả về sẽ là 0 hoặc 1
    model = LogisticRegression()
    i2= pd.predict([[Sepb,Ages,Hypertensions,Hearts, Glu_levels,Bmis,Smokess]])

    #Hàm pd.predict để đưa ra nhận cho tập dữ liệu, giá trị trả về sẽ là 0 hoặc 1

    i2= pd.predict([[Sepb,Ages,Hypertensions,Hearts,Glu_levels,Bmis,Smokess]])
    probability= pd.predict_proba([[Sepb,Ages,Hypertensions,Hearts,Glu_levels,Bmis,Smokess]])
    pb=probability[0][1]
    pb=round(pb,4)
    i=i2
    if Ages == 0 or Glu_levels == 0 or Bmis == 0 :
        messagebox.showwarning("Chưa điền đủ dữ liệu","Mời bạn nhập đủ dữ liệu")
    else:
        if i>=1:
            i=1
            messagebox.showinfo("Dự đoán ", " Bạn có %.2f %% nguy cơ bị đột quỵ! \n " %(pb*100))
        else:
            i=0
            messagebox.showinfo("Dự đoán "," Chúc mừng!Bạn không có nguy cơ bị đột quỵ")

# Accept terms
terms_frame = tkinter.LabelFrame(frame, text="Xác nhận")
terms_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)

accept_var = tkinter.StringVar(value="Not Accepted")
terms_check = tkinter.Checkbutton(terms_frame, text="Tôi đồng ý và xác nhận. ",
                  variable=accept_var, onvalue="Accepted", offvalue="Not Accepted")

terms_check.grid(row=0, column=0)

Button
button = tkinter.Button(frame,text="Dự Đoán",command= predict,borderwidth=5,font=( 'Arial 20 bold'))
button.grid(column=0,row=3,padx=20, pady=10, sticky="news")

window.mainloop()