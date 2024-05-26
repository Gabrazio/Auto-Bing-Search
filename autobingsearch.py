from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import nltk
import random

edge_options = webdriver.EdgeOptions()
driver = webdriver.Edge(options=edge_options)
words = nltk.corpus.words.words()

while True:
    try:
        searches = int(input("[ABS] How many searches do you want to make? > "))
    except ValueError:
        print("[ABS] Invalid input, please enter a number!")
        continue;
    break;

print("[ABS] Ok, I'll do " + str(searches) + " searches for you!")
i = 0

while(i < searches):
    driver.get("https://www.bing.com/")
    form = driver.find_element(By.ID, "sb_form_q")
    form.send_keys(random.choice(words) + " " + random.choice(words))
    time.sleep(4)
    form.send_keys('\ue007')
    time.sleep(2)
    i = i + 1
    print("[ABS] Searches completed: " + str(i))
    
print("[ABS] Finish! :)")
driver.quit()


    
