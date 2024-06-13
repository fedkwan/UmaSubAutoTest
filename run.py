import time
import importlib
import uiautomator2 as u2
import json

import ddddocr

# from paddleocr import PaddleOCR
import numpy as np

from setting.base import *
from setting.page import *
from method.image_handler import *
from module.cultivate.chose_scenario import *
from module.cultivate.chose_uma import *
from module.cultivate.chose_parent_uma import *
from module.cultivate.chose_support_card import *
from setting.destroy_account import *

logging.getLogger("airtest").setLevel(logging.ERROR)
logging.getLogger("ppocr").setLevel(logging.ERROR)
logging.getLogger("ddddocr").setLevel(logging.ERROR)


def get_page_and_expect_list(screen: np.array, page_list: list):
    pages_to_check = page_list if len(page_list) != 0 else dic.keys()
    for page in pages_to_check:
        p = dic[page]["points"]
        count = sum(1 for pk, pv in p.items() if np.all(screen[pk] == np.array(pv)))
        if count == 4:
            # print("4个点的颜色匹配成功！")
            _image = cv2.imread(ROOT_DIR + "/setting/page/" + page + ".png")
            handler = ImageHandler()
            best_match = handler.is_sub_image_in_box2(
                _image, screen, dic[page]["sub_image_position"]
            )
            if best_match:
                return page


def check_click():
    sub_image_file_li = get_png_files(ROOT_DIR + "/setting/click")
    for sub_image_file in sub_image_file_li:
        sub_image = cv2.imread(ROOT_DIR + "/setting/click/" + sub_image_file)
        matcher = ImageHandler()
        best_match = matcher.find_sub_image(sub_image, screen, 0.8)
        if best_match is not None:
            click_x, click_y = best_match["result"]
            d.click(click_x, click_y)
            time.sleep(DEFAULT_SLEEP_TIME)
            return True


def check_tap():
    _image = screen[1040:1075, 310:410]
    handler = ImageHandler()
    k = handler.get_text_from_image(ocr, _image)
    if k.lower() == "tap":
        d.click(360, 1050)
        time.sleep(DEFAULT_SLEEP_TIME)
        return True


def check_find():
    sub_image_file_li = get_png_files(ROOT_DIR + "/setting/find")
    for sub_image_file in sub_image_file_li:
        file_name_li = sub_image_file[0:-4].split("-")
        [click_x, click_y] = list(map(int, file_name_li[0].split(",")))
        [x0, x1, y0, y1] = list(map(int, file_name_li[1].split(",")))
        sub_image = cv2.imread(ROOT_DIR + "/setting/find/" + sub_image_file)
        handler = ImageHandler()
        _match = handler.is_sub_image_in_box(
            sub_image, screen, x0 - 10, x1 + 10, y0 - 10, y1 + 10
        )
        if _match:
            d.click(click_x, click_y)
            time.sleep(DEFAULT_SLEEP_TIME * 4)
            return True


def check_close():
    sub_image = cv2.imread(ROOT_DIR + "/setting/close.png")
    matcher = ImageHandler()
    best_match = matcher.find_sub_image(sub_image, screen, 0.8)
    if best_match is not None:
        click_x, click_y = best_match["result"]
        d.click(click_x, click_y)
        time.sleep(DEFAULT_SLEEP_TIME)
        return True


def page_action(page):

    if page == "mumu_main":
        d.click(360, 980)
        time.sleep(DEFAULT_SLEEP_TIME * 2)
        return True

    if page == "competition":
        d.click(650, 70)
        time.sleep(DEFAULT_SLEEP_TIME * 2)
        return True

    if page == "app_main":
        if np.all(screen[898, 680] == np.array([117, 50, 255])):
            d.click(650, 915)
            time.sleep(DEFAULT_SLEEP_TIME * 2)
            return True
        else:
            d.click(550, 1080)
            time.sleep(DEFAULT_SLEEP_TIME * 2)
            return True

    if page == "chose_scenario":
        chose_scenario(d, setting_dic)
        d.click(360, 1080)
        time.sleep(DEFAULT_SLEEP_TIME * 6)
        return

    if page == "chose_uma":
        chose_uma(d, p_ocr, setting_dic)
        d.click(360, 1080)
        time.sleep(DEFAULT_SLEEP_TIME * 6)
        return

    if page == "chose_parent_uma":
        if chose_parent_uma(d, setting_dic) is False:
            return
        else:
            d.click(360, 1080)
            time.sleep(DEFAULT_SLEEP_TIME * 6)
            return

    if page == "chose_support_card":
        chose_support_card(d, setting_dic)
        time.sleep(DEFAULT_SLEEP_TIME * 2)
        return

    if page == "cultivate_main":
        d.click(650, 1230)
        time.sleep(DEFAULT_SLEEP_TIME * 2)
        return

    if page == "set_name":

        # 将数据写入到JSON文件
        _data = {"already_focus": 0}
        with open(ROOT_DIR + "/running.json", "w") as f:
            json.dump(_data, f)

        d.click(360, 580)
        time.sleep(DEFAULT_SLEEP_TIME * 2)
        d.send_keys("20240612")
        time.sleep(DEFAULT_SLEEP_TIME * 2)
        d.click(360, 830)
        time.sleep(DEFAULT_SLEEP_TIME * 2)
        d.click(360, 830)
        return

    if page == "search_friend":
        _data = ""
        with open(ROOT_DIR + "/running.json", "r") as f:
            _data = json.load(f)
            print(_data)
        if _data["already_focus"] == 1:
            d.click(360, 1200)
            time.sleep(DEFAULT_SLEEP_TIME * 2)
            return
        else:
            d.click(620, 1080)
            time.sleep(DEFAULT_SLEEP_TIME * 4)
            return

    if page == "type_id":
        d.click(360, 590)
        time.sleep(DEFAULT_SLEEP_TIME * 4)
        d.send_keys("736088380579")
        time.sleep(DEFAULT_SLEEP_TIME * 2)
        d.click(520, 830)
        time.sleep(DEFAULT_SLEEP_TIME * 2)
        d.click(520, 830)
        return

    if page == "friend_detail":
        _data = ""
        with open(ROOT_DIR + "/running.json", "r") as f:
            _data = json.load(f)
            print(_data)
        if _data["already_focus"] == 0:

            d.click(360, 480)

            # 将数据写入到JSON文件
            _data = {"already_focus": 1}
            with open(ROOT_DIR + "/running.json", "w") as f:
                json.dump(_data, f)

            time.sleep(DEFAULT_SLEEP_TIME * 2)
            return
        else:
            d.click(360, 1180)
            time.sleep(DEFAULT_SLEEP_TIME * 2)
            return

    if page == "menu":
        d.click(560, 560)
        time.sleep(DEFAULT_SLEEP_TIME * 2)
        return

    if page == "options":
        d.click(560, 560)
        time.sleep(DEFAULT_SLEEP_TIME * 2)
        return

    if page == "destroy_account":
        destroy_account(d)
        time.sleep(DEFAULT_SLEEP_TIME * 2)
        return


setting_dic = importlib.import_module("customer_setting.setting_sub").data
dic = sub_page_data
page_list = []
jam = 0

d = u2.connect("127.0.0.1:16384")
ocr = ddddocr.DdddOcr()
p_ocr = PaddleOCR(use_angle_cls=True)
while True:
    screen = d.screenshot(format="opencv")

    page = get_page_and_expect_list(screen, page_list)
    print(page)
    if jam >= 1:
        if check_tap():
            continue
        if check_find():
            continue
        if check_click():
            continue
        if check_close():
            continue
        jam = 0
        page_list = []
        continue
    if page is None:
        jam += 1
        time.sleep(DEFAULT_SLEEP_TIME)
        continue

    page_action(page)
    print(page + " action done")

    except_page_list = dic[page]["expect_page_list"]
    print(except_page_list)

    time.sleep(DEFAULT_SLEEP_TIME * 2)
