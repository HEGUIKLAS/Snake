# Snake
A simple snake game, you can move uder an angle other than 0, 90, 180, 270 and also there are a few walls on the map
inspiration: https://en.wikipedia.org/wiki/Snake

![image](https://user-images.githubusercontent.com/114672940/196040463-42e6ca61-ed2d-4cbf-8b4d-610a47d7a020.png)


Movement:
  [A] / [K_LEFT] - rotate left
  [D] / [K_RIGHT] - rotate right
  [Q] - closes program


needed libraries:
  link to download library, optimalized for version 1.9.6 - https://www.pygame.org/download.shtml 
  console command for installing pygame - python3 -m pip install -U pygame --user
  
to run program:
program is optimalized for python 3.10.8
check if all needed libraries are installed
open main.py




The code is structured into four different files:
  main.py handles data from the three other files, it contains the class Game responsible for calling all usefull methods
  map.py  creates list of wall coordinates, draws self
  player.py handles inputs, snake movement, stores snake coords
  settings.txt all important variables used to set up game
put them in one file, or change the import statements to the correct path
