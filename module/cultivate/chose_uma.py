import uiautomator2 as u2

from setting.base import *
from paddleocr import PaddleOCR
from method.image_handler import *


def chose_uma(d: u2.connect, p_ocr: PaddleOCR, screen: np.array, setting_dic: dict):

    uma_name = setting_dic["uma_name"]

    text_image = screen[415:445, 35:155]
    handler = ImageHandler()
    text = handler.get_text_from_image_paddle(p_ocr, text_image)
    if text == uma_name:
        return

    icon_dir = ROOT_DIR + "/resource/icon"
    sub_image = cv2.imread(icon_dir + "/" + uma_name + ".png")
    handler = ImageHandler()
    best_match = handler.find_sub_image(sub_image, screen, 0.7)
    if best_match is not None:
        click_x, click_y = best_match["result"]
        d.click(click_x, click_y)
        return


# test
if __name__ == "__main__":
    _d = u2.connect("127.0.0.1:16384")
    _p_ocr = PaddleOCR(use_angle_cls=True)
    _setting_dic = {
        "uma_name": "daiwa_scarlet",
        "uma_chinese_name": "大和赤驥",
        "parent_uma_rank_1": 2,
        "parent_uma_rank_2": 3,
        "parent_uma_rank_friend": 2,
        "support_card_png_name": "200px-Support_thumb_30016.png",
    }
    chose_uma(_d, _p_ocr, _setting_dic)
