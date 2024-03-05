# ex-raceone

A retro side scroller game made with pygame

## Look and feel

- NES style graphics 8 bit
- fullscreen for widescreen diplays
- HD resolutions must be divisible by the games resolution so scaling works
- Native resolution is (256*240)

## Guides & Advises

### No Repeats

If code is repeated, make a class or function of it

### Use inheritance

Sprite > Static Entity > Dynamic Entity > Player

### Resolution

We will implement a system to scale the game and increase the native resolution of the game itself on the display.
We will also go over if the user chooses to turn fullscreen mode on.

### Layers

- BG 3
- BG 2
- BG 1
- Enemy
- Player
- Projectiles
- UI

### Game controller

- The controller is the core of the entire program
- The program pretty much start with the controller
- The controller contain the main game loop
- The controller contains and execute every game state (menu, level, ending, ...)
- It contains the logic for how to swap these state when necessary and how to clean them up

### State system

- Create a state class that contain all the logic necessary for states (game state, entity state)
- Every dynamic entity will have a stateGroup object that contains all of there states
The entitity can commands to this state group, and the state group will take care of its logic

### Animation system

- Every Dynamic entity will have an animation group similar to the state group
- The group will contain a list of all possible animation cycles and handle animation
- It will contains a function for sprite sheet to cut the sprites to an animation object
- Doing things this way with the animation state objects, removes a ton of code that would have to go into the entity classes themselves and makes it much easier to program once it is all implemented

### Constants file

- This file is like the .ini file found with a ton of games. it contains a ton of static variables that are used all through out your program. Window information, joystick information, game state names, directory information, fps, ...

### Event handler

- The eevent handler object will contain all the code for handling user input
- It will also have a joystick system in it that will work with any type of direct input or xinput device
- It will also be using a command design pattern for encapsulating the button input into their own object
- This will allow to give users an option to reassign buttons in game if they would like

## Brainstorming

- Side scroller game
  - style scrolling permanent
  - style retro arcade 8-bit 16-bit
  - style jetpack joyride

- Objectifs aller le plus loin possible
  - niveaux prédéfinis / construit  avec tiles ?
  - éviter les obstacles
  - side scrolling parallax

- Environnement et ressources:
  - futuriste,
  - hyper dynamique,
  - retro,
  - cyberpunk

- Style pyxel art + Spritessheet à prévoir

- Music pack de music Retro

- Premier jeux:
  - Moteur de jeux: Pygame
  - Langage de prog: Python

- Menu de sélection
  - Hub avec les différents niveaux
  - représenteé par des planetes animées
  - avec le planete generator

- Idéees
  - voir le déclun de la terre
  - planetes futuriste et post apo cyber
  - lore + commandes expliquer bulle de texte sur fondu

- Crédits

- ++ Bonus:
  - Score
  - Menu Option

- 3 différents niveaux Difficulté croissante

- Esquiver des obstacles

- Système de vie:
  - Barre de vie
  - Véhicule

- Avant de commencer un niveau Sprites:
  - READY
  - GO

- Vaisseau Terrestre

- Possibilité de saut en cloche/vague

- Fin sur credit
  - fond panorama sur les wastelands
  - scrolling vers le ciel
  - fin

## Credits

ansimuz - graphics
Juhani Junkala - musics & sounds
