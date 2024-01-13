# watcher (pip install -r requirements.txt --upgrade)
import os
import time
import webbrowser
import re
import pyautogui
import pytesseract
import urllib.request


def is_youtube_accessible():
    try:
        return urllib.request.urlopen("http://youtube.com", timeout=5).status == 200
    except:
        return False


def is_windows():
    return os.name == "nt"


def read_urls(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return [line.strip() for line in file if line.strip()]


def extract_time_from_screenshot(screenshot):
    ocr_result = pytesseract.image_to_string(screenshot)
    time_part = ocr_result.split(" / ")[1]
    cleaned_time = re.sub(r"[^0-9:]", "", time_part)
    minutes, seconds = map(int, cleaned_time.split(":"))
    if is_youtube_accessible():
        return (minutes * 60 + seconds)/2
    else:
        return minutes * 60 + seconds


url_file_path = "links.txt"
urls_to_process = read_urls(url_file_path)

if not is_youtube_accessible():
    click_coordinates = (1720, 720)
    region = (75, 1375, 90, 20)
    play_region = (45, 1385)
    for url in urls_to_process:
        try:
            webbrowser.open(url)
            time.sleep(6)
            pyautogui.doubleClick(click_coordinates)
            time.sleep(0.5)
            screenshot = pyautogui.screenshot(region=region)
            pyautogui.click(click_coordinates)
            screenshot.save("test.png")
            adjustment_seconds = extract_time_from_screenshot(screenshot)
            time.sleep(adjustment_seconds)
            pyautogui.hotkey("ctrl", "w")
        except IndexError as exception:
            print(exception)
else:
    click_coordinates = (1900, 580)
    if is_windows():
        target_color = (25, 100, 242)
        play_region = (45, 1400, 30, 30)
    else:
        target_color = (24, 101, 242)
        play_region = (45, 1395, 40, 40)
    region = (140, 1400, 160, 30)
    play_image_path = "play.png"
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
            adjustment_seconds = extract_time_from_screenshot(screenshot)
            time.sleep(adjustment_seconds)
            pyautogui.hotkey("ctrl", "w")
        except IndexError as exception:
            print(exception)
