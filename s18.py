import pygame
pygame.init()
screen = pygame.display.set_mode((700, 500))
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
screen.fill(WHITE)
rect_x = 0
rect_y = 0
rect_change_x = 1
rect_change_y = 1

done = True
while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
    pygame.draw.rect(screen, BLACK, [rect_x, rect_y, 5, 5])
    rect_x += rect_change_x
    rect_y += rect_change_y
    if rect_y > 495 or rect_y < 0:
        rect_change_y = rect_change_y * -1
    # exercise 1 : برگشت از گوشه های راست و چپ صفحه
    if rect_x > 695 or rect_x < 0:
        rect_change_x = -1 * rect_change_x
    pygame.display.flip()


# exercise 2: رسم اشکال هندسی 
# مثلث
# مربع
# مستطیل
# کمک
pygame.draw.polygon(screen, BLACK, [[], [],[]])