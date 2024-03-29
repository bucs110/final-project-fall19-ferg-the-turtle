:warning: Everything between << >> needs to be replaced (remove << >> after replacing)

# << Project Title >>
## CS 110 Final Project
###    Fall, 2019
### [Assignment Description](https://drive.google.com/open?id=1HLIk-539N9KiAAG1224NWpFyEl4RsPVBwtBZ9KbjicE)

 (https://github.com/bucs110/final-project-fall19-ferg-the-turtle)(#)

(https://docs.google.com/presentation/d/1YZ-FDzJOmY7Qsc7-lrNABPbtwpS0riJZNaZ1BiUilF4/edit#slide=id.p)(#)

### Team: Ferg the Turtle
#### Christopher Simak, Aidan Ferguson, Joe Lieberman

***

## Project Description
 This game is a 2-D sidescroller. The player spawns in as a character that runs sideways. In the way of the character are obstacles (spikes and wall). The player can fire a bullet to destroy these obstacles. If the player comes into contact with any of these obstacles, the game will end. As the game goes on, the player collects coins to increase his score.

***    

## User Interface Design
* << The Main Menu/Start Screen >>
    This screen is the first screen the user sees when main.py is ran. It contains the name of the game (Space Run),
    and the instructions. If the user hits the 'space' key, the game will run. If the user clicks the red x in the top
    right, they will exit out of the screen.
    ![startscreen](assets/Sprites/IMG_1642.jpg)
* << The Game Screen >>
    This screen is accessed by the user hitting space bar when on the start screen. On this screen, the character and
    screen will be moving. There also will be obstacles on the screen. Pressing the space bar or the up arrow will cause
    the character to jump up. Clicking the 'z' key will allow the character to shoot a bullet across the screen.
    Picture is not available, this is what it would/should look like (the middle picture):
    ![gamescreen](assets/gui_design.jpg)

* << The End Screen/Game Over Screen >>
    This screen is accessed when the character dies. It will say "Game Over. Press Space to play again". Pressing space
    will cause the game screen to pop up and the game will run again. To exit the game, the user should press the
    'red X' in the top left corner.space
    ![endscreen](assets/Sprites/IMG_1643.jpg)

***        

## Program Design
* Non-Standard libraries
    * Pygame (https://www.pygame.org/) - cross-platform set of Python modules designed for writing video games. It includes computer graphics and sound libraries designed to be used with the Python programming language.



    * << This picture represents the relationships between the different classes >>
        * ![gui design ](assets/mvcdesign.jpg)
    * This does not need to be overly detailed, but should show how your code fits into the Model/View/Controller paradigm.
* Classes
    * Hero - A class that defines the game character. It is a stationary character that appears to be moving by looping through a sprite sheet. It can jump to avoid obstacles such as spikes or walls, or shoot walls in order to avoid collisions.  
    * Spikes - A class that defines an obstacle that the game character must avoid. If the character and the sprite collide, the game will end.
    * Wall - A class that defines an obstacle that the game character must avoid. If the user shoots a bullet from the hero that collides with the wall, it will be erased from the screen.
    * Coin - A class that defines an object that the character can collide with  to increase the overall score of the current game. The coin appears to be spinning by looping through a list of sprites that display snapshots of a spinning coin.
    * Bullet - A class that defines an object that can be shot from the game character if the user presses a designated key. If the bullet collides with the sprite from the wall function, both bullet and wall will be erased.

***

## Tasks and Responsibilities
* You must outline the team member roles and who was responsible for each class/method, both individual and collaborative.

### Software Lead - << Aidan Ferguson  >>

 Worked as integration specialist by ensuring compatibility of the GUI against the controller, running periodic tests to gauge efficiency and quality of code. I used the process shown in the ATP to outline order in which different classes and methods were implemented. Proposed integration of different elements such as coin spinning and character animations were discussed and in each case our group was able to come to a conclusive decision on the conflict without setback.    

### Front End Specialist - << Joe Lieberman >>

Front-end lead conducted significant research on the controller and GUI of the program. The GUI (Graphical User
Interface) is the screen the user sees when they run the game. The GUI, in this case, consists of the gameIntroScreen,
game-screen, and gameOverScreen. I also worked with the Back End Specialist on incorporating the models into the
controller. The controller is where the GUI is created. The controller also contains most of the code for the game.

### Back End Specialist - << Chris Simak >>

 I helped with the “Model” portion of Space run by writing the major classes that would be used in the main game. I also created methods for the game mechanics of the hero such as run, jump, and run and shoot. I maintained persistent data by sending the position of the sprites to a json file. I worked with the Front End Specialist in the implementation of the classes into our Controller file which uses all of the sprites from the classes to create the game.


## Testing
*  Began by using pdb module to scan for minor errors/bugs within main controller file and all implemented classes. Once flagged bugs were addressed using the module, code was run in parts to verify the integrity of each end separately in order to avoid confusion over which classes and functions were functioning properly and when. If front end GUI opened successfully and the controller and its classes were free of error, I would then run the program from the gameIntroScreen and use controls to advance the game into game-screen, then operate the hero in the game and purposely lose by allowing the self.running behavior to end via an obstacle (either spikes, lava, or destructible wall) and ensure that self.hero.kill would deplete the hero's health and transition into gameOverScreen. (Current code maintains a GUI to game controller transition issue preventing game-screen from executing properly)

--ATP--

| Step                  | Procedure     | Expected Results  | Actual Results |
| ----------------------|:-------------:| -----------------:| -------------- |
|  1  | Run game program   | self.gameIntroScreen() displays controls: "Hit space to jump, Hit "z" to shoot. Press space to play." over (backgrounbndimg.jpg) |          |
|  2  | Press <spacebar> to exit menu and begin game  | self.state now == GAME, hero appears and starts self.running in sidescroller over game background   |               |
|  3  | Within game, press <space> when hero encounters obstacle  | timed right, hero will run jump over the spikes/lava and resume self.running |          |
|  4  | Allow hero to run into coin  | Hero will collect coin, causing self.bullets.add thus self.bullets != 0  |     |
|  5  | Press <z> when hero encounters wall  | With self.bullets != 0, hero shoots bullet at wall, causing self.wall.kill, wall breaks and hero continues running  |           |
|  6  | Allow hero to run into spikes/lava/wall, losing game  |  gameOverScreen() will run, causing self.hero.kill which will "kill" self.running and end the game  |         |    
