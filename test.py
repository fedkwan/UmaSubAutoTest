import time
import uiautomator2 as u2
import json
from datetime import datetime

# import ddddocr

# from paddleocr import PaddleOCR
import numpy as np

# from setting.base import *
from setting.page import *
# from method.image_handler import *


d = u2.connect("127.0.0.1:16384")
screen = d.screenshot(format="opencv")
p = sub_page_data["app_main"]["points"]
print(p)
count = sum(1 for pk, pv in p.items() if np.all(screen[pk] == np.array(pv)))
print(count)
for pk, pv in p.items():
    if np.all(screen[pk] == np.array(pv)):
        print(pk)
"""
        
        if count == 4:
            # print("4个点的颜色匹配成功！")
            _image = cv2.imread(ROOT_DIR + "/resource/page/" + page + ".png")
            handler = ImageHandler()
            best_match = handler.is_sub_image_in_box2(
                _image, screen, dic[page]["sub_image_position"]
            )
            if best_match:
                return page

"""