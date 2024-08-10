import pygame

pygame.init()

screen_width = 900
screen_height = 900

screen = pygame.display.set_mode((screen_width,screen_height))

#timer for framerate
timer = pygame.time.Clock()
fps = 60

#counter that counts to 30 and restarts, useful for when one side performs a checkmate and a rectangle flashes 2 times a second on the king's tile.
counter = 0

run = True

#chess table and background
bg = pygame.image.load('chess.jpg')
bg = pygame.transform.smoothscale(bg,(800,800))
bg2 = pygame.image.load('bg2.jpeg')
bg2 = pygame.transform.smoothscale(bg2,(1000,900))

status_font = pygame.font.Font('freesansbold.ttf',50)
font = pygame.font.Font('freesansbold.ttf',20)

pygame.display.set_caption('BATMAN STRATEGY INTERFACE')
icon = pygame.image.load('batman.png')
pygame.display.set_icon(icon)

#Player pieces, for the sake of simplicity, i will call Heroes' pieces "white pieces", and Villains' pieces "black pieces", this is totally not because i plagiarized some of the code.
white_pieces = ['rook','knight','bishop','king','queen','bishop','knight','rook',
               'pawn','pawn','pawn','pawn','pawn','pawn','pawn','pawn']

white_location = [(0,7),(1,7),(2,7),(3,7),(4,7),(5,7),(6,7),(7,7),
                  (0,6),(1,6),(2,6),(3,6),(4,6),(5,6),(6,6),(7,6)]
captured_white = []

black_pieces = ['rook','knight','bishop','king','queen','bishop','knight','rook',
               'pawn','pawn','pawn','pawn','pawn','pawn','pawn','pawn']

black_location = [(0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),
                  (0,1),(1,1),(2,1),(3,1),(4,1),(5,1),(6,1),(7,1)]
captured_black = []


# PIECES IMG
black_queen = pygame.image.load("Black/catwomanq.png")
black_queen = pygame.transform.smoothscale(black_queen,(80,90))
black_queen_small = pygame.transform.smoothscale(black_queen,(45,55))

black_king = pygame.image.load("Black/darkseidk.png")
black_king = pygame.transform.smoothscale(black_king,(80,90))
black_king_small = pygame.transform.smoothscale(black_king,(45,55))

black_pawn = pygame.image.load("Black/gridp.png")
black_pawn = pygame.transform.smoothscale(black_pawn,(80,90))
black_pawn_small = pygame.transform.smoothscale(black_pawn,(45,55))

black_knight = pygame.image.load("Black/harleykn.png")
black_knight = pygame.transform.smoothscale(black_knight,(80,90))
black_knight_small = pygame.transform.smoothscale(black_knight,(45,55))

black_bishop = pygame.image.load("Black/jokerb.png")
black_bishop = pygame.transform.smoothscale(black_bishop,(80,90))
black_bishop_small = pygame.transform.smoothscale(black_bishop,(45,55))

black_rook = pygame.image.load("Black/zodr.png")
black_rook = pygame.transform.smoothscale(black_rook,(80,90))
black_rook_small = pygame.transform.smoothscale(black_rook,(45,55))


white_queen = pygame.image.load("White/wonderwomanq.png")
white_queen = pygame.transform.smoothscale(white_queen,(80,90))
white_queen_small = pygame.transform.smoothscale(white_queen,(45,55))

white_king = pygame.image.load("White/supermank.png")
white_king = pygame.transform.smoothscale(white_king,(80,90))
white_king_small = pygame.transform.smoothscale(white_king,(45,55))

white_pawn = pygame.image.load("White/cyborgp.png")
white_pawn = pygame.transform.smoothscale(white_pawn,(70,90))
white_pawn_small = pygame.transform.smoothscale(white_pawn,(45,55))

white_knight = pygame.image.load("White/flashkn.png")
white_knight = pygame.transform.smoothscale(white_knight,(70,90))
white_knight_small = pygame.transform.smoothscale(white_knight,(45,55))

white_bishop = pygame.image.load("White/greenlanternb.png")
white_bishop = pygame.transform.smoothscale(white_bishop,(80,90))
white_bishop_small = pygame.transform.smoothscale(white_bishop,(45,55))

white_rook = pygame.image.load("White/batmanr.png")
white_rook = pygame.transform.smoothscale(white_rook,(80,90))
white_rook_small = pygame.transform.smoothscale(white_rook,(45,55))


#image list with the black and white variables that contain the images
#small images with the black and white small images for display when unit is captured

piece_list = ['rook','knight','bishop','king','queen','pawn']


black_images = [black_rook,black_knight,black_bishop,black_king,black_queen,black_pawn]
black_images_small = [black_rook_small,black_knight_small,black_bishop_small,black_king_small,black_queen_small,black_pawn_small]

white_images = [white_rook,white_knight,white_bishop,white_king,white_queen,white_pawn]
white_images_small = [white_rook_small,white_knight_small,white_bishop_small,white_king_small,white_queen_small,white_pawn_small]







#white turn no selection: 0, white turn selection: 1, black turn no selection: 2, black turn selection: 3

turn_step = 0
selection = 100
valid_moves = []
winner = ''
game_over = False
def draw_board():
    for i in range(32):
        column = i % 4
        row = i // 4
        
        turn_text = ["Heroes' Turn!","Select a tile.","Villains' Turn!","Select a tile."]
        screen.blit(status_font.render(turn_text[turn_step],True,'black'),(210,830))


#draw pieces on chess table :D

def draw_pieces():
    for i in range(len(white_pieces)):
        index = piece_list.index(white_pieces[i])
        screen.blit(white_images[index],(white_location[i][0]*90+40, white_location[i][1] *90 +40))

        if turn_step < 2:
            if selection == i:
                pygame.draw.rect(screen,'white',[white_location[i][0]*90+40,white_location[i][1]*90+40,90,90],2)
            

    for i in range(len(black_pieces)):
        index2 = piece_list.index(black_pieces[i])
        screen.blit(black_images[index2],(black_location[i][0]*90+40, black_location[i][1]*90+40))

        if turn_step >= 2:
            if selection == i:
                pygame.draw.rect(screen,'black',[black_location[i][0]*90+40,black_location[i][1]*90+40,90,90],2)








# Checking what path a pawn can take.
def check_pawn(position,color):
    moves_list = []
    if color == 'white':
        if (position[0],position[1]-1) not in white_location and \
            (position[0],position[1]-1) not in black_location and position[1] > 0 :
            moves_list.append((position[0],position[1]-1))
        if (position[0],position[1]-2) not in white_location and \
            (position[0],position[1]-2) not in black_location and position[1] == 6 :
            moves_list.append((position[0],position[1]-2))
        #attack opportunities
        if(position[0] +1, position[1]-1) in black_location:
            moves_list.append((position[0]+1,position[1]-1))
        if(position[0] -1, position[1]-1) in black_location:
            moves_list.append((position[0]-1,position[1]-1))
    
    else:
        if (position[0],position[1]+1) not in white_location and \
            (position[0],position[1]+1) not in black_location and position[1] < 7 :
            moves_list.append((position[0],position[1]+1))
        if (position[0],position[1]+2) not in white_location and \
            (position[0],position[1]+2) not in black_location and position[1] == 1 :
            moves_list.append((position[0],position[1]+2))
        #attack opportunities
        if(position[0] -1, position[1]+1) in white_location:
            moves_list.append((position[0]-1,position[1]+1))
        if(position[0] +1, position[1]+1) in white_location:
            moves_list.append((position[0]+1,position[1]+1))
    return moves_list

def check_rook(position,color):
    moves_list = []
    if color == 'white':
        enemies_list = black_location
        friends_list = white_location
    if color == 'black':
        enemies_list = white_location
        friends_list = black_location
    #for up down left right
    for i in range(4):
        path = True
        chain = 1        #length of move chain

        if i == 0:  #up
            x = 0
            y = -1
        elif i == 1: #down
            x = 0
            y = 1
        elif i == 2: #left
            x = -1
            y = 0
        else: #right
            x = 1
            y = 0
        while path:
            if (position[0] + (chain * x), position[1] + (chain * y)) not in friends_list and \
            0 <= position[0] + (chain * x) <= 7 and 0 <= position[1] + (chain * y) <= 7:               
                moves_list.append((position[0]+(chain*x),position[1]+(chain*y)))

                if (position[0] + (chain * x), position[1] + (chain * y)) in enemies_list:
                    path = False
                chain += 1    

            else:
                path = False


    return moves_list

#check valid knight moves
def check_knight(position,color):
    moves_list = []
    if color == 'white':
        enemies_list = black_location
        friends_list = white_location
    if color == 'black':
        enemies_list = white_location
        friends_list = black_location
    
    targets = [(1,-2),(-1,-2),(1,2),(-1,2),(2,-1),(2,1),(-2,-1),(-2,1)]
    for i in range(8):
        target = (position[0] + targets[i][0],position[1] + targets[i][1])
        if target not in friends_list and 0 <= target[0] <= 7 and 0 <= target[1] <=7:
            moves_list.append(target)

    return moves_list

#check valid bishop moves
def check_bishop(position,color):
    moves_list = []
    if color == 'white':
        enemies_list = black_location
        friends_list = white_location
    else:
        enemies_list = white_location
        friends_list = black_location

    #for up-right up-left down-right down-left
    for i in range(4):
        path = True
        chain = 1        #length of move chain

        if i == 0:  #up-right
            x = 1
            y = -1
        elif i == 1: #up-left
            x = -1
            y = -1
        elif i == 2: #down-right
            x = 1
            y = 1
        else: #down-left
            x = -1
            y = 1
        while path:
            if (position[0] + (chain * x), position[1] + (chain * y)) not in friends_list and \
            0 <= position[0] + (chain * x) <= 7 and 0 <= position[1] + (chain * y) <= 7:               
                moves_list.append((position[0]+(chain*x),position[1]+(chain*y)))

                if (position[0] + (chain * x), position[1] + (chain * y)) in enemies_list:
                    path = False
                chain += 1    

            else:
                path = False

    return moves_list

#check valid queen moves
def check_queen(position,color):
    moves_list= check_bishop(position,color)
    second_list = check_rook(position,color)
    for i in range(len(second_list)):
        moves_list.append(second_list[i])

    return moves_list

#check valid king moves
def check_king(position,color):
    moves_list = []
    if color == 'white':
        enemies_list = black_location
        friends_list = white_location
    else:
        enemies_list = white_location
        friends_list = black_location
    targets = [(0,-1),(0,1),(-1,0),(1,0),(1,-1),(-1,-1),(1,1),(-1,1)]
    for i in range(8): #up down left right up-right up-left down-right down-left
        target = (position[0] + targets[i][0],position[1] + targets[i][1])
        if target not in friends_list and 0 <= target[0] <= 7 and 0 <= target[1] <=7:
            moves_list.append(target)


    return moves_list     

#draws captured pieces on the right side of the screen, down to up for white pieces, and up to down for black pieces
def draw_captured():
    for i in range(len(captured_white)):
        captured_piece = captured_white[i]
        index = piece_list.index(captured_piece)
        screen.blit(black_images_small[index],(845,50*i))
    
    for i in range(len(captured_black)):
        captured_piece = captured_black[i]
        index = piece_list.index(captured_piece)
        screen.blit(white_images_small[index],(845,845-50*i))

#checking all moves available
def check_options(pieces,locations,turn):
    moves_list = []
    all_moves_list = []
    
    for i in range((len(pieces))): 
        location = locations[i]
        piece = pieces[i]
        if piece == 'pawn':
            moves_list = check_pawn(location,turn)
        elif piece == 'rook':
            moves_list = check_rook(location,turn)
        elif piece == 'knight':
            moves_list = check_knight(location,turn)
        elif piece == 'bishop':
            moves_list = check_bishop(location,turn)
        elif piece == 'queen':
            moves_list = check_queen(location,turn)
        elif piece == 'king':
            moves_list = check_king(location,turn)
        
        all_moves_list.append(moves_list)
    return all_moves_list

black_options = check_options(black_pieces,black_location, 'black')
white_options = check_options(white_pieces,white_location,'white')


#check for valid moves for selected piece

def check_valid_moves():
    if turn_step <2:
        options_list = white_options

    else:
        options_list = black_options
    valid_options = options_list[selection]
    return valid_options



#Draw valid moves for selected piece

def draw_valid(moves):
    if turn_step <2:
        color = 'white'
    
    else:
        color = 'black'

    for i in range(len(moves)):
        pygame.draw.circle(screen, color, (moves[i][0]*90+85,moves[i][1]*90+80),5)



def draw_check():
    if turn_step < 2:
        if 'king' in white_pieces:
            king_index = white_pieces.index('king')
            king_location = white_location[king_index]
            for i in range(len(black_options)):
                if king_location in black_options[i]:
                    if counter < 15:
                        pygame.draw.rect(screen,'dark red',[white_location[king_index][0]*90+40,white_location[king_index][1]*90+40,90,90],5)
    else:
        if 'king' in black_pieces:
            king_index = black_pieces.index('king')
            king_location = black_location[king_index]
            for i in range(len(white_options)):
                if king_location in white_options[i]:
                    if counter < 15:
                        pygame.draw.rect(screen,'dark red',[black_location[king_index][0]*90+40,black_location[king_index][1]*90+40,90,90],5)
                

def draw_game_over():
    pygame.draw.rect(screen,'black',[200,200,400,70])
    screen.blit(font.render(f'{winner} won the battle!',True,'white'), (210,210))
    screen.blit(font.render(f'Press ENTER to restart!',True,'white'), (210,240))


while run:
    timer.tick(fps)
    screen.fill((255, 87, 51))
    screen.blit(bg2,(0,0))
    screen.blit(bg,(0,0))
    draw_pieces()
    draw_board()
    draw_captured()

    if counter < 30:
        counter += 1
    else:
        counter = 0
    draw_check()

    if selection != 100:
        valid_moves = check_valid_moves()
        draw_valid(valid_moves)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not game_over:
            x_coord = event.pos[0] // 97 
            y_coord = event.pos[1] // 97 
            
            print ("x = ", event.pos[0])
            print ("y = ", event.pos[1])
            click_coords = (x_coord, y_coord)
            if turn_step < 2:
                if click_coords in white_location:
                    selection = white_location.index(click_coords)
                    if turn_step == 0:
                        turn_step = 1
                if click_coords in valid_moves and selection != 100:
                    white_location[selection] = click_coords
                    if click_coords in black_location:
                        black_piece = black_location.index(click_coords)
                        captured_white.append(black_pieces[black_piece])
                        if black_pieces[black_piece] == 'king':
                            winner = "HEROES"
                        black_pieces.pop(black_piece)
                        black_location.pop(black_piece)
                    black_options = check_options(black_pieces,black_location, 'black')
                    white_options = check_options(white_pieces,white_location,'white')
                    turn_step = 2
                    selection = 100
                    valid_moves = []
            if turn_step >= 2:
                if click_coords in black_location:
                    selection = black_location.index(click_coords)
                    if turn_step == 2:
                        turn_step = 3
                if click_coords in valid_moves and selection != 100:
                    black_location[selection] = click_coords
                    if click_coords in white_location:
                        white_piece = white_location.index(click_coords)
                        captured_black.append(white_pieces[white_piece])
                        if white_pieces[white_piece] == 'king':
                            winner = "VILLAINS"
                        white_pieces.pop(white_piece)
                        white_location.pop(white_piece)
                    black_options = check_options(black_pieces,black_location, 'black')
                    white_options = check_options(white_pieces,white_location,'white')
                    turn_step = 0
                    selection = 100
                    valid_moves = []    
        if event.type == pygame.KEYDOWN and game_over:
            if event.key == pygame.K_RETURN:
                game_over = False
                
                winner = ''
                turn_step = 0
                selection = 100
                valid_moves = []
                white_pieces = ['rook','knight','bishop','king','queen','bishop','knight','rook',
               'pawn','pawn','pawn','pawn','pawn','pawn','pawn','pawn']

                white_location = [(0,7),(1,7),(2,7),(3,7),(4,7),(5,7),(6,7),(7,7),
                                (0,6),(1,6),(2,6),(3,6),(4,6),(5,6),(6,6),(7,6)]
                captured_white = []

                black_pieces = ['rook','knight','bishop','king','queen','bishop','knight','rook',
                            'pawn','pawn','pawn','pawn','pawn','pawn','pawn','pawn']

                black_location = [(0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),
                                (0,1),(1,1),(2,1),(3,1),(4,1),(5,1),(6,1),(7,1)]
                captured_black = []
                black_options = check_options(black_pieces,black_location, 'black')
                white_options = check_options(white_pieces,white_location,'white')

    if winner != '':
        game_over = True
        draw_game_over()                

    pygame.display.update()
pygame.quit()