#MSPAINT in Python
#This is MS pain in a python format, the user can choose to pain a sqaure or a circle
#as well as clear, fill in areas, and draw in general
#There is a preview on the right side to show what will be printed including a color pallete on the left
#The user can also select the width and height of the program as well as can save and load pngs into the file application!

import  pygame

pygame.init()

try:
    WINDOW_WIDTH = int(input("Choose width of the window(450-1900): "))
    WINDOW_HEIGHT = int(input("Choose height of the window(250-1050): "))

    if WINDOW_WIDTH <450:
        WINDOW_WIDTH =450
    elif WINDOW_WIDTH>1900:
        WINDOW_WIDTH =1900
    if WINDOW_HEIGHT <250:
        WINDOW_HEIGHT =250
    elif WINDOW_HEIGHT>1050:
        WINDOW_HEIGHT =1050


except ValueError:
    print("You entered a letter/phrase! Try again")
    exit()

#the orginal constants of which I started this project with
#WINDOW_WIDTH = 600
#WINDOW_HEIGHT = 750
win = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))


pygame.display.set_caption("Python Paint")

#Features to add later in its lifetime....

#Fix FILL so it does it only for certain regions
#FIX FILL FOR IMPORTED PICTURES
#FIX LOAD FOR CERTAIN PICTURES SO THAT WINDOW RESIZES WITH LOADED PICTURE

#Features to possibly add now:
#ALLOW TO CHOOSE AND BROWSE FILES FOR PICTURE
#SAYS "SAVED!" WHEN CLICKING SAVE(USER CAN MAYBE ENTER NAME OF FILE WITH EXTENSION AS WELL)



def resetcolorselect():
    pygame.draw.rect(win,(255,0,0), (30,WINDOW_HEIGHT-120,30,30))#RED
    pygame.draw.rect(win,(0,255,0), (60,WINDOW_HEIGHT-120,30,30))#GREEN
    pygame.draw.rect(win,(0,0,255), (90,WINDOW_HEIGHT-120,30,30))#BLUE

    pygame.draw.rect(win,(255,255,0), (30,WINDOW_HEIGHT-90,30,30))#YELLOW
    pygame.draw.rect(win,(255,0,255), (60,WINDOW_HEIGHT-90,30,30))#MAGENTA
    pygame.draw.rect(win,(0,255,255), (90,WINDOW_HEIGHT-90,30,30))#CYAN

    pygame.draw.rect(win,(255,165,0), (30,WINDOW_HEIGHT-60,30,30))#ORANGE
    pygame.draw.rect(win,(0,0,0), (60,WINDOW_HEIGHT-60,30,30))#BLACK
    pygame.draw.rect(win,(255,255,255), (90,WINDOW_HEIGHT-60,30,30))#WHITE


    pygame.draw.rect(win,(0,0,0),(30,WINDOW_HEIGHT-125,90,5))#GRID FOR COLORS
    pygame.draw.rect(win,(0,0,0),(25,WINDOW_HEIGHT-125,5,100))
    pygame.draw.rect(win,(0,0,0),(30,WINDOW_HEIGHT-30,90,5))
    pygame.draw.rect(win,(0,0,0),(120,WINDOW_HEIGHT-125,5,100))

    pygame.draw.rect(win,(0,0,0),(30,WINDOW_HEIGHT-91,90,2))
    pygame.draw.rect(win,(0,0,0),(30,WINDOW_HEIGHT-61,90,2))
    pygame.draw.rect(win,(0,0,0),(59,WINDOW_HEIGHT-120,2,90))
    pygame.draw.rect(win,(0,0,0),(89,WINDOW_HEIGHT-120,2,90))


def initialize ():

    win.fill((255,255,255))
    pygame.draw.rect(win,(0,0,0), (0,WINDOW_HEIGHT-150,WINDOW_WIDTH,10))


    resetcolorselect()

    font = pygame.font.SysFont(None, 22)#PREVIEW
    img1 = font.render('Preview', True, (0,0,0))
    win.blit(img1, (WINDOW_WIDTH-120, WINDOW_HEIGHT-130))

    img2 = font.render('C', True, (0,0,0))
    win.blit(img2, (150, WINDOW_HEIGHT-112))
    
    pygame.draw.line(win, (0,0,0),(140,WINDOW_HEIGHT-120),(170,WINDOW_HEIGHT-120), 2)
    pygame.draw.line(win, (0,0,0),(140,WINDOW_HEIGHT-32),(170,WINDOW_HEIGHT-32), 2)
    pygame.draw.line(win, (0,0,0),(140,WINDOW_HEIGHT-120),(140,WINDOW_HEIGHT-32), 2)
    pygame.draw.line(win, (0,0,0),(170,WINDOW_HEIGHT-120),(170,WINDOW_HEIGHT-32), 2)

    pygame.draw.line(win, (0,0,0),(140,WINDOW_HEIGHT-90),(170,WINDOW_HEIGHT-90), 2)
    pygame.draw.line(win, (0,0,0),(140,WINDOW_HEIGHT-60),(170,WINDOW_HEIGHT-60), 2)
    

    img3 = font.render('F', True, (0,0,0))
    win.blit(img3, (151, WINDOW_HEIGHT-80))

    img4 = font.render('W', True, (0,0,0))
    win.blit(img4, (149, WINDOW_HEIGHT-50))




    pygame.draw.line(win,(0,0,0),(180,WINDOW_HEIGHT-120),(220,WINDOW_HEIGHT-120), 2)#SQUARE FOR SQU
    pygame.draw.line(win,(0,0,0),(180,WINDOW_HEIGHT-80),(220,WINDOW_HEIGHT-80), 2)
    pygame.draw.line(win,(0,0,0),(180,WINDOW_HEIGHT-120),(180,WINDOW_HEIGHT-80), 2)
    pygame.draw.line(win,(0,0,0),(220,WINDOW_HEIGHT-120),(220,WINDOW_HEIGHT-79), 2)

    img5 = font.render('SQU', True, (0,0,0))
    win.blit(img5, (185, WINDOW_HEIGHT-105))





    pygame.draw.circle(win,(0,0,0),(199,WINDOW_HEIGHT-44),20)#CIRCLE FOR CIR
    pygame.draw.circle(win,(255,255,255),(199,WINDOW_HEIGHT-44),18)

    img6 = font.render('CIR', True, (0,0,0))
    win.blit(img6, (185, WINDOW_HEIGHT-50))




    img7 = font.render('Save', True, (0,0,0))#SAVE
    win.blit(img7, (235, WINDOW_HEIGHT-110))

    pygame.draw.line(win,(0,0,0),(230,WINDOW_HEIGHT-115),(275,WINDOW_HEIGHT-115), 2)
    pygame.draw.line(win,(0,0,0),(230,WINDOW_HEIGHT-95),(275,WINDOW_HEIGHT-95), 2)
    pygame.draw.line(win,(0,0,0),(230,WINDOW_HEIGHT-115),(230,WINDOW_HEIGHT-95), 2)
    pygame.draw.line(win,(0,0,0),(275,WINDOW_HEIGHT-115),(275,WINDOW_HEIGHT-94), 2)

    img8 = font.render('Load', True, (0,0,0))#LOAD
    win.blit(img8, (235, WINDOW_HEIGHT-50))
    
    pygame.draw.line(win,(0,0,0),(230,WINDOW_HEIGHT-55),(275,WINDOW_HEIGHT-55), 2)
    pygame.draw.line(win,(0,0,0),(230,WINDOW_HEIGHT-35),(275,WINDOW_HEIGHT-35), 2)
    pygame.draw.line(win,(0,0,0),(230,WINDOW_HEIGHT-55),(230,WINDOW_HEIGHT-35), 2)
    pygame.draw.line(win,(0,0,0),(275,WINDOW_HEIGHT-55),(275,WINDOW_HEIGHT-34), 2)
    
    
    


def main():
    xRect=0
    yRect=0
    xCir = 0
    yCir = 0

    width = 100
    height = 100
    cirRad = 50
    run = True
    drawColor = [0,0,0]#DRAW RED BOX AROUND BLACK

    drawBool = True
    fillColor = [255,255,255]
    squDraw = False
    initialize()
    clock = pygame.time.Clock()

    pygame.draw.line(win,(255,0,0),(59,WINDOW_HEIGHT-60),(59,WINDOW_HEIGHT-30),2)
    pygame.draw.line(win,(255,0,0),(59,WINDOW_HEIGHT-61),(90,WINDOW_HEIGHT-61),2)
    pygame.draw.line(win,(255,0,0),(90,WINDOW_HEIGHT-61),(90,WINDOW_HEIGHT-30),2)
    pygame.draw.line(win,(255,0,0),(59,WINDOW_HEIGHT-30),(90,WINDOW_HEIGHT-30),2)
    pygame.draw.circle(win,(255,0,0),(199,WINDOW_HEIGHT-44),20)#CIRCLE FOR CIR
    pygame.draw.circle(win,(255,255,255),(199,WINDOW_HEIGHT-44),18)
    font = pygame.font.SysFont(None, 22)#PREVIEW
    img6 = font.render('CIR', True, (0,0,0))
    win.blit(img6, (185, WINDOW_HEIGHT-50))

    while run:



        msElapsed = clock.tick(10000)

        xRect = pygame.mouse.get_pos()[0]
        yRect = pygame.mouse.get_pos()[1]
        
        if yRect>= ((WINDOW_HEIGHT-150)-height/2):
            yRect = (WINDOW_HEIGHT-150)-height/2
        elif yRect<=0+height/2:
            yRect= 0+height/2

        if xRect>= (WINDOW_WIDTH- width/2):
            xRect = WINDOW_WIDTH- width/2
        elif xRect<= 0+ width/2:
            xRect = 0+ width/2
        
        xCir = pygame.mouse.get_pos()[0]
        yCir = pygame.mouse.get_pos()[1]

        if xCir>=WINDOW_WIDTH-cirRad:
            xCir = WINDOW_WIDTH-cirRad
        elif xCir<=cirRad:
            xCir = cirRad
        if yCir>= WINDOW_HEIGHT-150-cirRad:
            yCir = WINDOW_HEIGHT-150-cirRad
        elif yCir<=cirRad:
            yCir = cirRad

        if drawBool:#draw red box around "W"(write)
            pygame.draw.line(win, (255,0,0),(140,WINDOW_HEIGHT-60),(170,WINDOW_HEIGHT-60), 2)
            pygame.draw.line(win, (255,0,0),(170,WINDOW_HEIGHT-60),(170,WINDOW_HEIGHT-32), 2)
            pygame.draw.line(win, (255,0,0),(140,WINDOW_HEIGHT-60),(140,WINDOW_HEIGHT-32), 2)
            pygame.draw.line(win, (255,0,0),(140,WINDOW_HEIGHT-32),(170,WINDOW_HEIGHT-32), 2)
            
            pygame.draw.line(win, (0,0,0),(140,WINDOW_HEIGHT-90),(170,WINDOW_HEIGHT-90), 2)
            pygame.draw.line(win, (0,0,0),(140,WINDOW_HEIGHT-90),(140,WINDOW_HEIGHT-60), 2)
            pygame.draw.line(win, (0,0,0),(170,WINDOW_HEIGHT-90),(170,WINDOW_HEIGHT-60), 2)

        elif not drawBool:#Draw red box around "F"(fill)
            pygame.draw.line(win, (255,0,0),(140,WINDOW_HEIGHT-90),(170,WINDOW_HEIGHT-90), 2)
            pygame.draw.line(win, (255,0,0),(140,WINDOW_HEIGHT-60),(170,WINDOW_HEIGHT-60), 2)
            pygame.draw.line(win, (255,0,0),(140,WINDOW_HEIGHT-90),(140,WINDOW_HEIGHT-60), 2)
            pygame.draw.line(win, (255,0,0),(170,WINDOW_HEIGHT-90),(170,WINDOW_HEIGHT-60), 2)

            pygame.draw.line(win, (0,0,0),(170,WINDOW_HEIGHT-60),(170,WINDOW_HEIGHT-32), 2)
            pygame.draw.line(win, (0,0,0),(140,WINDOW_HEIGHT-60),(140,WINDOW_HEIGHT-32), 2)
            pygame.draw.line(win, (0,0,0),(140,WINDOW_HEIGHT-32),(170,WINDOW_HEIGHT-32), 2)



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif pygame.mouse.get_pressed()[0] and drawBool and pygame.mouse.get_pos()[1]<=(WINDOW_HEIGHT-150):
                if squDraw:
                    pygame.draw.rect(win,drawColor, ((xRect-(width/2)),(yRect-(height)/2),width,height))
                elif not squDraw:
                    pygame.draw.circle(win, drawColor,(xCir,yCir),cirRad)

            elif pygame.mouse.get_pressed()[0] and pygame.mouse.get_pos()[1]<=(WINDOW_HEIGHT-150) and not drawBool:
                fillColor = [255,255,255]
                fillColor = list(pygame.Surface.get_at(win,(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])))[0:3]

                for i in range(WINDOW_WIDTH):
                    for j in range(WINDOW_HEIGHT-150):
                        if list(pygame.Surface.get_at(win,[i,j]))[0] == fillColor[0] and list(pygame.Surface.get_at(win,[i,j]))[1] == fillColor[1] and list(pygame.Surface.get_at(win,[i,j]))[2] == fillColor[2] :
                            pygame.Surface.set_at(win,(i,j),(drawColor))

            elif pygame.mouse.get_pressed()[0] and 30<=pygame.mouse.get_pos()[0]<60 and WINDOW_HEIGHT-120<=pygame.mouse.get_pos()[1]<WINDOW_HEIGHT-90:#RED
                drawColor = [255,0,0]
                resetcolorselect()
                pygame.draw.line(win,(255,0,0),(29,WINDOW_HEIGHT-120),(29,WINDOW_HEIGHT-90),2)
                pygame.draw.line(win,(255,0,0),(29,WINDOW_HEIGHT-120),(59,WINDOW_HEIGHT-120),2)
                pygame.draw.line(win,(255,0,0),(59,WINDOW_HEIGHT-120),(59,WINDOW_HEIGHT-90),2)
                pygame.draw.line(win,(255,0,0),(29,WINDOW_HEIGHT-91),(59,WINDOW_HEIGHT-91),2)
            elif pygame.mouse.get_pressed()[0] and 60<=pygame.mouse.get_pos()[0]<90 and WINDOW_HEIGHT-120<=pygame.mouse.get_pos()[1]<WINDOW_HEIGHT-90:#GREEN
                drawColor = [0,255,0]
                resetcolorselect()
                pygame.draw.line(win,(255,0,0),(59,WINDOW_HEIGHT-120),(59,WINDOW_HEIGHT-90),2)
                pygame.draw.line(win,(255,0,0),(59,WINDOW_HEIGHT-120),(90,WINDOW_HEIGHT-120),2)
                pygame.draw.line(win,(255,0,0),(89,WINDOW_HEIGHT-120),(89,WINDOW_HEIGHT-90),2)
                pygame.draw.line(win,(255,0,0),(59,WINDOW_HEIGHT-91),(90,WINDOW_HEIGHT-91),2)
            elif pygame.mouse.get_pressed()[0] and 90<=pygame.mouse.get_pos()[0]<120 and WINDOW_HEIGHT-120<=pygame.mouse.get_pos()[1]<WINDOW_HEIGHT-90:#BLUE
                drawColor = [0,0,255]
                resetcolorselect()
                pygame.draw.line(win,(255,0,0),(90,WINDOW_HEIGHT-120),(90,WINDOW_HEIGHT-90),2)
                pygame.draw.line(win,(255,0,0),(90,WINDOW_HEIGHT-120),(120,WINDOW_HEIGHT-120),2)
                pygame.draw.line(win,(255,0,0),(120,WINDOW_HEIGHT-120),(120,WINDOW_HEIGHT-90),2)
                pygame.draw.line(win,(255,0,0),(90,WINDOW_HEIGHT-91),(120,WINDOW_HEIGHT-91),2)
            elif pygame.mouse.get_pressed()[0] and 30<=pygame.mouse.get_pos()[0]<60 and WINDOW_HEIGHT-90<=pygame.mouse.get_pos()[1]<WINDOW_HEIGHT-60:#YELLOW
                drawColor = [255,255,0]
                resetcolorselect()
                pygame.draw.line(win,(255,0,0),(29,WINDOW_HEIGHT-90),(29,WINDOW_HEIGHT-60),2)
                pygame.draw.line(win,(255,0,0),(29,WINDOW_HEIGHT-90),(59,WINDOW_HEIGHT-90),2)
                pygame.draw.line(win,(255,0,0),(59,WINDOW_HEIGHT-90),(59,WINDOW_HEIGHT-60),2)
                pygame.draw.line(win,(255,0,0),(29,WINDOW_HEIGHT-61),(59,WINDOW_HEIGHT-61),2)
            elif pygame.mouse.get_pressed()[0] and 60<=pygame.mouse.get_pos()[0]<90 and WINDOW_HEIGHT-90<=pygame.mouse.get_pos()[1]<WINDOW_HEIGHT-60:#MAGENTA
                drawColor = [255,0,255]
                resetcolorselect()
                pygame.draw.line(win,(255,0,0),(59,WINDOW_HEIGHT-90),(59,WINDOW_HEIGHT-60),2)
                pygame.draw.line(win,(255,0,0),(59,WINDOW_HEIGHT-90),(90,WINDOW_HEIGHT-90),2)
                pygame.draw.line(win,(255,0,0),(89,WINDOW_HEIGHT-90),(89,WINDOW_HEIGHT-60),2)
                pygame.draw.line(win,(255,0,0),(59,WINDOW_HEIGHT-61),(90,WINDOW_HEIGHT-61),2)
            elif pygame.mouse.get_pressed()[0] and 90<=pygame.mouse.get_pos()[0]<120 and WINDOW_HEIGHT-90<=pygame.mouse.get_pos()[1]<WINDOW_HEIGHT-60:#CYAN
                drawColor = [0,255,255]
                resetcolorselect()
                pygame.draw.line(win,(255,0,0),(90,WINDOW_HEIGHT-90),(90,WINDOW_HEIGHT-60),2)
                pygame.draw.line(win,(255,0,0),(90,WINDOW_HEIGHT-90),(120,WINDOW_HEIGHT-90),2)
                pygame.draw.line(win,(255,0,0),(120,WINDOW_HEIGHT-90),(120,WINDOW_HEIGHT-60),2)
                pygame.draw.line(win,(255,0,0),(90,WINDOW_HEIGHT-61),(120,WINDOW_HEIGHT-61),2)
            elif pygame.mouse.get_pressed()[0] and 30<=pygame.mouse.get_pos()[0]<60 and WINDOW_HEIGHT-60<=pygame.mouse.get_pos()[1]<WINDOW_HEIGHT-30:#ORANGE
                drawColor = [255,165,0]
                resetcolorselect()
                pygame.draw.line(win,(255,0,0),(29,WINDOW_HEIGHT-59),(29,WINDOW_HEIGHT-30),2)
                pygame.draw.line(win,(255,0,0),(29,WINDOW_HEIGHT-61),(59,WINDOW_HEIGHT-61),2)
                pygame.draw.line(win,(255,0,0),(59,WINDOW_HEIGHT-61),(59,WINDOW_HEIGHT-30),2)
                pygame.draw.line(win,(255,0,0),(29,WINDOW_HEIGHT-30),(59,WINDOW_HEIGHT-30),2)
            elif pygame.mouse.get_pressed()[0] and 60<=pygame.mouse.get_pos()[0]<90 and WINDOW_HEIGHT-60<=pygame.mouse.get_pos()[1]<WINDOW_HEIGHT-30:#BLACK
                drawColor = [0,0,0]
                resetcolorselect()
                pygame.draw.line(win,(255,0,0),(59,WINDOW_HEIGHT-60),(59,WINDOW_HEIGHT-30),2)
                pygame.draw.line(win,(255,0,0),(59,WINDOW_HEIGHT-61),(90,WINDOW_HEIGHT-61),2)
                pygame.draw.line(win,(255,0,0),(90,WINDOW_HEIGHT-61),(90,WINDOW_HEIGHT-30),2)
                pygame.draw.line(win,(255,0,0),(59,WINDOW_HEIGHT-30),(90,WINDOW_HEIGHT-30),2)
            elif pygame.mouse.get_pressed()[0] and 90<=pygame.mouse.get_pos()[0]<120 and WINDOW_HEIGHT-60<=pygame.mouse.get_pos()[1]<WINDOW_HEIGHT-30:#WHITE
                drawColor = [255,255,255]
                resetcolorselect()
                pygame.draw.line(win,(255,0,0),(90,WINDOW_HEIGHT-60),(90,WINDOW_HEIGHT-30),2)
                pygame.draw.line(win,(255,0,0),(90,WINDOW_HEIGHT-61),(120,WINDOW_HEIGHT-61),2)
                pygame.draw.line(win,(255,0,0),(120,WINDOW_HEIGHT-61),(120,WINDOW_HEIGHT-30),2)
                pygame.draw.line(win,(255,0,0),(90,WINDOW_HEIGHT-30),(120,WINDOW_HEIGHT-30),2)
            elif event.type == pygame.MOUSEWHEEL and drawBool:
                if event.y == 1:
                    if width < 100 and  height < 100 and squDraw:
                        pygame.draw.rect(win,(255,255,255),(WINDOW_WIDTH-90-(width/2),WINDOW_HEIGHT-60-(height/2),width,height))#PREVIEWBOX
                        pygame.draw.rect(win,(255,255,255),(WINDOW_WIDTH-90-(width/2),WINDOW_HEIGHT-62-(height/2),width,2))#PREVIEW OUTLINE(1-4)
                        pygame.draw.rect(win,(255,255,255),(WINDOW_WIDTH-90-(width/2),WINDOW_HEIGHT-60+(height/2),width,2))
                        pygame.draw.rect(win,(255,255,255),(WINDOW_WIDTH-90-(width/2),WINDOW_HEIGHT-60-(height/2),2,height))
                        pygame.draw.rect(win,(255,255,255),(WINDOW_WIDTH-90+(width/2),WINDOW_HEIGHT-62-(height/2),2,height+4))
                        width += 1 
                        height += 1
                    elif cirRad < 50 and not squDraw:
                        pygame.draw.circle(win,(255,255,255),(WINDOW_WIDTH-90,WINDOW_HEIGHT-60),cirRad+2)#PREVIEWCIR
                        cirRad+=1
                elif event.y == -1:
                    if width >=1 and height >= 1 and squDraw:
                        pygame.draw.rect(win,(255,255,255),(WINDOW_WIDTH-90-(width/2),WINDOW_HEIGHT-60-(height/2),width,height))#PREVIEWBOX
                        pygame.draw.rect(win,(255,255,255),(WINDOW_WIDTH-90-(width/2),WINDOW_HEIGHT-62-(height/2),width,2))#PREVIEW OUTLINE(1-4)
                        pygame.draw.rect(win,(255,255,255),(WINDOW_WIDTH-90-(width/2),WINDOW_HEIGHT-60+(height/2),width,2))
                        pygame.draw.rect(win,(255,255,255),(WINDOW_WIDTH-90-(width/2),WINDOW_HEIGHT-60-(height/2),2,height))
                        pygame.draw.rect(win,(255,255,255),(WINDOW_WIDTH-90+(width/2),WINDOW_HEIGHT-62-(height/2),2,height+4))
                        width -= 1
                        height -= 1
                    elif cirRad >= 1 and not squDraw:
                        pygame.draw.circle(win,(255,255,255),(WINDOW_WIDTH-90,WINDOW_HEIGHT-60),cirRad+2)#PREVIEWCIR
                        cirRad-=1

            elif pygame.mouse.get_pressed()[0] and 140<=pygame.mouse.get_pos()[0]<170 and WINDOW_HEIGHT-120<=pygame.mouse.get_pos()[1]<WINDOW_HEIGHT-90:#CLEAR
                pygame.draw.rect(win,(255,255,255),(0,0,WINDOW_WIDTH,WINDOW_HEIGHT-150))
            elif pygame.mouse.get_pressed()[0] and 140<=pygame.mouse.get_pos()[0]<170 and WINDOW_HEIGHT-90<=pygame.mouse.get_pos()[1]<WINDOW_HEIGHT-60:#FILL
                drawBool = False

                pygame.draw.rect(win,(255,255,255),(WINDOW_WIDTH-141,WINDOW_HEIGHT-115,105,108))
                pygame.draw.circle(win,(255,255,255),(WINDOW_WIDTH-90,WINDOW_HEIGHT-60),cirRad+8)

                font2 = pygame.font.SysFont(None, 50)#PREVIEW
                img9 = font2.render('FILL', True, (0,0,0))
                win.blit(img9, (WINDOW_WIDTH-125, WINDOW_HEIGHT-80))

            elif pygame.mouse.get_pressed()[0] and 140<=pygame.mouse.get_pos()[0]<170 and WINDOW_HEIGHT-60<=pygame.mouse.get_pos()[1]<WINDOW_HEIGHT-32:#DRAW REGULAR
                drawBool = True
            elif pygame.mouse.get_pressed()[0] and 180<=pygame.mouse.get_pos()[0]<220 and WINDOW_HEIGHT-120<=pygame.mouse.get_pos()[1]<WINDOW_HEIGHT-80 and drawBool:#DRAW SQUARE
                squDraw = True

                pygame.draw.circle(win,(255,255,255),(WINDOW_WIDTH-90,WINDOW_HEIGHT-60),cirRad+8)#PREVIEWCIR
                pygame.draw.rect(win,(255,255,255),(WINDOW_WIDTH-140,WINDOW_HEIGHT-110,100,100))

                pygame.draw.line(win,(255,0,0),(180,WINDOW_HEIGHT-120),(220,WINDOW_HEIGHT-120), 2)#SQUARE FOR SQU
                pygame.draw.line(win,(255,0,0),(180,WINDOW_HEIGHT-80),(220,WINDOW_HEIGHT-80), 2)
                pygame.draw.line(win,(255,0,0),(180,WINDOW_HEIGHT-120),(180,WINDOW_HEIGHT-80), 2)
                pygame.draw.line(win,(255,0,0),(220,WINDOW_HEIGHT-120),(220,WINDOW_HEIGHT-79), 2)

                pygame.draw.circle(win,(0,0,0),(199,WINDOW_HEIGHT-44),20)#CIRCLE FOR CIR
                pygame.draw.circle(win,(255,255,255),(199,WINDOW_HEIGHT-44),18)
                font = pygame.font.SysFont(None, 22)#PREVIEW
                img6 = font.render('CIR', True, (0,0,0))
                win.blit(img6, (185, WINDOW_HEIGHT-50))

            elif pygame.mouse.get_pressed()[0] and ((pygame.mouse.get_pos()[0]-199)**2+(pygame.mouse.get_pos()[1]-(WINDOW_HEIGHT-44))**2 ) <= 20**2:#DRAW CIRCLE
                squDraw = False

                pygame.draw.rect(win,(255,255,255),(WINDOW_WIDTH-141,WINDOW_HEIGHT-115,105,108))
                pygame.draw.circle(win,(255,255,255),(WINDOW_WIDTH-90,WINDOW_HEIGHT-60),cirRad)#PREVIEWCIR

                pygame.draw.circle(win,(255,0,0),(199,WINDOW_HEIGHT-44),20)#CIRCLE FOR CIR
                pygame.draw.circle(win,(255,255,255),(199,WINDOW_HEIGHT-44),18)
                font = pygame.font.SysFont(None, 22)#PREVIEW
                img6 = font.render('CIR', True, (0,0,0))
                win.blit(img6, (185, WINDOW_HEIGHT-50))

                pygame.draw.line(win,(0,0,0),(180,WINDOW_HEIGHT-120),(220,WINDOW_HEIGHT-120), 2)#SQUARE FOR SQU
                pygame.draw.line(win,(0,0,0),(180,WINDOW_HEIGHT-80),(220,WINDOW_HEIGHT-80), 2)
                pygame.draw.line(win,(0,0,0),(180,WINDOW_HEIGHT-120),(180,WINDOW_HEIGHT-80), 2)
                pygame.draw.line(win,(0,0,0),(220,WINDOW_HEIGHT-120),(220,WINDOW_HEIGHT-79), 2)

            elif pygame.mouse.get_pressed()[0] and 230<=pygame.mouse.get_pos()[0]<275 and WINDOW_HEIGHT-115<=pygame.mouse.get_pos()[1]<WINDOW_HEIGHT-95:#SAVE
                rect = pygame.Rect(0,0,WINDOW_WIDTH,WINDOW_HEIGHT-150)
                sub = win.subsurface(rect)
                screenshot = pygame.Surface((WINDOW_WIDTH,WINDOW_HEIGHT-150))
                screenshot.blit(sub, (0,0))
                pygame.image.save(screenshot, "savepythonPaint.jpg")
                
                pygame.draw.line(win,(255,0,0),(230,WINDOW_HEIGHT-115),(275,WINDOW_HEIGHT-115), 2)
                pygame.draw.line(win,(255,0,0),(230,WINDOW_HEIGHT-95),(275,WINDOW_HEIGHT-95), 2)
                pygame.draw.line(win,(255,0,0),(230,WINDOW_HEIGHT-115),(230,WINDOW_HEIGHT-95), 2)
                pygame.draw.line(win,(255,0,0),(275,WINDOW_HEIGHT-115),(275,WINDOW_HEIGHT-94), 2)

                pygame.draw.line(win,(0,0,0),(230,WINDOW_HEIGHT-55),(275,WINDOW_HEIGHT-55), 2)
                pygame.draw.line(win,(0,0,0),(230,WINDOW_HEIGHT-35),(275,WINDOW_HEIGHT-35), 2)
                pygame.draw.line(win,(0,0,0),(230,WINDOW_HEIGHT-55),(230,WINDOW_HEIGHT-35), 2)
                pygame.draw.line(win,(0,0,0),(275,WINDOW_HEIGHT-55),(275,WINDOW_HEIGHT-34), 2)
            elif pygame.mouse.get_pressed()[0] and 230<=pygame.mouse.get_pos()[0]<275 and WINDOW_HEIGHT-55<=pygame.mouse.get_pos()[1]<WINDOW_HEIGHT-35:#LOAD
                pictureLoad = pygame.image.load("loadpythonPaint.jpg",)
                pictureLoad = pygame.transform.scale(pictureLoad, (WINDOW_WIDTH, WINDOW_HEIGHT-150))
                win.blit(pictureLoad,(0,0))

                pygame.draw.line(win,(255,0,0),(230,WINDOW_HEIGHT-55),(275,WINDOW_HEIGHT-55), 2)
                pygame.draw.line(win,(255,0,0),(230,WINDOW_HEIGHT-35),(275,WINDOW_HEIGHT-35), 2)
                pygame.draw.line(win,(255,0,0),(230,WINDOW_HEIGHT-55),(230,WINDOW_HEIGHT-35), 2)
                pygame.draw.line(win,(255,0,0),(275,WINDOW_HEIGHT-55),(275,WINDOW_HEIGHT-34), 2)

                pygame.draw.line(win,(0,0,0),(230,WINDOW_HEIGHT-115),(275,WINDOW_HEIGHT-115), 2)
                pygame.draw.line(win,(0,0,0),(230,WINDOW_HEIGHT-95),(275,WINDOW_HEIGHT-95), 2)
                pygame.draw.line(win,(0,0,0),(230,WINDOW_HEIGHT-115),(230,WINDOW_HEIGHT-95), 2)
                pygame.draw.line(win,(0,0,0),(275,WINDOW_HEIGHT-115),(275,WINDOW_HEIGHT-94), 2)

            if squDraw and drawBool:
                pygame.draw.rect(win,drawColor,(WINDOW_WIDTH-90-(width/2),WINDOW_HEIGHT-60-(height/2),width,height))#PREVIEWBOX
            elif not squDraw and drawBool:
                pygame.draw.circle(win,(0,0,0),(WINDOW_WIDTH-90,WINDOW_HEIGHT-60),cirRad+2)
                pygame.draw.circle(win,drawColor,(WINDOW_WIDTH-90,WINDOW_HEIGHT-60),cirRad)

            if drawColor != [0,0,0] and squDraw and drawBool:
                pygame.draw.rect(win,(0,0,0),(WINDOW_WIDTH-90-(width/2),WINDOW_HEIGHT-62-(height/2),width,2))#PREVIEW OUTLINE(1-4)
                pygame.draw.rect(win,(0,0,0),(WINDOW_WIDTH-90-(width/2),WINDOW_HEIGHT-60+(height/2),width,2))
                pygame.draw.rect(win,(0,0,0),(WINDOW_WIDTH-90-(width/2),WINDOW_HEIGHT-60-(height/2),2,height))
                pygame.draw.rect(win,(0,0,0),(WINDOW_WIDTH-90+(width/2),WINDOW_HEIGHT-62-(height/2),2,height+4))



        pygame.display.update()


main()
pygame.quit
