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
* << A wireframe or drawing of the user interface concept along with a short description of the interface. You should have one for each screen in your program. >>
    * For example, if your program has a start screen, game screen, and game over screen, you should include a wireframe / screenshot / drawing of each one and a short description of the components
* << You should also have a screenshot of each screen for your final GUI >>

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
|  3  | Within game, press <space> when hero encounters obstacle  | timed right, hero will run jump over the spikes/lava and resume self.running
|  4  |
