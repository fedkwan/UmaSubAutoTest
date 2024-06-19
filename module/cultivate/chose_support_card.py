import importlib

import uiautomator2 as u2

from setting.base import *
from method.utils import *
from method.image_handler import *

logging.getLogger("airtest").setLevel(logging.ERROR)


def chose_support_card(d: u2.connect, setting_dic: dict):

    while True:
        screen = d.screenshot(format="opencv")

        # 牌组标题栏的绿色
        if np.all(screen[240, 480] == np.array([73, 201, 73])):

            if np.all(screen[409, 148] == np.array([21, 219, 154])):
                d.click(148, 409)
                time.sleep(DEFAULT_SLEEP_TIME * 2)
                continue

            elif np.all(screen[409, 360] == np.array([21, 219, 154])):
                d.click(360, 409)
                time.sleep(DEFAULT_SLEEP_TIME * 2)
                continue

            elif np.all(screen[409, 571] == np.array([21, 219, 154])):
                d.click(571, 409)
                time.sleep(DEFAULT_SLEEP_TIME * 2)
                continue

            elif np.all(screen[682, 148] == np.array([21, 219, 154])):
                d.click(148, 682)
                time.sleep(DEFAULT_SLEEP_TIME * 2)
                continue

            elif np.all(screen[682, 360] == np.array([21, 219, 154])):
                d.click(360, 682)
                time.sleep(DEFAULT_SLEEP_TIME * 2)
                continue

            # 支援卡的加号在不在，在的话点击进去
            elif np.all(screen[679, 571] == np.array([23, 219, 153])):
                d.click(571, 679)
                time.sleep(DEFAULT_SLEEP_TIME * 2)
                continue

            # 不在的话说明搞定了，开始培育
            else:
                d.click(360, 1080)
                time.sleep(DEFAULT_SLEEP_TIME * 4)
                return

        # 选择支援 / 选择好友支援 / 最后确认 的标题栏都是这样的
        if np.all(screen[40, 360] == np.array([8, 215, 146])) and np.all(
            screen[85, 360] == np.array([12, 195, 109])
        ):
            # 用标题栏来判断，这里是选择好友支援
            if np.all(screen[116, 692] == np.array([142, 120, 125])):
                # 直接点击第一位的卡片
                d.click(360, 300)
                time.sleep(DEFAULT_SLEEP_TIME * 2)
                continue

            elif (
                np.all(screen[130, 660] == np.array([12, 201, 117]))
                and np.all(screen[360, 380] == np.array([178, 110, 255]))
                and np.all(screen[360, 40] == np.array([247, 179, 36]))
            ):
                d.click(520, 1180)
                time.sleep(DEFAULT_SLEEP_TIME * 2)
                continue

            # 这里是选择支援
            else:
                sub_image_file_li = get_png_files(ROOT_DIR + "/setting/support_card")
                for sub_image_file in sub_image_file_li:
                    sub_image = cv2.imread(
                        ROOT_DIR + "/setting/support_card/" + sub_image_file
                    )
                    matcher = ImageHandler()
                    best_match = matcher.find_sub_image(sub_image, screen, 0.8)
                    if best_match is not None:
                        click_x, click_y = best_match["result"]
                        d.click(click_x, click_y)
                        time.sleep(DEFAULT_SLEEP_TIME * 2)
                        break


# test
if __name__ == "__main__":
    _d = u2.connect("127.0.0.1:16384")
    _setting_dic = importlib.import_module("customer_setting.setting_1").data
    chose_support_card(_d, _setting_dic)
