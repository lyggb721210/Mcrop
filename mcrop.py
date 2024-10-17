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
import os
import time
import pygame
from sys import exit

from colorama import init, Back, Fore, Style

init()
wall = Back.LIGHTBLACK_EX + Fore.LIGHTBLACK_EX + "  "
road = Back.WHITE + Fore.WHITE + "  "
user = Back.BLUE + Fore.BLUE + "  "
door = Back.GREEN + Fore.GREEN + "  "
save_v = 3.0


def get_map(plat: list, lever: int):
    _map = []
    for i in plat[lever]:
        if i == 1:
            i = wall
        elif i == 2:
            i = road
        elif i == 3:
            i = user
        elif i == 4:
            i = door
        elif i == "\n":
            i = "\n"
        else:
            print(Fore.RED + "err:Map loading error." + Style.RESET_ALL)
        _map.append(i)
    _map.append(Style.RESET_ALL)
    return _map


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
        _language = input()
        try:
            _a = int(_language) - 1
            if _a <= len(files):
                file = "./lang/" + files[_a]
                with open("./save/save.json", "w", encoding='utf-8') as f:
                    f.write(json.dumps(
                        {
                            "save": True,
                            "v": save_v,
                            "lever": 0,
                            "lang_file": file,
                        },
                        sort_keys=True,
                        indent=4
                    ))
                return file

        except ValueError:
            pass


def put_map(themap, screen):
    width = 50
    x = 5
    y = 5
    for i in range(len(themap) - 1):
        if themap[i] == "\n":
            y = y + width
            x = 5
        elif themap[i] == wall:
            pygame.draw.rect(screen, "red", (x, y, width, width), width=0)
            x = x + width
        elif themap[i] == road:
            pygame.draw.rect(screen, "white", (x, y, width, width), width=0)
            x = x + width
        elif themap[i] == door:
            pygame.draw.rect(screen, "green", (x, y, width, width), width=0)
            x = x + width
        elif themap[i] == user:
            pygame.draw.rect(screen, "blue", (x, y, width, width), width=0)
            x = x + width


def main():
    # 检查存档6
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    try:
        with open("./save/save.json", "r", encoding='utf-8') as f:
            save = json.load(f)

        if 3.0 <= save["v"] <= 3.2:
            # if len(save) >= 5 and float(save[0][0:4]) >= 2.12:
            if save["save"]:
                lever = save["lever"]
                lang_file = save["lang_file"]
                message = json.load(open(lang_file, "r", encoding='utf-8'))
                print(message.get("menu"))
                if lever != 0:
                    print(message.get("go_on_game"))
                print(message.get("clean_save"))
            else:
                lever = 0
                lang_file = choose_language_file()
                message = json.load(open(lang_file, "r", encoding='utf-8'))
                print(message.get("menu"))
                print(message.get("clean_save"))
        else:
            lang_file = choose_language_file()
            message = json.load(open(lang_file, "r", encoding='utf-8'))
            print(message.get("welcome"))
            print(message.get("menu"))
            print(message.get("clean_save"))
            lever = 0
            print(message.get("save_load_err1"))
        # f.close()
    except:
        lang_file = choose_language_file()
        message = json.load(open(lang_file, "r", encoding='utf-8'))
        print(message.get("menu"))
        lever = 0
        print(message.get("save_load_err1"))

    with open("./maps.json", "r", encoding='utf-8') as f:
        the_map = json.load(f)
    last_print = "  "
    a = input("")
    in_map = get_map(the_map["maps"], lever)
    if a == "1":
        lever = 0
        in_map = get_map(the_map['maps'], lever)
    if a == "3":
        if not ("lever" in dir()):
            # print(message.get("3error"))
            exit()
        else:
            if lever >= len(the_map["maps"]) - 1:
                print(message["end"])
                exit()
            # in_map = get_map(the_map["maps"], lever)
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
        pygame.init()
        while True:
            screen = pygame.display.set_mode((1280, 720))
            pygame.display.set_caption("McroP")
            clock = pygame.time.Clock()
            screen.fill((135, 206, 250))
            put_map(in_map, screen)
            running = True
            while running:
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_w:
                            add = in_map.index(user)
                            acd = add - in_map.index("\n") - 1
                            if acd > 0 and in_map[acd] == road:
                                in_map[add] = road
                                in_map[acd] = user
                                put_map(in_map,screen)
                            elif in_map[acd] == door:
                                pygame.quit()
                                running = False
                        elif event.key == pygame.K_a:
                            add = in_map.index(user)
                            acd = add - 1
                            if acd > 0 and in_map[acd] == road:
                                in_map[add] = road
                                in_map[acd] = user
                                put_map(in_map,screen)
                            elif in_map[acd] == door:
                                pygame.quit()
                                running = False
                        elif event.key == pygame.K_d:
                            add = in_map.index(user)
                            acd = add + 1
                            if acd > 0 and in_map[acd] == road:
                                in_map[add] = road
                                in_map[acd] = user
                                put_map(in_map,screen)
                            elif in_map[acd] == door:
                                pygame.quit()
                                running = False
                        elif event.key == pygame.K_s:
                            add = in_map.index(user)
                            acd = add + in_map.index("\n") + 1
                            if acd > 0 and in_map[acd] == road:
                                in_map[add] = road
                                in_map[acd] = user
                                put_map(in_map,screen)
                            elif in_map[acd] == door:
                                pygame.quit()
                                running = False
            cost_time = round(time.time() - time1, 2)
            while True:
                clear(os.name)
                print(message.get("lever_end"), end="")
                print(str(cost_time) + "s")
                if auto_save:
                    with open("./save/save.json", "w", encoding='utf-8') as f:
                        f.write(json.dumps(
                            {
                                "save": True,
                                "v": 3.0,
                                "lever": lever + 1,
                                "lang_file": lang_file,
                            },
                            sort_keys=True,
                            indent=4
                        ))
                    # f.close()
                    print(message["autosafed"])
                a = input("")
                clear(os.name)
                if a == "1":
                    if lever < len(the_map["maps"]) - 1:
                        lever = lever + 1
                        in_map = get_map(the_map["maps"], lever)
                        time1 = time.time()
                        break
                    elif lever >= len(the_map["maps"]) - 1:
                        print(message["end"])
                        exit()
                elif a == "2":
                    exit()

        # while True:
        #     clear(os.name)
        #     c = 0
        #     outmap = ""
        #     while c != len(in_map):
        #         outmap = outmap + in_map[c]
        #         c = c + 1
        #     print(outmap)
        #     print(last_print)
        #     print(message.get("in_game"))
        #     b = input("")
        #     if b == "w" or b == "W":
        #         add = in_map.index(user)
        #         acd = add - in_map.index("\n") - 1
        #     elif b == "a" or b == "A":
        #         add = in_map.index(user)
        #         acd = add - 1
        #     elif b == "d" or b == "D":
        #         add = in_map.index(user)
        #         acd = add + 1
        #     elif b == "s" or b == "S":
        #         add = in_map.index(user)
        #         acd = add + in_map.index("\n") + 1
        #     else:
        #         last_print = message["err"]
        #         continue
        #     if acd <= 0:
        #         last_print = message["hit_wall"]
        #     elif acd > 0:
        #         if in_map[acd] == wall:
        #             last_print = message["hit_wall"]
        #         elif in_map[acd] == road:
        #             last_print = "  "
        #             in_map[add] = road
        #             in_map[acd] = user
        #         elif in_map[acd] == door:
        #             cost_time = round(time.time() - time1, 2)
        #             while True:
        #                 clear(os.name)
        #                 print(message.get("lever_end"), end="")
        #                 print(str(cost_time) + "s")
        #                 if auto_save:
        #                     with open("./save/save.json", "w", encoding='utf-8') as f:
        #                         f.write(json.dumps(
        #                             {
        #                                 "save": True,
        #                                 "v": 3.0,
        #                                 "lever": lever + 1,
        #                                 "lang_file": lang_file,
        #                             },
        #                             sort_keys=True,
        #                             indent=4
        #                         ))
        #                     # f.close()
        #                     print(message["autosafed"])
        #                 a = input("")
        #                 clear(os.name)
        #                 if a == "1":
        #                     if lever < len(the_map["maps"]) - 1:
        #                         lever = lever + 1
        #                         in_map = get_map(the_map["maps"], lever)
        #                         time1 = time.time()
        #                         break
        #                     elif lever >= len(the_map["maps"]) - 1:
        #                         print(message["end"])
        #                         exit()
        #                 elif a == "2":
        #                     exit()
    elif a == "2":
        print(message.get("help").format(wall=wall + Style.RESET_ALL, road=road + Style.RESET_ALL,
                                         user=user + Style.RESET_ALL, door=door + Style.RESET_ALL))
        input()
    elif a == "4":
        with open("./save/save.json", "w", encoding='utf-8') as f:
            f.write(json.dumps(
                {
                    "v": 3.0,
                    "save": False,
                },
                sort_keys=True,
                indent=4
            ))
        # f.close()

    # else:
    # print(message.get("input_err"))


if __name__ == '__main__':
    main()
