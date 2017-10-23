import pygame, sys

class hpbar(object):
    def __init__(self, hpchunks, screen, posx, posy):
        global val_per_chunk
        self.hpchunks = hpchunks # hpchunk can either be 125 or 250
        self.screen = screen
        self.posx = posx
        self.posy = posy
        self.unit_h = 18
        self.unit_w = 250
        
        self.image = pygame.image.load('hpbar.png')
        self.total_hp = [self.posx + 3, self.posy + 3, self.unit_w, self.unit_h] 
        self.startPos = 253
        self.cur_hp = 250
        
        self.hp_change = False
        screen.blit(self.image, [self.posx, self.posy])
        pygame.display.flip()

    def loss(self, loss_val):
    	self.loss_val = loss_val
    	self.cur_hp -= self.loss_val
    	self.hp_change = True

    	val_per_chunk = self.unit_w / self.hpchunks	# units of a single chunk e.g. 250 / 125 = 2
    	total_chunk = self.loss_val * val_per_chunk	# e.g. if loss = 10, then the total chunk will be 10 * 2 
    	chunkPosx = self.posx + 3 					# e.g. if hpchunk = 125, then the hp will be in chunks of two
    	
    	healthbar = [0, 255, 0]
    	BackBar = [0, 0, 0]
    	total_chunk = 0  # first iterative value
    	
    	pygame.draw.rect(self.screen, BackBar, self.total_hp, 0) # hp bar 
    	#chunkPosx -= (val_per_chunk * self.loss_val)            # x position of chunk (for bar)
    	#total_chunk += (val_per_chunk * self.loss_val)        	 # total size of chunk
    		
    	if self.cur_hp <= self.unit_w - 128: # yellow zone
    		healthbar = [255, 255, 0]
    	if self.cur_hp <= self.unit_w - 191: # red zone
    		if val_per_chunk == 25:
    			healthbar = [255, 255, 255]
    		else:
    			healthbar = [255, 0, 0]
    	if self.cur_hp <= self.unit_w + 0:
    		print "game over"
    	pygame.draw.rect(self.screen, healthbar, [self.posx+3, self.posy + 3, self.cur_hp, self.unit_h], 0) #current visible hp
    	pygame.display.flip()
    	
    def HpTextDisplay(self):
    	hpFont = pygame.font.Font(None, 40)
    	hp = str(self.cur_hp)
    	hpText = hpFont.render('HP:' + hp, 0, [0, 0, 0])
    	TextPos = [self.posx, self.posy + 30]
    	screen.blit(hpText, TextPos)
    	pygame.display.flip()

pygame.init()
screen = pygame.display.set_mode([720, 480])
screen.fill((255, 255, 255))
newbar = hpbar(250, screen, 300, 300)
newbar.loss(100)

while True:
    for event in pygame.event.get():
   		if event.type == pygame.QUIT:
   			exit()
   			
   		key = pygame.key.get_pressed()
   		if key[pygame.K_ESCAPE]:
   			exit()