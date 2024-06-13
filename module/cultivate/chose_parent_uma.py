import importlib

import uiautomator2 as u2

from setting.base import *
from method.image_handler import *
from setting.destroy_account import *


def chose_parent_uma(d: u2.connect, setting_dic: dict):

    while True:
        screen = d.screenshot(format="opencv")

        # 第1位 隔壁的蓝色来判断，是准备进入选种马阶段
        if np.all(screen[660, 110] == np.array([247, 179, 36])):

            # 如果没有【遗传树】的灰色，右边没有就点右边
            if np.all(screen[775, 555] != np.array([196, 196, 196])):
                d.click(450, 800)
                time.sleep(DEFAULT_SLEEP_TIME)

            # 如果没有【遗传树】的灰色，左边没有就点左边
            elif np.all(screen[775, 215] != np.array([196, 196, 196])):
                d.click(110, 800)
                time.sleep(DEFAULT_SLEEP_TIME)

            # 两边都选好了，就点下一步
            else:
                break

        # 选马娘里面，蓝色边框就是第1位
        if np.all(screen[1025, 360] == np.array([247, 179, 36])):
            d.click(220, 780)
            time.sleep(DEFAULT_SLEEP_TIME * 2)
            d.click(360, 1080)
            time.sleep(DEFAULT_SLEEP_TIME * 2)
            return

        # 选马娘里面，粉色边框就是第2位
        if np.all(screen[690, 360] == np.array([193, 142, 251])):

            # 如果租借右上角的还剩X次的粉色还存在，就借好友的（没钱别怪我）
            if np.all(screen[635, 700] == np.array([117, 50, 255])):
                d.click(530, 655)
                time.sleep(DEFAULT_SLEEP_TIME * 2)
                d.click(220, 780)
                time.sleep(DEFAULT_SLEEP_TIME * 2)
                d.click(360, 1080)
                time.sleep(DEFAULT_SLEEP_TIME * 2)
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
                break

        time.sleep(DEFAULT_SLEEP_TIME)

        # 这里统一处理一下吧，不想放到外面的循环去处理，显得比较整洁
        sub_image = cv2.imread(ROOT_DIR + "/resource/general/ok.png")
        handler = ImageHandler()
        best_match = handler.find_sub_image(sub_image, screen)
        if best_match is not None:
            click_x, click_y = best_match["result"]
            d.click(click_x, click_y)
            time.sleep(DEFAULT_SLEEP_TIME)


# test
if __name__ == "__main__":
    _d = u2.connect("127.0.0.1:16384")
    _setting_dic = importlib.import_module("customer_setting.setting_1").data
    chose_parent_uma(_d, _setting_dic)
