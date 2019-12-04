:warning: Everything between << >> needs to be replaced (remove << >> after replacing)

# << Project Title >>
## CS 110 Final Project
###    Fall, 2019
### [Assignment Description](https://drive.google.com/open?id=1HLIk-539N9KiAAG1224NWpFyEl4RsPVBwtBZ9KbjicE)

<< [https://github.com/<repo>](#) >>

<< [link to demo presentation slides](#) >>

### Team: Ferg the Turtle
#### Christopher Simak, Aidan Ferguson, Joe Lieberman

***

## Project Description
<< Give an overview of your project  >>

***    

## User Interface Design
* << The Main Menu/Start Screen >>
    This screen is the first screen the user sees when main.py is ran. It contains the name of the game (Space Run),
    and the instructions. If the user hits the 'space' key, the game will run. If the user clicks the red x in the top
    right, they will exit out of the screen.
    ![startscreen](assets/Sprites/IMG_1642.jpg)
   *<< The Game Screen >>
    This screen is accessed by the user hitting space bar when on the start screen. On this screen, the character and
    screen will be moving. There also will be obstacles on the screen. Pressing the space bar or the up arrow will cause
    the character to jump up. Clicking the 'z' key will allow the character to shoot a bullet across the screen.
    Picture is not available, this is what it would/should look like:
    ![gamescreen](assets/Sprites/IMG_1644.jpg)
    *<< The End Screen/Game Over Screen >>
    This screen is accessed when the character dies. It will say "Game Over. Press Space to play again". Pressing space
    will cause the game screen to pop up and the game will run again. To exit the game, the user should press the
    'red X' in the top left corner.space
    ![endscreen](assets/Sprites/IMG_1643.jpg)

***        

## Program Design
* Non-Standard libraries
    * << You should have a list of any additional libraries or modules used (pygame, request) beyond non-standard python. >>
    * For each additional module you should include
        * url for the module documentation
        * a short description of the module
* Class Interface Design
    * << A simple drawing that shows the class relationships in your code (see below for an example). >>
        * ![gui design ](assets/gui_design.jpg)
    * This does not need to be overly detailed, but should show how your code fits into the Model/View/Controller paradigm.
* Classes
    * << You should have a list of each of your classes with a description. >>

***

## Tasks and Responsibilities
* You must outline the team member roles and who was responsible for each class/method, both individual and collaborative.

### Software Lead - << Aidan Ferguson  >>

<< Worked as integration specialist by... >>

### Front End Specialist - << Joe Lieberman >>

<< Front-end lead conducted significant research on... >>

### Back End Specialist - << Chris Simak >>

<< The back end specialist... >>

## Testing
* << Describe your testing strategy for your project. >>
    * << Example >>

* Your ATP

| Step                  | Procedure     | Expected Results  | Actual Results |
| ----------------------|:-------------:| -----------------:| -------------- |
|  1  | Run game program   | self.gameIntroScreen() displays controls: "Hit space to jump, Hit "z" to shoot. Press space to play." over (backgrounbndimg.jpg) |          |
|  2  | Press <spacebar> to exit menu and begin game  | self.state now == GAME, hero appears and starts self.running in sidescroller over game background   |               |
|  3  | Within game, press <space> when hero encounters obstacle  | timed right, hero will run jump over the spikes/lava and resume self.running |          |
|  4  | Allow hero to run into coin  | Hero will collect coin, causing self.bullets.add thus self.bullets != 0  |     |
|  5  | Press <z> when hero encounters wall  | With self.bullets != 0, hero shoots bullet at wall, causing self.wall.kill, wall breaks and hero continues running  |           |
|  6  | Allow hero to run into spikes/lava/wall, losing game  |  gameOverScreen() will run, causing self.hero.kill which will "kill" self.running and end the game  |         |    
