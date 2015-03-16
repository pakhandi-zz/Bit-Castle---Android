import pygame
import sys
import random
import urllib, urllib2
try:
	import android
except ImportError:
	android = None

pygame.init()
pygame.display.init()

background_color = (255,255,255) #White
man_color = (0,0,0)
wall_color = (240,150,0)
red = (255,0,0)
green = (0, 155, 0)
gate_color = (255,0,0)
grey = (128,128,128)
(width, height) = (200, 700)

wall_x = []
wall_y = []
wall_length = []
wall_width = []
WALLS = 22

death_x = []
death_y = []

recharge_x = []
recharge_y = []
initial_charge_array = [  700  ,  700  ,  700  ,  700  ,  400  ,  400  ,  400  ,  400  ,  300  ,  300  ,  100 ]
clock_tick_array =     [  80   ,  80   ,  80   ,  90   ,  90   ,  100   ,  110   ,  110   ,  120   ,  120   ,  140  ]
new_recharge_array =   [  140  ,  130  ,  100  ,  100  ,  120  ,  120  ,  130  ,  130  ,  150  ,  150  ,  100 ]
max_deaths_array =     [  2    ,  3    ,  4    ,  4    ,  6    ,  6    ,  6    ,  6    ,  6    ,  6    ,  10  ]
max_recharges_array =  [  6    ,  6    ,  6    ,  6    ,  6    ,  6    ,  5    ,  5    ,  4    ,  4    ,  4   ]
dead_time_array =      [  1800 ,  1500 ,  1500 ,  1200 ,  1200 ,  1100 ,  1100 ,  1000 ,  1000 ,  800  ,  800 ]

global DEATHS
global RECHARGES

global gate_x
global gate_y
global reached_gate

global doexit
global isrunning

global curr_score
curr_score = 0

global DELAY
DELAY = 150

global EXTRA_CHARGE
EXTRA_CHARGE = 0

global INITIAL_CHARGE, NEW_RECHARGE, CLOCK_TICK, PLAYER_NAME, HLEVEL
global PLAYER,  entry2, input2 , HIGHSCORE


def name():
	pygame.init()
	screen = pygame.display.set_mode((width+200, height))
	global PLAYER_NAME
	PLAYER_NAME = ""
	font = pygame.font.Font("arial.ttf", 20)
	font1 = pygame.font.Font("arial.ttf", 20)
	if android:
			android.show_keyboard()
			android.map_key(android.KEYCODE_BACK, pygame.QUIT)
			android.map_key(android.KEYCODE_A, pygame.K_a)
			android.map_key(android.KEYCODE_B, pygame.K_b)
			android.map_key(android.KEYCODE_C, pygame.K_c)
			android.map_key(android.KEYCODE_D, pygame.K_d)
			android.map_key(android.KEYCODE_E, pygame.K_e)
			android.map_key(android.KEYCODE_F, pygame.K_f)
			android.map_key(android.KEYCODE_G, pygame.K_g)
			android.map_key(android.KEYCODE_H, pygame.K_h)
			android.map_key(android.KEYCODE_I, pygame.K_i)
			android.map_key(android.KEYCODE_J, pygame.K_j)
			android.map_key(android.KEYCODE_K, pygame.K_k)
			android.map_key(android.KEYCODE_L, pygame.K_l)
			android.map_key(android.KEYCODE_M, pygame.K_m)
			android.map_key(android.KEYCODE_N, pygame.K_n)
			android.map_key(android.KEYCODE_O, pygame.K_o)
			android.map_key(android.KEYCODE_P, pygame.K_p)
			android.map_key(android.KEYCODE_Q, pygame.K_q)
			android.map_key(android.KEYCODE_R, pygame.K_r)
			android.map_key(android.KEYCODE_S, pygame.K_s)
			android.map_key(android.KEYCODE_T, pygame.K_t)
			android.map_key(android.KEYCODE_U, pygame.K_u)
			android.map_key(android.KEYCODE_V, pygame.K_v)
			android.map_key(android.KEYCODE_W, pygame.K_w)
			android.map_key(android.KEYCODE_X, pygame.K_x)
			android.map_key(android.KEYCODE_Y, pygame.K_y)
			android.map_key(android.KEYCODE_Z, pygame.K_z)
			android.map_key(android.KEYCODE_DEL, pygame.K_BACKSPACE)
			android.map_key(android.KEYCODE_ENTER, pygame.K_RETURN)
			android.map_key(android.KEYCODE_BACK, pygame.K_ESCAPE)

	while True:
		for evt in pygame.event.get():
			if evt.type == pygame.MOUSEBUTTONUP:
				if android:
						android.show_keyboard()
			if evt.type == pygame.KEYDOWN:
				if len(PLAYER_NAME)<=10:
					if evt.key == pygame.K_a:
						PLAYER_NAME += "a";
					if evt.key == pygame.K_b:
						PLAYER_NAME += "b";
					if evt.key == pygame.K_c:
						PLAYER_NAME += "c";
					if evt.key == pygame.K_d:
						PLAYER_NAME += "d";
					if evt.key == pygame.K_e:
						PLAYER_NAME += "e";
					if evt.key == pygame.K_f:
						PLAYER_NAME += "f";
					if evt.key == pygame.K_g:
						PLAYER_NAME += "g";
					if evt.key == pygame.K_h:
						PLAYER_NAME += "h";
					if evt.key == pygame.K_i:
						PLAYER_NAME += "i";
					if evt.key == pygame.K_j:
						PLAYER_NAME += "j";
					if evt.key == pygame.K_k:
						PLAYER_NAME += "k";
					if evt.key == pygame.K_l:
						PLAYER_NAME += "l";
					if evt.key == pygame.K_m:
						PLAYER_NAME += "m";
					if evt.key == pygame.K_n:
						PLAYER_NAME += "n";
					if evt.key == pygame.K_o:
						PLAYER_NAME += "o";
					if evt.key == pygame.K_p:
						PLAYER_NAME += "p";
					if evt.key == pygame.K_q:
						PLAYER_NAME += "q";
					if evt.key == pygame.K_r:
						PLAYER_NAME += "r";
					if evt.key == pygame.K_s:
						PLAYER_NAME += "s";
					if evt.key == pygame.K_t:
						PLAYER_NAME += "t";
					if evt.key == pygame.K_u:
						PLAYER_NAME += "u";
					if evt.key == pygame.K_v:
						PLAYER_NAME += "v";
					if evt.key == pygame.K_w:
						PLAYER_NAME += "w";
					if evt.key == pygame.K_x:
						PLAYER_NAME += "x";
					if evt.key == pygame.K_y:
						PLAYER_NAME += "y";
					if evt.key == pygame.K_z:
						PLAYER_NAME += "z";
				if evt.key == pygame.K_BACKSPACE:
					PLAYER_NAME = PLAYER_NAME[:-1]
				if evt.key == pygame.K_RETURN and len(PLAYER_NAME)>1:
					if android:
						android.hide_keyboard()
					return
				if evt.key == pygame.K_ESCAPE:
					if android:
						android.show_keyboard()
				
			elif evt.type == pygame.QUIT:
				return
		screen.fill((0, 0, 0))
		block = font.render(PLAYER_NAME, True, (255, 255, 255))
		screen.blit(font.render("Enter Player Name : ", True, (255, 255, 255)), (120,150))
		rect = block.get_rect()
		rect.center = screen.get_rect().center
		screen.blit(block, rect)
		pygame.display.flip()

def loading_screen():
	screen = pygame.display.set_mode((width+200, height))
	pygame.display.set_caption("Bit Castle")
	screen.fill((0,0,0))
	font = pygame.font.Font("arial.ttf", 18)
	block = font.render("LOADING..", True, (255, 255, 255))
	rect = block.get_rect()
	rect.center = screen.get_rect().center
	screen.blit(block, rect)
	
	pygame.draw.circle(screen, green, (200, 350), 80, 5)
	pygame.display.flip()

def init_game():
	global DELAY, EXTRA_CHARGE, curr_score, HIGHSCORE
	DELAY =150
	HIGHSCORE = 0
	EXTRA_CHARGE = 0
	curr_score = 0
	return

def upload():
	#Function to uplaod score

def highscores():
	#Function to display LeaderBoard

def show_level(nlevel):
	screen = pygame.display.set_mode((width+200, height))
	pygame.display.set_caption("Bit Castle")
	screen.fill((0,0,0))
	font = pygame.font.Font("arial.ttf", 30)
	block = font.render(str(nlevel+1), True, (255, 255, 255))
	rect = block.get_rect()
	rect.center = screen.get_rect().center
	screen.blit(block, rect)
	pygame.draw.circle(screen, green, (200, 350), 80, 5)
	pygame.display.flip()

	isrunning = True
	curr_time = 0

	if android:
		android.map_key(android.KEYCODE_BACK, pygame.K_ESCAPE)

	while isrunning:
		curr_time+=1
		if (curr_time/5)%2==0:
			block = font.render(str(nlevel+1), True, (255, 255, 255))
			rect = block.get_rect()
			rect.center = screen.get_rect().center
			screen.blit(block, rect)
			pygame.draw.circle(screen, green, (200, 350), 80, 5)
			pygame.display.flip()
		else:
			block = font.render(str(nlevel+1), True, (255, 255, 255))
			rect = block.get_rect()
			rect.center = screen.get_rect().center
			screen.blit(block, rect)
			pygame.draw.circle(screen, red, (200, 350), 80, 5)
			pygame.display.flip()

		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN:
				coord = pygame.mouse.get_pos()
				print coord[0], " ", coord[1]
				if coord[0]>=120 and coord[0]<=280 and coord[1]>=270 and coord[1]<=430:
					return
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					return

def gameover_Screen():
	
	
	global curr_score
	
	global PLAYER_NAME

	length = len(PLAYER_NAME)
	length = length * 13
	spaces = 400 - length
	start_x = spaces/2

	screen = pygame.display.set_mode((width+200, height))
	font1 = pygame.font.Font("arial.ttf", 15)
	font2 = pygame.font.Font("arial.ttf", 30)
	font3 = pygame.font.Font("arial.ttf", 20)
	
	pygame.display.set_caption("Bit Castle")
	screen.fill(background_color)

	pygame.display.flip()
	isrunning = True



	while isrunning:
		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN:
				coord = pygame.mouse.get_pos()
				print coord[0], coord[1]
				if coord[0]>=320 and coord[0]<=370 and coord[1]>=570 and coord[1]<=630:
					return

			if event.type == pygame.QUIT:
				exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_p or event.key == pygame.K_z:
					return
				if event.key == pygame.K_q:
					exit()
		screen.fill((0,0,0))
		screen.blit(font2.render("Bit Castle", True, green), (148,100))
		screen.blit(font2.render("Congrats", True, (37,14,182)), (150, 150))
		screen.blit(font2.render(PLAYER_NAME, True, green), (start_x, 200))
		pygame.draw.rect( screen, red, [320, 570, 50, 60] )
		coinpic = pygame.image.load('coin.png')
		screen.blit(coinpic, (190, 265))
		screen.blit(font1.render(str(curr_score), True, (255,255,255)), (210,260))
		
		
		screen.blit(font1.render("Touch to Start Again", True, (0,0,0)), (140, 380))
		pygame.display.update()

def change_name():
	file = open("x.txt", 'w')
	name()
	global PLAYER_NAME
	file.write(PLAYER_NAME)
	file.close()
	return

def start_Screen():
	init_game()
	if android:
		android.init()
	
	isrunning = True
	while isrunning:
		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN:
				coord = pygame.mouse.get_pos()
				print coord[0], coord[1]
				if coord[0]>=130 and coord[0]<=270 and coord[1]>=240 and coord[1]<=280:
					screen.fill(background_color)
					return

				if coord[0]>=130 and coord[0]<=270 and coord[1]>=290 and coord[1]<=330:
					loading_screen()
					highscores()

				if coord[0]>=130 and coord[0]<=270 and coord[1]>=340 and coord[1]<=380:
					change_name()				
				
			if event.type == pygame.QUIT:
				sys.exit(0)
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_p:
					screen.fill(background_color)
					return
				if event.key == pygame.K_r:
					rules()
		screen = pygame.display.set_mode((width+200, height))
		font1 = pygame.font.Font("arial.ttf", 20)
		font2 = pygame.font.Font("arial.ttf", 30)
		pygame.display.set_caption("Bit Castle")
		screen.fill((0,0,0))
		screen.blit(font2.render( "Bit Castle", True, green), (135,100) )

		screen.blit(font1.render( "Start", True, green), (178, 250))
		pygame.draw.rect( screen, (0,255,255), [130, 240, 140, 40], 3 )

		screen.blit(font1.render( "LeaderBoard", True, green), (142, 300))
		pygame.draw.rect( screen, (0,255,255), [130, 290, 140, 40], 3 )

		screen.blit(font1.render( "Change Name", True, green), (138, 350))
		pygame.draw.rect( screen, (0,255,255), [130, 340, 140, 40], 3 )

		myrect = screen.get_rect()		

		pygame.display.flip()

def pause_Screen(curr_score):
	screen = pygame.display.set_mode((width, height))
	font1 = pygame.font.Font("arial.ttf", 20)
	font2 = pygame.font.Font("arial.ttf", 20)
	pygame.display.set_caption("Bit Castle")
	screen.fill(background_color)
	screen.blit(font2.render("Paused", True, green), (48,100))
	screen.blit(font1.render("Press Z to Resume",True, (0,0,0)), (30,200))
	coinpic = pygame.image.load('coin.png')
	screen.blit(coinpic, (60, 245))
	screen.blit(font1.render(str(curr_score), True, (0,0,0)), (80,240))
	
	pygame.display.flip()
	isrunning = True
	while isrunning:
		if android:
			android.show_keyboard()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit(0)
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_p or event.key == pygame.K_z:
					return
				if event.key == pygame.K_q:
					sys.exit(0)

def start_level(nlevel):

	global HLEVEL
	HLEVEL = nlevel

	show_level(nlevel)

	if nlevel >= 10:
		nlevel = 10

	global HIGHSCORE
	global INITIAL_CHARGE
	global CLOCK_TICK, NEW_RECHARGE
	global EXTRA_CHARGE
	global key_x
	global key_y
	global got_key
	global DELAY
	global WALLS
	global gate_x
	global DEATHS
	global isrunning
	global doexit
	global gate_y
	global reached_gate
	global curr_score
	global RECHARGES

	del wall_x[:]
	del wall_y[:]
	del wall_length[:]
	del wall_width[:]
	del death_x[:]
	del death_y[:]
	del recharge_x[:]
	del recharge_y[:]

	screen = pygame.display.set_mode((width, height))
	pygame.display.set_caption("Bit Castle")
	screen.fill(background_color)
	pygame.display.flip()

	

	INITIAL_CHARGE = initial_charge_array[nlevel]
	INITIAL_CHARGE += EXTRA_CHARGE
	battery = INITIAL_CHARGE

	isdead = False

	CLOCK_TICK = clock_tick_array[nlevel]
	NEW_RECHARGE = new_recharge_array[nlevel]

	MAX_DEATHS = max_deaths_array[nlevel]
	MAX_RECHARGES = max_recharges_array[nlevel]
	
	

	font1 = pygame.font.Font("arial.ttf", 20)
	font4 = pygame.font.Font("arial.ttf", 16)


	
	isrunning = True

	
	doexit = False

	
	gate_x = 100
	
	gate_y = 0
	
	reached_gate = False

	
	got_key = False
	key_y = random.randint(260,280)
	key_x = random.randint(10,180)

	

	
	DEATHS = 0
	
	RECHARGES = 0

	curr_x = 90
	curr_y = 570
	last_x = 90
	last_y = 590
	dir_x_change = 0
	dir_y_change = 0

	touched_wall_lower = False
	touched_wall_upper = False
	touched_wall_right = False
	touched_wall_left = False

	clock = pygame.time.Clock()

	gatepic = pygame.image.load('door.png')
	keypic = pygame.image.load('key.png')

	for i in range(600):
		if i%100==0 and DEATHS<MAX_DEATHS:
			curr_death_x = random.randint(10,40)
			curr_death_y = i+curr_death_x
			curr_death_x = random.randint(0,190)
			death_x.append(curr_death_x)
			death_y.append(curr_death_y)
			DEATHS = DEATHS + 1
			if nlevel > 9 and DEATHS < MAX_DEATHS:
				curr_death_x = random.randint(10,40)
				curr_death_y = i+curr_death_x
				curr_death_x = random.randint(0,190)
				death_x.append(curr_death_x)
				death_y.append(curr_death_y)
				DEATHS = DEATHS + 1

		if i%100==0 and RECHARGES<MAX_RECHARGES:
			curr_recharge_x = random.randint(10,40)
			curr_recharge_y = i+curr_recharge_x
			curr_recharge_x = random.randint(0,190)
			recharge_x.append(curr_recharge_x)
			recharge_y.append(curr_recharge_y)
			RECHARGES = RECHARGES + 1
			#print c
		
		if i==0:
			continue
		
		if i%50!=0:
			i = i-1
			continue
		temp = 0
		for j in range(2):
			curr_wall_width = 10
			curr_wall_length = random.randint(40,60)
			curr_wall_y = i
			
			if j==1:
				curr_wall_x = random.randint(temp+30,200-curr_wall_length)
			else:
				curr_wall_x = random.randint(0,100-curr_wall_length)

			wall_x.append(curr_wall_x)
			wall_y.append(curr_wall_y)
			wall_length.append(curr_wall_length)
			wall_width.append(curr_wall_width)
			temp = curr_wall_x + curr_wall_length

			
	curr_time = 0
	pygame.display.update()
	torch = False

	
	target_time = 0

	if android:
		android.hide_keyboard()
		android.accelerometer_enable(True)
		android.map_key(android.KEYCODE_BACK, pygame.K_ESCAPE)

	
	while isrunning:
		curr_time+=1
		reached_gate = False
		if android:
			if android.check_pause():
				android.wait_for_resume()
		if android:
			tup1 = android.accelerometer_reading()
			if(tup1[0]>1.0):
				dir_x_change = -1
			elif tup1[0]<-1.0:
				dir_x_change = +1

			if tup1[1]>0:
				dir_y_change = +1
			else:
				dir_y_change = -1

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit(0)
			if event.type == pygame.MOUSEBUTTONDOWN:
				if curr_time > target_time:
					torch = True
				if battery <=0 :
					torch = False
			if event.type == pygame.MOUSEBUTTONUP and torch==True:
				torch = False
				target_time = curr_time + DELAY
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					return 0
				if event.key == pygame.K_z:
					pause_Screen(curr_score)
				if event.key == pygame.K_LEFT:
					dir_x_change = -1
					dir_y_change = 0
				elif event.key == pygame.K_RIGHT:
					dir_x_change = 1
					dir_y_change = 0
				elif event.key == pygame.K_UP:
					dir_y_change = -1
					dir_x_change = 0
				elif event.key == pygame.K_DOWN:
					dir_y_change = 1
					dir_x_change = 0


		if curr_x >= key_x and curr_x <= key_x+10 and curr_y >= key_y and curr_y<=key_y+10:
			got_key = True
		if curr_x+10 >= key_x and curr_x+10 <= key_x+10 and curr_y >= key_y and curr_y<=key_y+10:
			got_key = True
		if curr_x+10 >= key_x and curr_x+10 <= key_x+10 and curr_y+10 >= key_y and curr_y+10 <= key_y+10:
			got_key = True
		if curr_x >= key_x and curr_x <= key_x+10 and curr_y+10 >= key_y and curr_y+10 <= key_y+10:
			got_key = True

		if curr_x >= gate_x and curr_x <= gate_x+10 and curr_y >= gate_y and curr_y<=gate_y+10:
			reached_gate = True
		if curr_x+10 >= gate_x and curr_x+10 <= gate_x+10 and curr_y >= gate_y and curr_y<=gate_y+10:
			reached_gate = True
		if curr_x+10 >= gate_x and curr_x+10 <= gate_x+10 and curr_y+10 >= gate_y and curr_y+10 <= gate_y+10:
			reached_gate = True
		if curr_x >= gate_x and curr_x <= gate_x+10 and curr_y+10 >= gate_y and curr_y+10 <= gate_y+10:
			reached_gate = True



		if reached_gate and got_key:
			curr_score+=battery
			return 1

		for i in range(DEATHS):
			if curr_x >= death_x[i] and curr_x <= death_x[i]+10 and curr_y >= death_y[i] and curr_y<=death_y[i]+10:
				isdead = True
			if curr_x+10 >= death_x[i] and curr_x+10 <= death_x[i]+10 and curr_y >= death_y[i] and curr_y<=death_y[i]+10:
				isdead = True
			if curr_x+10 >= death_x[i] and curr_x+10 <= death_x[i]+10 and curr_y+10 >= death_y[i] and curr_y+10 <= death_y[i]+10:
				isdead = True
			if curr_x >= death_x[i] and curr_x <= death_x[i]+10 and curr_y+10 >= death_y[i] and curr_y+10 <= death_y[i]+10:
				isdead = True

		for i in range(RECHARGES):
			if curr_x >= recharge_x[i] and curr_x <= recharge_x[i]+10 and curr_y >= recharge_y[i] and curr_y<=recharge_y[i]+10:
				battery += NEW_RECHARGE
				recharge_x.remove(recharge_x[i])
				recharge_y.remove(recharge_y[i])
				RECHARGES-=1
				break;
			if curr_x+10 >= recharge_x[i] and curr_x+10 <= recharge_x[i]+10 and curr_y >= recharge_y[i] and curr_y<=recharge_y[i]+10:
				battery += NEW_RECHARGE
				recharge_x.remove(recharge_x[i])
				recharge_y.remove(recharge_y[i])
				RECHARGES-=1
				break;
			if curr_x+10 >= recharge_x[i] and curr_x+10 <= recharge_x[i]+10 and curr_y+10 >= recharge_y[i] and curr_y+10 <= recharge_y[i]+10:
				battery += NEW_RECHARGE
				recharge_x.remove(recharge_x[i])
				recharge_y.remove(recharge_y[i])
				RECHARGES-=1
				break;
			if curr_x >= recharge_x[i] and curr_x <= recharge_x[i]+10 and curr_y+10 >= recharge_y[i] and curr_y+10 <= recharge_y[i]+10:
				battery += NEW_RECHARGE
				recharge_x.remove(recharge_x[i])
				recharge_y.remove(recharge_y[i])
				RECHARGES-=1
				break;

		for i in range(WALLS):
			if ( (curr_x < wall_x[i]+wall_length[i] and curr_x >= wall_x[i]) or (curr_x+10 < wall_x[i]+wall_length[i] and curr_x+10 > wall_x[i]) ) and curr_y <= wall_y[i]+10 and curr_y>=wall_y[i]:
				touched_wall_lower = True

			if ( (curr_x < wall_x[i]+wall_length[i] and curr_x >= wall_x[i]) or (curr_x+10 < wall_x[i]+wall_length[i] and curr_x+10 > wall_x[i]) ) and curr_y+10 <= wall_y[i]+10 and curr_y+10 >=wall_y[i]:
				touched_wall_upper = True

			if curr_x >= wall_x[i] and curr_x <= wall_x[i]+wall_length[i] and ( (curr_y >= wall_y[i] and curr_y < wall_y[i]+wall_width[i]) or (curr_y+10 > wall_y[i] and curr_y+10 <= wall_y[i]+wall_width[i])):
				touched_wall_right = True

			if curr_x+10 >= wall_x[i] and curr_x+10 <= wall_x[i]+wall_length[i] and ( (curr_y >= wall_y[i] and curr_y < wall_y[i]+wall_width[i]) or (curr_y+10 > wall_y[i] and curr_y+10 <= wall_y[i]+wall_width[i])):
				touched_wall_left = True

		if curr_x <= 0:
			touched_wall_right = True
		if curr_x+10 >= width:
			touched_wall_left = True
		if curr_y <= 0:
			touched_wall_lower = True
		if curr_y+10 > 580:
			touched_wall_upper = True

		if curr_x >= width or curr_x < 0 or curr_y < 0 or curr_y >= height:
			doexit = True

		if curr_time > dead_time_array[nlevel]:
			isdead = True

		if isdead:
			HIGHSCORE = curr_score
			loading_screen()
			upload()
			gameover_Screen()
			return 0
			

		if touched_wall_upper and dir_y_change>0:
			curr_y = curr_y
		elif touched_wall_upper and dir_y_change<=0:
			curr_y += dir_y_change
		elif touched_wall_lower and dir_y_change<=0:
			curr_y = curr_y
		elif touched_wall_lower and dir_y_change>0:
			curr_y += dir_y_change
		if not touched_wall_upper and not touched_wall_lower:
			curr_y += dir_y_change

		if touched_wall_left and dir_x_change>0:
			curr_x = curr_x
		elif touched_wall_left and dir_x_change<=0:
			curr_x += dir_x_change
		elif touched_wall_right and dir_x_change<=0:
			curr_x = curr_x
		elif touched_wall_right and dir_x_change>0:
			curr_x += dir_x_change
		if not touched_wall_right and not touched_wall_left:
			curr_x += dir_x_change

		last_x = curr_x
		last_y = curr_y

		touched_wall_lower = False
		touched_wall_upper = False
		touched_wall_left = False
		touched_wall_right = False
 

		if not torch or battery<=0:
			screen.fill((0,0,0))
			pygame.draw.rect( screen, (255,255,255), [curr_x,curr_y,10,10] )
			

			
		else:
			battery=battery-1
			screen.fill(background_color)

			for i in range(WALLS):
				pygame.draw.rect( screen, wall_color, [wall_x[i],wall_y[i],wall_length[i],10] )

			for i in range(DEATHS):
				pygame.draw.rect( screen, red, [death_x[i],death_y[i],10,10] )
				
			for i in range(RECHARGES):
				pygame.draw.rect( screen, green, [recharge_x[i],recharge_y[i],10,10] )
				
			
			if not got_key:
				screen.blit(keypic, (key_x, key_y))

			if not reached_gate:
				gate_color = red
			else:
				gate_color = green

			screen.blit(gatepic, (gate_x, gate_y))
			pygame.draw.rect( screen, man_color, [curr_x,curr_y,10,10] )
			

		pygame.draw.rect( screen, (0,0,0), (0,580,200,120))
		screen.blit(font1.render(str(battery),True, (255,255,255)), (30,580))
		screen.blit(font1.render("Level : "+str(nlevel+1),True, (255,255,255)), (55,680))
		screen.blit(font1.render(str(curr_score), True, (255,255,255)), (40, 640))
		if not got_key:
			screen.blit(font1.render("Key??",True, red), (80,580))
		else:
			screen.blit(font4.render("Get to the Door",True, green), (80,580))
		if curr_time<=target_time:
			screen.blit(font4.render("Torch will be back in : "+str(target_time - curr_time),True, red), (10,615))
		else:
			screen.blit(font1.render("Torch ready",True, green), (10,615))
		screen.blit(font1.render("Time Left : "+str(dead_time_array[nlevel] - curr_time), True, (255,255,255)), (30, 660))

		pygame.display.update()

		clock.tick(CLOCK_TICK)

def show_start():
	global HLEVEL
	nlevel = 1
	HLEVEL = nlevel

	if nlevel >= 10:
		nlevel = 10

	global HIGHSCORE

	global wall_x, wall_y, wall_length, wall_width, death_y, death_x, recharge_x, recharge_y
	global INITIAL_CHARGE
	global CLOCK_TICK, NEW_RECHARGE
	global EXTRA_CHARGE
	global DELAY
	global WALLS
	global gate_x
	global key_x
	global key_y
	global got_key
	global isrunning
	global doexit
	global curr_score
	global DEATHS
	global gate_y
	global reached_gate
	global RECHARGES

	del wall_x[:]
	del wall_y[:]
	del wall_length[:]
	del wall_width[:]
	del death_x[:]
	del death_y[:]
	del recharge_x[:]
	del recharge_y[:]

	screen = pygame.display.set_mode((width, height))
	pygame.display.set_caption("Bit Castle")
	screen.fill(background_color)
	pygame.display.flip()

	

	INITIAL_CHARGE = initial_charge_array[nlevel]
	INITIAL_CHARGE += EXTRA_CHARGE
	battery = INITIAL_CHARGE

	isdead = False

	CLOCK_TICK = 20
	NEW_RECHARGE = new_recharge_array[nlevel]

	MAX_DEATHS = max_deaths_array[nlevel]
	MAX_RECHARGES = max_recharges_array[nlevel]
	
	

	font1 = pygame.font.Font("arial.ttf", 20)
	font4 = pygame.font.Font("arial.ttf", 16)

	
	isrunning = True

	
	doexit = False

	
	gate_x = 100
	
	gate_y = 0
	
	reached_gate = False

	
	got_key = False
	key_y = 265
	key_x = 82

	
	DEATHS = 0
	
	RECHARGES = 0

	curr_x = 90
	curr_y = 570
	last_x = 90
	last_y = 590
	dir_x_change = 0
	dir_y_change = 0

	touched_wall_lower = False
	touched_wall_upper = False
	touched_wall_right = False
	touched_wall_left = False

	clock = pygame.time.Clock()

	gatepic = pygame.image.load('door.png')
	keypic = pygame.image.load('key.png')

	torch = True

	death_x.append(120)
	death_y.append(120)

	death_x.append(50)
	death_y.append(230)

	death_x.append(120)
	death_y.append(310)

	DEATHS = 3

	recharge_x.append(150)
	recharge_y.append(110)

	recharge_x.append(80)
	recharge_y.append(235)

	recharge_x.append(180)
	recharge_y.append(320)

	recharge_x.append(10)
	recharge_y.append(440)

	RECHARGES = 4

	wall_x = [ 27 , 122 , 44 , 128 , 26 , 133 , 5 , 134 , 4 , 91 , 28 , 134 , 16 , 102 , 8 , 140 , 38 , 133 , 56 , 133 , 20 , 122] 
	wall_y = [ 50 , 50 , 100 , 100 , 150 , 150 , 200 , 200 , 250 , 250 , 300 , 300 , 350 , 350 , 400 , 400 , 450 , 450 , 500 , 500 , 550 , 550]
	wall_length = [53 , 52 , 48 , 52 , 53 , 52 , 59 , 59 , 54 , 55 , 45 , 46 , 51 , 53 , 55 , 42 , 54 , 60 , 40 , 50 , 56 , 54]
	wall_width = [ 10 , 10 , 10 , 10 , 10 , 10 , 10 , 10 , 10 , 10, 10 , 10 , 10 , 10 , 10 , 10 , 10 , 10 , 10 , 10 , 10 , 10]

	WALLS = 22

			
	curr_time = 0
	pygame.display.update()

	target_time = 0

	dir_y_change = -2
	flag = 0

	while isrunning:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit(0)
		curr_time+=1

		if curr_y == 520:
			if curr_x == 120:
				dir_x_change = 0
				dir_y_change = -2
			else:
				dir_x_change = +2
				dir_y_change = 0

		elif curr_y == 410:
			if curr_x == 190:
				dir_x_change = 0
				dir_y_change = -2
			else: 
				dir_x_change = +2
				dir_y_change = 0

		elif curr_y == 320:
			dir_y_change = 0
			dir_x_change = -2

		reached_gate = False

		if curr_x >= key_x and curr_x <= key_x+10 and curr_y >= key_y and curr_y<=key_y+10:
			got_key = True
		if curr_x+10 >= key_x and curr_x+10 <= key_x+10 and curr_y >= key_y and curr_y<=key_y+10:
			got_key = True
		if curr_x+10 >= key_x and curr_x+10 <= key_x+10 and curr_y+10 >= key_y and curr_y+10 <= key_y+10:
			got_key = True
		if curr_x >= key_x and curr_x <= key_x+10 and curr_y+10 >= key_y and curr_y+10 <= key_y+10:
			got_key = True

		if curr_x >= gate_x and curr_x <= gate_x+10 and curr_y >= gate_y and curr_y<=gate_y+10:
			reached_gate = True
		if curr_x+10 >= gate_x and curr_x+10 <= gate_x+10 and curr_y >= gate_y and curr_y<=gate_y+10:
			reached_gate = True
		if curr_x+10 >= gate_x and curr_x+10 <= gate_x+10 and curr_y+10 >= gate_y and curr_y+10 <= gate_y+10:
			reached_gate = True
		if curr_x >= gate_x and curr_x <= gate_x+10 and curr_y+10 >= gate_y and curr_y+10 <= gate_y+10:
			reached_gate = True



		if reached_gate and got_key:
			return 0

		for i in range(DEATHS):
			if curr_x >= death_x[i] and curr_x <= death_x[i]+10 and curr_y >= death_y[i] and curr_y<=death_y[i]+10:
				isdead = True
			if curr_x+10 >= death_x[i] and curr_x+10 <= death_x[i]+10 and curr_y >= death_y[i] and curr_y<=death_y[i]+10:
				isdead = True
			if curr_x+10 >= death_x[i] and curr_x+10 <= death_x[i]+10 and curr_y+10 >= death_y[i] and curr_y+10 <= death_y[i]+10:
				isdead = True
			if curr_x >= death_x[i] and curr_x <= death_x[i]+10 and curr_y+10 >= death_y[i] and curr_y+10 <= death_y[i]+10:
				isdead = True

		for i in range(RECHARGES):
			if curr_x >= recharge_x[i] and curr_x <= recharge_x[i]+10 and curr_y >= recharge_y[i] and curr_y<=recharge_y[i]+10:
				battery += NEW_RECHARGE
				recharge_x.remove(recharge_x[i])
				recharge_y.remove(recharge_y[i])
				RECHARGES-=1
				break;
			if curr_x+10 >= recharge_x[i] and curr_x+10 <= recharge_x[i]+10 and curr_y >= recharge_y[i] and curr_y<=recharge_y[i]+10:
				battery += NEW_RECHARGE
				recharge_x.remove(recharge_x[i])
				recharge_y.remove(recharge_y[i])
				RECHARGES-=1
				break;
			if curr_x+10 >= recharge_x[i] and curr_x+10 <= recharge_x[i]+10 and curr_y+10 >= recharge_y[i] and curr_y+10 <= recharge_y[i]+10:
				battery += NEW_RECHARGE
				recharge_x.remove(recharge_x[i])
				recharge_y.remove(recharge_y[i])
				RECHARGES-=1
				break;
			if curr_x >= recharge_x[i] and curr_x <= recharge_x[i]+10 and curr_y+10 >= recharge_y[i] and curr_y+10 <= recharge_y[i]+10:
				battery += NEW_RECHARGE
				recharge_x.remove(recharge_x[i])
				recharge_y.remove(recharge_y[i])
				RECHARGES-=1
				break;


		for i in range(WALLS):
			if ( (curr_x < wall_x[i]+wall_length[i] and curr_x >= wall_x[i]) or (curr_x+10 < wall_x[i]+wall_length[i] and curr_x+10 > wall_x[i]) ) and curr_y <= wall_y[i]+10 and curr_y>=wall_y[i]:
				touched_wall_lower = True

			if ( (curr_x < wall_x[i]+wall_length[i] and curr_x >= wall_x[i]) or (curr_x+10 < wall_x[i]+wall_length[i] and curr_x+10 > wall_x[i]) ) and curr_y+10 <= wall_y[i]+10 and curr_y+10 >=wall_y[i]:
				touched_wall_upper = True

			if curr_x >= wall_x[i] and curr_x <= wall_x[i]+wall_length[i] and ( (curr_y >= wall_y[i] and curr_y < wall_y[i]+wall_width[i]) or (curr_y+10 > wall_y[i] and curr_y+10 <= wall_y[i]+wall_width[i])):
				touched_wall_right = True

			if curr_x+10 >= wall_x[i] and curr_x+10 <= wall_x[i]+wall_length[i] and ( (curr_y >= wall_y[i] and curr_y < wall_y[i]+wall_width[i]) or (curr_y+10 > wall_y[i] and curr_y+10 <= wall_y[i]+wall_width[i])):
				touched_wall_left = True

		if curr_x <= 0:
			touched_wall_right = True
		if curr_x+10 >= width:
			touched_wall_left = True
		if curr_y <= 0:
			touched_wall_lower = True
		if curr_y+10 > 580:
			touched_wall_upper = True

		if curr_x >= width or curr_x < 0 or curr_y < 0 or curr_y >= height:
			doexit = True

		if isdead:
			return 0

		if touched_wall_upper and dir_y_change>0:
			curr_y = curr_y
		elif touched_wall_upper and dir_y_change<=0:
			curr_y += dir_y_change
		elif touched_wall_lower and dir_y_change<=0:
			curr_y = curr_y
		elif touched_wall_lower and dir_y_change>0:
			curr_y += dir_y_change
		if not touched_wall_upper and not touched_wall_lower:
			curr_y += dir_y_change

		if touched_wall_left and dir_x_change>0:
			curr_x = curr_x
		elif touched_wall_left and dir_x_change<=0:
			curr_x += dir_x_change
		elif touched_wall_right and dir_x_change<=0:
			curr_x = curr_x
		elif touched_wall_right and dir_x_change>0:
			curr_x += dir_x_change
		if not touched_wall_right and not touched_wall_left:
			curr_x += dir_x_change

		last_x = curr_x
		last_y = curr_y

		touched_wall_lower = False
		touched_wall_upper = False
		touched_wall_left = False
		touched_wall_right = False
 

		if not torch or battery<=0:
			screen.fill((0,0,0))
			pygame.draw.rect( screen, (255,255,255), [curr_x,curr_y,10,10] )
			
		else:
			battery = battery - 1
			screen.fill(background_color)

			for i in range(WALLS):
				pygame.draw.rect( screen, wall_color, [wall_x[i],wall_y[i],wall_length[i],10] )

			for i in range(DEATHS):
				pygame.draw.rect( screen, red, [death_x[i],death_y[i],10,10] )

			for i in range(RECHARGES):
				pygame.draw.rect( screen, green, [recharge_x[i],recharge_y[i],10,10] )
			
			if not got_key:
				screen.blit(keypic, (key_x, key_y))

			if not reached_gate:
				gate_color = red
			else:
				gate_color = green

			screen.blit(gatepic, (gate_x, gate_y))
			pygame.draw.rect( screen, man_color, [curr_x,curr_y,10,10] )

		pygame.draw.rect( screen, (0,0,0), (0,580,200,120))

		screen.blit(font1.render(str(battery),True, (255,255,255)), (30,580))
		screen.blit(font1.render("Level : "+str(nlevel+1),True, (255,255,255)), (55,680))
		screen.blit(font1.render(str(curr_score), True, (255,255,255)), (40, 640))
		if not got_key:
			screen.blit(font1.render("Key??",True, red), (80,580))
		else:
			screen.blit(font4.render("Get to the Door",True, green), (80,580))
		if curr_time<=target_time:
			screen.blit(font4.render("Torch will be back in : "+str(target_time - curr_time),True, red), (10,615))
		else:
			screen.blit(font1.render("Torch ready",True, green), (10,615))
		screen.blit(font1.render("Time Left : "+str(dead_time_array[nlevel] - curr_time), True, (255,255,255)), (30, 660))
		pygame.display.update()

		clock.tick(100)

def main():
	global PLAYER_NAME
	try:
		file = open("x.txt",'r+') 
		PLAYER_NAME = file.read()
		if len(PLAYER_NAME)==0:
			file.close()
			file = open("x.txt", 'w')
			name()
			file.write(PLAYER_NAME)
			file.close()
	except:
		file = open("x.txt", 'w')
		name()
		file.write(PLAYER_NAME)
		file.close()

	show_start()

	PLAYER_NAME = PLAYER_NAME.upper()

	start_Screen()

	j=0
	for i in range(100):
		res = start_level(j)
		j+=1
		if res == 0:
			print "dead"
			start_Screen()
			j=0
		print j

if __name__ == "__main__":
	main()