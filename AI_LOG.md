# AI Usage Log
**Project:** Fix-It Felix Jr. – Pygame  
**Development Period:** November 2026  
**AI Tools Used:** ChatGPT and Claude

The following details are recorded.
- Date and team member
- Task and prompt used
- AI-generated suggestions or code received
- Student changes and reasoning
- Tests/validation performed
- Final result

# AI Usage Log for Building, Windows, and Menu

##  1. Project Structure and Initial Code Skeleton

**Date:** November 10, 2026  
**Task and Prompt Used:**

"Can you give me a reference design for the initial project structure for our Fix-It Felix Pygame project, including folders, Python files, class responsibilities, method skeletons and naming conventions."

**AI Suggestions:**
- Proposed separate folders for entities, states and other supporting modules.
- Suggested class responsibilities and initial method structures.
- Recommended `config.py` for centralized game constants.

**Student Changes:**
- Reviewed the proposed structure and discussed file responsibilities with teammates.
- Followed the agreed class, file and method naming conventions.
- Used the suggested skeleton as the foundation for individual implementations.

**Tests/Validation:**
- Reviewed class responsibilities and method interfaces.
- Checked compatibility between members' assigned modules.

**Final Result:** Established a consistent project structure that supported independent development and integration.

---

## 2. Abstract GameObject Structure

**Date:** November 12, 2026  
**Task and Prompt Used:**

"Help design an abstract GameObject parent class for our Pygame project. What common attributes and methods should it contain, and how should other entities inherit from it?"

**AI Suggestions:**
- Recommended using `ABC` and `@abstractmethod` for abstraction.
- Suggested common methods such as `update(dt)` and `draw(screen)`.
- Explained how subclasses could override abstract methods with their own implementations.

**Student Changes:**
- Implemented the abstract parent class in `entities/game_object.py`.
- Kept shared functionality in the parent class and entity-specific behaviour in subclasses.
- Followed the method naming conventions established during project planning.

**Tests/Validation:**
- Reviewed abstract method definitions.
- Checked that child classes implemented the required methods before instantiation.

**Final Result:** Established a common abstract structure for game entities, supporting inheritance and consistent class design.

---

## 3. Building and Brick Wall Construction

**Date:** November 13, 2026  
**Task and Prompt Used:**

"Guide me in constructing a four-floor building with 16 windows and systematically arranged bricks. How can I calculate their positions and organize the objects using separate classes?"

**AI Suggestions:**
- Recommended nested loops for generating four floors and four windows per floor.
- Suggested using collections to manage multiple Window and Brick objects.
- Explained coordinate calculations for consistent spacing and alignment.
- Recommended using shared dimensions from `config.py`.

**Student Changes:**
- Implemented building construction in `entities/building.py`.
- Organized window and brick placement according to the building dimensions.
- Used configuration constants to maintain consistent positioning.
- Kept building management separate from individual object rendering.

**Tests/Validation:**
- Inspected the four-floor, 16-window arrangement.
- Checked brick alignment, spacing and building dimensions.
- Adjusted object positions after visual inspection.

**Final Result:** Implemented the building structure with systematically positioned windows and bricks.

---

## 4. Window Repair and Three-Space-Bar Mechanism

**Date:** November 13, 2026  
**Task and Prompt Used:**

"How can I implement a window repair system where each broken window requires the player to press the Space bar three times before it changes into its fixed appearance?"

**AI Suggestions:**
- Suggested using a counter to track the number of Space-bar presses.
- Recommended handling `pygame.KEYDOWN` and checking `pygame.K_SPACE`.
- Explained how to check the repair counter against the required three-press condition.
- Suggested changing the window's condition and appearance after the third press.

**Student Changes:**
- Implemented the repair counter in `entities/window.py`.
- Connected Space-bar input to the window repair interaction.
- Updated the window's condition and visual appearance after three successful presses.
- Prevented already repaired windows from receiving additional repair progress.

**Tests/Validation:**
- Checked the window appearance before repair and after each Space-bar press.
- Verified that the third press changed the window into its fixed appearance.
- Checked that repaired windows could no longer accumulate repair progress.

**Final Result:** Implemented the three-Space-bar repair mechanism with a visual transition from broken to fixed windows.

---

## 5. Image Asset Path Handling

**Date:** November 14, 2026  
**Task and Prompt Used:**

"I am loading images using `pygame.image.load('path')` directly. How can I make image paths more reliable across different directories and computers?"

**AI Suggestions:**
- Recommended `os.path.join()` for combining directory paths.
- Suggested `os.path.dirname(__file__)` and `os.path.abspath()` for locating paths relative to the Python file.
- Explained how to construct reusable asset paths.

**Student Changes:**
- Replaced direct path construction with `os.path.join()`.
- Adapted the paths to the project's `assets/` folder.
- Applied consistent path handling when loading menu backgrounds and character images.

**Tests/Validation:**
- Ran the game to check whether images loaded correctly.
- Checked asset paths after organizing project folders.

**Final Result:** Improved asset path handling and reduced dependency on manually written relative paths.

---

## 6. Character and Window Image State Changes

**Date:** November 14, 2026  
**Task and Prompt Used:**

"How can I switch character and window images according to their states? I want Felix and Ralph to display different images when idle or hurt, and windows to have different appearances when broken or repaired."

**AI Suggestions:**
- Recommended storing separate image surfaces for different states.
- Suggested using state variables or enumerations to determine which image to display.
- Explained how `screen.blit()` displays the currently selected image.
- Recommended loading images once rather than repeatedly during drawing.

**Student Changes:**
- Organized image assets according to their visual states.
- Applied state-based image selection where appropriate.
- Used window conditions to determine broken and repaired appearances.
- Coordinated character image-state integration with the relevant entity implementations.

**Tests/Validation:**
- Inspected image changes between different states.
- Checked image rendering and positioning during gameplay.

**Final Result:** Established state-based image switching for character appearances and window conditions.

---

## 7. Abstract Game State and Menu Text Rendering

**Date:** November 14, 2026  
**Task and Prompt Used:**

"How can I create an abstract GameState class and display text in my Pygame menu, including the game title, Start button and keyboard instructions?"

**AI Suggestions:**
- Recommended abstract methods such as `enter()`, `handle_event(event)`, `update(dt)` and `draw(screen)`.
- Explained Pygame font initialization and text rendering using `pygame.font.Font()` and `render()`.
- Suggested using `screen.blit()` to position rendered text.
- Recommended keeping menu-specific drawing and event handling inside MenuState.

**Student Changes:**
- Implemented the abstract base class in `states/game_state.py`.
- Created menu text elements in `states/menu_state.py`.
- Adjusted font sizes, text positions and visual hierarchy.
- Added instructions for Enter/Space to start and Escape to quit.

**Tests/Validation:**
- Inspected the visibility and alignment of menu text.
- Checked that the title and instructions were readable.
- Reviewed the abstract methods implemented by the concrete menu state.

**Final Result:** Completed the abstract game-state structure and menu text-rendering functionality.

---

## 8. Menu Button, Mouse Events and State Transition

**Date:** November 15, 2026  
**Task and Prompt Used:**

"How can I make the Start button interactive using both mouse clicks and keyboard inputs, and switch from MenuState to PlayingState when the player starts the game?"

**AI Suggestions:**
- Recommended handling `pygame.MOUSEBUTTONDOWN` and `pygame.KEYDOWN` events.
- Suggested using `pygame.Rect` and `collidepoint()` to detect clicks inside the Start button.
- Explained how to request a state transition through the GameManager.
- Recommended keeping state-switching logic separate from menu drawing.

**Student Changes:**
- Implemented mouse click detection for the Start button.
- Connected Enter, Space and mouse click interactions to the start functionality.
- Integrated the transition from MenuState to PlayingState through the project's state-management structure.
- Kept Escape as the menu-specific quit instruction.

**Tests/Validation:**
- Tested clicks inside and outside the Start button.
- Tested Enter and Space as alternative start controls.
- Verified that the game transitioned from the menu to gameplay correctly.

**Final Result:** Implemented an interactive main menu supporting mouse and keyboard input and the transition to PlayingState.

---

## 9. UML Class Diagram – Initial Structure

**Date:** November 16, 2026  
**Task and Prompt Used:**

"create a draw.io UML class diagram skeleton with our project's classes, relationships and appropriate UML arrows so that I can add the attributes and methods in that file. Have the skeleton structure already constructed according to our project details so I can adjust it over."

**AI Suggestions:**
- Generated the initial class boxes and diagram layout.
- Provided inheritance and association relationships with connecting UML arrows.
- Organized the diagram into a framework for further editing.

**Student Changes:**
- Opened the generated diagram in draw.io.
- Updated the actual class attributes and methods to align with the project's implementation.
- Reviewed and adjusted relationships and layout to reflect the implemented code.

**Tests/Validation:**
- Compared the diagram against the actual Python files.
- Checked class names, attributes, methods and UML relationships.

**Final Result:** Produced the UML class diagram using Claude's initial framework, with independent modifications and confirmations.

## AI Usage Log for Game Flow and Management
##  1: Ralph Class Design and Introduction Logic

**Date:** 13 November 2026  
 
**Task:** Implementing Ralph's introduction and random window destruction.

**Prompt Used:**
"Help me implement Ralph's introduction, where he randomly selects windows on each floor and climbs the building to destroy them."

**AI-generated suggestions or code received:**
- Suggested using a set to store selected window positions and prevent duplicates.
- Suggested selecting at least one window from every floor.
- Explained how to use `random.choice()` and `random.sample()` for random selection.
- Explained how Ralph could communicate with Building to destroy selected windows.

**Student changes and reasoning:**
- Implemented `start_intro()` independently using nested loops and random selection.
- Used tuples `(floor_number, window_number)` to identify selected windows.
- Changed the number of broken windows to a fixed eight while keeping their positions random.
- Implemented `destroy_window()` to request Building to break the selected window.

**Tests/validation performed:**
- Reviewed the selection algorithm to ensure eight unique windows are selected.
- Checked that at least one window is selected from every floor.
- Runtime testing is pending.

**Final result:**
Completed the random window selection and window destruction request logic.

---

##  2: Ralph Climbing Movement

**Date:** 13 November 2026  
 
**Task:** Implementing Ralph's movement between selected windows.

**Prompt Used:**
"Help me calculate Ralph's movement towards each selected window while preventing him from overshooting the target."

**AI-generated suggestions or code received:**
- Explained how to calculate horizontal and vertical distance using `dx` and `dy`.
- Suggested using `math.hypot()` to calculate the distance to the target.
- Explained frame-independent movement using delta time (`dt`).
- Suggested comparing the remaining distance with the maximum movement distance per frame.

**Student changes and reasoning:**
- Implemented the movement calculation independently.
- Used `step = dt * self._move_speed` to determine the maximum movement per frame.
- Used normalized direction values to move Ralph towards the target.
- Made Ralph snap to the exact target position when the remaining distance is smaller than the movement step.

**Tests/validation performed:**
- Reviewed the movement calculations and overshooting prevention logic.
- Full gameplay testing is pending integration with Building.

**Final result:**
Completed the basic climbing movement and target-arrival logic.

---

##  3: Ralph Introduction Completion

**Date:** 13 November 2026  
 
**Task:** Implementing the transition after Ralph finishes destroying windows.

**Prompt Used:**
"What should happen when Ralph finishes destroying all eight selected windows?"

**AI-generated suggestions or code received:**
- Suggested changing Ralph's state to `RalphState.INTRO_FINISHED`.
- Suggested resetting rooftop movement and attack timers.
- Discussed moving Ralph to a fixed rooftop starting position after the introduction.

**Student changes and reasoning:**
- Implemented `finish_intro()` by changing the state and resetting `_move_timer` and `_attack_timer`.
- Deferred rooftop positioning until the building layout and dimensions are finalized.

**Tests/validation performed:**
- Reviewed the state assignment and timer resets.
- Completed the introduction-ending method, including Ralph's transition and positioning on the rooftop.

**Final result:**
Completed the initial introduction-ending method. Rooftop positioning remains pending.

---

##  4: Brick Creation and Ralph Debris Integration

**Date:** 13 November 2026  
 
**Task:** Implementing Ralph's debris creation method.

**Prompt Used:**
"How should Ralph create Brick objects and pass their dimensions and falling speed?"

**AI-generated suggestions or code received:**
- Explained the separation of responsibilities between Ralph, Brick and PlayingState.
- Suggested that Ralph should create and return Brick objects without storing them.
- Explained how to unpack a dimension tuple from the configuration file.
- Confirmed the required Brick constructor arguments.

**Student changes and reasoning:**
- Reviewed the Brick class implemented by another team member.
- Implemented `drop_debris()` independently.
- Used `BRICK_SIZE` and unpacked it into `brick_width` and `brick_height`.
- Passed Ralph's current position and `_debris_speed` to the Brick constructor.
- Returned the created Brick object so PlayingState can manage the active debris collection.

**Tests/validation performed:**
- Checked that the arguments match the Brick constructor.
- Reviewed the dimension tuple unpacking.
- Runtime testing and collision testing are pending.

**Final result:**
Completed Ralph's `drop_debris()` method. The `attack()` method and integration with PlayingState remain pending.

---

##  5: Configuration Compatibility Review

**Date:** 13 November 2026  
 
**Task:** Reviewing and updating shared configuration variables.

**Prompt Used:**
"Compare the original and updated config.py files and check whether existing variables are preserved and required variables are added."

**AI-generated suggestions or code received:**
- Identified renamed and missing configuration variables.
- Suggested maintaining compatibility with existing imports.
- Recommended using `BRICK_SIZE` as a tuple and unpacking it when needed.
- Suggested restoring compatibility for existing constants such as `TOTAL_LIVES` and `WINDOW_TITLE`.

**Student changes and reasoning:**
- Reviewed the updated configuration provided by the team.
- Adopted the fixed `BROKEN_WINDOWS = 8` setting.
- Used `BRICK_SIZE` instead of separate brick dimension constants.
- Discussed configuration compatibility with other team members.

**Tests/validation performed:**
- Compared variable names between the original and updated configurations.
- Checked existing imports against the updated variable names.
- Full project import testing is pending.

**Final result:**
Identified configuration compatibility requirements and agreed on the updated naming approach.

---

##  6: GitHub Collaboration Setup

**Date:** 13 November 2026  
 
**Task:** Setting up GitHub collaboration and an individual development branch.

**Prompt Used:**
"Explain how three team members can use GitHub to share code, work on separate branches and combine their changes."

**AI-generated suggestions or code received:**
- Explained repositories, branches, commits, pushes, pulls and pull requests.
- Suggested using GitHub Desktop for easier version control.
- Recommended creating a separate branch for individual development.
- Explained how to synchronize changes with the shared repository.

**Student changes and reasoning:**
- Cloned the team's existing private repository.
- Created and published an individual branch named `feature/member-3-Lin`.
- Opened the cloned project in Visual Studio Code.
- Verified that the active branch was the individual development branch rather than `main`.

**Tests/validation performed:**
- Verified the active branch using `git branch`.
- Confirmed that the branch was published through GitHub Desktop.

**Final result:**
Successfully configured a personal development branch for independent coding and collaboration.

---

##  7: Ralph Rooftop Patrol Movement

**Date:** 14 November 2026  
 
**Task:** Implementing Ralph's rooftop positioning and continuous patrol movement.

**Prompt Used:**  
"Help me implement Ralph's rooftop movement. He should finish his introduction, move onto the roof, patrol horizontally, and reverse direction when reaching either edge."

**AI-generated suggestions or code received:**
- Explained how to use Building's existing roof properties instead of recalculating roof dimensions in Ralph.
- Suggested positioning Ralph at the left edge of the roof after the introduction.
- Explained how to calculate Ralph's vertical position using the roof's top coordinate and his height.
- Suggested using a direction variable to control horizontal movement.
- Explained how to clamp Ralph's position and reverse direction at the rooftop boundaries.

**Student changes and reasoning:**
- Implemented `finish_intro(building)` to position Ralph on the rooftop.
- Changed Ralph's state to `MOVING` after finishing the introduction.
- Reset the movement and attack timers.
- Implemented `move_rooftop(dt, building)` using the roof properties provided by Building.
- Used boundary checks to prevent Ralph from moving outside the rooftop.

**Tests/validation performed:**
- Reviewed the rooftop positioning calculations.
- Checked the left and right boundary conditions manually.
- Runtime testing is pending.

**Final result:**
Completed Ralph's rooftop positioning and horizontal patrol movement, including direction reversal at both boundaries.

---

##  8: Implementing Ralph's Attack Cycle and Difficulty-Based Timing

**Date:** 14 November 2026  
 
**Task:** Implementing Ralph's repeated attack cycle and connecting attack timing to difficulty settings.

**Prompt Used:**  
"Help me implement Ralph's attack cycle. He should move for a configured interval, stop to attack, pause for 0.8 seconds, and then resume moving. Explain how to use separate timers for movement and attacking."

**AI-generated suggestions or code received:**
- Explained the difference between `_move_timer` and `_attack_timer`.
- Suggested using `_move_interval` to determine how long Ralph moves before attacking.
- Suggested using `_attack_duration` to control the length of the attacking phase.
- Explained how to use `_attack_performed` to prevent multiple attacks during the same attacking phase.
- Recommended resetting the timers when transitioning between states.
- Explained how PlayingState could supply different movement intervals and debris speeds according to difficulty.

**Student changes and reasoning:**
- Implemented separate movement and attack timers.
- Used `_move_timer` to track Ralph's movement duration.
- Used `_attack_timer` to track the attacking duration.
- Set `_attack_duration` to 0.8 seconds.
- Implemented transitions between `MOVING` and `ATTACKING` inside `update()`.
- Implemented `set_attack_parameters()` to receive the spawn interval and debris speed from PlayingState.
- Assigned the spawn interval to `_move_interval` and the falling speed to `_debris_speed`.
- Removed the unnecessary `_attack_interval` attribute because `_move_interval` already handled the required timing.

**Tests/validation performed:**
- Reviewed the timer calculations and state transitions manually.
- Checked that the attack flag and timers reset after each attack.
- Runtime testing with the difficulty system is pending.

**Final result:**
Implemented Ralph's repeated movement and attack cycle, allowing his attack frequency and debris speed to change according to the game's difficulty.

---

##  9: Implementing Random Brick Generation and Returning Bricks

**Date:** 14 November 2026  
 
**Task:** Implementing Ralph's attack method and allowing newly generated Brick objects to be received by PlayingState.

**Prompt Used:**  
"Help me implement Ralph's attack method so that each attack creates one to three random bricks. Also, how should Ralph return these Brick objects to PlayingState?"

**AI-generated suggestions or code received:**
- Suggested using `random.randint(1, 3)` to determine the number of bricks per attack.
- Explained how to reuse the existing `drop_debris()` method to create individual Brick objects.
- Suggested storing the newly created bricks in a list.
- Explained how to initialize an empty list in `update()` and return it after processing Ralph's current state.
- Recommended returning an empty list during frames when Ralph does not generate any bricks.

**Student changes and reasoning:**
- Implemented `attack()` to generate a random number of bricks between one and three.
- Reused `drop_debris()` to construct each Brick object.
- Modified `update()` to initialize `new_bricks` as an empty list.
- Assigned the result of `self.attack()` to `new_bricks` when an attack occurs.
- Added `return new_bricks` outside the state conditions so PlayingState can receive the generated objects.
- Kept `_attack_performed` to ensure bricks are generated only once per attack.

**Tests/validation performed:**
- Reviewed the random brick generation logic.
- Checked that `update()` returns a list regardless of Ralph's current state.
- Integration and runtime testing with PlayingState are pending.

**Final result:**
Completed Ralph's random brick generation and return mechanism. Newly created Brick objects can now be passed to PlayingState for management.

---

##  10: Planning Ralph and Entity Integration with PlayingState

**Date:** 14 November 2026  
 
**Task:** Reviewing the PlayingState structure and planning the integration of Ralph, Building, Player and Brick objects.

**Prompt Used:**  
"Review my PlayingState skeleton and explain how it should coordinate Ralph, Building, Player and falling debris. Help me decide the correct implementation order without changing the agreed method names."

**AI-generated suggestions or code received:**
- Explained the responsibilities of the existing PlayingState methods.
- Suggested initializing fresh gameplay objects and resetting variables inside `enter()`.
- Explained the distinction between `_entities` for the main game objects and `_debris` for falling Brick objects.
- Explained how PlayingState should receive newly generated bricks from Ralph's `update()` method.
- Warned against updating Ralph more than once per frame because this would affect his movement and attack timing.
- Recommended implementing `enter()` first, followed by debris integration, entity updates and collision handling.

**Student changes and reasoning:**
- Reviewed the responsibilities of the existing PlayingState methods.
- Decided to retain the existing class structure and method names.
- Planned to keep the main game objects separate from the falling debris collection.
- Decided to implement PlayingState incrementally, starting with object initialization.

**Tests/validation performed:**
- Reviewed the PlayingState skeleton and its dependencies.
- Actual implementation and integration testing are pending.

**Final result:**
Established an implementation sequence for integrating Ralph's completed core logic into PlayingState while maintaining the agreed project architecture.


##  11: Implementing Window Repair Tracking in Building

**Date:** 15 November 2026  
 
**Topic:** OOP Encapsulation, Window State Management and Repair Tracking  
**Task:** Implementing window repair tracking in Building to determine when Felix has repaired all windows broken by Ralph.

**Prompt Used:**  
"How should I implement get_repaired_count() and update all_windows_repaired() in my Building class so the game only considers windows that Ralph originally broke?"

**AI-generated suggestions or code received:**
- Suggested creating a set named `_windows_to_repair` to record the floor and window number of each window Ralph breaks.
- Explained how to update `break_window()` to record newly broken windows.
- Suggested implementing `get_repaired_count()` to count windows that Ralph originally broke and Felix has fully repaired.
- Suggested updating `all_windows_repaired()` to compare the repaired count with the total number of recorded windows.
- Explained why `get_broken_windows()` cannot be used to determine the original total because it only returns windows that are currently broken.
- Suggested adding `get_total_windows_to_repair()` to provide the original number of windows requiring repair.

**Student changes and reasoning:**
- Added `_windows_to_repair` as a set in the `Building` constructor.
- Updated `break_window()` to record each window Ralph breaks using `(floor_number, window_number)`.
- Implemented `get_repaired_count()` using a loop to identify windows that have been fully repaired.
- Updated `all_windows_repaired()` to check whether all recorded windows have been repaired.
- Added `get_total_windows_to_repair()` so other classes can retrieve the original repair requirement without directly accessing Building's private attribute.
- Kept `get_broken_windows()` unchanged because it identifies windows that are currently broken.

**Tests/validation performed:**
- Reviewed the implementation with AI and corrected the tuple-based window identification logic.
- Checked the expected behaviour before Ralph breaks any windows, after windows are broken, after some repairs, and after all repairs are completed.
- Actual runtime testing has not yet been performed.

**Final result:**
The Building class can now track the windows originally broken by Ralph, count the windows fully repaired by Felix, and determine when all required repairs are completed. This also provides the information needed for the win condition and gameplay HUD.


##  12: Implementing Gameplay HUD in PlayingState

**Date:** 15 November 2026  
 
**Topic:** Pygame Text Rendering and HUD Implementation  
**Task:** Implementing a basic HUD to display the remaining game time, Felix's lives and window repair progress.

**Prompt Used:**  
"Can you give me the code and explain how to implement a HUD inside PlayingState to display the timer, remaining lives and repaired-window count?"

**AI-generated suggestions or code received:**
- Suggested creating a reusable Pygame font using `pygame.font.Font()`.
- Provided a `draw_hud()` method to display the timer, lives and repair progress.
- Explained time formatting using division, modulo and formatted strings.
- Recommended retrieving gameplay information from Player and Building rather than storing duplicate values in PlayingState.

**Student changes and reasoning:**
- Added `_hud_font` to initialize the HUD font.
- Implemented `draw_hud()` to display the three gameplay indicators.
- Added the HUD drawing call inside `draw()` so it appears after Felix becomes controllable.
- Used Building's public methods to retrieve repair progress.

**Tests/validation performed:**
- Reviewed the HUD code and corrected a font variable naming mistake.
- Runtime testing has not yet been performed.

**Final result:**
Implemented a basic gameplay HUD in PlayingState that displays the timer, Felix's remaining lives and window repair progress.