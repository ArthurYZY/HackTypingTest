import typing
import sys
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

wpm = 300

options = webdriver.ChromeOptions()
driver_path = "./chromedriver.exe"
driver = webdriver.Chrome(driver_path, options=options)

def get_typing_list(word_box):
    typing_list = []
    words = words_box.find_elements_by_class_name("word")
    for word in words:
        letters = [i.get_attribute('innerHTML') for i in word.find_elements_by_class_name("letter")]
        typing_list.extend(letters)
        typing_list.append(Keys.SPACE)

    return typing_list


def typing(typing_list, wpm=100):
    typing_area = driver.find_element_by_class_name("hidden-input")
    word_cnt = sum([1 for i in typing_list if i == Keys.SPACE])
    stride = word_cnt / wpm * 60 / len(typing_list)
    print(len(typing_list), stride)
    print(len(typing_list) * stride)
    delay = 18 / 1000
    for letter in typing_list:
        typing_area.send_keys(letter)
        sleep(max(stride - delay, 0))


if __name__ == '__main__':
    driver.get("https://barneyzhao.gitee.io/typing-cn/#/monkey")
    words_box = driver.find_element_by_class_name("words-box")
    typing_list = get_typing_list(words_box)
    
    typing(typing_list, wpm)