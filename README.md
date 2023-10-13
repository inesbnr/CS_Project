# CS_Project
Philomène, Guillaume, Inès
# Torn Game

## Rules

Torn is an online game where players move at a constant speed using keyboard arrows. Players can change their direction by using the arrow keys. The game screen is divided into a grid, and each time a player passes through a cell, it is colored according to the player's color. If a player passes through a cell already colored (either by themselves or another player), they die. Colliding with the screen's borders also results in the player's death. The winner is the player who remains on the game board the longest.

## Table of Contents
1. [Installation](#installation)
2. [Usage](#usage)
3. [Progress & Obstacles](#progress--obstacles)
4. [Authors](#authors)

## Installation

To install and run the Torn game on your system, follow these steps:

1. **Download the Game:**
   - Download the game files.

2. **Extract the ZIP File:**
   - Unzip the downloaded ZIP file into your preferred directory.

3. **Network Configuration:**
   - Configure the IP address for your network.

4. **Launch the Game:**
   - Open the `server.py` and 'client.py' files in VSCode.
   - Run the server file first and then the client file.

6. **Ready to Play:**
   - The game will start, and after the game ends, you can click "Restart" or close the window to start a new game.

## Configuration

(Description of any additional configuration steps)

## Usage

This game is straightforward to use. Once the game is running, players can change direction using the arrow keys and must avoid obstacles such as screen borders and other players' paths. When the game ends, a "Restart" button appears, allowing players to start a new game.

## Progress & Obstacles

In the process of creating our program, we initially focused on developing the client-server architecture, ensuring smooth data flow.

Initially, we created the game for single-player mode, incorporating essential conditions and constraints, such as movement, obstacles, screen borders, and more.

Concurrently, we implemented the necessary classes for creating a player, transmitting their data to other clients, and receiving data from others.

Subsequently, we integrated the game into the client-server program, enabling communication between different players in the same game.

However, not all features work as intended, and we made various code modifications on both the game and the client structure. This resulted in multiple files and game versions:

- `jeu_seul.py`: This file contains a fully functional single-player game.
- `threads_philomèneInesGuillaume.zip`: These files were initially focused on synchronous game launching, but later code changes caused asynchronicity. The files included are `jeu.py` and `server.py`.


----------------------------- IMPORTANT  --------------------------

  
- `Threads.zip`: This set of files includes `server.py` to launch a server that can accommodate up to four clients (IP address and port need to be adjusted according to your connection, line: 111). It also includes `client.py`, which contains a useful class in `server.py`, and `test.py`, which allows you to launch a client. You can run it multiple times, keeping the server's limit in mind, and it displays multiple players playing simultaneously. **Note:** Collisions work most of the time, so if it doesn't work on the first attempt, it is recommended to relaunch. There are some missing details regarding the end of the game and its restart due to time constraints.





In summary, we encountered various challenges and obstacles during this project, including synchronizing movements between players, efficiently managing collisions, and assembling different components.

To improve this program, we would enrich the features, optimize performance, and offer a smooth and entertaining gaming experience for all participants. For example, we could change the player's shape to a motorcycle (as in the movie) and add a point system to create a ranking based on players' performance (not just the winner). We are excited to continue this project and create an exceptional final version of the "Torn" game.

As we conclude this week, we are somewhat disappointed not to have completed the project, but we are mostly pleased to have acquired all this new knowledge.

## Authors

- Guillaume Egmmann
- Ines Beaunoir
- Philomène Lamonnerie
