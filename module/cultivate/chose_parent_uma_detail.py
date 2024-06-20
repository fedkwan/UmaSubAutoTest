import json

import uiautomator2 as u2

from setting.base import *
from method.image_handler import *
from setting.destroy_account import *


def chose_parent_uma_detail(d: u2.connect, screen: np.array, setting_dic: dict):

    _blue = np.array([247, 179, 36])
    _pink = np.array([178, 110, 255])

    # 是否已经选中马娘，看决定按钮是否已经变色
    if np.all(screen[1050, 360] == np.array([6, 224, 164])):
        d.click(360, 1080)
        return

    # 选马娘里面，蓝色边框就是第1位，这里默认应该是按登陆日期升序，会选择黄金船
    elif np.all(screen[1025, 360] == _blue):
        d.click(220, 780)
        return

    # 选马娘里面，粉色边框就是第2位，这里默认应该是按登陆日期升序，会选择伏特加
    elif np.all(screen[1025, 360] == _pink):

        # 如果租借右上角的还剩X次的粉色还存在，就借好友的
        if np.all(screen[635, 700] == np.array([117, 50, 255])):

            # 如果租借栏还没变绿，还在自己的栏，那就点租借栏
            if np.all(screen[650, 400] != np.array([8, 218, 153])):
                d.click(530, 655)
                return

            # 如果已经选中了租借栏
            else:
                _path = ROOT_DIR + "/running.json"
                with open(_path, "r", encoding="utf-8") as _f:
                    _data = json.load(_f)
                
                # 如果关注列表非空，就选择第一个好友的马
                if _data["already_focus"] == 1:
                    d.click(220, 780)
                    return
                # 如果为空，跳转到 click 识图，前往关注好友的页面
                else:
                    return
        # 如果租借右上角的还剩X次的粉色不存在，选择伏特加
        else:
            d.click(360, 780)
            return


# test
if __name__ == "__main__":
    _d = u2.connect("127.0.0.1:16384")
    _setting_dic = {
        "uma_name": "daiwa_scarlet",
        "uma_chinese_name": "大和赤驥",
        "parent_uma_rank_1": 2,
        "parent_uma_rank_2": 3,
        "parent_uma_rank_friend": 2,
        "support_card_png_name": "200px-Support_thumb_30016.png",
    }
    chose_parent_uma_detail(_d, _setting_dic)
