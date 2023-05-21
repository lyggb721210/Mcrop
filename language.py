#-*-coding:utf8;-*-
def choose_language():
    while True :
        language = input("请选择您要使用的语言 Please select the language you want to use：\n1. 中 文 \n2. English\n请输入前面序号")
        if language == "1" :
            break
        elif language == "2" :
            break
    return language


language = choose_language()

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
        "1": "这是一个地图闯关游戏\n在游戏中可以输入w,a,s,d来控制的移动 \n(输入后要按enter表示确定)\n'🧱'是墙，'🔲'是空地\n祝您游玩愉快",
        "2": "This is a map breaking game .\nIn the game, you can enter w, a, s, and d to control😊 's movement\n(After input, press enter to confirm)\n'🧱' is a wall, '🔲' is an open space.\nHave a good time."
    },
    "input_err": {
        "1": "请输入正确的数字",
        "2": "Please enter the correct number."
    },

}


def display_message(message_dict, language):
    print(message_dict.get(language))


def get_message(message_dict):
    return message.get(message_dict)

# end def


display_message(message.get("welcome"), language)
