import pygame

pygame.init()
screen = pygame.display.set_mode([400, 280])

map = [['0' for x in range(20)] for y in range(14)]

mode = '0'
running = True
while running == True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

		if event.type == pygame.MOUSEBUTTONDOWN:
			map[pygame.mouse.get_pos()[1] // 20][pygame.mouse.get_pos()[0] // 20] = mode

		if event.type == pygame.KEYDOWN:
			if pygame.key.get_pressed()[pygame.K_0]:
				mode = '0'
			if pygame.key.get_pressed()[pygame.K_1]:
				mode = '1'
			if pygame.key.get_pressed()[pygame.K_2]:
				mode = '2'
			if pygame.key.get_pressed()[pygame.K_3]:
				mode = '3'
			if pygame.key.get_pressed()[pygame.K_6]:
				mode = '6'
			if pygame.key.get_pressed()[pygame.K_p]:
				for y in range(14):
					print(map[y])

	screen.fill((255, 255, 255))
	for y in range(14):
		for x in range(20):
			case = map[y][x]
			if case == '1':
				pygame.draw.rect(screen, (200, 200, 200), [x * 20, y * 20, 20, 20])
			elif case == '2':
				pygame.draw.rect(screen, (255, 255, 0), [x * 20 + 6, y * 20 + 4, 4, 8])
			elif case == '3':
				pygame.draw.rect(screen, (255, 0, 0), [x * 20 + 6, y * 20 + 2, 4, 12])
			elif case == '6':
				pygame.draw.rect(screen, (100, 100, 100), [x * 20, y * 20, 20, 20])

	pygame.display.flip()
