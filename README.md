# 2v2Game
# Epic 2 vs 2 Battle Game

This project is a simple graphical user interface (GUI) for a 2 vs 2 battle game implemented using Python's Tkinter library. Players can set up two teams, each with two characters of different types (Warrior, Mage, Archer), and watch them battle it out.

## Features

* **Team Setup:** Allows users to name two teams and select the type for each of the two characters in each team.
* **Character Types:** Supports three character types: Warrior, Mage, and Archer, each with potentially different stats and abilities (defined in the `game_logic.py` file).
* **Visual Battle:** Displays the battle progress in a text output area, showing attacks, special abilities, and character health.
* **Health Bars:** Provides visual health bars for each character, updating in real-time during the battle.
* **Turn-Based System:** The battle proceeds in turns, with teams alternating attacks.
* **Random Actions:** Characters randomly choose between a basic attack and a special ability during their turn.
* **Background Image:** Features a visually appealing background image for the game window.
* **Styled GUI:** Utilizes `ttk` widgets and custom styles for a more modern and user-friendly interface.

## Technologies Used

* **Python:** The primary programming language.
* **Tkinter:** Python's standard GUI library for creating the graphical interface.
* **tkinter.ttk:** The themed Tkinter widgets, providing a more modern look and feel.
* **PIL (Pillow):** Python Imaging Library used for handling and displaying the background image.
* **random:** For randomizing character actions during the battle.
* **game\_logic.py:** (Expected) A separate Python file containing the logic for characters, teams, and battle mechanics.

## Installation

1.  **Clone the repository:**
    ```bash
    git clone <YOUR_REPOSITORY_URL>
    cd <YOUR_REPOSITORY_NAME>
    ```

2.  **Install the necessary libraries:**
    ```bash
    pip install Pillow
    ```
    *(Note: Ensure you have a `game_logic.py` file in the same directory with the necessary classes (Character, Warrior, Mage, Archer, Team) and their logic.)*

## Running the Game

1.  **Execute the main script:**
    ```bash
    python your_script_name.py  # Replace 'your_script_name.py' with the actual name of this file
    ```
    This will open the game window.

2.  **Set up the teams:**
    * Enter names for Team 1 and Team 2.
    * Use the dropdown menus to select the character type for each of the four characters.

3.  **Start the battle:**
    * Click the "Start Battle!" button to begin the simulation.
    * The battle progress, including attacks and health updates, will be displayed in the output text area.
    * Health bars will update dynamically.
    * A message box will appear announcing the winning team when the battle ends.



**Note:** Make sure to replace `/Users/angela.plescia/Desktop/Biomedical Project/2v2Game.jpg` in the `GameGUI` class with the correct path to your background image for the application to run without errors. If the image is not found, the game will use a default background color.

## Potential Improvements

* **More Detailed Game Logic:** Implement more complex battle mechanics, character stats, and special abilities in `game_logic.py`.
* **Character Names:** Allow users to name individual characters.
* **Visual Battle Display:** Enhance the visual representation of the battle with animations or more detailed output.
* **Character Stats Display:** Show character stats (health, attack, etc.) in the GUI.
* **Turn Indicator:** Clearly indicate whose turn it is during the battle.
* **Logging:** Implement logging of the battle events to a file.
* **Error Handling:** Add more robust error handling for invalid inputs.
* **Configuration File:** Allow customization of character types and their initial stats through a configuration file.

## Author
[AngelaPle]

