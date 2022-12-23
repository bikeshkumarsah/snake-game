
#importing libraries
import pygame,sys,random,os

#initialising pygame
pygame.mixer.init()

pygame.init()
#setting screen dimensions with pixels
SCREEN_WIDTH=720
SCREEN_HEIGHT=1600

# Initialize colors
white=(255,255,255)
green=(0,65,0)
red=(255,0,0)
black=(0,0,0)
#create game window
gameWindow=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

pygame.display.set_caption('SnakesWithBikesh')

homeimg=pygame.image.load('home.png')


homeimg=pygame.transform.scale(homeimg,(SCREEN_WIDTH, SCREEN_HEIGHT)).convert_alpha()
diedimg=pygame.image.load("died.png")
diedimg=pygame.transform.scale(diedimg,(SCREEN_WIDTH,SCREEN_HEIGHT)).convert_alpha()



fps=60

clock=pygame.time.Clock()
font=pygame.font.SysFont(None,55)
def text_score(text,color,x,y):
    screen_text=font.render(text,True,color)
    gameWindow.blit(screen_text,[x,y])
font2=pygame.font.SysFont(None,130)
def text_lose(text,color,x,y):
    screen_text=font2.render(text,True,color)
    gameWindow.blit(screen_text,[x,y])

#Snake Plotting 

def plot_snake(gameWindow,color,snk_list,snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow,color,[x,y,snake_size,snake_size])
    
def welcome():
    exit_game=False
    while not exit_game:
        gameWindow.fill(green)
        gameWindow.blit(homeimg,(0,0))

        #text_score('Welcome To Snakes',black,180,600)
        #text_score('Press Space bar to play',black,150,670)
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit_game=True
            if event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE or event.type==pygame.MOUSEBUTTONDOWN:
                pygame.mixer.music.load('music.mp3')
                pygame.mixer.music.play()
                gameloop()
        pygame.display.update()
        clock.tick(fps)
        
  
def gameloop():
    #Game specific Variables
    food_x=random.randint(20,SCREEN_WIDTH//2)
    food_y=random.randint(20,SCREEN_HEIGHT//2)
    score=0
    exit_game=False
    game_over=False
    init_velocity=5
    velocity_x=0
    velocity_y=0
    snake_x=46
    snake_y=65
    snake_size=30
    snk_list=[] 
    snk_length=1
    if (not os.path.exists('hiscore.txt')):
        with open("hiscore.txt",'w')as f:
            f.write('0')
    with open('hiscore.txt','r')as f:
        hiscore=f.read()
            
    while not exit_game:
        if game_over:
            with open('hiscore.txt','w')as f:
                f.write(str(hiscore))
            #gameWindow.fill(white)
            gameWindow.blit(diedimg,(0,0))
            #text_lose('Game Over',red,180,500)
            text_lose(str(score),green,215,60)
            #text_score('Score:'+ str(score),red,400,100)
            #text_score('Want To Play again ',black,200,760)
            #text_score('Press Enter To Play Again ',black,150,850)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True
                if event.type==pygame.KEYDOWN and (event.key==pygame.K_RETURN) or event.type==pygame.MOUSEBUTTONDOWN:
                    
                    pygame.mixer.music.load('music.mp3')
                    pygame.mixer.music.play()
                    gameloop()
        else:
            for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        exit_game=False
                    if event.type==pygame.KEYDOWN:
                        if event.key==pygame.K_w or event.key==pygame.K_RIGHT or event.key==pygame.K_SPACE :
                            velocity_x=init_velocity
                            velocity_y=0
                        if event.key==pygame.K_LEFT or event.key==pygame.K_a or event.key==pygame.K_BACKSPACE :
                            velocity_x-=init_velocity
                            velocity_y=0
                        if event.key==pygame.K_s or event.key==pygame.K_UP:
                                velocity_y-=init_velocity
                                velocity_x=0
                        if event.key==pygame.K_d or event.key==pygame.K_DOWN:
                                velocity_y=init_velocity
                                velocity_x=0
                        if event. type==pygame.KEYDOWN and event.key==pygame. K_RETURN or event.type==pygame.MOUSEBUTTONUP:
                                score+=10
                                
                                
               
            snake_x+=velocity_x
            snake_y+=velocity_y
            if abs(snake_x-food_x)<20 and abs(snake_y - food_y)<20:
                pygame.mixer.music.load('point.wav')
                pygame.mixer.music.play()
                score+=10
                pygame.mixer.music.load('music.mp3')
                pygame.mixer.music.play()               
                
                if score>int(hiscore):
                    hiscore=score  
                             
                food_x=random.randint(20,SCREEN_WIDTH//2)
                food_y=random.randint(20,SCREEN_HEIGHT//2)
                snk_length+=5
                
                               
            gameWindow.fill(green)
         
            
            
            text_score('Score:'+ str(score)+" Hiscore :"+str(hiscore),red,0,5)
            
        
        
            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)
            plot_snake(gameWindow,black,snk_list,snake_size)
            if len(snk_list)>snk_length:
                del snk_list[0]
            if head in snk_list[:-1]:
                game_over=True
                pygame.mixer.music.load('death.mp3')
                pygame.mixer.music.play()
            if snake_x<0 or snake_x>SCREEN_WIDTH or snake_y<0 or snake_y>SCREEN_HEIGHT:
                game_over=True
                pygame.mixer.music.load('death.mp3')
                pygame.mixer.music.play()
                
            pygame.draw.rect(gameWindow,red,[food_x,food_y,snake_size,snake_size])
            
        pygame.display.update()
    
        clock.tick(fps)
welcome()    


pygame.quit()
quit()
sys.exit()
    