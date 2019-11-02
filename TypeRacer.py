#! python3

import time
import random
import os
from selenium import webdriver

class TypeRacerPublicGame(webdriver.Chrome):
    def __init__(self, private_game_url = False, element_wait = 30):
        super().__init__() #Inherit methods from webdriver.Chrome class
        if private_game_url == False:
            self.get('https://play.typeracer.com/')
            self.private_game = False
        else:
            self.private_game = True
            self.get(private_game_url)
        self.implicitly_wait(element_wait)

    def click_start_race(self):
        if self.private_game == False:
            self.find_element_by_xpath("//a[contains(text(),'Enter a typing race')]").click()
        else:
            self.find_element_by_xpath("//a[@class='raceAgainLink']").click()
    
    def get_typing_string(self):
        #Absolute paths are used since CSS classes and element id are randomzied
        if self.private_game == False:
            first_word_path = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[2]/td[2]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[2]/td[3]/table[1]/tbody[1]/tr[2]/td[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[1]/td[1]/div[1]/div[1]/span[1]'
            first_word__path_part2 = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[2]/td[2]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[2]/td[3]/table[1]/tbody[1]/tr[2]/td[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[1]/td[1]/div[1]/div[1]/span[2]'
            following_string_path = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[2]/td[2]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[2]/td[3]/table[1]/tbody[1]/tr[2]/td[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[1]/td[1]/div[1]/div[1]/span[3]'
        else:
            first_word_path =  '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[2]/td[2]/div[1]/div[1]/table[1]/tbody[1]/tr[3]/td[1]/div[1]/div[1]/table[1]/tbody[1]/tr[2]/td[3]/table[1]/tbody[1]/tr[2]/td[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[1]/td[1]/div[1]/div[1]/span[1]'
            first_word__path_part2 = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[2]/td[2]/div[1]/div[1]/table[1]/tbody[1]/tr[3]/td[1]/div[1]/div[1]/table[1]/tbody[1]/tr[2]/td[3]/table[1]/tbody[1]/tr[2]/td[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[1]/td[1]/div[1]/div[1]/span[2]'
            following_string_path = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[2]/td[2]/div[1]/div[1]/table[1]/tbody[1]/tr[3]/td[1]/div[1]/div[1]/table[1]/tbody[1]/tr[2]/td[3]/table[1]/tbody[1]/tr[2]/td[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[1]/td[1]/div[1]/div[1]/span[3]'
            
        
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
    os.chdir("C:/Users/Josiah/Documents/Song-Lyric-Script")
    public_game = TypeRacerPublicGame()
    public_game.click_start_race()
    public_game.get_typing_string()
    public_game.start_typing(wait_interval_begin = 0.01, wait_interval_end = 0.06)
    
if __name__ == '__main__':
    main()
   
    