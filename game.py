from pygame import *

windos = display.set_mode((700,500))
fon = transform.scale(image.load('svat.png'),(700,500))
display.set_caption('pin-pong')
watch = time.Clock()
font.unit()
write= font.Font(None,40)
FPS = 60
s_x = 3
s_y = 3

class GameSprite(sprite.Sprite):
    def __init__ (self, player_image, player_speed, player_x, player_y,wei = 20,hei = 65):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (wei,hei))
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

platf_1 = Player('cot.jpg',4,10,295)
platf_2 = Player('cot.jpg',4,670,295)
ball = GameSprite('robot.png',0,350,250,60,60)
final = False
game = True
lis_1 = write.render('второй игрок проиграл', (255,0,0))
while game:

    windos.blit(fon,(0,0))

    for e in event.get():
        if e.type == QUIT:
            game = False

    if final != True:
        ball.rect.x += s_x
        ball.rect.y += s_y

        if ball.rect.y >= 450 or ball.rect.y <= 0:
            s_y *= -1

        if sprite.collide_rect(platf_1,ball) or sprite.collide_rect(platf_2,ball):
            s_x *= -1

        if ball.rect.x >= 650:
            final = True
            windos.blit(lis_1,(245,200))

        if ball.rect.x <= 0:
            final = True

        ball.reset()
        platf_1.update_l()
        platf_2.update_r()
        platf_1.reset()
        platf_2.reset()

    display.update()
    watch.tick(FPS)
