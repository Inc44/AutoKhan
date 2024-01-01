# watcher
import pyautogui
import webbrowser
import time
import pytesseract
import re
import urllib.request
def youtube_connection():
    try:
        return urllib.request.urlopen('youtube.com', timeout=5).status == 200
    except:
        return False

import os
def windows():
    return True if os.name == 'nt' else False
if not youtube_connection():
    click_coordinates = (490, 800)
    region = (510, 790, 90, 20)
    url_file_path = "links.txt"
    with open(url_file_path, "r", encoding="utf-8") as file:
        urls_to_process = [line.strip() for line in file if line.strip()]
    for url in urls_to_process:
        try:
            webbrowser.open(url)
            time.sleep(6)
            pyautogui.click(click_coordinates)
            screenshot = pyautogui.screenshot(region=region)
            screenshot.save("test.png")
            ocr_result = pytesseract.image_to_string(screenshot)
            time_part = ocr_result.split(" / ")[1]
            time_part_cleaned = cleaned_var = re.sub(r"[^0-9:]", "", time_part)
            minutes, seconds = map(int, time_part_cleaned.split(":"))
            total_seconds = minutes * 60 + seconds
            adjustment_seconds = total_seconds + 6
            time.sleep(adjustment_seconds)
            pyautogui.hotkey("ctrl", "w")
        except IndexError as exception:
            print(exception)
elif windows():
    click_coordinates = (1725, 650)
    target_color = (25, 100, 242)
    play_region = (45, 1400, 30, 30)
else:
    click_coordinates = (1900, 580)
    target_color = (24, 101, 242)
    play_region = (45, 1395, 40, 40)
region = (140, 1400, 160, 30)
url_file_path = "links.txt"
play_image_path = "play.png"
with open(url_file_path, "r", encoding="utf-8") as file:
    urls_to_process = [line.strip() for line in file if line.strip()]
for url in urls_to_process:
    try:
        webbrowser.open(url)
        time.sleep(6)
        if pyautogui.screenshot().getpixel(click_coordinates) == target_color:
            pyautogui.click(click_coordinates)
        time.sleep(1)
        pyautogui.doubleClick(click_coordinates)
        time.sleep(1)
        pyautogui.press("0")
        time.sleep(1)
        start = pyautogui.position()
        pyautogui.moveTo(start[0] - 40, start[1], duration=0.5)
        pyautogui.moveTo(start[0], start[1], duration=0.5)
        screenshot = pyautogui.screenshot(region=region)
        screenshot.save("test.png")
        try:
            play_required = pyautogui.locateOnScreen(
                play_image_path, region=play_region, confidence=0.9
            )
        except:
            play_required = None
        if play_required != None:
            pyautogui.press("k")
        ocr_result = pytesseract.image_to_string(screenshot)
        time_part = ocr_result.split(" / ")[1]
        time_part_cleaned = cleaned_var = re.sub(r"[^0-9:]", "", time_part)
        minutes, seconds = map(int, time_part_cleaned.split(":"))
        total_seconds = minutes * 60 + seconds
        adjustment_seconds = total_seconds / 2 + 6
        time.sleep(adjustment_seconds)
        pyautogui.hotkey("ctrl", "w")
    except IndexError as exception:
        print(exception)