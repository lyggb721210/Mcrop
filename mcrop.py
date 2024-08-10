"""
这是一个在Python上运行的迷宫挑战游戏
This is a maze challenge game on Python.
Email 邮箱：lyggb721210@163.com
Author 作者：lygyxr / lyggb721210 / yxr
Version 当前版本：V1.1
Please report any bugs to the author.
如果有BUG请报告给作者。
"""

import json
import map
# import language as l
import os
import time

from colorama import init

init()


def clear(system):
    if system == "posix":
        os.system("clear")
    elif system == "nt":
        os.system("cls")


def choose_language_file():
    clear(os.name)
    while True:
        print("请选择您要使用的语言 Please select the language you want to use:")
        files = os.listdir("./lang")
        for i in files:
            print(i)
        print("请输入前面序号。Please enter the preceding serial number.")
        _language = (input())
        try:
            _a = int(_language) - 1
            if _a <= len(files):
                return "./lang/" + files[_a]
        except ValueError:
            pass


if __name__ == "__main__":
    # 检查存档
    if os.path.exists("save.txt"):
        try:
            f = open("save.txt", "r")
            save = f.readlines()

            if 2.2 > float(save[0][0:3]) >= 2:
                # if len(save) >= 5 and float(save[0][0:4]) >= 2.12:
                lang_file = save[4][0:-2]
                message = json.load(open(lang_file, "r"))
                print(message.get("menu"))
                lever = int(save[2][0:2])
                print(message.get("go_on_game"))
                print(message.get("clean_save"))
            else:
                lang_file = choose_language_file()
                message = json.load(open(lang_file, "r"))
                print(message.get("welcome"))
                print(message.get("menu"))
                lever = 0
                print(message.get("save_load_err1"))
            f.close()
        except:
            lang_file = choose_language_file()
            message = json.load(open(lang_file, "r"))
            print(message.get("menu"))
            lever = 0
            print(message.get("save_load_err1"))
    else:
        lang_file = choose_language_file()
        message = json.load(open(lang_file, "r"))
        print(message.get("menu"))

    last_print = "  "
    a = input("")
    if a == "1":
        lever = 0
        in_map = map.get_map(lever)
    if a == "3":
        if not ("lever" in dir()):
            # print(message.get("3error"))
            exit()
        else:
            if lever >= len(map.map) - 1:
                print(message["end"])
                exit()
            in_map = map.get_map(lever=lever)
    if a == "1" or a == "3":
        while True:
            print(message["check_autosafe"], end='')
            q = input()
            if q == "y" or q == "Y" or q == "":
                auto_save = True
                break
            elif q == "N" or q == "n":
                auto_save = False
                break
        # 游戏开始
        time1 = time.time()
        while True:
            clear(os.name)
            c = 0
            outmap = ""
            while c != len(in_map):
                outmap = outmap + in_map[c]
                c = c + 1
            print(outmap)
            print(last_print)
            print(message.get("in_game"))
            b = input("")
            if b == "w" or b == "W":
                add = in_map.index(map.user)
                acd = add - in_map.index("\n") - 1
            elif b == "a" or b == "A":
                add = in_map.index(map.user)
                acd = add - 1
            elif b == "d" or b == "D":
                add = in_map.index(map.user)
                acd = add + 1
            elif b == "s" or b == "S":
                add = in_map.index(map.user)
                acd = add + in_map.index("\n") + 1
            else:
                last_print = message["err"]
                continue
            if acd <= 0:
                last_print = message["hit_wall"]
            elif acd > 0:
                if in_map[acd] == map.wall:
                    last_print = message["hit_wall"]
                elif in_map[acd] == map.road:
                    last_print = "  "
                    in_map[add] = map.road
                    in_map[acd] = map.user
                elif in_map[acd] == map.door:
                    cost_time = round(time.time() - time1, 2)
                    while True:
                        clear(os.name)
                        print(
                            message.get("lever_end"), end=""
                        )
                        print(str(cost_time) + "s")
                        if auto_save:
                            f = open("save.txt", "w")
                            print(
                                "2.13",
                                "这是一个存档文件（McroP）。  This is a save file for McroP",
                                str(lever + 1),
                                time.asctime(),
                                lang_file,
                                sep="\n",
                                end="",
                                file=f,
                            )
                            f.close()
                            print(
                                message["autosafed"])
                        a = input("")
                        clear(os.name)
                        if a == "1":
                            if lever < len(map.map) - 1:
                                lever = lever + 1
                                in_map = map.get_map(lever)
                                time1 = time.time()
                                break
                            elif lever >= len(map.map) - 1:
                                print(message["end"])
                                exit()
                        elif a == "2":
                            exit()
    elif a == "2":
        print(message.get("help"))
        input()
    elif a == "4":
        if not os.path.exists("save.txt"):
            exit()
        os.remove("save.txt")
    # else:
    # print(message.get("input_err"))
