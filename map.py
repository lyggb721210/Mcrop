# 这是一个地图文件
# 需要配合main.py文件使用
# 地图文件版本：V1.03
# 作者：yxr / 栗子味东方 /lyggb63
# 邮箱：lyggb721210@163.com
# 如有BUG请报告给作者

# This is a map file.
# It needs to be used with main.py file.
# Map file version: V1.03
# Author: yxr/栗子味东方l/lyggb63
# Email: lyggb721210@163.com
# Please report any bugs to the author

from colorama import Back, Fore, Style,init
init()

v = 1.03

wall = Back.LIGHTBLACK_EX+Fore.LIGHTBLACK_EX+"  "
road = Back.WHITE+Fore.WHITE+"  "
user = Back.BLUE+Fore.BLUE+"  "
door = Back.GREEN+Fore.GREEN+"  "

map = [
    ["1", "1", "1", "1", "1", "1", "1", "\n",
        "1", "3", "2", "2", "2", "4", "1", "\n",
        "1", "1", "1", "1", "1", "1", "1", "\n"],
    ["1", "1", "1", "1", "1", "1", "1", "\n",
     "1", "3", "2", "2", "2", "1", "1", "\n",
     "1", "1", "1", "2", "1", "1", "1", "\n",
     "1", "2", "2", "2", "1", "1", "1", "\n",
     "1", "1", "1", "2", "2", "2", "4", "\n",
     "1", "1", "1", "1", "1", "1", "1", "\n"],
    ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "\n",
          "1", "1", "3", "2", "2", "2", "2", "1", "1", "2", "2", "2", "2", "1", "\n",
          "1", "1", "2", "1", "1", "1", "2", "2", "2", "2", "1", "1", "2", "1", "\n",
          "1", "1", "2", "1", "1", "1", "2", "1", "2", "1", "1", "1", "2", "1", "\n",
          "1", "1", "2", "1", "1", "1", "2", "1", "2", "2", "1", "2", "2", "1", "\n",
          "1", "2", "2", "2", "2", "2", "2", "1", "1", "2", "1", "2", "1", "1", "\n",
          "1", "2", "1", "1", "1", "1", "1", "1", "1", "2", "1", "2", "1", "1", "\n",
          "1", "2", "2", "1", "2", "2", "2", "2", "2", "2", "1", "2", "2", "1", "\n",
          "1", "1", "2", "1", "2", "1", "1", "1", "1", "1", "1", "1", "2", "1", "\n",
          "1", "1", "1", "1", "1", "2", "2", "2", "2", "1", "2", "1", "2", "1", "\n",
          "1", "1", "2", "2", "2", "2", "1", "1", "2", "2", "2", "2", "2", "1", "\n",
          "1", "1", "4", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "\n"],
    ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "\n",
          "1", "1", "3", "2", "2", "2", "2", "1", "1", "2", "1", "2", "2", "1", "\n",
          "1", "1", "2", "1", "1", "1", "2", "1", "2", "2", "1", "1", "2", "1", "\n",
          "1", "1", "2", "1", "1", "1", "2", "1", "2", "1", "1", "1", "2", "1", "\n",
          "1", "1", "2", "1", "1", "1", "2", "2", "2", "2", "1", "2", "2", "1", "\n",
          "1", "2", "2", "2", "2", "2", "2", "1", "1", "2", "1", "2", "1", "1", "\n",
          "1", "2", "1", "1", "1", "1", "1", "1", "1", "1", "2", "2", "1", "1", "\n",
          "1", "2", "2", "1", "2", "2", "2", "2", "2", "2", "1", "1", "2", "1", "\n",
          "1", "1", "2", "2", "2", "1", "1", "1", "2", "1", "1", "1", "2", "1", "\n",
          "1", "1", "1", "1", "1", "2", "2", "2", "2", "1", "2", "1", "2", "1", "\n",
          "1", "1", "2", "2", "2", "2", "1", "1", "2", "2", "2", "2", "2", "1", "\n",
          "1", "1", "4", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "\n"]]


def get_map(lever: int):
    _map = []
    for i in map[lever]:
        if i == "1":
            i = wall
        elif i == "2":
            i = road
        elif i == "3":
            i = user
        elif i == "4":
            i = door
        elif i == "\n":
            i = "\n"
        else:
            print(Fore.RED+"err:Map lodes error."+Style.RESET_ALL)
        _map.append(i)
    _map.append(Style.RESET_ALL)
    return _map
