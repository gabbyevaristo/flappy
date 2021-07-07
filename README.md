# Flappy Bird Re-Creation

This is a re-creation of Flappy Bird, built fully with PyGame. Also implemented is an online two-player mode.


## To run the instance locally

1. Clone the repository
2. Using a virtual environment is recommended but not essential (skip if you are not using one) <br/>
&nbsp;&nbsp;&nbsp; 1. In your terminal, run ``` pip install pipenv ```  <br/>
&nbsp;&nbsp;&nbsp; 2. In your terminal, run ``` pipenv shell ``` to activate the virtual environment <br/>
3. In your terminal, run ``` python run_game.py ```. Running this will always give you access to single player mode. For two player mode to work, the server must be activated.

To learn how to host your own server, I suggest watching the following video: https://www.youtube.com/watch?v=KQasIwElg3w&t=1114s. The only change to the code base will be the changing the ``` host ``` attribute inside of ``` network.py ``` to match the address of the server you created.
