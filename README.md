:warning: Everything between << >> needs to be replaced (remove << >> after replacing)

# << Project Title >>
## CS 110 Final Project
###    Fall, 2019
### [Assignment Description](https://drive.google.com/open?id=1HLIk-539N9KiAAG1224NWpFyEl4RsPVBwtBZ9KbjicE)

 https://github.com/bucs110/final-project-fall19-ferg-the-turtle](#)

<< [https://docs.google.com/presentation/d/1SOa7nczo0ujqRfF9WA12pPim8GYhwKMPLZFRsVfK1ZM/edit#slide=id.p](#) >>

### Team: Ferg the Turtle
#### Christopher Simak, Aidan Ferguson, Joe Lieberman

***

## Project Description
<< Give an overview of your project  >>

***    

## User Interface Design
* << A wireframe or drawing of the user interface concept along with a short description of the interface. You should have one for each screen in your program. >>
    * For example, if your program has a start screen, game screen, and game over screen, you should include a wireframe / screenshot / drawing of each one and a short description of the components
* << You should also have a screenshot of each screen for your final GUI >>

***        

## Program Design
* Non-Standard libraries
    * Pygame (https://www.pygame.org/) - cross-platform set of Python modules designed for writing video games. It includes computer graphics and sound libraries designed to be used with the Python programming language.
    *


    * << This picture represents the relationships between the different classes >>
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

 The back end specialist helped with the “Model” portion of Space run by writing the major classes that would be used in the main game. He also created methods for the game mechanics of the hero such as run, jump, and run and shoot.He maintained persistent data by sending the position of the sprites to a json file. He collaborated with the Front End Specialist in the implementation of the classes into our Controller file which uses all of the sprites from the classes to create the game.


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
