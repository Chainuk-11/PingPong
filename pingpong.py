from pygame import *

w, h = 700, 500
window = display.set_mode((w, h))
display.set_caption('Игра шутер')

class GameSprite(sprite.Sprite):
    def  __init__(self, imagefile, x, y, w, h, speed):
       super().__init__()
       self.image = transform.scale(image.load(imagefile),(w, h))
       self.speed = speed
       self.rect = self.image.get_rect()
       self.rect.x = x
       self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Raketka(GameSprite):
    def update_L(self):
        k = key.get_pressed()
        if k[K_a] and self.rect.y > 0:
            self.rect.y -= self.speed
        if k[K_z] and self.rect.y < h -80:
            self.rect.y += self.speed

    def update_R(self):
        k = key.get_pressed()
        if k[K_UP] and self.rect.y >  0:
            self.rect.y -= self.speed
        if k[K_DOWN] and self.rect.y < h -80:
            self.rect.y += self.speed

class Ball(GameSprite):
    def init(self):
        self.speed_x = self.speed
        self.speed_y = self.speed
    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.y < 50:
            self.speed_y *= -1
        if self.rect.y >= h-50:
            self.speed_y *= -1
        if sprite.collide_rect(self, raketka_R):
            self.speed_x *= -1
            self.rect.x += self.speed_x
        if sprite.collide_rect(self, raketka_L):
            self.speed_x *= -1
            self.rect.x += self.speed_x

ball = Ball('ball.png', 350, 300, 50, 50, 10)
ball.init()
raketka_L = Raketka('raketka1.png', 10, 20, 50, 80, 15)
raketka_R = Raketka('raketka2.png', 640, 320, 50, 80, 15)

font.init()
font1 = font.SysFont('Arial', 26)
text_L = font1.render('Проиграла левая ракетка', 1, (255,0,0))
text_R = font1.render('Проиграла правая ракетка', 1, (255,0,0))


game  = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    window.fill((0, 114, 180))
    ball.reset()
    if not finish:
        ball.update()
    if ball.rect.x < 5:
        finish = True
        window.blit(text_L, (180,250))

    if ball.rect.x > w-10:
        finish = True
        window.blit(text_R, (180,250))


    raketka_L.reset()
    raketka_L.update_L()

    raketka_R.reset()
    raketka_R.update_R()

    display.update()
    time.delay(50)