from pygame import *

windos = display.set_mode((700,500))
fon = transform.scale(image.load('svat.png'),(700,500))
display.set_caption('pin-pong')
watch = time.Clock()
FPS = 60

class GameSprite(sprite.Sprite):
    def __init__ (self, player_image, player_speed, player_x, player_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (10, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        windos.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y >0:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y <435:
            self.rect.y += self.speed

    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 435:
            self.rect.y += self.speed

platf_1 = Player('tviter.png',4,10,295)
platf_2 = Player('tviter.png',4,680,295)


game = True
while game:

    windos.blit(fon,(0,0))

    for e in event.get():
        if e.type == QUIT:
            game = False


    platf_1.update_l()
    platf_2.update_r()
    platf_1.reset()
    platf_2.reset()

    display.update()
    watch.tick(FPS)