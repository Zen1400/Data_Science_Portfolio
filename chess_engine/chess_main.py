# Handle user data and display current_tate object
import chess_eng
import pygame as p

WIDTH = HEIGHT = 512
MAX_FPS = 15
DIMENSIONS = 8
SQ_SIZE = HEIGHT / DIMENSIONS
IMAGES = {}



def load_images() :
    pieces = ["wR", "wN", "wB", "wK", "wQ", "wP",
              "bR", "bN", "bB", "bK", "bQ", "bP"]

    for piece in pieces :

        IMAGES[piece] = p.transform.scale(p.image.load(f"images/{piece}.png"), (SQ_SIZE, SQ_SIZE))


# Main Driver, handle user input and update the graphics

def main() :

    p.init()

    screen = p.display.set_mode(size =(WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("White"))

    gs = chess_eng.GameState()

    i = -1 # Used to undo a move and access history

    # Only do it once before the while loop
    load_images()

    running = True

    square_selected = () # keep track of last square selected by the user
    player_clicks = [] # keep track of player clicks, two tuples (1,2), ((1,4))

    while running :



        for e in p.event.get() :
            if e.type ==  p.QUIT :
                running = False


            elif e.type == p.MOUSEBUTTONDOWN :
                location = p.mouse.get_pos() # x,y coordinates of mouse
                col = int(location[0] // SQ_SIZE)
                row = int(location[1] // SQ_SIZE)

                # undo if player clicks on the same square twice
                if square_selected == (row, col) :
                    square_selected = ()
                    player_clicks = []
                else :
                    square_selected = (row, col)
                    player_clicks.append(square_selected)

                if len(player_clicks) == 2 :


                    move = chess_eng.Move(player_clicks[0], player_clicks[1],gs.board)

                    gs.make_move(move)

                    player_clicks = []


        keys = p.key.get_pressed()
        if keys[p.K_LEFT]:
            if -i < (len(gs.history))   :
                i -= 1
                gs.board = gs.history[i]

        if keys[p.K_RIGHT] :

            if i < -1 :
                i += 1
                gs.board = gs.history[i]



        draw_game_state(screen, gs)
        clock.tick(MAX_FPS)
        p.display.update()


def draw_game_state(screen, gs) :
    """Responsible for graphics of a current game state"""
    draw_board(screen)
    draw_pieces(screen, gs.board)



def draw_board(screen) :
    colors = [p.Color('light gray'), p.Color('dark green')]

    for r in range(DIMENSIONS) :

        for c in range(DIMENSIONS) :

            color = colors[((r+c)%2)]
            p.draw.rect(screen, color, p.Rect(c* SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))




def draw_pieces(screen, board) :
    """Called once per frame"""
    for r in range(DIMENSIONS) :
        for c in range(DIMENSIONS) :
            piece = board[r][c]

            if piece != '--' :
                screen.blit(IMAGES[piece], p.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))


if __name__ == "__main__":
    main()
