#导入库
import tkinter as tk


username=tk.StringVar()
password=tk.StringVar()

#定义
root=tk.Tk()
root.geometry('300x180')
root.title("登录")
page=tk.Frame(root)
page.pack()


#登录页：

#空行
tk.Label(page).grid(row=0,column=0)



#账户
tk.Label(page,text="账户：").grid(row=1,column=1)
tk.Entry(page,textvariable=username).grid(row=1,column=2)




#定义login函数
def login():
    name=username.get()
    pwd=password.get()
    print(name,pwd)






#密码
tk.Label(page,text="密码：").grid(row=2,column=1,pady=10)
tk.Entry(page,textvariable=password).grid(row=2,column=2)



#下方按钮
tk.Button(page,text='登录',command=login).grid(row=3,column=1,pady=10)
tk.Button(page,text='退出',command=quit).grid(row=3,column=2)
root.mainloop()
