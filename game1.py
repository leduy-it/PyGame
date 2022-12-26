import pygame
from sys import exit
import time
import math

pygame.init()
screen_size = (600,1000)
screen = pygame.display.set_mode(screen_size)


# sound = pygame.mixer.Sound('music.mp3')

total_seconds = 0
start_count = False

BACK_GROUND = (48, 51, 48)
BUTTON = (43, 255, 230)
LOADING_BAR_FRAME = (19, 99, 90)
LOADING_BAR = (105, 207, 122)
CLOCK_FRAME = (255, 208, 0)
CLOCK = (250, 255, 117)
CENTER_CLOCK = (255, 186, 38)
CLOCK_WISE = (255, 139, 43)
TEXT_SIGN = (18, 96, 122)
running = True
BLACK = (0,0,0)
STOP = (219, 26, 26)
clock_font = pygame.font.SysFont('sans', 120)
font = pygame.font.SysFont('sans', 60)
plus_sign = font.render('+', True, TEXT_SIGN)
minus_sign = font.render('-', True, TEXT_SIGN)
start_text = font.render('START', True, CLOCK)
reset_text = font.render('RESET' , True, TEXT_SIGN)
total_time = 1;
pygame.display.set_caption('Lê Văn Duy - 20521233')

clock = pygame.time.Clock()
while running:
	clock.tick(60)
	screen.fill(BACK_GROUND)
	#Get mouse position with pygame library
	mouse_x, mouse_y = pygame.mouse.get_pos()
	# print("(", mouse_x, "," , mouse_y, ")")
	#Draw 4 button up down
	pygame.draw.rect(screen, BUTTON, (50,50,75,75))
	pygame.draw.rect(screen, BUTTON, (200,50,75,75))
	pygame.draw.rect(screen, BUTTON, (50,270,75,75))
	pygame.draw.rect(screen, BUTTON, (200,270,75,75))

	#Draw 2 button Start End
	pygame.draw.rect(screen, BUTTON, (350, 50,220,75))
	pygame.draw.rect(screen, BUTTON, (350, 270,220,75))
	#Draw loading bar
	pygame.draw.rect(screen, LOADING_BAR_FRAME, (50, 850, 400 , 75) )


	#Draw CLOCK
	pygame.draw.circle(screen, CLOCK_FRAME,(250,600), 160 )
	pygame.draw.circle(screen, CLOCK,(250,600), 150 )
	pygame.draw.circle(screen, CENTER_CLOCK,(250,600), 10 )

	#Draw clockwise
	pygame.draw.line(screen, CLOCK_WISE,(250,600) ,  (250,455) , 5)

	#Draw sign
	screen.blit(plus_sign , (68,55))
	screen.blit(plus_sign , (218,55))
	screen.blit(minus_sign , (78,275))
	screen.blit(minus_sign , (228,275))
	screen.blit(start_text , (360,62))
	screen.blit(reset_text , (360,282))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

		if event.type == pygame.MOUSEBUTTONDOWN:
			# pygame.mixer.pause()
			if ( 50 < mouse_x < 125 and 50 < mouse_y < 125):
				print("plus + hour")
				total_seconds += 60
			if ( 200 < mouse_x < 275 and 50 < mouse_y < 125):
				print("plus + minute")
				total_seconds += 1
			if ( 50 < mouse_x < 125 and 270 < mouse_y < 335):
				print("plus - hour")
				total_seconds -= 60
			if ( 200 < mouse_x < 275 and 270 < mouse_y < 335):
				print("plus - minute")
				total_seconds -= 1

			if ( 350 < mouse_x < 570 and 50 < mouse_y < 125):
				print("START")
				total_time = total_seconds
				if total_time ==0:
					total_time =1
				start_count = True
			if ( 350 < mouse_x < 570 and 270 < mouse_y < 335):
				print("RESET")
				total_seconds = 0
				print("after reset", total_seconds)

	seconds = int(total_seconds%60)

	minutes = int(total_seconds/60)
	clock_count_down = str(minutes) + " : " + str(seconds)
	if start_count:
		total_seconds -= 1
		print(total_seconds)
		#Render Clock bar
		pygame.draw.rect(screen, LOADING_BAR, (50, 850, 400 * (total_seconds/total_time) , 75 ))
		if(total_seconds ==0):
			#Play sound Main menu
			# pygame.mixer.Sound.play(sound)
			pass
		time.sleep(0.01)
	if(total_seconds <=0):
		total_seconds=0
	if total_seconds == 0:
		start_count = False


	x_second = 250+ 150*(math.sin(seconds*6*(math.pi/180)))
	y_second = 600 -150*(math.cos(seconds*6*(math.pi/180)))
	x_minute = 250+ 100*(math.sin(minutes*6*(math.pi/180)))
	y_minute = 600 -100*(math.cos(minutes*6*(math.pi/180)))
	#Render Clock count down
	clock_count_down_text = clock_font.render(clock_count_down, True, CLOCK)
	screen.blit( clock_count_down_text, (55, 150))

	#Render the second hand and minute hand
	pygame.draw.line(screen, CLOCK_WISE, (250,600) , (x_second,y_second) , 5)
	pygame.draw.line(screen, STOP, (250,600) , (x_minute,y_minute) , 5)

	


	pygame.display.flip()
print("da ngat vong lap")

pygame.display.quit()
pygame.quit()
exit()