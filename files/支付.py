import time
mon = 1000
while True:
    print('欢迎来到haloged支付')
    print('1.支付')
    print('2.余额')
    print('3.收款码')
    print('4.关于软件')
    print('5.退出')
    print('每周四是haloged支付的会员日，享8折优惠哦！')
    start = int(input('我是您的私人管家，请问有什么可以帮您？'))
    if (start == 1):
        print('正在加载中......')
        time.sleep(2)
        print('加载成功！')
        vip = input('请问您有没有haloged会员？y/n')
        if (vip == 'y' or vip == 'Y'):
            week = input('今天是星期几？[纯数字]')
            if (week == 4):
                commodity1 = int(input('请输入第一个商品的价格：[数字带小数点][每次只能支付三个商品]'))
                commodity2 = int(input('请输入第二个商品的价格：[数字带小数点][每次只能支付三个商品]'))
                commodity3 = int(input('请输入第三个商品的价格：[数字带小数点][每次只能支付三个商品]'))
                money = (commodity1 + (commodity2 + commodity3 * 0.8))
                print('一共是',money,'元')
                allow = input('是否支付？y/n')
                if (allow == 'y' or allow == 'Y'):
                    if (mon >= money):
                        mon = (mon + money)
                        print('支付成功！')
                        continue
                    else :
                        print('余额不足')
                elif (allow == 'n' or allow == 'N') :
                    continue
                else :
                    print('输入错误')
            else :
                commodity21 = int(input('请输入第一个商品的价格：[数字带小数点][每次只能支付三个商品]'))
                commodity22 = int(input('请输入第二个商品的价格：[数字带小数点][每次只能支付三个商品]'))
                commodity23 = int(input('请输入第三个商品的价格：[数字带小数点][每次只能支付三个商品]'))
                money2 = (commodity21 + (commodity22 + commodity23))
                print('一共是',money2,'元')
                allow2 = input('是否支付？y/n')
                if (allow2 == 'y' or allow2 == 'Y'):
                    if (mon >= money2):
                        mon = (mon + money2)
                        print('支付成功！')
                        continue
                    else :
                        print('余额不足')
                elif (allow == 'n' or allow == 'N') :
                    continue
                else :
                    print('输入错误')
        elif (vip == 'N' or vip == 'n') :
            commodity31 = int(input('请输入第一个商品的价格：[数字带小数点][每次只能支付三个商品]'))
            commodity32 = int(input('请输入第二个商品的价格：[数字带小数点][每次只能支付三个商品]'))
            commodity33 = int(input('请输入第三个商品的价格：[数字带小数点][每次只能支付三个商品]'))
            money3 = (commodity31 + (commodity32 + commodity33))
            print('一共是',money3,'元')
            allow3 = input('是否支付？y/n')
            if (allow3 == 'y' or allow3 == 'Y'):
                if (mon >= money3):
                    mon = (mon + money3)
                    print('支付成功！')
                    continue
                else :
                    print('余额不足')
            elif (allow == 'n' or allow == 'N') :
                continue
            else :
                print('输入错误')
        else :
            print('输入错误')
            continue
    elif (start == 2) :
        print('正在加载中......')
        time.sleep(2)
        print('您的余额是',mon,'元')
        recharge = input('是否充值？y/n')
        if (recharge == 'y' or recharge == 'Y'):
            much = int(input('充多少？'))
            mon = (mon + much)
            print('正在充值......')
            time.sleep(2)
            print('充值成功！')
            continue
        else :
            continue
    elif (start == 3) :
        print('正在加载中......')
        time.sleep(2)
        print('功能开发中，敬请期待！')
        continue
    elif (start == 4) :
        print('正在加载中......')
        time.sleep(2)
        print('关于软件')
        print('软件作者：谨慎的熔岩龙Ef_m')
        print('作者B站主页：https://space.bilibili.com/518055250')
        print('作者编程猫主页：https://shequ.codemao.cn/user/493919874')
        print('软件版本：v0.0.1')
        print('更新日志请查看https://www.yuque.com/haloged/uw43rd/ewk9gi')
        continue
    elif (start == 5) :
        signout = input('是否退出？')
        if (signout == 'y' or signout == 'Y'):
            break
        elif (signout == 'n' or signout == 'N') :
            continue
        else :
            print('输入错误')
    else :
        print('输入错误')
