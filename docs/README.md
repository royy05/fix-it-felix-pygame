
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

The project is organized into separate modules, with each file responsible for specific aspects of the game.

- **main.py:** Entry point of the application. Initializes and starts the game.
- **game_manager.py:** Controls the main game loop, game flow, and interactions between game components.
- **player.py:** Handles Felix's movement, actions, and player-related behaviors.
- **config.py:** Stores game constants, settings, and configuration values.
- **assets/:** Contains game resources, including images and sounds.

*Refer to the repository for the complete file structure.*

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
pip install pygame
```

## 7. How to Run the Game

Execute the following command from the project directory:

```bash
python main.py
```

The game window should open, allowing you to start playing.

## 8. Game Controls

Refer to the in-game instructions for the available controls.

| Control | Action |
|---|---|
| Arrow Keys or WASD | Character movement |
| Space | Fix broken windows |
| Mouseclick Start button | Start the game |
| ESC or Mouseclick Quit Button | Exit the game |

## 9. Development Team

This project was developed collaboratively as part of an Object-Oriented Programming course at Thammasat University.

| Team Member | Contribution |
|---|---|
| Thant Htut Aung | Felix, Bricks, Sound, and Win/Lose screen |
| Lin Lat Eain | Game Flow, Management, Ralph |
| Soe Yu Nandar | Building, Windows, Menu, Game State |

## 10. Future Improvements

- Introduce additional levels of difficulty and environments.
- Add more character animations and sound effects.
- Improve enemy and gameplay mechanics.
- Implement additional power-ups and challenges for the player.

---

**Course:** SF211 Object-Oriented Programming
**University:** Thammasat University  
**Project:** Fix-It Felix Jr.

