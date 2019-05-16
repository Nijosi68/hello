import sys

import pygame

from settings import Settings
from ship import Ship

def run_game():
    #Initialise game and create a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion : Fatman Productions")
    
    # Make a ship.
    ship = Ship(screen)
    # Set backgound colour.
    bg_colour = (230, 230, 230)

    # Start the main loop for the game.
    while True:

        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Redraw the screen during each pass through the loop.
        screen.fill(ai_settings.bg_colour)
        ship.blitme()

        # Make the most recently drawn screen visiable.
        pygame.display.flip()

run_game()
