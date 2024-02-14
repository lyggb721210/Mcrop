# 邮箱：lyggb721210@163.com
# 作者：yxr / lyggb721210
# 当前版本：V0.91
# Email: lyggb721210@163.com
# Author: yxr / lyggb721210
# Version: V0.91


import map
import language as l
import os
import time


def clear(system):
    if system == "posix":
        os.system("clear")
    elif system == "nt":
        os.system("cls")


# end def

if __name__ == "__main__":
    # 检查存档
    if os.path.exists("save.txt"):
        try:
            f = open("save.txt", "r")
            save = f.readlines()
            if 2.2 <= float(save[0][0:3]) <= 2:
                l.language = l.choose_language()
                l.display_message(l.message.get("welcome"), l.language)
                l.display_message(l.message.get("menu"), l.language)
                lever = 0
                l.display_message(l.message.get("save_load_err1"), l.language)
            elif 2.2 > float(save[0][0:3]) >= 2:
                if len(save) >= 5 and float(save[0][0:4]) >= 2.12:
                    l.language = save[4][0:2]
                l.display_message(l.message.get("menu"), l.language)
                lever = int(save[2][0:2])
                l.display_message(l.message.get("go_on_game"), l.language)
                l.display_message(l.message.get("clean_save"), l.language)
            f.close()
        except:
            l.language = l.choose_language()
            l.display_message(l.message.get("menu"), l.language)
            lever = 0
            l.display_message(l.message.get("save_load_err1"), l.language)
    else:
        l.language = l.choose_language()
        l.display_message(l.message.get("menu"), l.language)

    last_print = "  "
    a = input("")
    if a == "1":
        lever = 0
        in_map = map.get_map(lever)
    if a == "1" or a == "3":
        while True:
            q = input(l.display_message(l.message.get("check_autosafe"), l.language))
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
            l.display_message(l.message.get("in_game"), l.language)
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
                last_print = l.get_message("err")[l.language]
                continue
            if acd <= 0:
                last_print = l.get_message("hit_wall")[l.language]
            elif acd > 0:
                if in_map[acd] == map.wall:
                    last_print = l.get_message("hit_wall")[l.language]
                elif in_map[acd] == map.road:
                    last_print = "  "
                    in_map[add] = map.road
                    in_map[acd] = map.user
                elif in_map[acd] == map.door:
                    cost_time = round(time.time() - time1, 2)
                    while True:
                        clear(os.name)
                        l.display_message(l.message.get("lever_end"), l.language)
                        print(" 用时：" + str(cost_time) + "s")
                        if auto_save:
                            f = open("save.txt", "w")
                            print("2.13",
                                  "这是一个存档文件（McroP）。  This is a save file for McroP",
                                  str(lever + 1),
                                  time.asctime(),
                                  l.language,
                                  sep="\n", end="", file=f)
                            f.close()
                            l.display_message(l.message["autosafed"], l.language)
                        a = input()
                        clear(os.name)
                        if a == "1":
                            if lever < len(map.map) - 1:
                                lever = lever + 1
                                in_map = map.get_map(lever)
                                time1 = time.time()
                                break
                            elif lever >= len(map.map) - 1:
                                l.display_message(l.message["end"], l.language)
                                exit()
                        elif a == "2":
                            exit()
    elif a == "2":
        l.display_message(l.message.get("help"), l.language)
        input()
    elif a == "4":
        os.remove("save.txt")
    else:
        l.display_message(l.message.get("input_err"), l.language)
