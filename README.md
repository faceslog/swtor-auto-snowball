# Automation Script for Star Wars™: The Old Republic™ during the snowball event

![Farming Parcels](assets/demo.gif)

## Prerequisites

1. **Install Python**:
   - Ensure Python is installed and added to your system PATH.
   - You can download Python from [python.org](https://www.python.org/).

2. **Install Required Dependencies**:

   - Create a virtual env and activate it:
     ```sh
     python -m venv myenv
     myenv/Scripts/Activate.ps1
     ```

   - Install the dependencies by running:
     ```
     pip install -r requirements.txt
     ```

## Setup

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

## Running the Script

1. **In-Game Preparations**:
   - Go to your stronghold or a safe area in the game where you won't be interrupted.
   - Place the **cannon** and **snowball** actions on your quickbars.
   - Ensure you have a pet summoned and set it as your target.
   - Make sure you are within range to use the cannon.
   - If possible use the interface provided as `assets/ui.xml` in this repo

2. **Start the Script**:
   - Run the script from your terminal or IDE:
     ```
     python snow.py
     ```
   - The script will start after a 5-second delay.

3. **How It Works**:
   - The script will:
     1. Use the cannon and click its debuff.
     2. Use the snowball and click its debuff.
     3. Continuously accept parcels as they appear.

3. **Stop the Script**:
   - Press the `Q` key at any time to safely exit the program.

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

