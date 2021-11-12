from typing import Tuple, Union

Color = Union[str, Tuple[int, int, int]]


CSI = "\033["
RESET_ALL = f"{CSI}0m"
BOLD = f"{CSI}1m"
DIM = f"{CSI}2m"
ITALIC = f"{CSI}3m"
UNDERLINE = f"{CSI}4m"
BLINK = f"{CSI}5m"
CROSS = f"{CSI}9m"
DOUBLE_UNDERLINE = f"{CSI}21m"
Conceal = "8"  # INVISIBLE

STYLES = ["bold", "dim", "cross", "blink", "underline", "double_underline", "italic"]

STYLE_MAP = {
    "b": BOLD,
    "d": DIM,
    "c": CROSS,
    "k": BLINK,
    "u": UNDERLINE,
    "U": DOUBLE_UNDERLINE,
    "i": ITALIC,
}

RESET_BOLD_AND_DIM = f"{CSI}22m"
RESET_ITALIC = f"{CSI}23m"
RESET_UNDERLINE = f"{CSI}24m"
RESET_BLINK = f"{CSI}25m"
RESET_CROSS = f"{CSI}29m"
RESET_COLOR = f"{CSI}39m"
RESET_BACKGROUND = f"{CSI}49m"

STYLE_RESET_MAP = {
    "b": RESET_BOLD_AND_DIM,
    "d": RESET_BOLD_AND_DIM,
    "c": RESET_CROSS,
    "k": RESET_BLINK,
    "u": RESET_UNDERLINE,
    "U": RESET_UNDERLINE,
    "i": RESET_ITALIC,
}

# NUMBERS OF SEQUENCE (in str because it is always used in str format)
N_RESET_ALL = "0"
N_BOLD = "1"
N_DIM = "2"
N_ITALIC = "3"
N_UNDERLINE = "4"
N_DOUBLE_UNDERLINE = "21"
N_BLINK = "5"
N_CROSS = "9"

N_RESET_BOLD_AND_DIM = "22"
N_RESET_ITALIC = "23"
N_RESET_UNDERLINE = "24"
N_RESET_BLINK = "25"
N_RESET_CROSS = "29"
N_RESET_COLOR = "39"
N_RESET_BACKGROUND = "49"

COLOR_SUCCESS = "green"
COLOR_FAILURE = "red"
COLOR_INFO = "dodger_blue"
STYLE_SUCCESS = "b"
STYLE_FAILURE = "b"
STYLE_INFO = "b"
TXT_SUCCESS = "[+]"
TXT_FAILURE = "[-]"
TXT_INFO = "[ ]"

COLORS = {
    "alice_blue": (240, 248, 255),
    "antique_white": (250, 235, 215),
    "antique_white1": (255, 239, 219),
    "antique_white2": (238, 223, 204),
    "antique_white3": (205, 192, 176),
    "antique_white4": (139, 131, 120),
    "aquamarine": (127, 255, 212),
    "aquamarine1": (127, 255, 212),
    "aquamarine2": (118, 238, 198),
    "aquamarine3": (102, 205, 170),
    "aquamarine4": (69, 139, 116),
    "azure": (240, 255, 255),
    "azure1": (240, 255, 255),
    "azure2": (224, 238, 238),
    "azure3": (193, 205, 205),
    "azure4": (131, 139, 139),
    "beige": (245, 245, 220),
    "bisque": (255, 228, 196),
    "bisque1": (255, 228, 196),
    "bisque2": (238, 213, 183),
    "bisque3": (205, 183, 158),
    "bisque4": (139, 125, 107),
    "black": (0, 0, 0),
    "blanched_almond": (255, 235, 205),
    "blue": (0, 0, 255),
    "blue1": (0, 0, 255),
    "blue2": (0, 0, 238),
    "blue3": (0, 0, 205),
    "blue4": (0, 0, 139),
    "blue_violet": (138, 43, 226),
    "brown": (165, 42, 42),
    "brown1": (255, 64, 64),
    "brown2": (238, 59, 59),
    "brown3": (205, 51, 51),
    "brown4": (139, 35, 35),
    "burlywood": (222, 184, 135),
    "burlywood1": (255, 211, 155),
    "burlywood2": (238, 197, 145),
    "burlywood3": (205, 170, 125),
    "burlywood4": (139, 115, 85),
    "cadet_blue": (95, 158, 160),
    "cadet_blue1": (152, 245, 255),
    "cadet_blue2": (142, 229, 238),
    "cadet_blue3": (122, 197, 205),
    "cadet_blue4": (83, 134, 139),
    "chartreuse": (127, 255, 0),
    "chartreuse1": (127, 255, 0),
    "chartreuse2": (118, 238, 0),
    "chartreuse3": (102, 205, 0),
    "chartreuse4": (69, 139, 0),
    "chocolate": (210, 105, 30),
    "chocolate1": (255, 127, 36),
    "chocolate2": (238, 118, 33),
    "chocolate3": (205, 102, 29),
    "chocolate4": (139, 69, 19),
    "coral": (255, 127, 80),
    "coral1": (255, 114, 86),
    "coral2": (238, 106, 80),
    "coral3": (205, 91, 69),
    "coral4": (139, 62, 47),
    "cornflower_blue": (100, 149, 237),
    "cornsilk": (255, 248, 220),
    "cornsilk1": (255, 248, 220),
    "cornsilk2": (238, 232, 205),
    "cornsilk3": (205, 200, 177),
    "cornsilk4": (139, 136, 120),
    "cyan": (0, 255, 255),
    "cyan1": (0, 255, 255),
    "cyan2": (0, 238, 238),
    "cyan3": (0, 205, 205),
    "cyan4": (0, 139, 139),
    "dark_blue": (0, 0, 139),
    "dark_cyan": (0, 139, 139),
    "dark_goldenrod": (184, 134, 11),
    "dark_goldenrod1": (255, 185, 15),
    "dark_goldenrod2": (238, 173, 14),
    "dark_goldenrod3": (205, 149, 12),
    "dark_goldenrod4": (139, 101, 8),
    "dark_gray": (169, 169, 169),
    "dark_green": (0, 100, 0),
    "dark_grey": (169, 169, 169),
    "dark_khaki": (189, 183, 107),
    "dark_magenta": (139, 0, 139),
    "dark_olive_green": (85, 107, 47),
    "dark_olive_green1": (202, 255, 112),
    "dark_olive_green2": (188, 238, 104),
    "dark_olive_green3": (162, 205, 90),
    "dark_olive_green4": (110, 139, 61),
    "dark_orange": (255, 140, 0),
    "dark_orange1": (255, 127, 0),
    "dark_orange2": (238, 118, 0),
    "dark_orange3": (205, 102, 0),
    "dark_orange4": (139, 69, 0),
    "dark_orchid": (153, 50, 204),
    "dark_orchid1": (191, 62, 255),
    "dark_orchid2": (178, 58, 238),
    "dark_orchid3": (154, 50, 205),
    "dark_orchid4": (104, 34, 139),
    "dark_red": (139, 0, 0),
    "dark_salmon": (233, 150, 122),
    "dark_sea_green": (143, 188, 143),
    "dark_sea_green1": (193, 255, 193),
    "dark_sea_green2": (180, 238, 180),
    "dark_sea_green3": (155, 205, 155),
    "dark_sea_green4": (105, 139, 105),
    "dark_slate_blue": (72, 61, 139),
    "dark_slate_gray": (47, 79, 79),
    "dark_slate_gray1": (151, 255, 255),
    "dark_slate_gray2": (141, 238, 238),
    "dark_slate_gray3": (121, 205, 205),
    "dark_slate_gray4": (82, 139, 139),
    "dark_slate_grey": (47, 79, 79),
    "dark_turquoise": (0, 206, 209),
    "dark_violet": (148, 0, 211),
    "debian_red": (215, 7, 81),
    "deep_pink": (255, 20, 147),
    "deep_pink1": (255, 20, 147),
    "deep_pink2": (238, 18, 137),
    "deep_pink3": (205, 16, 118),
    "deep_pink4": (139, 10, 80),
    "deep_sky_blue": (0, 191, 255),
    "deep_sky_blue1": (0, 191, 255),
    "deep_sky_blue2": (0, 178, 238),
    "deep_sky_blue3": (0, 154, 205),
    "deep_sky_blue4": (0, 104, 139),
    "dim_gray": (105, 105, 105),
    "dim_grey": (105, 105, 105),
    "dodger_blue": (30, 144, 255),
    "dodger_blue1": (30, 144, 255),
    "dodger_blue2": (28, 134, 238),
    "dodger_blue3": (24, 116, 205),
    "dodger_blue4": (16, 78, 139),
    "firebrick": (178, 34, 34),
    "firebrick1": (255, 48, 48),
    "firebrick2": (238, 44, 44),
    "firebrick3": (205, 38, 38),
    "firebrick4": (139, 26, 26),
    "floral_white": (255, 250, 240),
    "forest_green": (34, 139, 34),
    "gainsboro": (220, 220, 220),
    "ghost_white": (248, 248, 255),
    "gold": (255, 215, 0),
    "gold1": (255, 215, 0),
    "gold2": (238, 201, 0),
    "gold3": (205, 173, 0),
    "gold4": (139, 117, 0),
    "goldenrod": (218, 165, 32),
    "goldenrod1": (255, 193, 37),
    "goldenrod2": (238, 180, 34),
    "goldenrod3": (205, 155, 29),
    "goldenrod4": (139, 105, 20),
    "gray": (190, 190, 190),
    "gray0": (0, 0, 0),
    "gray1": (3, 3, 3),
    "gray10": (26, 26, 26),
    "gray100": (255, 255, 255),
    "gray11": (28, 28, 28),
    "gray12": (31, 31, 31),
    "gray13": (33, 33, 33),
    "gray14": (36, 36, 36),
    "gray15": (38, 38, 38),
    "gray16": (41, 41, 41),
    "gray17": (43, 43, 43),
    "gray18": (46, 46, 46),
    "gray19": (48, 48, 48),
    "gray2": (5, 5, 5),
    "gray20": (51, 51, 51),
    "gray21": (54, 54, 54),
    "gray22": (56, 56, 56),
    "gray23": (59, 59, 59),
    "gray24": (61, 61, 61),
    "gray25": (64, 64, 64),
    "gray26": (66, 66, 66),
    "gray27": (69, 69, 69),
    "gray28": (71, 71, 71),
    "gray29": (74, 74, 74),
    "gray3": (8, 8, 8),
    "gray30": (77, 77, 77),
    "gray31": (79, 79, 79),
    "gray32": (82, 82, 82),
    "gray33": (84, 84, 84),
    "gray34": (87, 87, 87),
    "gray35": (89, 89, 89),
    "gray36": (92, 92, 92),
    "gray37": (94, 94, 94),
    "gray38": (97, 97, 97),
    "gray39": (99, 99, 99),
    "gray4": (10, 10, 10),
    "gray40": (102, 102, 102),
    "gray41": (105, 105, 105),
    "gray42": (107, 107, 107),
    "gray43": (110, 110, 110),
    "gray44": (112, 112, 112),
    "gray45": (115, 115, 115),
    "gray46": (117, 117, 117),
    "gray47": (120, 120, 120),
    "gray48": (122, 122, 122),
    "gray49": (125, 125, 125),
    "gray5": (13, 13, 13),
    "gray50": (127, 127, 127),
    "gray51": (130, 130, 130),
    "gray52": (133, 133, 133),
    "gray53": (135, 135, 135),
    "gray54": (138, 138, 138),
    "gray55": (140, 140, 140),
    "gray56": (143, 143, 143),
    "gray57": (145, 145, 145),
    "gray58": (148, 148, 148),
    "gray59": (150, 150, 150),
    "gray6": (15, 15, 15),
    "gray60": (153, 153, 153),
    "gray61": (156, 156, 156),
    "gray62": (158, 158, 158),
    "gray63": (161, 161, 161),
    "gray64": (163, 163, 163),
    "gray65": (166, 166, 166),
    "gray66": (168, 168, 168),
    "gray67": (171, 171, 171),
    "gray68": (173, 173, 173),
    "gray69": (176, 176, 176),
    "gray7": (18, 18, 18),
    "gray70": (179, 179, 179),
    "gray71": (181, 181, 181),
    "gray72": (184, 184, 184),
    "gray73": (186, 186, 186),
    "gray74": (189, 189, 189),
    "gray75": (191, 191, 191),
    "gray76": (194, 194, 194),
    "gray77": (196, 196, 196),
    "gray78": (199, 199, 199),
    "gray79": (201, 201, 201),
    "gray8": (20, 20, 20),
    "gray80": (204, 204, 204),
    "gray81": (207, 207, 207),
    "gray82": (209, 209, 209),
    "gray83": (212, 212, 212),
    "gray84": (214, 214, 214),
    "gray85": (217, 217, 217),
    "gray86": (219, 219, 219),
    "gray87": (222, 222, 222),
    "gray88": (224, 224, 224),
    "gray89": (227, 227, 227),
    "gray9": (23, 23, 23),
    "gray90": (229, 229, 229),
    "gray91": (232, 232, 232),
    "gray92": (235, 235, 235),
    "gray93": (237, 237, 237),
    "gray94": (240, 240, 240),
    "gray95": (242, 242, 242),
    "gray96": (245, 245, 245),
    "gray97": (247, 247, 247),
    "gray98": (250, 250, 250),
    "gray99": (252, 252, 252),
    "green": (0, 255, 0),
    "green1": (0, 255, 0),
    "green2": (0, 238, 0),
    "green3": (0, 205, 0),
    "green4": (0, 139, 0),
    "green_yellow": (173, 255, 47),
    "grey": (190, 190, 190),
    "grey0": (0, 0, 0),
    "grey1": (3, 3, 3),
    "grey10": (26, 26, 26),
    "grey100": (255, 255, 255),
    "grey11": (28, 28, 28),
    "grey12": (31, 31, 31),
    "grey13": (33, 33, 33),
    "grey14": (36, 36, 36),
    "grey15": (38, 38, 38),
    "grey16": (41, 41, 41),
    "grey17": (43, 43, 43),
    "grey18": (46, 46, 46),
    "grey19": (48, 48, 48),
    "grey2": (5, 5, 5),
    "grey20": (51, 51, 51),
    "grey21": (54, 54, 54),
    "grey22": (56, 56, 56),
    "grey23": (59, 59, 59),
    "grey24": (61, 61, 61),
    "grey25": (64, 64, 64),
    "grey26": (66, 66, 66),
    "grey27": (69, 69, 69),
    "grey28": (71, 71, 71),
    "grey29": (74, 74, 74),
    "grey3": (8, 8, 8),
    "grey30": (77, 77, 77),
    "grey31": (79, 79, 79),
    "grey32": (82, 82, 82),
    "grey33": (84, 84, 84),
    "grey34": (87, 87, 87),
    "grey35": (89, 89, 89),
    "grey36": (92, 92, 92),
    "grey37": (94, 94, 94),
    "grey38": (97, 97, 97),
    "grey39": (99, 99, 99),
    "grey4": (10, 10, 10),
    "grey40": (102, 102, 102),
    "grey41": (105, 105, 105),
    "grey42": (107, 107, 107),
    "grey43": (110, 110, 110),
    "grey44": (112, 112, 112),
    "grey45": (115, 115, 115),
    "grey46": (117, 117, 117),
    "grey47": (120, 120, 120),
    "grey48": (122, 122, 122),
    "grey49": (125, 125, 125),
    "grey5": (13, 13, 13),
    "grey50": (127, 127, 127),
    "grey51": (130, 130, 130),
    "grey52": (133, 133, 133),
    "grey53": (135, 135, 135),
    "grey54": (138, 138, 138),
    "grey55": (140, 140, 140),
    "grey56": (143, 143, 143),
    "grey57": (145, 145, 145),
    "grey58": (148, 148, 148),
    "grey59": (150, 150, 150),
    "grey6": (15, 15, 15),
    "grey60": (153, 153, 153),
    "grey61": (156, 156, 156),
    "grey62": (158, 158, 158),
    "grey63": (161, 161, 161),
    "grey64": (163, 163, 163),
    "grey65": (166, 166, 166),
    "grey66": (168, 168, 168),
    "grey67": (171, 171, 171),
    "grey68": (173, 173, 173),
    "grey69": (176, 176, 176),
    "grey7": (18, 18, 18),
    "grey70": (179, 179, 179),
    "grey71": (181, 181, 181),
    "grey72": (184, 184, 184),
    "grey73": (186, 186, 186),
    "grey74": (189, 189, 189),
    "grey75": (191, 191, 191),
    "grey76": (194, 194, 194),
    "grey77": (196, 196, 196),
    "grey78": (199, 199, 199),
    "grey79": (201, 201, 201),
    "grey8": (20, 20, 20),
    "grey80": (204, 204, 204),
    "grey81": (207, 207, 207),
    "grey82": (209, 209, 209),
    "grey83": (212, 212, 212),
    "grey84": (214, 214, 214),
    "grey85": (217, 217, 217),
    "grey86": (219, 219, 219),
    "grey87": (222, 222, 222),
    "grey88": (224, 224, 224),
    "grey89": (227, 227, 227),
    "grey9": (23, 23, 23),
    "grey90": (229, 229, 229),
    "grey91": (232, 232, 232),
    "grey92": (235, 235, 235),
    "grey93": (237, 237, 237),
    "grey94": (240, 240, 240),
    "grey95": (242, 242, 242),
    "grey96": (245, 245, 245),
    "grey97": (247, 247, 247),
    "grey98": (250, 250, 250),
    "grey99": (252, 252, 252),
    "honeydew": (240, 255, 240),
    "honeydew1": (240, 255, 240),
    "honeydew2": (224, 238, 224),
    "honeydew3": (193, 205, 193),
    "honeydew4": (131, 139, 131),
    "hot_pink": (255, 105, 180),
    "hot_pink1": (255, 110, 180),
    "hot_pink2": (238, 106, 167),
    "hot_pink3": (205, 96, 144),
    "hot_pink4": (139, 58, 98),
    "indian_red": (205, 92, 92),
    "indian_red1": (255, 106, 106),
    "indian_red2": (238, 99, 99),
    "indian_red3": (205, 85, 85),
    "indian_red4": (139, 58, 58),
    "ivory": (255, 255, 240),
    "ivory1": (255, 255, 240),
    "ivory2": (238, 238, 224),
    "ivory3": (205, 205, 193),
    "ivory4": (139, 139, 131),
    "khaki": (240, 230, 140),
    "khaki1": (255, 246, 143),
    "khaki2": (238, 230, 133),
    "khaki3": (205, 198, 115),
    "khaki4": (139, 134, 78),
    "lavender": (230, 230, 250),
    "lavender_blush": (255, 240, 245),
    "lavender_blush1": (255, 240, 245),
    "lavender_blush2": (238, 224, 229),
    "lavender_blush3": (205, 193, 197),
    "lavender_blush4": (139, 131, 134),
    "lawn_green": (124, 252, 0),
    "lemon_chiffon": (255, 250, 205),
    "lemon_chiffon1": (255, 250, 205),
    "lemon_chiffon2": (238, 233, 191),
    "lemon_chiffon3": (205, 201, 165),
    "lemon_chiffon4": (139, 137, 112),
    "light_blue": (173, 216, 230),
    "light_blue1": (191, 239, 255),
    "light_blue2": (178, 223, 238),
    "light_blue3": (154, 192, 205),
    "light_blue4": (104, 131, 139),
    "light_coral": (240, 128, 128),
    "light_cyan": (224, 255, 255),
    "light_cyan1": (224, 255, 255),
    "light_cyan2": (209, 238, 238),
    "light_cyan3": (180, 205, 205),
    "light_cyan4": (122, 139, 139),
    "light_goldenrod": (238, 221, 130),
    "light_goldenrod1": (255, 236, 139),
    "light_goldenrod2": (238, 220, 130),
    "light_goldenrod3": (205, 190, 112),
    "light_goldenrod4": (139, 129, 76),
    "light_goldenrod_yellow": (250, 250, 210),
    "light_gray": (211, 211, 211),
    "light_green": (144, 238, 144),
    "light_grey": (211, 211, 211),
    "light_pink": (255, 182, 193),
    "light_pink1": (255, 174, 185),
    "light_pink2": (238, 162, 173),
    "light_pink3": (205, 140, 149),
    "light_pink4": (139, 95, 101),
    "light_salmon": (255, 160, 122),
    "light_salmon1": (255, 160, 122),
    "light_salmon2": (238, 149, 114),
    "light_salmon3": (205, 129, 98),
    "light_salmon4": (139, 87, 66),
    "light_sea_green": (32, 178, 170),
    "light_sky_blue": (135, 206, 250),
    "light_sky_blue1": (176, 226, 255),
    "light_sky_blue2": (164, 211, 238),
    "light_sky_blue3": (141, 182, 205),
    "light_sky_blue4": (96, 123, 139),
    "light_slate_blue": (132, 112, 255),
    "light_slate_gray": (119, 136, 153),
    "light_slate_grey": (119, 136, 153),
    "light_steel_blue": (176, 196, 222),
    "light_steel_blue1": (202, 225, 255),
    "light_steel_blue2": (188, 210, 238),
    "light_steel_blue3": (162, 181, 205),
    "light_steel_blue4": (110, 123, 139),
    "light_yellow": (255, 255, 224),
    "light_yellow1": (255, 255, 224),
    "light_yellow2": (238, 238, 209),
    "light_yellow3": (205, 205, 180),
    "light_yellow4": (139, 139, 122),
    "lime_green": (50, 205, 50),
    "linen": (250, 240, 230),
    "magenta": (255, 0, 255),
    "magenta1": (255, 0, 255),
    "magenta2": (238, 0, 238),
    "magenta3": (205, 0, 205),
    "magenta4": (139, 0, 139),
    "maroon": (176, 48, 96),
    "maroon1": (255, 52, 179),
    "maroon2": (238, 48, 167),
    "maroon3": (205, 41, 144),
    "maroon4": (139, 28, 98),
    "medium_aquamarine": (102, 205, 170),
    "medium_blue": (0, 0, 205),
    "medium_orchid": (186, 85, 211),
    "medium_orchid1": (224, 102, 255),
    "medium_orchid2": (209, 95, 238),
    "medium_orchid3": (180, 82, 205),
    "medium_orchid4": (122, 55, 139),
    "medium_purple": (147, 112, 219),
    "medium_purple1": (171, 130, 255),
    "medium_purple2": (159, 121, 238),
    "medium_purple3": (137, 104, 205),
    "medium_purple4": (93, 71, 139),
    "medium_sea_green": (60, 179, 113),
    "medium_slate_blue": (123, 104, 238),
    "medium_spring_green": (0, 250, 154),
    "medium_turquoise": (72, 209, 204),
    "medium_violet_red": (199, 21, 133),
    "midnight_blue": (25, 25, 112),
    "mint_cream": (245, 255, 250),
    "misty_rose": (255, 228, 225),
    "misty_rose1": (255, 228, 225),
    "misty_rose2": (238, 213, 210),
    "misty_rose3": (205, 183, 181),
    "misty_rose4": (139, 125, 123),
    "moccasin": (255, 228, 181),
    "navajo_white": (255, 222, 173),
    "navajo_white1": (255, 222, 173),
    "navajo_white2": (238, 207, 161),
    "navajo_white3": (205, 179, 139),
    "navajo_white4": (139, 121, 94),
    "navy": (0, 0, 128),
    "navy_blue": (0, 0, 128),
    "old_lace": (253, 245, 230),
    "olive_drab": (107, 142, 35),
    "olive_drab1": (192, 255, 62),
    "olive_drab2": (179, 238, 58),
    "olive_drab3": (154, 205, 50),
    "olive_drab4": (105, 139, 34),
    "orange": (255, 165, 0),
    "orange1": (255, 165, 0),
    "orange2": (238, 154, 0),
    "orange3": (205, 133, 0),
    "orange4": (139, 90, 0),
    "orange_red": (255, 69, 0),
    "orange_red1": (255, 69, 0),
    "orange_red2": (238, 64, 0),
    "orange_red3": (205, 55, 0),
    "orange_red4": (139, 37, 0),
    "orchid": (218, 112, 214),
    "orchid1": (255, 131, 250),
    "orchid2": (238, 122, 233),
    "orchid3": (205, 105, 201),
    "orchid4": (139, 71, 137),
    "pale_goldenrod": (238, 232, 170),
    "pale_green": (152, 251, 152),
    "pale_green1": (154, 255, 154),
    "pale_green2": (144, 238, 144),
    "pale_green3": (124, 205, 124),
    "pale_green4": (84, 139, 84),
    "pale_turquoise": (175, 238, 238),
    "pale_turquoise1": (187, 255, 255),
    "pale_turquoise2": (174, 238, 238),
    "pale_turquoise3": (150, 205, 205),
    "pale_turquoise4": (102, 139, 139),
    "pale_violet_red": (219, 112, 147),
    "pale_violet_red1": (255, 130, 171),
    "pale_violet_red2": (238, 121, 159),
    "pale_violet_red3": (205, 104, 137),
    "pale_violet_red4": (139, 71, 93),
    "papaya_whip": (255, 239, 213),
    "peach_puff": (255, 218, 185),
    "peach_puff1": (255, 218, 185),
    "peach_puff2": (238, 203, 173),
    "peach_puff3": (205, 175, 149),
    "peach_puff4": (139, 119, 101),
    "peru": (205, 133, 63),
    "pink": (255, 192, 203),
    "pink1": (255, 181, 197),
    "pink2": (238, 169, 184),
    "pink3": (205, 145, 158),
    "pink4": (139, 99, 108),
    "plum": (221, 160, 221),
    "plum1": (255, 187, 255),
    "plum2": (238, 174, 238),
    "plum3": (205, 150, 205),
    "plum4": (139, 102, 139),
    "powder_blue": (176, 224, 230),
    "purple": (160, 32, 240),
    "purple1": (155, 48, 255),
    "purple2": (145, 44, 238),
    "purple3": (125, 38, 205),
    "purple4": (85, 26, 139),
    "red": (255, 0, 0),
    "red1": (255, 0, 0),
    "red2": (238, 0, 0),
    "red3": (205, 0, 0),
    "red4": (139, 0, 0),
    "rosy_brown": (188, 143, 143),
    "rosy_brown1": (255, 193, 193),
    "rosy_brown2": (238, 180, 180),
    "rosy_brown3": (205, 155, 155),
    "rosy_brown4": (139, 105, 105),
    "royal_blue": (65, 105, 225),
    "royal_blue1": (72, 118, 255),
    "royal_blue2": (67, 110, 238),
    "royal_blue3": (58, 95, 205),
    "royal_blue4": (39, 64, 139),
    "saddle_brown": (139, 69, 19),
    "salmon": (250, 128, 114),
    "salmon1": (255, 140, 105),
    "salmon2": (238, 130, 98),
    "salmon3": (205, 112, 84),
    "salmon4": (139, 76, 57),
    "sandy_brown": (244, 164, 96),
    "sea_green": (46, 139, 87),
    "sea_green1": (84, 255, 159),
    "sea_green2": (78, 238, 148),
    "sea_green3": (67, 205, 128),
    "sea_green4": (46, 139, 87),
    "seashell": (255, 245, 238),
    "seashell1": (255, 245, 238),
    "seashell2": (238, 229, 222),
    "seashell3": (205, 197, 191),
    "seashell4": (139, 134, 130),
    "sienna": (160, 82, 45),
    "sienna1": (255, 130, 71),
    "sienna2": (238, 121, 66),
    "sienna3": (205, 104, 57),
    "sienna4": (139, 71, 38),
    "sky_blue": (135, 206, 235),
    "sky_blue1": (135, 206, 255),
    "sky_blue2": (126, 192, 238),
    "sky_blue3": (108, 166, 205),
    "sky_blue4": (74, 112, 139),
    "slate_blue": (106, 90, 205),
    "slate_blue1": (131, 111, 255),
    "slate_blue2": (122, 103, 238),
    "slate_blue3": (105, 89, 205),
    "slate_blue4": (71, 60, 139),
    "slate_gray": (112, 128, 144),
    "slate_gray1": (198, 226, 255),
    "slate_gray2": (185, 211, 238),
    "slate_gray3": (159, 182, 205),
    "slate_gray4": (108, 123, 139),
    "slate_grey": (112, 128, 144),
    "snow": (255, 250, 250),
    "snow1": (255, 250, 250),
    "snow2": (238, 233, 233),
    "snow3": (205, 201, 201),
    "snow4": (139, 137, 137),
    "spring_green": (0, 255, 127),
    "spring_green1": (0, 255, 127),
    "spring_green2": (0, 238, 118),
    "spring_green3": (0, 205, 102),
    "spring_green4": (0, 139, 69),
    "steel_blue": (70, 130, 180),
    "steel_blue1": (99, 184, 255),
    "steel_blue2": (92, 172, 238),
    "steel_blue3": (79, 148, 205),
    "steel_blue4": (54, 100, 139),
    "tan": (210, 180, 140),
    "tan1": (255, 165, 79),
    "tan2": (238, 154, 73),
    "tan3": (205, 133, 63),
    "tan4": (139, 90, 43),
    "thistle": (216, 191, 216),
    "thistle1": (255, 225, 255),
    "thistle2": (238, 210, 238),
    "thistle3": (205, 181, 205),
    "thistle4": (139, 123, 139),
    "tomato": (255, 99, 71),
    "tomato1": (255, 99, 71),
    "tomato2": (238, 92, 66),
    "tomato3": (205, 79, 57),
    "tomato4": (139, 54, 38),
    "turquoise": (64, 224, 208),
    "turquoise1": (0, 245, 255),
    "turquoise2": (0, 229, 238),
    "turquoise3": (0, 197, 205),
    "turquoise4": (0, 134, 139),
    "violet": (238, 130, 238),
    "violet_red": (208, 32, 144),
    "violet_red1": (255, 62, 150),
    "violet_red2": (238, 58, 140),
    "violet_red3": (205, 50, 120),
    "violet_red4": (139, 34, 82),
    "wheat": (245, 222, 179),
    "wheat1": (255, 231, 186),
    "wheat2": (238, 216, 174),
    "wheat3": (205, 186, 150),
    "wheat4": (139, 126, 102),
    "white": (255, 255, 255),
    "white_smoke": (245, 245, 245),
    "yellow": (255, 255, 0),
    "yellow1": (255, 255, 0),
    "yellow2": (238, 238, 0),
    "yellow3": (205, 205, 0),
    "yellow4": (139, 139, 0),
    "yellow_green": (154, 205, 50),
}
COLOR_NAMES = list(COLORS)
