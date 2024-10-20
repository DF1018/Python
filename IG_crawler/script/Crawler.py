from DrissionPage import ChromiumPage
from userinfo import USERNAME,PASSWORD
import requests
import os


class IG_Crawler:
    def __init__(self,_link:str,target_id:str,folder_name:str) -> None:
        self.cp = ChromiumPage()
        self._link=_link
        self.target_id = target_id
        self.folder_name = folder_name
    

    def ig_login(self, USERNAME: str, PASSWORD: str) -> None:
        try:
            cp = self.cp
            cp.get(self._link)
            # 嘗試找到用戶名輸入框，如果找不到則已經登入
            username_input = cp.ele('._aa4b _add6 _ac4d _ap35')
            if username_input:
                username_input.input(USERNAME)
                password_input = cp.ele('._aa4b _add6 _ac4d _ap35')
                password_input.input(PASSWORD)
                cp.ele('css:._acan._acap._acas._aj1-._ap30').click()
                print("\n---------------success login-------------------\n")
            else:
                raise Exception("Already logged in")
        except Exception as e:
            print("\n---------------already login-------------------\n")
            return None


    def ig_get_avatar(self) -> str:
        cp = self.cp
        _link = self._link
        target_id = self.target_id
        
        target_link = _link + target_id + "/"
        cp.get(target_link)
        try:
            img_src=cp.ele(f"@alt={target_id}的大頭貼照").attr("src")
        except:
            img_src=cp.ele("@alt^大頭貼照").attr("src")
        
        with open( self.folder_name + "/" + "target_info.py","w+",encoding="utf-8") as f:
            f.write("avatar = '"+img_src+"'")
        f.close()
        
        print(img_src)
        print("\n------------------success get avatar & updata------------------------\n")
        return img_src
        
    def download_img(self, img_url:str) -> None:
        # 使用requests發送HTTP GET請求獲取圖片數據
        response = requests.get(img_url)
        if response.status_code == 200:
            # 構造保存圖片的文件名
            folder_path = os.path.join(self.folder_name, self.target_id)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            
            file_name = folder_path + "/" + self.target_id + "_" + ".jpg"
            with open(file_name, 'wb') as f:
                for chunk in response.iter_content(1024):
                    f.write(chunk)
            print(f"Image saved as {file_name}")
        else:
            print(f"Failed to download image from {img_url}")  


def main():
    target_id = ""
    _link = 'https://www.instagram.com/'
    now_path = r"C:\Users\user\Documents\My program\Python\Hacking\IG_hacking"
    os.chdir(now_path)
    
    IC=IG_Crawler(_link=_link,target_id=target_id,folder_name=now_path)
    #IC.ig_login(USERNAME=USERNAME,PASSWORD=PASSWORD)
    img_src=IC.ig_get_avatar()
    IC.download_img(img_src)
        
        
if __name__ == "__main__":
    main()