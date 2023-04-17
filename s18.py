import pygame
pygame.init()
screen = pygame.display.set_mode((700, 500))
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
screen.fill(WHITE)
rect_x = 50
rect_y = 50
rect_change_x = 1
rect_change_y = 1

done = True
while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
    pygame.draw.rect(screen, BLACK, [rect_x, rect_y, 50, 50])
    rect_x += rect_change_x
    rect_y += rect_change_y
    if rect_y > 450 or rect_y < 0:
        rect_change_y = rect_change_y * -1
    # exercise 1 : برگشت از گوشه های راست و چپ صفحه
    pygame.display.flip()


# exercise 2: رسم اشکال هندسی 
# مثلث
# مربع
# مستطیل
# کمک
pygame.draw.polygon(screen, BLACK, [[], [],[]])