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


def clear_text():
    clear_text = None
    clear_type = None
    try:
        os.system("cls")
        clear_text = True
        clear_type = "cls"
    except:
        clear_text = False
    if clear_text == False:
        try:
            os.system("clear")
            clear_text = True
            clear_type = "clear"
        except:
            clear_text = False
    return clear_text, clear_type


def clear(clear_result):
    if clear_result[1]:
        os.system(clear_result)
# end def


def main():
    clear_result = clear_text()
    nmber = 0
    inmap = map.inmap[nmber]
    l.display_message(l.message.get("menu"), l.language)
    lastprint = "  "
    a = input("")
    if a == "1":
        while True:
            clear(clear_result)
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
                if inmap[acd] == "■":
                    lastprint = l.get_message("hit_wall").get(l.language)
                elif inmap[acd] == "□":
                    lastprint = "  "
                    inmap[add] = "□"
                    inmap[acd] = "😊"
                elif inmap[acd] == "🚪":
                    while True:
                        l.display_message(l.message.get(
                            "lever_end"), l.language)
                        a = input()
                        clear(clear_result)
                        if a == "1":
                            if nmber < len(inmap):
                                nmber = nmber + 1
                                inmap = map.inmap[nmber]
                                break
                            elif nmber >= len(inmap):
                                l.display_message(
                                    l.message.get("end"), l.language)
                                exit()
                        elif a == "2":
                            exit()
    elif a == "2":
        l.display_message(l.message.get("help"), l.language)
    else:
        l.display_message(l.message.get("input_err"), l.language)


if __name__ == '__main__':
    main()
