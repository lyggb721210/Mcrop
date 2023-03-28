#coding=utf-8
"""
这是作者的第2个python程序若有问题请见谅
有BUG可联系作者
邮箱：lyggb721210@163.com
作者：yxr / 栗子味东方
当前版本：V1.23

This is the author's second python program. If there is any problem, please forgive me
The author can be contacted if there is a bug
Email: lyggb721210@163.com
Author: yxr/栗子味东方/lyggb721210
Current version: V1.23
"""
import turtle
print("欢迎使用")
#以下为地图部分
import map
nmber = 0
inmap = map.inmap[nmber]
#特殊字符（□，■）
print("1.新游戏 New Game.\n2.帮助 Help.")
lastprint = "  "
print("请输入前面序号 Please enter the front serial number.")
a = input("")
if a == "1":
    while 1 == 1:
        c = 0
        outmap = ""
        while c != len(inmap):
            outmap = outmap + inmap[c]
            c = c + 1
        print(outmap)
        print(lastprint)
        print("请输入w,a,s,d. Please enter w, a, s, d.")
        b = input("")
        if b == "w":
            add = inmap.index("😊")
            acd = add - inmap.index("\n") - 1
        elif b == "a":
            add = inmap.index("😊")
            acd = add - 1
        elif b == "d":
            add = inmap.index("😊")
            acd = add + 1
        elif b == "s":
            add = inmap.index("😊")
            acd = add + inmap.index("\n") + 1
        else:
            lastprint = "请输入w,a,s,d(上,左,下,右) Please enter w, a, s, d (top, left, bottom, right)."
            continue
        if acd <= 0:
            lastprint = "啊，碰墙了 Ah, I hit the wall."
        elif acd > 0:
            if inmap[acd] == "■":
                lastprint = "啊，碰墙了 Ah, I hit the wall."
            elif inmap[acd] == "□":
                lastprint = "  "
                inmap[add] = "□"
                inmap[acd] = "😊"
            elif inmap[acd] == "🚪":
                print("成功通关! Successful customs clearance!")
                print("1.下一关 Next level.")
                print("2.退出 Exit.")
                print("请输入前面序号 Please enter the front serial number.")
                a = input()
                if a == "1":
                    if nmber < len(inmap):
                        nmber = nmber + 1
                        inmap = map.inmap[nmber]
                    elif nmber >= len(inmap):
                        print("关卡已结束 The level has ended.")
                        exit()
                elif a == "2":
                    exit()
elif a == 2:
    print("这是一个地图闯关游戏 This is a map breaking game .\n")
    print("在游戏中可以输入w,a,s,d来控制😊的移动 \n In the game, you can enter w, a, s, and d to control 😊 's movement")
    print("(输入后要按enter表示确定) (After input, press enter to confirm)\n")
    print("'■'是墙，'□'是空地。 '■' is a wall, '□' is an open space.")
    print("祝您游玩愉快 Have a good time.")
else:
    print("请输入正确的数字 Please enter the correct number.")