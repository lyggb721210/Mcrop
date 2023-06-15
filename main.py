#-*-coding:utf8;-*-
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

import map
import language as l
import os


def clear(system):
    if system == "posix":
        os.system("clear")
    elif system == "nt":
        os.system("cls")


# end def

if __name__ == "__main__":
    if os.path.exists("save.txt"):
        f = open("save.txt", "r")
        save = f.readlines()
        if float(save[0][0:3]) >= 2:
            l.display_message(l.message.get("menu"), l.language)
            lever = 0
            if l.language == 1:
                print("err:存档加载错误")
            else:
                print("err:Archive loading error")

        elif float(save[0][0:3]) < 2:
            l.display_message(l.message.get("menu"), l.language)
            lever =int(save[1][0:2])
            if l.language == "1":
                print(" 3.继续游戏")
            else:
                print(" 3.Continue the game")
    else:
        l.display_message(l.message.get("menu"), l.language)

    lastprint = "  "
    a = input("")
    if a== "1" :
        lever=0
    inmap=map.map[lever]
    while True:
        if l.language=="1":
            q=input("是否启用自动保存？[Y/n]")
        else:
            q=input("Whether to enable automatic save？[Y/n]")
        if q=="y" or "Y" or "":
            autosave=True
            break
        elif q=="N" or "n":
            autosave=False
            break
    if a == "1" or "2":
        while True:
            clear(os.name)
            c = 0
            outmap = ""
            while c != len(inmap):
                outmap = outmap + inmap[c]
                c = c + 1
            print(outmap)
            print(lastprint)
            l.display_message(l.message.get("in_game"), l.language)
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
                lastprint = l.get_message("err").get(l.language)
                continue
            if acd <= 0:
                lastprint = l.get_message("hit_wall").get(l.language)
            elif acd > 0:
                if inmap[acd] == "🧱":
                    lastprint = l.get_message("hit_wall").get(l.language)
                elif inmap[acd] == "🔲":
                    lastprint = "  "
                    inmap[add] = "🔲"
                    inmap[acd] = "😊"
                elif inmap[acd] == "🚪":
                    while True:
                        clear(os.name)
                        l.display_message(l.message.get("lever_end"), l.language)
                        if autosave :
                            f=open("save.txt","w")
                            f.writelines(["1.0\n",str(lever)])
                        if l.language=='1':
                            print('已自动保存')
                        else:
                            print("Automatically saved")
                        a = input()
                        clear(os.name)
                        if a == "1":
                            if lever < len(map.inmap) - 1:
                                lever = lever + 1
                                inmap = map.map[lever]
                                break
                            elif lever >= len(map.map) - 1:
                                l.display_message(l.message.get("end"), l.language)
                                exit()
                        elif a == "2":
                            exit()
    elif a == "2":
        l.display_message(l.message.get("help"), l.language)
    else:
        l.display_message(l.message.get("input_err"), l.language)
