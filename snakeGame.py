# Snake Game

# To Do:
# Play, Quit, Settings menu
# In settings menu, enable/disable sound, set difficulty
# Use python logo for food image
# Add sounds
# Log high score

# imports required for this to run
import pygame, sys, random, time

check_errors = pygame.init()

if check_errors[1] > 0:
    print("(!) Had {0} inistalization errors! Exiting!".format(check_errors[1]))
    sys.exit(-1)
else:
    print("(+) PyGame successfully initialized!")

# Play Surface
playSurface = pygame.display.set_mode((720, 460))
pygame.display.set_caption('Py the Snake')
time.sleep(2)

# Colors
red = pygame.Color(255,0,0) # Color Red used for GameOver text
green = pygame.Color(0,255,0) # Color Green used for Py the Snake
black = pygame.Color(0,0,0) # Color Black used for things like score and other text
brown = pygame.Color(166,42,42) # Color Brown used for food
white = pygame.Color(255,255,255) # Color White used for the background

# FPS controller
fpsController = pygame.time.Clock()

# Important Variables
snakePos = [100,50] # Py's Starting Position
snakeBody = [[100,50], [90,50], [80,50]] # Py's Body, in the start Position
direction = 'RIGHT' # The default direction that Py is moving in
changeto = direction # Change the direction
foodPos = [random.randrange(1,72)*10,random.randrange(1,46)*10] # The position of the food
foodSpawn = True # Tells the game to initially spawn food
score = 0 # The starting score

# GameOver function
def gameOver():
    gameOverFont = pygame.font.SysFont('FreeMono', 72) # The font for GameOver
    gameOverSurface = gameOverFont.render('Game Over!', True, red) # The GameOver text
    gameOverRectangle = gameOverSurface.get_rect() # Changes the surface and font to a rectangle
    gameOverRectangle.midtop = (360, 15) # The XY coordinates to place the GameOver rectangle
    playSurface.blit(gameOverSurface,gameOverRectangle) # Place the GameOver text on to the surface
    showScore(0)
    pygame.display.flip() # Refresh the screen
    time.sleep(3)
    quitGame()

# Score function
def showScore(choice=1):
    scoreFont = pygame.font.SysFont('FreeMono', 24) # The font for the scoreFont
    scoreSurface = scoreFont.render('Score : {0}'.format(score), True, black)
    scoreRectangle = scoreSurface.get_rect() # Changes the surface and font to a rectangle
    if choice == 1:
        scoreRectangle.midtop = (80, 10)
    else:
        scoreRectangle.midtop = (360, 120)
    playSurface.blit(scoreSurface, scoreRectangle)

# Play function
## Insert code from Main Logic

# QuitGame function
def quitGame():
    pygame.quit()
    sys.exit()

# Main Logic
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quitGame()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == ord('d') or event.key == ord('D'):
                changeto = 'RIGHT'
            if event.key == pygame.K_LEFT or event.key == ord('a') or event.key == ord('A'):
                changeto = 'LEFT'
            if event.key == pygame.K_UP or event.key == ord('w') or event.key == ord('W'):
                changeto = 'UP'
            if event.key == pygame.K_DOWN or event.key == ord('s') or event.key == ord('S'):
                changeto = 'DOWN'
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))

    # Direction Validation
    if changeto == 'RIGHT' and not direction == 'LEFT':
        direction='RIGHT'
    if changeto == 'LEFT' and not direction == 'RIGHT':
        direction='LEFT'
    if changeto == 'UP' and not direction == 'DOWN':
        direction='UP'
    if changeto == 'DOWN' and not direction == 'UP':
        direction='DOWN'

    # Update Py's direction
    if direction == 'RIGHT':
        snakePos[0] += 10
    if direction == 'LEFT':
        snakePos[0] -= 10
    if direction == 'UP':
        snakePos[1] -= 10
    if direction == 'DOWN':
        snakePos[1] += 10

    # Py's awesome Body and food mechinism
    snakeBody.insert(0, list(snakePos))
    if snakePos[0] == foodPos[0] and snakePos[1] == foodPos[1]:
        foodSpawn = False
        score += 1
    else:
        snakeBody.pop()

    # Food spawn
    if foodSpawn == False:
        foodPos = [random.randrange(1,72)*10,random.randrange(1,46)*10] # The position of the food
    foodSpawn = True

    # Draw the game!
    playSurface.fill(white) # Play surface drawn first
    for pos in snakeBody: # Draw Py!
        pygame.draw.rect(playSurface, green, pygame.Rect(pos[0],pos[1],10,10))

    pygame.draw.rect(playSurface, brown, pygame.Rect(foodPos[0],foodPos[1],10,10)) # Draw some food, because Py is hungry

    if snakePos[0] > 710 or snakePos[0] < 0: # GameOver if Py hits an X wall
        gameOver()
    if snakePos[1] > 450 or snakePos[1] < 0: # GameOver if Py hits a Y wall
        gameOver()

    #GameOver if Py hits himself
    for block in snakeBody[1:]:
        if snakePos[0] == block[0] and snakePos[1] == block[1]:
            gameOver()

    showScore()
    pygame.display.flip()
    fpsController.tick(23)
