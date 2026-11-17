
# Fix-It Felix Jr. — Reimplementation of the famous 2D Arcade Game

## 1. Project Overview

**Fix-It Felix Jr.** is a 2D arcade game inspired by the classic arcade game of the same name.

The player controls Felix, whose mission is to repair damaged windows throughout a building while avoiding obstacles and dealing with damage caused by Ralph.

The project was developed using Python and Pygame, applying Object-Oriented Programming (OOP) principles to organize game mechanics, character behaviors, and interactions.

## 2. Game Features

- **Player Movement:** Control Felix and navigate through different building levels.
- **Window Repair System:** Repair all broken windows to complete the objective.
- **Enemy Mechanics:** Ralph breaks at least one window on each floor, with a total of 8 broken windows, and then drops bricks to fall onto Felix by staying on the roof.
- **Collision Detection:** Detect interactions between characters, objects, and the environment.
- **Time Limit:** Complete all window repairs within 60 seconds without losing 3 lives given.
- **Life System:** The player must maintain at least one remaining life to win.
- **Win Condition:** Successfully repair all broken windows within 60 seconds while having at least one life remaining.
- **Lose Condition:** The game ends if the player loses all lives or the timer reaches zero while broken windows remain.

## 3. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Pygame | Game development and graphics |
| OOP | Game architecture and code organization |
| Git & GitHub | Version control and collaboration |

## 4. Project Structure

The project is organized into separate modules and packages, with each file responsible for specific aspects of the game. This modular structure improves code organization, maintainability, and separation of responsibilities.

```text
fix-it-felix-pygame/
│
├── main.py
├── config.py
├── events.py
├── .gitignore
├── AI_LOG.md
│
├── entities/
│   ├── game_object.py
│   ├── player.py
│   ├── ralph.py
│   ├── building.py
│   ├── window.py
│   └── brick.py
│
├── managers/
│   ├── game_manager.py
│   └── sound_manager.py
│
├── states/
│   ├── game_state.py
│   ├── menu_state.py
│   ├── playing_state.py
│   ├── win_state.py
│   └── lose_state.py
│
├── assets/
│   ├── audio/
│   │   ├── backgroundsound.mp3
│   │   ├── felixgetsdamage.wav
│   │   ├── felixrepair.wav
│   │   ├── lose.wav
│   │   ├── ralphdestory.wav
│   │   ├── ralphdestorywindow.wav
│   │   └── win.wav
│   │
│   └── images/
│       ├── background/
│       ├── characters/
│       │   ├── felix/
│       │   └── ralph/
│       ├── objects/
│       └── windows/
│
└── docs/
    └── fix_it_felix_jr_classdiagram.drawio.png
```

### Main Files and Their Responsibilities

**Root Files**

- **main.py:** Entry point of the application. Initializes Pygame, creates the game window, and starts the GameManager.
- **config.py:** Stores game constants, settings, dimensions, speeds, and configuration values.
- **events.py:** Defines custom Pygame events used for communication between game components.
- **.gitignore:** Specifies files and directories that Git should ignore.
- **AI_LOG.md:** Documents the use of AI assistance during project development.

**entities/ – Game Objects**

- **game_object.py:** Defines the abstract base class for physical game objects, providing common attributes and behaviors.
- **player.py:** Handles Felix's movement, window repair actions, lives, and player-related behaviors.
- **ralph.py:** Controls Ralph's introduction, rooftop movement, window destruction, and brick attacks.
- **building.py:** Manages the building structure, windows, roof, and repair progress.
- **window.py:** Represents individual windows and manages their repair conditions and states.
- **brick.py:** Handles falling bricks, movement, and collision detection with the player.

**managers/ – Game Management**

- **game_manager.py:** Controls the main game loop, overall game flow, application-level event handling, and transitions between game states.
- **sound_manager.py:** Manages background music and sound effects triggered by game events.

**states/ – Game States**

- **game_state.py:** Defines the abstract base class for all game states, establishing a common interface.
- **menu_state.py:** Manages the main menu and starting the game.
- **playing_state.py:** Coordinates gameplay logic and interactions between game entities, including player input, updates, collisions, difficulty progression, and win/lose conditions.
- **win_state.py:** Displays the screen when the player successfully completes the game.
- **lose_state.py:** Displays the game-over screen when the player loses.

**assets/ – Game Resources**

- **audio/:** Contains background music and sound effects.
- **images/:** Contains visual resources such as images for game objects, characters, and background.

**docs/ – Documentation**

- Contains the UML class diagram illustrating the project's class structure and relationships.


## 5. Object-Oriented Programming Concepts

The project demonstrates several important OOP principles:

### Encapsulation
Groups related attributes and methods within classes, keeping game object data and behaviors organized.

### Abstraction
Hides complex implementation details behind simple methods and interfaces, making game components easier to use.

### Inheritance
Allows specialized classes to reuse attributes and behaviors from parent classes, reducing code duplication.

### Polymorphism
Allows different objects to respond to the same method call in their own ways, supporting flexible game behavior.

### Composition
Builds complex game components by combining independent objects and classes.

### State Management
Uses game states to control different stages of the application, determining which actions and behaviors are active at a given time.

## 6. Installation

Make sure Python 3 is installed on your computer.

**Step 1: Clone the repository**

```bash
git clone https://github.com/royy05/fix-it-felix-pygame.git
```

**Step 2: Navigate to the project directory**

```bash
cd fix-it-felix-pygame
```

**Step 3: Install the required dependency**

```bash
pip install pygame-ce
```

## 7. How to Run the Game

Execute the following command from the project directory:

```bash
python main.py
```

The game window should open, allowing you to start playing.

## 8. Game Controls

You can also refer to the in-game instructions for the available controls in the menu screen.

| Control | Action |
|---|---|
| Arrow Keys or WASD | Character movement during gameplay |
| Left Mouse-click on Start button or Press Space or Enter | Start the game |
| Space (x3 times) | Fix broken windows |
| Left Mouse-click on Quit Button or Press ESC | Exit the game | 

## 9. Development Team

This project was developed collaboratively as part of an Object-Oriented Programming course at Thammasat University.

| Team Member | Contribution |
|---|---|
| Thant Htut Aung | Felix, Brick, Sound, and Win/Lose screen |
| Lin Lat Eain | Game Flow, Management, Ralph |
| Soe Yu Nandar | Building, Windows, Menu, Images, and Game State |

## 10. Future Improvements

- Introduce additional levels of difficulty and environments.
- Add more character animations and sound effects.
- Improve enemy and gameplay mechanics.
- Implement additional power-ups and challenges for the player.

## 11. Credits and Sources

We would like to acknowledge the original creators and sources of the visual and audio assets used in this project.

### Images

| Asset | Source |
|---|---|
| Ralph Idle | [IndieDB – Fix-It Felix Jr.](https://www.indiedb.com/games/fix-it-felix-jr/images/fix-it-felix-jr-image) |
| Felix Fix | [IndieDB – Fix-It Felix Jr.](https://www.indiedb.com/games/fix-it-felix-jr/images/fix-it-felix-jr-image) |
| Ralph Throw | [Villains Wiki – Wreck-It Ralph (Arcade Game)](https://villains.fandom.com/wiki/Wreck-It_Ralph_(Arcade_Game)) |
| Felix Idle | [Pixilart – Fix-It Felix Jr.](https://www.pixilart.com/art/fix-it-felix-jr-f0b006efc5e3) |
| Felix Hurt | Generated using ChatGPT (OpenAI) |
| Background | Generated using Claude |
| Window_fixed | Generated using Claude |
| Window_broken | Generated using Claude |
| Roof | Generated using Claude |
| Brick | Generated using Claude |
| Building_wall | Generated using Claude |

### Sound Effects and Music

- [The Sounds Resource – Fix-It Felix Jr.](https://sounds.spriters-resource.com/pc_computer/fixitfelixjr/asset/414318/) – Source for game sound effects.

### Libraries and Technologies

- [Python](https://www.python.org/) – Main programming language.
- [Pygame](https://www.pygame.org/) – Game development library used for graphics, audio, and event handling.

### Inspiration

- **Fix-It Felix Jr.** – Original arcade game that inspired this reimplementation.

### AI Assistance

- **ChatGPT (OpenAI) & Claude** – Used to assist with development, debugging, code explanations, and documentation. Detailed records of AI assistance are provided in `AI_LOG.md`.

*All third-party assets remain the property of their respective creators and are acknowledged here for attribution purposes.*
---

**Course:** SF211 Object-Oriented Programming
**University:** Thammasat University  
**Project:** Fix-It Felix Jr.

