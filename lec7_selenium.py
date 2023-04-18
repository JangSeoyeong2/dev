import mypw
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


from selenium.webdriver.common.by import By


from selenium.webdriver.common.keys import Keys
# 터미널에 pip install pyperclip 설치하고 실행
import pyperclip
import time


#크롬 드라이버 업데이트
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

#웹 페이지로 이동
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com")

# 아이디 입력
id =driver.find_element(By.CSS_SELECTOR, "#id")
id.click()
#id.send_keys("dlswls39")
pyperclip.copy('dlswls39')
id.send_keys(Keys.CONTROL, 'v' )
time.sleep(2)

#비밀번호 입력
pw = driver.find_element(By.CSS_SELECTOR, "#pw")
pw.click()
# pw.send_keys(mypw.naver_pw)
pyperclip.copy(mypw.naver_pw)
pw.send_keys(Keys.CONTROL, 'v')
time.sleep(2)


input()