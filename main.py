# coding=utf-8
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

if __name__ == '__main__':
    lever = 0
    inmap = map.inmap[lever]
    l.display_message(l.message.get("menu"), l.language)
    lastprint = "  "
    a = input("")
    if a == "1":
        while True :    
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
                        a = input()
                        clear(os.name)
                        if a == "1":
                            if lever < len(map.inmap)-1:
                                lever = lever + 1
                                inmap = map.inmap[lever]
                                break
                            elif lever >= len(map.inmap)-1:
                                l.display_message(l.message.get("end"), l.language)
                                exit()
                        elif a == "2":
                            exit()
    elif a == "2":
        l.display_message(l.message.get("help"), l.language)
    else:
        l.display_message(l.message.get("input_err"), l.language)
