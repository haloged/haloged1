from tkinter import *


class daikuanCalc(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack()

        self.yearsVar = StringVar()  # 贷款年限
        self.amountVar = StringVar()  # 贷款金额
        self.rateVar = StringVar()  # 贷款利率
        self.total1Var = StringVar()  # 总还款额
        self.totalInterest1Var = StringVar()  # 总利息额
        self.monthRepay = StringVar()  # 月均还款

        Label(self, text="").grid(row=0, column=0, columnspan=6)
        Label(self, text="还款方式", font=('楷体', 15), height=2).grid(row=1, column=0, columnspan=3, rowspan=2)
        Label(self, text=":", font=('楷体', 15)).grid(row=1, column=3, rowspan=2)
        Label(self, text="贷款年限", font=('楷体', 15), height=2).grid(row=3, column=0, columnspan=3, rowspan=2)
        Label(self, text="(年):", font=('楷体', 15)).grid(row=3, column=3, rowspan=2)
        Label(self, text="贷款金额", font=('楷体', 15), height=2).grid(row=5, column=0, columnspan=3, rowspan=2)
        Label(self, text="(万元):", font=('楷体', 15)).grid(row=5, column=3, rowspan=2)
        Label(self, text="贷款利率", font=('楷体', 15), height=2).grid(row=7, column=0, columnspan=3, rowspan=2)
        Label(self, text="(%):", font=('楷体', 15)).grid(row=7, column=3, rowspan=2)
        Label(self, text="月均还款", font=('楷体', 15)).grid(row=11, column=0, columnspan=3, rowspan=2)
        Label(self, text="(元):", font=('楷体', 15), height=2).grid(row=11, column=3, rowspan=2)
        Label(self, text="利息总额", font=('楷体', 15)).grid(row=13, column=0, columnspan=3, rowspan=2)
        Label(self, text="(元):", font=('楷体', 15), height=2).grid(row=13, column=3, rowspan=2)
        Label(self, text="还款总额", font=('楷体', 15)).grid(row=15, column=0, columnspan=3, rowspan=2)
        Label(self, text="(元):", font=('楷体', 15), height=2).grid(row=15, column=3, rowspan=2)

        Entry(self, textvariable=self.yearsVar).grid(row=3, column=4, columnspan=5, rowspan=2)
        Entry(self, textvariable=self.amountVar).grid(row=5, column=4, columnspan=5, rowspan=2)
        Entry(self, textvariable=self.rateVar).grid(row=7, column=4, columnspan=5, rowspan=2)
        Entry(self, textvariable=self.monthRepay).grid(row=11, column=4, columnspan=5, rowspan=2)
        Entry(self, textvariable=self.totalInterest1Var).grid(row=13, column=4, columnspan=5, rowspan=2)
        Entry(self, textvariable=self.total1Var).grid(row=15, column=4, columnspan=5, rowspan=2)

        val = IntVar()  # 获取单选按钮的值
        val.set(0)

        r0 = Radiobutton(self, text='等额本息', font=('楷体', 15), variable=val, value=0, height=2)
        r0.grid(row=1, column=4, columnspan=3)
        r1 = Radiobutton(self, text='等额本金', font=('楷体', 15), variable=val, value=1, height=2)
        r1.grid(row=1, column=7, columnspan=3)

        def cmd():
            if val.get() == 0:
                # 获取输入的参数

                years = eval(self.yearsVar.get())  # 贷款年限
                amount = eval(self.amountVar.get())  # 贷款本金
                rate = eval(self.rateVar.get()) / 100 / 12  # 将年化利率转为月利率，单位为1

                # 计算每月还款
                monthRepayment = (amount * rate * ((1 + rate) ** (years * 12))) / ((1.0 + rate) ** (years * 12) - 1.0)

                # 显示计算结果
                total = monthRepayment * 12 * years  # 总还款金额
                self.total1Var.set(format(total, ".3f"))
                self.monthRepay.set(format(monthRepayment, '.3f'))

                totalInterest = total - amount  # 总利息
                self.totalInterest1Var.set(format(totalInterest, '.3f'))

            else:

                # 获取输入的参数
                years = eval(self.yearsVar.get())  # 贷款年限
                amount = eval(self.amountVar.get())  # 贷款本金
                rate = eval(self.rateVar.get()) / 100 / 12  # 将年化利率转为月利率，单位为1
                month_amount = amount / (years * 12)

                # 储存月均还款
                monthRepayment = []
                for i in range(1, (years * 12) + 1):
                    monthpayment = month_amount + (amount - (i - 1) * month_amount) * rate
                    monthRepayment.append(monthpayment)

                # 显示结果
                total = sum(monthRepayment)
                self.total1Var.set(format(total, ".3f"))
                self.monthRepay.set(format(total / (years * 12), '.3f'))

                totalInterest = total - amount
                self.totalInterest1Var.set(format(totalInterest, '.3f'))

        def clear():  # 重新计算时清空
            self.yearsVar.set('')
            self.amountVar.set('')
            self.rateVar.set('')
            self.total1Var.set('')
            self.totalInterest1Var.set('')
            self.monthRepay.set('')

        Button(self, text='计 算', font=('楷体', 15), width='10', command=cmd).grid(row=9, column=3, rowspan=2)
        Button(self, text='重新计算', font=('楷体', 15), width='10', command=clear).grid(row=9, column=5, columnspan=3,
                                                                                   rowspan=2)


if __name__ == '__main__':
    app = Tk()
    app.title('贷款计算器')
    app.resizable(0, 0)
    apps = daikuanCalc(app)
    app.resizable(0, 0)
    app.mainloop()
