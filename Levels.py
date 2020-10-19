class Level:
    #Generic super-class used to define a level. For each level with level" 
    #specific info we should create a separate child class"
    
    def __init__(self, ball):
        
        # Lists of sprites used in all levels.
        self.wall_list = None
        
        self.background = None   #In parent class none; we can change this per level
        self.wall_list = pygame.sprite.Group()  #list of walls; see child class
        self.ball = ball

    def update(self):
        self.wall_list.update() #Update everything in this level
        
    def draw(self, screen):
        #Draw everything on this level
        self.wall_list.draw(screen)



class Level_01(Level):
    #definition for level 1
    
    def __init__(self, ball):
        Level.__init__(self, ball) # Call the parent constructor
        self.background = pygame.image.load("PUT BACKGROUND IMAGE HERE").convert()
        self.background.set_colorkey(PUT COLOR HERE)
        

        walls = [Wall(screen, 0, 0, "horizontal", screenWidth),
                 Wall(screen, 0, 0, "vertical", screenHeight),
                 Wall(screen, screenWidth-10, 0, "vertical", screenHeight),
                 Wall(screen, 0, screenHeight-10, "horizontal", screenWidth),
                 Wall(screen, 200, 200, "horizontal", 200),
                 Wall(screen, 500, 200, "vertical", 300)] 

        
        # Go through the array above and add platforms
        for wall in walls:
           #not sure if this will work yet
           block = platforms.Platform(platform[0])
           block.rect.x = platform[1]
           block.rect.y = platform[2]
           self.wall_list.add(block)
            
            
class Level_02(Level):
    #definition for level 2
    
    def __init__(self, ball):
        Level.__init__(self, ball) # Call the parent constructor
        self.background = pygame.image.load("PUT BACKGROUND IMAGE HERE").convert()
        self.background.set_colorkey(PUT COLOR HERE)
        

        walls = [Wall(screen, 0, 0, "horizontal", screenWidth),
                 Wall(screen, 0, 0, "vertical", screenHeight),
                 Wall(screen, screenWidth-10, 0, "vertical", screenHeight),
                 Wall(screen, 0, screenHeight-10, "horizontal", screenWidth)]
                #Only has surrounding walls now

        
        # Go through the array above and add platforms
        for wall in walls:
           #not sure if this will work yet
           block = platforms.Platform(platform[0])
           block.rect.x = platform[1]
           block.rect.y = platform[2]
           self.wall_list.add(block)
