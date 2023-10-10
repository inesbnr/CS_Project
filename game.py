import pygame

#class Player permet de dénirir les joueurs en fonction de leir position, de leur couleur, forme, il retient les zones de passage du joeur
class Player():
    def __init__(self,x,y,width,height,color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x,y,width,height)
        self.vel = 3
        self.passage = None
    
    def draw(self,win):
        pygame.draw.rect(win, self.color, self.rect)

    #def les déplacements du joeur
    def move(self):
        keys =pygame.key.get_pressed()#dictionnary of all thekeys if 0 we are not pressing the key
        if keys[pygame.K_LEFT]:
            self.x -= self.vel
        if keys[pygame.K_RIGHT]:
            self.x += self.vel
        if keys[pygame.K_UP]:
            self.y -= self.vel
        if keys[pygame.K_DOWN]:
            self.y += self.vel

        self.update()

    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)



class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[None for _ in range(width)] for _ in range(height)]
        self.cell_size = 15  # Adjust the cell size as needed

    def draw(self, win):
        for y in range(self.height):
            for x in range(self.width):
                cell_color = self.grid[y][x]
                if cell_color:
                    pygame.draw.rect(win, cell_color, (x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size))

    def occupy_cell(self, x, y, color):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.grid[y][x] = color



class Game:
    def __init__(self, num_players):
        self.players = [Player(50, 50, 20, 20, (255, 0, 0)) for _ in range(num_players)]


    def update_player_passage(self, player_index, passage):
        if 0 <= player_index < len(self.players):
            self.players[player_index].passage = passage

    def updte_player_passage(self, player_id, x, y):
        if 0<= player_id < len(self.players):
            self.players[player_id].x = x
            self.players[player_id].y = y
            self.players[player_id].update()


    def move_players(self):
        for player in self.players:
            player.move()
            self.check_player_position(player)

    def check_player_position(self, player):
        x = player.x // self.board.cell_size
        y = player.y // self.board.cell_size

        if self.board.grid[y][x] is None:
            self.board.occupy_cell(x, y, player.color)
        else:
            # The cell is already occupied, player loses
            self.players.remove(player)

    def draw_players(self,win):
        for player in self.players:
            player.draw(win)

    def draw_board(self, win):
        self.board.draw(win)

# Example usage:
pygame.init()

# Set up the screen and clock (you'll need to add this part)
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

game = Game(4)  # Initialize the game with 4 players

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    game.move_players()  # Move the players and check positions
    screen.fill((0, 0, 0))  # Clear the screen
    game.draw_board(screen)  # Draw the game board
    game.draw_players(screen)  # Draw the players
    pygame.display.update()  # Update the display
    clock.tick(60)  # Cap the frame rate to 60 FPS


