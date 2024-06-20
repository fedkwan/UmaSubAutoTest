import time
import uiautomator2 as u2
import json
from datetime import datetime

import ddddocr

# from paddleocr import PaddleOCR
import numpy as np

from setting.base import *
from setting.page import *
from method.image_handler import *
from module.cultivate.chose_uma import *
from module.cultivate.chose_parent_uma_detail import *
from module.cultivate.chose_support_card import *
from setting.destroy_account import *

logging.getLogger("airtest").setLevel(logging.ERROR)
logging.getLogger("ppocr").setLevel(logging.ERROR)
logging.getLogger("ddddocr").setLevel(logging.ERROR)


def get_page_and_expect_list(dic: dict, screen: np.array, page_list: list):
    pages_to_check = page_list if len(page_list) != 0 else dic.keys()
    for page in pages_to_check:
        p = dic[page]["points"]
        count = sum(1 for pk, pv in p.items() if np.all(screen[pk] == np.array(pv)))
        if count == 4:
            # print("4个点的颜色匹配成功！")
            _image = cv2.imread(ROOT_DIR + "/resource/page/" + page + ".png")
            handler = ImageHandler()
            best_match = handler.is_sub_image_in_box2(
                _image, screen, dic[page]["sub_image_position"]
            )
            if best_match:
                return page


def check_click():
    sub_image_file_li = get_png_files(ROOT_DIR + "/resource/click")
    for sub_image_file in sub_image_file_li:
        sub_image = cv2.imread(ROOT_DIR + "/resource/click/" + sub_image_file)
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
    sub_image_file_li = get_png_files(ROOT_DIR + "/resource/find")
    for sub_image_file in sub_image_file_li:
        file_name_li = sub_image_file[0:-4].split("-")
        [click_x, click_y] = list(map(int, file_name_li[-2].split(",")))
        [x0, x1, y0, y1] = list(map(int, file_name_li[-1].split(",")))
        sub_image = cv2.imread(ROOT_DIR + "/resource/find/" + sub_image_file)
        handler = ImageHandler()
        _match = handler.is_sub_image_in_box(
            sub_image, screen, x0 - 10, x1 + 10, y0 - 10, y1 + 10
        )
        if _match:
            d.click(click_x, click_y)
            time.sleep(DEFAULT_SLEEP_TIME * 4)
            return True


def check_close():
    sub_image = cv2.imread(ROOT_DIR + "/resource/close.png")
    matcher = ImageHandler()
    best_match = matcher.find_sub_image(sub_image, screen, 0.8)
    if best_match is not None:
        click_x, click_y = best_match["result"]
        d.click(click_x, click_y)
        time.sleep(DEFAULT_SLEEP_TIME)
        return True


setting_dic = {
    "uma_name": "daiwa_scarlet",
    "uma_chinese_name": "大和赤驥",
    "parent_uma_rank_1": 2,
    "parent_uma_rank_2": 3,
    "parent_uma_rank_friend": 2,
}


def page_action(page, p_ocr, screen, setting_dic):

    if page == "app_main":
        # 如果是第一次登录的账号，领取钻石和体力药水
        if np.all(screen[898, 680] == np.array([117, 50, 255])):
            d.click(650, 915)
            return
        else:
            d.click(550, 1080)
            return

    if page == "chose_scenario":
        cropped_image = screen[90:118, 432:512]
        handler = ImageHandler()
        text = handler.get_text_from_image(ocr, cropped_image)
        num = find_numbers_in_string(text, "rude")
        print(num)
        if num < 30:
            # 跳到竞赛页面统一重置账号
            d.click(520, 1220)
            return
        else:
            d.click(360, 1080)
            return

    if page == "chose_uma":
        chose_uma(d, p_ocr, screen, setting_dic)
        d.click(360, 1080)
        return

    if page == "chose_parent_uma":
        # 如果没有【遗传树】的灰色，哪边没有就点哪边
        if np.all(screen[775, 215] != np.array([196, 196, 196])):
            d.click(110, 800)
            return
        elif np.all(screen[775, 555] != np.array([196, 196, 196])):
            d.click(450, 800)
            return
        else:
            d.click(360, 1080)
            return

    if page == "chose_parent_uma_detail":
        chose_parent_uma_detail(d, screen, setting_dic)
        return

    if page == "friend":
        _data = ""
        with open(ROOT_DIR + "/running.json", "r") as f:
            _data = json.load(f)
        if _data["already_focus"] == 1:
            d.click(360, 1200)
            time.sleep(DEFAULT_SLEEP_TIME * 2)
            return
        else:
            d.click(620, 1080)
            time.sleep(DEFAULT_SLEEP_TIME * 4)
            return

    if page == "search_id":
        # 底部输入框的白色
        bottom_point = screen[1200, 400]
        # 此为【请输入训练员ID】的D字的灰色
        wood_gray = np.array([120, 144, 177])
        id_d_point = screen[585, 430]
        # 如果【请输入训练员ID】字样还在
        if np.all(id_d_point == wood_gray):
            if np.all(bottom_point != np.array([255, 255, 255])):
                d.click(360, 580)
                time.sleep(DEFAULT_SLEEP_TIME * 2)
                return
            else:
                d.send_keys("736088380579")
                time.sleep(DEFAULT_SLEEP_TIME * 2)
                return
        else:
            d.click(520, 830)
            time.sleep(DEFAULT_SLEEP_TIME * 2)
            return

    if page == "friend_detail":
        _data = ""
        with open(ROOT_DIR + "/running.json", "r") as f:
            _data = json.load(f)
            print(_data)
        if _data["already_focus"] == 0:
            d.click(360, 480)
            # 将数据写入到JSON文件
            _data["already_focus"] = 1
            with open(ROOT_DIR + "/running.json", "w") as f:
                json.dump(_data, f)
            time.sleep(DEFAULT_SLEEP_TIME * 2)
            return
        else:
            d.click(360, 1180)
            time.sleep(DEFAULT_SLEEP_TIME * 2)
            return

    # 支援卡 牌组页面
    if page == "support_card":
        support_card(d, screen)
        return

    if page == "chose_support_card":
        chose_support_card(d, setting_dic)
        return

    if page == "chose_friend_support_card":
        d.click(360, 300)
        return

    # 跳到竞赛页面来重置账户
    if page == "competition":
        _data = ""
        with open(ROOT_DIR + "/running.json", "r") as f:
            _data = json.load(f)
            print(_data)
        if _data["already_focus"] == 1:
            # 将数据写入到JSON文件
            _data["already_focus"] = 0
            with open(ROOT_DIR + "/running.json", "w") as f:
                json.dump(_data, f)
            d.click(650, 70)
            time.sleep(DEFAULT_SLEEP_TIME * 2)
            return

    if page == "cultivate_main":
        d.click(650, 1230)
        return

    if page == "trainer_log_in":
        # 底部输入框的白色
        bottom_point = screen[1150, 400]
        # 训练员名称默认为2024，此为第一个2的底部的颜色
        first_number_point = screen[585, 200]
        if np.all(first_number_point == np.array([255, 255, 255])):
            if np.all(bottom_point != np.array([255, 255, 255])):
                d.click(360, 580)
                time.sleep(DEFAULT_SLEEP_TIME * 2)
                return
            else:
                d.send_keys("2024")
                time.sleep(DEFAULT_SLEEP_TIME * 2)
                return
        else:
            d.click(360, 830)
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


page_list = []

d = u2.connect("127.0.0.1:16384")
ocr = ddddocr.DdddOcr()
p_ocr = PaddleOCR(use_angle_cls=True)
while True:
    screen = d.screenshot(format="opencv")

    page = get_page_and_expect_list(sub_page_data, screen, page_list)
    print(page)
    if page is None:
        time.sleep(DEFAULT_SLEEP_TIME * 2)
        if check_tap():
            continue
        if check_find():
            continue
        if check_click():
            continue
        if check_close():
            continue
        page_list = []
        continue

    page_action(page, p_ocr, screen, setting_dic)
    print(page + " action done")

    except_page_list = sub_page_data[page]["expect_page_list"]
    print(except_page_list)

    time.sleep(DEFAULT_SLEEP_TIME * 2)
