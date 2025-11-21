import pygame
pygame.init()

screen = pygame.display.set_mode((400, 300))
clock = pygame.time.Clock()

# Definir el rectángulo que contiene el arco y los ángulos de inicio/fin
rect = pygame.Rect(100, 100, 200, 100)
start_angle = 0  # En radianes
end_angle = 3.14  # Pi radianes = 180 grados

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((255, 255, 255))
    
    # Dibujar arco (línea curva)
    pygame.draw.arc(screen, (0, 0, 0), rect, start_angle, end_angle, 2)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()