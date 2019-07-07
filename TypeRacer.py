#! python3

import time
import random
from selenium import webdriver

class TypeRacerPublicGame(webdriver.Chrome):
    def __init__(self, element_wait = 30):
        super().__init__() #Inherit methods from webdriver.Chrome class
        self.get('https://play.typeracer.com/')
        self.implicitly_wait(element_wait)

    def click_start_race(self):
        self.find_element_by_xpath("//a[contains(text(),'Enter a typing race')]").click()
    
    def get_typing_string(self):
        #Absolute paths are used since CSS id's are randomized
        first_word_path = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[2]/td[2]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[2]/td[3]/table[1]/tbody[1]/tr[2]/td[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[1]/td[1]/div[1]/div[1]/span[1]'
        first_word__path_part2 = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[2]/td[2]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[2]/td[3]/table[1]/tbody[1]/tr[2]/td[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[1]/td[1]/div[1]/div[1]/span[2]'
        following_string_path = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[2]/td[2]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[2]/td[3]/table[1]/tbody[1]/tr[2]/td[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[1]/td[1]/div[1]/div[1]/span[3]'
        
        first_word = self.find_element_by_xpath(first_word_path).text
        first_word = first_word + self.find_element_by_xpath(first_word__path_part2).text
        following_string = self.find_element_by_xpath(following_string_path).text
        
        full_string = f'{first_word} {following_string}'
        return(full_string)
    
    def start_typing(self, wait_interval_begin = 0.05, wait_interval_end = 0.20):
        typing_box = self.find_element_by_xpath("//input[@class='txtInput']")
        random_wait = random.uniform(wait_interval_begin, wait_interval_end)
        full_string = self.get_typing_string()
        for string in full_string.split():
            for letter in string:
                time.sleep(random_wait)
                typing_box.send_keys(letter)
            typing_box.send_keys(' ')
            
def main():
    public_game = TypeRacerPublicGame()
    public_game.click_start_race()
    public_game.get_typing_string()
    public_game.start_typing(wait_interval_begin = 0.01, wait_interval_end = 0.05)
    
if __name__ == '__main__':
    main()