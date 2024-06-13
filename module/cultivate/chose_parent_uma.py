import uiautomator2 as u2

from setting.base import *
from method.image_handler import *
from setting.destroy_account import *


def chose_parent_uma_detail(d: u2.connect, screen: np.array, setting_dic: dict):

    # 选马娘里面，蓝色边框就是第1位
    if np.all(screen[1025, 360] == np.array([247, 179, 36])):
        d.click(220, 780)
        return

    # 选马娘里面，粉色边框就是第2位
    if np.all(screen[690, 360] == np.array([193, 142, 251])):

        # 如果租借右上角的还剩X次的粉色还存在，就借好友的（没钱别怪我）
        if np.all(screen[635, 700] == np.array([117, 50, 255])):
            d.click(530, 655)
            return

        # 否则就选自己的吧
        else:
            """d.click(360, 780)
            time.sleep(DEFAULT_SLEEP_TIME * 2)
            d.click(360, 1080)
            time.sleep(DEFAULT_SLEEP_TIME * 2)
            return"""
            d.click(520, 1220)
            time.sleep(DEFAULT_SLEEP_TIME * 2)



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
