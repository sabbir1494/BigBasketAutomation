import os
from datetime import datetime


class ScreenshotUtils:

    @staticmethod
    def capture(driver, name):

        screenshot_directory = "screenshots"

        if not os.path.exists(screenshot_directory):
            os.makedirs(screenshot_directory)

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        file_name = f"{name}_{timestamp}.png"

        file_path = os.path.join(
            screenshot_directory,
            file_name
        )

        driver.save_screenshot(file_path)

        return file_path