# -*-coding:utf8;-*-
from colorama import Fore, Style


def choose_language():
    while True:
        language = input(
            "请选择您要使用的语言 Please select the language you want to use：\n1. 中 文 \n2. English\n请输入前面序号")
        if language == "1":
            break
        elif language == "2":
            break
    return language


language = ""

message = {
    "welcome": {
        "1": "欢迎使用",
        "2": "Welcome to use"
    },
    "menu": {
        "1": " 1.新游戏\n 2.帮助\n 请输入前面序号",
        "2": " 1.New Game\n 2.Help.\n Please enter the front serial number."
    },
    "in_game": {
        "1": "请输入w,a,s,d.",
        "2": "Please enter w, a, s, d."
    },
    "err": {
        "1": "请输入w,a,s,d(上,左,下,右)",
        "2": "Please enter w, a, s, d (top, left, bottom, right)."
    },
    "hit_wall": {
        "1": "啊，碰墙了",
        "2": "Ah, I hit the wall."
    },
    "lever_end": {
        "1": " 成功通关!\n 1.下一关\n 2.退出\n 请输入前面序号",
        "2": " Successful customs cloms clearance\n 1.Next level\n 2.Exit\n Please enter the front serial number."
    },
    "end": {
        "1": "关卡已结束",
        "2": "The level has ended."
    },
    "help": {
        "1": "这是一个地图闯关游戏\n在游戏中可以输入w,a,s,d来控制的移动 \n(输入后要按enter表示确定)\n'🧱'是墙，'🔲'是空地\n祝您游玩愉快 \n按Enter键退出。",
        "2": "This is a map breaking game .\nIn the game, you can enter w, a, s, and d to control😊 's movement\n(After input, press enter to confirm)\n'🧱' is a wall, '🔲' is an open space.\nHave a good time.\nPress Enter to exit."
    },
    "input_err": {
        "1": "请输入正确的数字",
        "2": "Please enter the correct number."
    },
    "save_load_err1": {
        "1": Fore.RED + "err:存档加载错误" + Style.RESET_ALL,
        "2": Fore.RED + "err:Archive loading error" + Style.RESET_ALL
    },
    "check_autosafe": {
        "1": "是否启用自动保存？[Y/n]",
        "2": "Whether to enable automatic save？[Y/n]"
    },
    "autosafed": {
        "1": "已自动保存",
        "2": "Automatically saved"
    },
    "go_on_game": {
        "1": " 3.继续游戏",
        "2": " 3.Continue the game"
    },
    "clean_save": {
        "1": " 4.清除存档和语言并退出",
        "2": " 4.Clear Archive and Language and Exit"
    }
}


def display_message(message_dict, language):
    print(message_dict.get(language))


def get_message(message_dict):
    return message.get(message_dict)

# end def
