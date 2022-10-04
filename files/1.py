from tkinter import *
from tkinter.scrolledtext import ScrolledText
def Shielding(content):
    return b'\xe2\x80\xaa'.decode(
        'UTF-8').join([i for i in content])


def _write():
    st2['state'] = NORMAL
    st2.delete(0.0, "end")
    print(st.get('0.0', 'end'))
    print(Shielding(st.get('0.0', 'end')))
    st2.insert(0.0, Shielding(st.get('0.0', 'end')))
    st2['state'] = DISABLED
def copy():
    st2['state'] = NORMAL
    st2.event_generate('<<Copy>>')
    st2['state'] = DISABLED

def main():
    win = Tk()
    win.title('防喵工具')
    win.resizable(width=False, height=False)
    win.wm_attributes('-topmost', 0)
    Label(win, text='内\n容', font=(10)).grid(row=0, column=0, rowspan=3)
    st = ScrolledText(win, height=10,width=20)
    st.grid(row=0, column=1, columnspan=3, rowspan=3)
    Label(win, text='转\n换', font=(10)).grid(row=4, column=0, rowspan=3)
    st2 = ScrolledText(win, height=10, width=20, state=DISABLED)
    st2.grid(row=4, column=1, columnspan=3, rowspan=3)


    Button(win, text='转换', command=_write, width=10,
        height=6).grid(row=0, column=5, rowspan=4)

    Button(win, text='复制 选中状态', command=copy, width=10,
        height=3).grid(row=5, column=5, rowspan=1)
    Button(win, text='退出', command=exit, width=10,
        height=3).grid(row=6, column=5, rowspan=1)

    mainloop()
    #print(Shielding(input()))
if __name__=='__main__':
    main()
