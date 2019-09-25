import pygame

pygame.init()

win=pygame.display.set_mode((500,500))
pygame.display.set_caption("Vurhd game")

main=pygame.image.load('main.jpeg')
main=pygame.transform.scale(main, (500,500))
name=pygame.image.load('name.png')
name=pygame.transform.scale(name, (280,320))
logo=pygame.image.load('logo.png')
logo=pygame.transform.scale(logo, (60,60))
win.blit(main,(0,0))
win.blit(name,(130,0))
win.blit(logo,(425,420))

pygame.display.update()
i=0
while i<200:
    pygame.time.delay(10)
    i+=1
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            run=False

# explaination 1
exp1=pygame.image.load('exp1.jpeg')
exp1=pygame.transform.scale(exp1, (500,500))
win.blit(exp1,(0,0))
win.blit(logo,(425,420))
pygame.display.update()
i=0
while i<340:
    pygame.time.delay(10)
    i+=1
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            run=False

# explaination 2
exp2=pygame.image.load('exp2.jpeg')
exp2=pygame.transform.scale(exp2, (500,500))
win.blit(exp2,(0,0))
win.blit(logo,(425,420))
pygame.display.update()
i=0
while i<500:
    pygame.time.delay(10)
    i+=1
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            run=False
# explaination 3
exp3=pygame.image.load('exp3.jpeg')
exp3=pygame.transform.scale(exp3, (500,500))
win.blit(exp3,(0,0))

point3=pygame.image.load('point3.png')
point3=pygame.transform.scale(point3, (125,125))

point1=pygame.image.load('point1.png')
point1=pygame.transform.scale(point1, (126,127))

point2=pygame.image.load('point2.png')
point2=pygame.transform.scale(point2, (125,126))

win.blit(point1,(30,215))
win.blit(point2,(185,215))
win.blit(point3,(365,215))
win.blit(logo,(425,420))


pygame.display.update()
i=0
while i<130:
    pygame.time.delay(10)
    i+=1
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            run=False


# explaination 4
start=pygame.image.load('start.jpeg')
start=pygame.transform.scale(start, (500,500))
win.blit(start,(0,0))

win.blit(logo,(425,420))
pygame.display.update()
i=0
while i<50:
    pygame.time.delay(10)
    i+=1
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            run=False
# game starts
img=pygame.image.load('mario.png')
img=pygame.transform.scale(img, (64,64))

imgr=[pygame.image.load('mright0.png'),pygame.image.load('mright0.png'),pygame.image.load('mright1.png'),pygame.image.load('mright1.png'),pygame.image.load('mright2.png'),pygame.image.load('mright2.png'),pygame.image.load('mright3.png'),pygame.image.load('mright3.png')]
imgr=[pygame.transform.scale(imgr[0], (64,64)),pygame.transform.scale(imgr[1], (64,64)),pygame.transform.scale(imgr[2], (64,64)),pygame.transform.scale(imgr[3], (64,64)),pygame.transform.scale(imgr[4], (64,64)),pygame.transform.scale(imgr[5], (64,64))]

imgl=[pygame.transform.flip(imgr[0], True, False),pygame.transform.flip(imgr[1], True, False),pygame.transform.flip(imgr[2], True, False),pygame.transform.flip(imgr[3], True, False),pygame.transform.flip(imgr[4], True, False),pygame.transform.flip(imgr[5], True, False)]
imgl=[pygame.transform.scale(imgl[0], (64,64)),pygame.transform.scale(imgl[1], (64,64)),pygame.transform.scale(imgl[2], (64,64)),pygame.transform.scale(imgl[3], (64,64)),pygame.transform.scale(imgl[4], (64,64)),pygame.transform.scale(imgl[5], (64,64))]

bg=pygame.image.load('firstimage.jpeg')
bg=pygame.transform.scale(bg, (500,500))

imgjumping=pygame.image.load('mariojumping.png')
imgjumping=pygame.transform.scale(imgjumping, (55,70))

enemy1=pygame.image.load('enemy1.png')
enemy1=pygame.transform.scale(enemy1, (55,70))

enemy2=pygame.image.load('enemy2.png')
enemy2=pygame.transform.scale(enemy2, (55,70))

enemy3=pygame.image.load('enemy3.png')
enemy3=pygame.transform.scale(enemy3, (55,70))

point3=pygame.image.load('point3.png')
point3=pygame.transform.scale(point3, (55,70))

point1=pygame.image.load('point1.png')
point1=pygame.transform.scale(point1, (55,70))

point2=pygame.image.load('point2.png')
point2=pygame.transform.scale(point2, (55,70))


score=0
x=200
y=430

vel=5
cnt=6
ht=10
neg=1

x1=10
y1=43
v1=10
face1=1

x2=70
y2=175
v2=7
face2=-1

x3=340
y3=320
v3=5
face3=-1

isLeft=True
isRight=False
run=True
jumping=False

img1=point1
font=pygame.font.SysFont('comicsans',30,True)
font1=pygame.font.SysFont('comicsans',100)
font2=pygame.font.SysFont('comicsans',100,True,True)

while run:
    pygame.time.delay(50)

    if(face1==1):
        if(x1>=500):
            face1=-1
            img1=enemy1                  
            x1+=v1*face1
            
        else:
            x1+=v1*face1
            img1=point1  
    else:
        if(x1<=0):
            face1=1
            x1+=v1*face1
            img1=point1  
        else:
            x1+=v1*face1
            img1=enemy1  
            

    if(face2==1):
        if(x2>=500):
            face2=-1
            img2=point2
            x2+=v2*face2
        else:
            x2+=v2*face2
            img2=enemy2
    else:                           
        if(x2<=0):
            face2=1
            img2=enemy2
            x2+=v2*face2
        else:
            x2+=v2*face2
            img2=point2
            

    if(face3==1):
        if(x3>=500):
            face3=-1
            img3=point3
            x3+=v3*face3
        else:
            x3+=v3*face3
            img3=enemy3
    else:                           
        if(x3<=0):
            face3=1
            img3=enemy3
            x3+=v3*face3
        else:                   # -1 POINT
            x3+=v3*face3
            img3=point3
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False


    keys=pygame.key.get_pressed()

    if not jumping:
        if keys[pygame.K_LEFT] and x>0:
            x-=vel
            img=imgl[x%6]
        if keys[pygame.K_RIGHT] and x<500:
            x+=vel
            img=imgr[x%6]                               
        if keys[pygame.K_UP] and y>5:
            y-=vel
        if keys[pygame.K_DOWN] and y<500-70:
            y+=vel
        if keys[pygame.K_SPACE]:
            jumping=True

        win.blit(bg,(0,0))
        win.blit(img,(x,y))
        text=font.render('SCORE: '+str(score),1,(0,0,0))
        win.blit(text,(350,10))
        pygame.display.flip()
        pygame.display.update()
        
    else:
        if(ht>0 and neg==1):
            y-=ht*ht*0.5*neg
            ht-=1
        elif(ht<=0 and neg==1):
            neg=-1;
            ht=10
        elif(ht>0 and neg==-1):
            y-=ht*ht*0.5*neg
            ht-=1
        else:
            neg=1
            ht=10
            jumping=False
        
        
        win.blit(bg,(0,0))
        win.blit(img1,(x1,y1))
        win.blit(img2,(x2,y2))
        win.blit(img3,(x3,y3))
        text=font.render('SCORE: '+str(score),1,(0,0,0))
        win.blit(text,(350,10))
        win.blit(imgjumping,(x,y))

        if( abs(x-x1)<=35 and abs(y-y1)<=35):
            if face1==1:
                score+=1
                text=font1.render('+1',1,(255,0,0))
                win.blit(text,(250-(text.get_width()/2),200))
                pygame.display.update()
                i=0
                while i<5:
                    pygame.time.delay(10)
                    i+=1
                    for event in pygame.event.get():
                        if event.type==pygame.QUIT:
                            i=6
                            pygame.quit()
            else:
                text=font2.render('GAME OVER',1,(255,20,3))
                win.blit(text,(250-(text.get_width()/2),250))
                text=font.render('YOUR SCORE: '+str(score),1,(55,20,3))
                win.blit(text,(250-(text.get_width()/2),320))

                pygame.display.update()
                i=0
                while i<300:
                    pygame.time.delay(10)
                    i+=1
                pygame.quit()
                run=False


        elif(abs(x-x2)<=35 and abs(y-y2)<=35):
            if face2==-1:
                score+=1
                text=font1.render('+1',1,(255,0,0))
                win.blit(text,(250-(text.get_width()/2),200))
                pygame.display.update()
                i=0
                while i<5:
                    pygame.time.delay(10)
                    i+=1
                    for event in pygame.event.get():
                        if event.type==pygame.QUIT:
                            i=6
                            pygame.quit()
            else:
                text=font2.render('GAME OVER',1,(255,20,3))
                win.blit(text,(250-(text.get_width()/2),250))
                text=font.render('YOUR SCORE: '+str(score),1,(55,20,3))
                win.blit(text,(250-(text.get_width()/2),320))

                pygame.display.update()
                i=0
                while i<300:
                    pygame.time.delay(10)
                    i+=1
                    
                pygame.quit()
                run=False


        elif(abs(x-x3)<=35 and abs(y-y3)<=35):
            if face3==-1:
                score+=1
                text=font1.render('+1',1,(255,0,0))
                win.blit(text,(250-(text.get_width()/2),200))
                pygame.display.update()
                i=0
                while i<5:
                    pygame.time.delay(10)
                    i+=1
                    for event in pygame.event.get():
                        if event.type==pygame.QUIT:
                            i=6
                            pygame.quit()
            else:
                text=font2.render('GAME OVER',1,(255,20,3))
                win.blit(text,(250-(text.get_width()/2),250))
                text=font.render('YOUR SCORE: '+str(score),1,(55,20,3))
                win.blit(text,(250-(text.get_width()/2),320))

                pygame.display.update()
                i=0
                while i<300:
                    pygame.time.delay(10)
                    i+=1
                    
                pygame.quit()
                run=False

        
        pygame.display.flip()
        pygame.display.update()

pygame.quit()

