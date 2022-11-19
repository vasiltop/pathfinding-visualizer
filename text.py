import pygame

def text_objects(text, font):
    textSurface = font.render(text, True, (255,255,255))
    return textSurface, textSurface.get_rect()

def message_display(d,text, center):
    largeText = pygame.font.Font('freesansbold.ttf', 12)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (center)
    d.blit(TextSurf, TextRect)
