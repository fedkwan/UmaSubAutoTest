sub_page_data = {
    "app_main": {
        "points": {
            (1264, 300): [220, 130, 0],  # y,x : b, g, r
            (1264, 330): [220, 130, 0],
            (1264, 360): [220, 130, 0],
            (920, 650): [102, 68, 221],
        },
        "sub_image_position": [220, 270, 1090, 1110],  # x0, x1, y0, y1
        "expect_page_list": ["chose_scenario"],
    },
    "chose_scenario": {
        "points": {
            (222, 500): [101, 54, 247],
            (222, 520): [101, 54, 247],
            (222, 630): [101, 54, 247],
            (222, 650): [101, 54, 247],
        },
        "sub_image_position": [527, 620, 127, 157],
        "expect_page_list": ["chose_uma"],
    },
    "chose_uma": {
        "points": {
            (460, 150): [36, 217, 121],
            (460, 410): [36, 217, 121],
            (460, 670): [36, 217, 121],
            (367, 64): [34, 204, 255],
        },
        "sub_image_position": [470, 563, 402, 432],
        "expect_page_list": ["chose_parent_uma"],
    },
    "chose_parent_uma": {
        "points": {
            (460, 150): [36, 217, 121],
            (460, 410): [36, 217, 121],
            (460, 670): [36, 217, 121],
            (180, 520): [80, 144, 255],
        },
        "sub_image_position": [382, 447, 654, 678],
        "expect_page_list": ["chose_support_card", "chose_parent_uma_detail"],
    },
    "chose_parent_uma_detail": {
        "points": {
            (460, 150): [36, 217, 121],
            (460, 410): [36, 217, 121],
            (460, 670): [36, 217, 121],
            (180, 520): [80, 144, 255],
        },
        "sub_image_position": [40, 186, 979, 1004],
        "expect_page_list": ["chose_support_card"],
    },
    "friend": {
        "points": {
            (135, 630): [8, 137, 71],
            (135, 640): [8, 137, 71],
            (135, 650): [8, 137, 71],
            (135, 660): [8, 137, 71],
        },
        "sub_image_position": [572, 672, 1063, 1100],
        "expect_page_list": ["app_main", "search_id"],
    },
    "search_id": {
        "points": {
            (435, 200): [12, 195, 107],
            (435, 210): [12, 195, 107],
            (435, 510): [12, 195, 107],
            (435, 520): [12, 195, 107],
        },
        # "sub_image_position": [270, 461, 574, 608],
        "sub_image_position": [587, 615, 574, 602],
        "expect_page_list": ["friend_detail"],
    },
    "friend_detail": {
        "points": {
            (80, 200): [12, 197, 113],
            (80, 210): [12, 197, 113],
            (80, 520): [12, 197, 113],
            (80, 530): [12, 197, 113],
        },
        "sub_image_position": [80, 185, 564, 596],
        "expect_page_list": ["app_main"],
    },
    "support_card": {
        "points": {
            (240, 40): [73, 201, 73],
            (240, 480): [73, 201, 73],
            (790, 480): [162, 102, 255],
            (790, 660): [162, 102, 255],
        },
        "sub_image_position": [472, 562, 901, 930],
        "expect_page_list": [
            "chose_support_card",
            "chose_friend_support_card",
            "last_confirm",
        ],
    },
    "chose_support_card": {
        "points": {
            (80, 200): [12, 197, 113],
            (80, 210): [12, 197, 113],
            (80, 520): [12, 197, 113],
            (80, 530): [12, 197, 113],
        },
        "sub_image_position": [539, 568, 1057, 1079],
        "expect_page_list": ["support_card"],
    },
    "chose_friend_support_card": {
        "points": {
            (80, 200): [12, 197, 113],
            (80, 210): [12, 197, 113],
            (80, 520): [12, 197, 113],
            (80, 530): [12, 197, 113],
        },
        "sub_image_position": [512, 664, 230, 258],
        "expect_page_list": ["support_card"],
    },
    "last_confirm": {
        "points": {
            (80, 200): [12, 197, 113],
            (80, 210): [12, 197, 113],
            (80, 520): [12, 197, 113],
            (80, 530): [12, 197, 113],
        },
        "sub_image_position": [385, 443, 357, 380],
        "expect_page_list": ["confirm_skip_empty", "cultivate_main"],
    },
    "confirm_skip_empty": {
        "points": {
            (435, 200): [12, 195, 107],
            (435, 210): [12, 195, 107],
            (435, 510): [12, 195, 107],
            (435, 520): [12, 195, 107],
        },
        "sub_image_position": [243, 297, 681, 738],
        "expect_page_list": ["confirm_skip_select"],
    },
    "confirm_skip_select": {
        "points": {
            (435, 200): [12, 195, 107],
            (435, 210): [12, 195, 107],
            (435, 510): [12, 195, 107],
            (435, 520): [12, 195, 107],
        },
        "sub_image_position": [243, 297, 681, 738],
        "expect_page_list": ["cultivate_main"],
    },
    "event_shorten_setting": {
        "points": {
            (350, 200): [12, 195, 109],
            (350, 210): [12, 195, 109],
            (350, 510): [12, 195, 109],
            (350, 520): [12, 195, 109],
        },
        "sub_image_position": [60, 90, 420, 450],
        "expect_page_list": ["cultivate_main"],
    },
    "cultivate_main": {
        "points": {
            (840, 600): [204, 187, 14],
            (840, 690): [204, 187, 14],
            (850, 600): [204, 187, 14],
            (850, 690): [204, 187, 14],
        },
        "sub_image_position": [560, 640, 957, 1037],
        "expect_page_list": ["cultivate_menu"],
    },
    "cultivate_menu": {
        "points": {
            (350, 200): [12, 195, 109],
            (350, 210): [12, 195, 109],
            (350, 510): [12, 195, 109],
            (350, 520): [12, 195, 109],
        },
        "sub_image_position": [519, 596, 539, 577],
        "expect_page_list": ["give_up"],
    },
    "give_up": {
        "points": {
            (435, 200): [12, 195, 107],
            (435, 210): [12, 195, 107],
            (435, 510): [12, 195, 107],
            (435, 520): [12, 195, 107],
        },
        "sub_image_position": [480, 556, 816, 854],
        "expect_page_list": ["app_main"],
    },
    "competition": {
        "points": {
            (950, 320): [109, 84, 89],
            (950, 400): [109, 84, 89],
            (1106, 400): [109, 84, 89],
            (1106, 420): [109, 84, 89],
        },
        "sub_image_position": [434, 561, 901, 940],
        "expect_page_list": ["app_main"],
    },
    "app_menu": {
        "points": {
            (80, 200): [12, 197, 113],
            (80, 210): [12, 197, 113],
            (80, 520): [12, 197, 113],
            (80, 530): [12, 197, 113],
        },
        "sub_image_position": [390, 630, 360, 420],
        "expect_page_list": ["destroy_account"],
    },
    "destroy_account": {
        "points": {
            (80, 200): [12, 197, 113],
            (80, 210): [12, 197, 113],
            (80, 520): [12, 197, 113],
            (80, 530): [12, 197, 113],
        },
        "sub_image_position": [34, 139, 119, 151],
        "expect_page_list": ["app_main"],
    },
    "trainer_log_in": {
        "points": {
            (435, 200): [12, 195, 107],
            (435, 210): [12, 195, 107],
            (435, 510): [12, 195, 107],
            (435, 520): [12, 195, 107],
        },
        "sub_image_position": [413, 474, 647, 710],
        "expect_page_list": ["app_main"],
    },
}
