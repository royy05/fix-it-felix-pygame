# AI Usage Log

Record each AI-assisted task with:
- Date and team member
- Task and prompt used
- AI-generated suggestions or code received
- Student changes and reasoning
- Tests/validation performed
- Final result

TODO: Add entries as the project develops.

# AI Usage Log – Member 3 (Lin Lat Eain)

## Entry 1: Ralph Class Design and Introduction Logic

**Date:** 13 November 2026  
**Team Member:** Member 3 – Lin Lat Eain  
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

## Entry 2: Ralph Climbing Movement

**Date:** 13 November 2026  
**Team Member:** Member 3 – Lin Lat Eain  
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

## Entry 3: Ralph Introduction Completion

**Date:** 13 November 2026  
**Team Member:** Member 3 – Lin Lat Eain  
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
- Integration testing with PlayingState is pending.

**Final result:**
Completed the initial introduction-ending method. Rooftop positioning remains pending.

---

## Entry 4: Brick Creation and Ralph Debris Integration

**Date:** 13 November 2026  
**Team Member:** Member 3 – Lin Lat Eain  
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

## Entry 5: Configuration Compatibility Review

**Date:** 13 November 2026  
**Team Member:** Member 3 – Lin Lat Eain  
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

## Entry 6: GitHub Collaboration Setup

**Date:** 13 November 2026  
**Team Member:** Member 3 – Lin Lat Eain  
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