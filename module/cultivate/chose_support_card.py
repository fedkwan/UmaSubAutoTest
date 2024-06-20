import importlib

import uiautomator2 as u2

from setting.base import *
from method.utils import *
from method.image_handler import *


def support_card(d: u2.connect, screen: np.array):

    if np.all(screen[409, 148] == np.array([21, 219, 154])):
        d.click(148, 409)

    elif np.all(screen[409, 360] == np.array([21, 219, 154])):
        d.click(360, 409)

    elif np.all(screen[409, 571] == np.array([21, 219, 154])):
        d.click(571, 409)

    elif np.all(screen[682, 148] == np.array([21, 219, 154])):
        d.click(148, 682)

    elif np.all(screen[682, 360] == np.array([21, 219, 154])):
        d.click(360, 682)

    # 支援卡的加号在不在，在的话点击进去
    elif np.all(screen[679, 571] == np.array([23, 219, 153])):
        d.click(571, 679)

    # 都不在的话说明搞定了，开始培育
    else:
        d.click(360, 1080)
    return


def chose_support_card(d: u2.connect, screen: np.array):
    # 这里是选择支援
    sub_image_file_li = get_png_files(ROOT_DIR + "/resource/support_card")
    for sub_image_file in sub_image_file_li:
        sub_image = cv2.imread(ROOT_DIR + "/resource/support_card/" + sub_image_file)
        matcher = ImageHandler()
        best_match = matcher.find_sub_image(sub_image, screen, 0.8)
        if best_match is not None:
            click_x, click_y = best_match["result"]
            d.click(click_x, click_y)
            break
    return

# test
if __name__ == "__main__":
    _d = u2.connect("127.0.0.1:16384")
    _setting_dic = importlib.import_module("customer_setting.setting_1").data
    chose_support_card(_d, _setting_dic)
