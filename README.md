# Automation Script for Star Wars™: The Old Republic™ during the snowball event

![Farming Parcels](assets/demo.gif)

[![Download Exe](https://custom-icon-badges.demolab.com/badge/-Download-blue?style=for-the-badge&logo=download&logoColor=white "Download exe")](https://github.com/faceslog/swtor-auto-snowball/releases/download/latest/snow.exe)

## A) Prerequisites (You can skip this step if you use the build from the release page)

1. **Install Python**:
   - Ensure Python is installed and added to your system PATH.
   - You can download Python from [python.org](https://www.python.org/).

2. **Install Required Dependencies**:
   - Open a terminal as admin (required for swtor autoclick for some users)
   - Create a virtual env and activate it using powershell:
     ```sh
     python -m venv myenv
     # For powershell use .ps1 for cmd use .bat 
     myenv/Scripts/Activate.ps1
     ```

   - Install the dependencies by running:
     ```
     pip install -r requirements.txt
     ```

## B) Running the Script

1. **In-Game Preparations**:
   - Go to your stronghold or a safe area in the game where you won't be interrupted.
   - Place the **cannon** and **snowball** actions on your quickbars.
   - Ensure you have a pet summoned and set it as your target.
   - Make sure you are within range to use the cannon and snowball (around +1m).
   - If possible use the interface provided as `assets/ui.xml` in this repo

2. **Start the Script**:
   - If using the script run the script from your terminal or IDE:
     ```
     python snow.py
     ```
   - If using the .exe just launch it (sometimes you need to launch it as admin if it cannot get the focus of the window on swtor happens with autoclicker)
   - The script will start after a 5-second delay.

3. **How It Works**:
   - The script will:
     1. Use the cannon and click its debuff.
     2. Use the snowball and click its debuff.
     3. Continuously accept parcels as they appear.

3. **Stop the Script**:
   - Long Press (2sec) the `Q` key at any time to safely exit the program.

## Good to know:

1. **Image Assets**:
   - Place images of your cannon, snowball, debuffs, and accept button in the same directory as the script.
   - Ensure the images are named correctly:
     - `icon1.JPG`: Image of the cannon.
     - `debuff1.JPG`: Image of the cannon debuff.
     - `icon2.JPG`: Image of the snowball.
     - `debuff2.JPG`: Image of the snowball debuff.
     - `accept.JPG`: Image of the accept button for the parcels.

2. **Cooldown Times**:
   - Adjust the cooldowns in the script if needed:
     - Default cannon cooldown: **6 seconds**.
     - Default snowball cooldown: **14 seconds**.

## Notes

- Ensure the game is running in a resolution and settings where the icons and buttons are clearly visible for the script to identify them.
- If an icon or button is not detected, update the corresponding image to better match the in-game appearance.
- This script is designed to automate repetitive tasks. Use responsibly and ensure compliance with game rules to avoid any violations.

## Troubleshooting

- **Window Not Found**:
  - Ensure the game window title matches the one specified in the script (`Star Wars™: The Old Republic™`).
  - Check your open windows and update the `application_window_title` variable in the script if necessary.

- **Icons Not Detected**:
  - Verify that the images match the in-game icons.
  - Ensure the game is not running in a minimized state or on a secondary monitor.

## Disclaimer

This script is provided as-is without any guarantees. Use at your own discretion and risk. The creators are not responsible for any consequences arising from the use of this script.

