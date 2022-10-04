import turtle
import time
print("欢迎来到这个游戏！")
turtle.pensize(100090)
turtle.penup()
turtle.write("温馨提示，本游戏有一些是在Pyhon_shell中实现，请注意您的Pyhon_shell","simsun")
turtle.hideturtle()
start_tips=int(turtle.numinput("温馨提示","温馨提示，本游戏有一些是在Pyhon_shell中实现，请注意您的Pyhon_shell。(输入1即可)1.一 2.二"))
start_recharge=int(turtle.numinput("充值入口","请问你要充值吗？1.是的 2.坚决不冲"))
if start_recharge==1:
    start_recharge_pay=int(turtle.numinput("确认订单","请问您是微信还是支付宝？1.微信 2.支付宝"))
    print("充值成功！您已获得1000000000000000金币，代价是你的信用卡被刷爆了")
elif start_recharge==2:
    print("你有三秒钟决定是否充值")
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    start_forced_recharge_pay=int(turtle.numinput("游戏","冲还是不冲？1.冲 2.不冲"))
    if start_forced_recharge_pay==1:
        print("充值成功！")
    elif start_forced_recharge_pay==2:
        print("鬼！")
        turtle.clear()
        turtle.write("游戏结束","simsun")
