from pygame import * 
from random import randint
win_width=500
win_height=500
window = display.set_mode((win_width,win_height))#создаем объект окна игры - и задаем ему размер
display.set_caption("MY GAME")
WHITE=(255,255,255)#Создаем белый цветс помощью RGB
RED=(255,0,0)
BLUE=(0,0,255)

#Создаем персонажа
hero = image.load('platform.png')#d_,jq.JPG
hero = transform.scale(hero,(100,50))#РАЗМЕР ПЛАТФОРМЫ 
gero = image.load('bird.png')#wot.JPG
gero = transform.scale(gero,(50,50))#РАЗМЕР ПТИЦЫ 
rect1 = hero.get_rect()#создаем 
rect1.x=230
rect1.y=450

rect2 = gero.get_rect()#создаем 
rect2.x=50
rect2.y=50
cathed=0
passed=0
font.init()
font24=font.SysFont('Arial', 24)
font50=font.SysFont('Arial', 50)
text1=font24.render("Поймано: "+str(cathed),True,(0,150,0))
text2=font24.render("Пропущено: "+str(passed),True,(255,0,0))
textWIN=font50.render("Победа!",True,(0,150,0))
textLose=font50.render("Поражение",True,(150,0,0))
background=image.load('fon.png')#strv.JPG
background=transform.scale(background,(win_width,win_height))#фон 
clock=time.Clock()
FPS=150


text3=font24.render("FPS: "+str(FPS),True,(150,150,0))

game="in_process"
#Запускаем основной игровой цикл
while True:
	#фон
	if game=="in_process":
		window.blit(background,(0,0))
		window.blit(text1,(0,20))
		window.blit(text2,(370,20))
		window.blit(text3,(400,450))
		window.blit(hero,(rect1.x,rect1.y))
		window.blit(gero,(rect2.x,rect2.y))
		display.update()#фиксируем изменения - пишется всегда в конце
		rect2.y+=1
		if rect2.y>win_height:#рандои
			passed+=1
			FPS-=10
			text3=font24.render("FPS: "+str(FPS),True,(150,150,0))
			text2=font24.render("Пропущено:"+str(passed),True,(255,0,0))
			rect2.x=randint(0, win_height-25)
			rect2.y=0
		if rect1.colliderect(rect2):#касание
			cathed+=1
			FPS+=10
			text1=font24.render("Поймано:"+str(cathed),True,(0,150,0))
			text3=font24.render("FPS: "+str(FPS),True,(150,150,0))
			rect2.x=randint(0, win_height-25)
			rect2.y=0

		#Управление для персонажа
		keys = key.get_pressed()
		if keys[K_LEFT] and rect1.x>0:
			rect1.x-=1
		elif keys[K_RIGHT] and rect1.x+70<win_width:
			rect1.x+=1
		#далее счет победы/поражения
		if passed>=3:
			game='Lose'
		if cathed>=10:
			game='win'
	elif game=='win':
		window.blit(textWIN,(200,220))
		display.update()
	elif game=='Lose':
		window.blit(textLose,(150,220))
		display.update()
	for i in event.get():
		if i.type==QUIT:
			quit()
		if i.type==KEYDOWN and game!='in_process':
			if i.key==K_SPACE:
				passed=0
				cathed=0
				FPS=150
				text1=font24.render("Поймано:"+str(cathed),True,(0,150,0))
				text2=font24.render("Пропущено:"+str(passed),True,(255,0,0))
				text3=font24.render("FPS: "+str(FPS),True,(150,150,0))
				rect2.x=randint(0, win_height-25)
				rect2.y=0
				rect1.x=230
				rect1.y=450
				game="in_process"
	clock.tick(FPS)
#ДЗ при каждом пойманом FPS+=10 и показывать фпс