import pygame
from sys import exit
pygame.init()

game_active = True
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('my game')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 80)


sky_surf = pygame.image.load('graphics/Sky.png').convert()
ground_surf = pygame.image.load('graphics/ground.png').convert()
text_surf = test_font.render('My game', False, (64, 64, 64))
text_rect = text_surf.get_rect(midbottom=(400, 80))
snail_surf = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surf.get_rect(midbottom=(600, 300))
player_surf = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()

player_rect = player_surf.get_rect(midbottom = (40, 300))
player_gravity = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom == 300:
                    player_gravity = -22
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                snail_rect.left = 800
                game_active = True


       
        
      
                
    if game_active:
        screen.blit(sky_surf, (0, 0))
        screen.blit(ground_surf, (0, 300)) 
        pygame.draw.rect(screen, '#c0e8ec', text_rect)
        screen.blit(text_surf, text_rect)
        
        snail_rect.left -= 4
        if snail_rect.right <= 0: snail_rect.left = 800
            


        screen.blit(snail_surf, snail_rect)
    
        # Player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        screen.blit(player_surf, player_rect)

        # Collision
        if snail_rect.colliderect(player_rect):
            game_active = False
    else:
        screen.fill('Yellow')
   
    pygame.display.update()
    clock.tick(60)