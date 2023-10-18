import pygame

pygame.init()


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

# Rectangle's Dimensions
player = pygame.Rect((250,250,50,50))

run = True

while run:
    
    # Background Color of Screen
    screen.fill((0,0,0))
    
    # Rectangle Player in RED color
    pygame.draw.rect(screen,(255,0,0),player)
    
    
    
    # Event Handling
    key = pygame.key.get_pressed()
    
    if key[pygame.K_a] == True:
        
        player.move_ip(-1,0)
        
    if key[pygame.K_LEFT]:
        
        player.move_ip(-1,0)
        
    elif key[pygame.K_d] == True:
        
        player.move_ip(1,0)  
              
    elif key[pygame.K_RIGHT]:
        
        player.move_ip(1,0)        
        
    elif key[pygame.K_w] == True:
        
        player.move_ip(0,-1)
        
    elif key[pygame.K_UP]:
        
        player.move_ip(0,-1)
        
    elif key[pygame.K_s] == True:
        
        player.move_ip(0,1)
        
    elif key[pygame.K_DOWN]:
        
        player.move_ip(0,1)
        
        
    # For loop to quit game
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            
            run = False
            
    pygame.display.update()
    
pygame.quit()
         
        

    