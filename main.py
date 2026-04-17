import pygame

pygame.init()

# Gets the current screen dimensions for full screen mode
info = pygame.display.Info()
screen_width, screen_height = info.current_w, info.current_h

window = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
pygame.display.set_caption("PetQuest: Secret Paws")

# Resize the background image to fit screen dimensions
original_bg = pygame.image.load("assets/images/home_bg.png").convert()
home_bg = pygame.transform.smoothscale(original_bg, (screen_width, screen_height))

# Gets the coordinates to center the background image on the screen
bg_rect = home_bg.get_rect()
bg_rect.center = (screen_width // 2, screen_height // 2 )

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

    # Exit full screen mode with (ESC) key
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        running = False

  window.blit(home_bg, bg_rect)
  pygame.display.flip()

pygame.quit()