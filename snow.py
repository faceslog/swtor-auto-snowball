import pyautogui
import time
import keyboard
import pygetwindow as gw
import os

# ------------------- Utility Functions -------------------
def bring_window_to_foreground(window_title):
    """
    Activate the specified window and bring it to the foreground.
    """
    try:
        windows = gw.getWindowsWithTitle(window_title)
        if windows:
            windows[0].activate()
    except Exception as e:
        print(f"Error bringing window to foreground: {e}")
        available_windows = gw.getAllTitles()
        print(f"Available windows: {available_windows}")
        exit()

def locate_and_click(image_path, confidence=0.8, right_click=False):
    """
    Locate an image on the screen and perform a click action.
    """
    try:
        location = pyautogui.locateCenterOnScreen(image_path, confidence=confidence)
        if location:
            if right_click:
                pyautogui.rightClick(location)
            else:
                pyautogui.click(location)

            time.sleep(0.5)  # Short delay after clicking
            return location
    except pyautogui.ImageNotFoundException:
        return None
    return None

def process_icon_and_debuff(icon_path, debuff_path, cooldown, last_action_time):
    """
    Handle the process of interacting with an icon and its debuff.
    """
    current_time = time.time()
    if current_time - last_action_time >= cooldown:
        if locate_and_click(icon_path, confidence=0.6):
            locate_and_click(debuff_path, confidence=0.8, right_click=True)
            return current_time
        else:
            print(f"Could not locate icon on the screen. Maybe was not ready yet, retrying ...")
    return last_action_time

# ------------------- Main Automation Logic -------------------
def automate_actions(cannon_icon, cannon_debuff, snowball_icon, snowball_debuff, cooldown_cannon, cooldown_snowball, accept_button, window_title):
    """
    Automates the process of interacting with icons and accepting packages.
    """
    last_action_cannon = 0
    last_action_snowball = 0
    packages_collected = 0

    print("Automation running. Press 'Q' to quit.")
    bring_window_to_foreground(window_title)

    while True:
        if keyboard.is_pressed('q'):
            print("Exiting program...")
            break

        # Process cannon icon and debuff
        last_action_cannon = process_icon_and_debuff(
            cannon_icon, cannon_debuff, cooldown_cannon, last_action_cannon
        )

        # Process accept button
        if locate_and_click(accept_button, confidence=0.8):
            packages_collected += 1

        # Process snowball icon and debuff
        last_action_snowball = process_icon_and_debuff(
            snowball_icon, snowball_debuff, cooldown_snowball, last_action_snowball
        )

        # Process accept button again
        if locate_and_click(accept_button, confidence=0.8):
            packages_collected += 1

        time.sleep(1)

    print(f"Total packages collected: {packages_collected}")

# ------------------- Entry Point -------------------
if __name__ == "__main__":
    # Paths to your icon images
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    cannon_icon_path = os.path.join(base_dir, "assets/icon1.JPG")
    cannon_debuff_path = os.path.join(base_dir, "assets/debuff1.JPG")
    snowball_icon_path = os.path.join(base_dir, "assets/icon2.JPG")
    snowball_debuff_path = os.path.join(base_dir, "assets/debuff2.JPG")
    accept_button_path = os.path.join(base_dir, "assets/accept.JPG")

    # Cooldown times in seconds
    cooldown_cannon = 7
    cooldown_snowball = 14

    print("Starting in 5 seconds. Press 'Q' to quit once launched...")
    time.sleep(5)

    application_window_title = "Star Wars™: The Old Republic™"

    print("Launching automation!")
    
    automate_actions(
        cannon_icon_path,
        cannon_debuff_path,
        snowball_icon_path,
        snowball_debuff_path,
        cooldown_cannon,
        cooldown_snowball,
        accept_button_path,
        application_window_title
    )
