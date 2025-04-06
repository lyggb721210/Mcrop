"""
这是一个在Python上运行的迷宫挑战游戏
This is a maze challenge game on Python.
Email 邮箱：lyggb721210@163.com
Version 当前版本：V2.1-pre1
Please report any bugs to the author.
如果有BUG请报告给作者。

Copyright (c) 2025 yxrlyg & lyggb721210
   McroP is licensed under Mulan PSL v2.
   You can use this software according to the terms and conditions of the Mulan PSL v2.
   You may obtain a copy of Mulan PSL v2 at:
            http://license.coscl.org.cn/MulanPSL2
   THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND, EITHER EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT, MERCHANTABILITY OR FIT FOR A PARTICULAR PURPOSE.
   See the Mulan PSL v2 for more details.
"""

import json
import os
import time
import pygame
from sys import exit
from Setting import *
import locale


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
                lang_file = choose_language_file()
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
    # last_print = "  "
    a = input("")
    # in_map = get_map(the_map["maps"], lever)
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
        in_map = get_map(the_map["maps"], lever)
    if a == "1" or a == "3":
        while True:
            print(message["check_auto_safe"], end='')
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
            screen, clock = create_window()
            put_map(in_map, screen)
            running = True
            while running:  # 游戏主循环
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit()
                    elif event.type == pygame.KEYDOWN:
                        print(time.time() - time1)
                        local = in_map.index(user)                     
                        if event.key == pygame.K_w:
                            destination = local - in_map.index("\n") - 1
                            running = move_user(in_map, screen, local, destination)
                        elif event.key == pygame.K_a:
                            destination = local - 1
                            running = move_user(in_map, screen, local, destination)
                        elif event.key == pygame.K_d:
                            destination = local + 1
                            running = move_user(in_map, screen, local, destination)
                        elif event.key == pygame.K_s:
                            destination = local + in_map.index("\n") + 1
                            running = move_user(in_map, screen, local, destination)
            cost_time = round(time.time() - time1, 2)
            while True:  # 过关结算循环
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


def create_window():
    screen = pygame.display.set_mode(ScreenSize)
    pygame.display.set_caption("McroP")
    clock = pygame.time.Clock()
    screen.fill((135, 206, 250))
    return screen, clock


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
    """清除终端中显示的内容"""
    if system == "posix":
        os.system("clear")
    elif system == "nt":
        os.system("cls")


def choose_language_file():
    """选择游戏的语言,返回语言文件的路径"""
    # clear(os.name)
    system_lang = locale.getdefaultlocale()[0].split('_')[0]
    files = os.listdir("./lang")
    lang_mapping = {file.split('.')[0]: file for file in files}
    if system_lang in lang_mapping:
        file = "./lang/" + lang_mapping[system_lang]

    else:
        if "en.json" in lang_mapping:
            file = "./lang/" + lang_mapping["en"]
        else:
            print(Fore.RED + "err:Language file not found." + Style.RESET_ALL)
            exit(1)

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


def put_map(themap: list, screen):
    """画地图"""
    width = (ScreenSize[1] - 50) // (len(themap) // (themap.index("\n") + 1))
    x = (ScreenSize[0] - themap.index("\n") * width) // 2
    y = 10
    for i in range(len(themap) - 1):
        if themap[i] == "\n":
            y = y + width
            x = (ScreenSize[0] - themap.index("\n") * width) // 2
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


def move_user(in_map: list, screen, local: int, destination: int):
    """根据destination的值移动人物，返回running"""
    running = True
    if destination > 0 and in_map[destination] == road:
        in_map[local] = road
        in_map[destination] = user
        put_map(in_map, screen)
    elif in_map[destination] == door:
        pygame.quit()
        running = False
    return running


if __name__ == '__main__':
    main()
