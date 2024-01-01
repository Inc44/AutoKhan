# pip install PyAutoGUI
# pip install opencv-python
import pyautogui
import pyperclip
import numpy
import time
import os


def windows():
    return True if os.name == "nt" else False


class ScreenProcessor:
    def __init__(self, search_region, link_region):
        self.search_region = search_region
        self.link_region = link_region
        self.links = set()

    def process_matches(self, matches, link_image_path):
        for match in matches:
            center = pyautogui.center(match)
            pyautogui.moveTo(center.x - 12, center.y)
            pyautogui.click(button="right")
            if not windows():
                time.sleep(0.3)
            link_match = pyautogui.locateOnScreen(
                link_image_path, region=self.link_region
            )
            if link_match:
                link_center = pyautogui.center(link_match)
                pyautogui.moveTo(link_center.x - 12, link_center.y)
                pyautogui.click()
                self.links.add(pyperclip.paste())

    def is_screen_unchanged(self, threshold=0.01):
        before_scroll = pyautogui.screenshot(region=self.search_region)
        pyautogui.scroll(-700) if windows() else pyautogui.scroll(-10)
        after_scroll = pyautogui.screenshot(region=self.search_region)
        difference = numpy.sum(numpy.array(before_scroll) != numpy.array(after_scroll))
        return difference / numpy.prod(self.search_region[2:]) < threshold

    def run(self, image_paths):
        while True:
            for image_path in image_paths:
                matches = pyautogui.locateAllOnScreen(
                    image_path, region=self.search_region
                )
                try:
                    self.process_matches(matches, "link.png")
                except:
                    continue
            if self.is_screen_unchanged():
                break

        with open("links.txt", "a", encoding="utf-8") as file:
            for link in self.links:
                file.write(link + "\n")
        print(f"Saved {len(self.links)} unique links to links.txt")


# image_paths = ["article.png", "article_done.png", "video.png", "video_done.png", "video_half_done.png", "video_review.png"]
# image_paths = ["article.png", "video.png", "video_half_done.png", "video_review.png"] #NOT DONE
image_paths = ["article_done.png", "video_done.png"]  # DONE
search_region = (475, 115, 45, 1300) if windows() else (470, 145, 50, 1270)
link_region = (475, 115, 45, 1300) if windows() else (470, 145, 70, 1270)
processor = ScreenProcessor(search_region=search_region, link_region=link_region)
processor.run(image_paths)
