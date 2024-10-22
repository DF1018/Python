from functools import reduce
import os
from script import Crawler
from script import userinfo
from script.Crawler import IG_Crawler
from script.userinfo import USERNAME, PASSWORD

def pipe(arg, *functions):
    return reduce(lambda result, func: func(result), functions, arg)

def Crawler(_link=None):
    target_id = " "
    _link = _link or 'https://www.instagram.com/'
    now_path = r"C:\Users\user\Documents\My program\Python\Hacking\IG_hacking"
    os.chdir(now_path)

    # 初始化 IG_Crawler 並進行操作
    IC = IG_Crawler(_link=_link, target_id=target_id, folder_name=now_path)
    IC.ig_login(USERNAME=USERNAME, PASSWORD=PASSWORD)
    img_src = IC.ig_get_avatar()
    IC.download_img(img_src)
    return None  # 這裡返回 None 或其他默認值作為下一個函數的輸入

def pipeline():
    result = pipe(None, Crawler)
    return result

if __name__ == "__main__":
    pipeline()