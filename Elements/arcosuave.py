import pygame
import math

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Línea curva con pygame.draw.lines()")
clock = pygame.time.Clock()

# Generar puntos para una curva senoidal
points = [(50 + i*15, 300 + 100 * math.sin(i/5)) for i in range(50)]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((240, 240, 240))
    
    # Dibujar la curva suave
    pygame.draw.lines(screen, (0, 100, 255), False, points, 4)
    
    # Dibujar puntos de control (opcional)
    for point in points[::5]:  # Mostrar cada 5 puntos
        pygame.draw.circle(screen, (255, 0, 0), (int(point[0]), int(point[1])), 3)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()