import pygame
import random
import math

# Configuración inicial
WIDTH, HEIGHT = 800, 600
CIRCLE_RADIUS = 10
LINE_COLOR = (0, 255, 0)
CIRCLE_COLOR = (255, 0, 0)
TEXT_COLOR = (255, 255, 255)
BG_COLOR = (30, 30, 30)

# Longitudes deseadas entre círculos
target_lengths = [100, 100, 141]
num_circles = len(target_lengths) + 1

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Círculos con líneas")
font = pygame.font.SysFont(None, 24)
clock = pygame.time.Clock()

# Generar posiciones de círculos con distancias aproximadas a las longitudes dadas
def generate_circle_positions(lengths):
    positions = []
    x, y = random.randint(100, WIDTH - 100), random.randint(100, HEIGHT - 100)
    positions.append((x, y))

    for length in lengths:
        angle = random.uniform(0, 2 * math.pi)
        dx = length * math.cos(angle)
        dy = length * math.sin(angle)
        x += dx
        y += dy

        # Mantener dentro de los bordes
        x = max(CIRCLE_RADIUS, min(WIDTH - CIRCLE_RADIUS, x))
        y = max(CIRCLE_RADIUS, min(HEIGHT - CIRCLE_RADIUS, y))

        positions.append((x, y))

    return positions

# Dibujar líneas con longitudes etiquetadas
def draw_lines_with_lengths(surface, positions):
    for i in range(len(positions) - 1):
        p1 = positions[i]
        p2 = positions[i + 1]
        pygame.draw.line(surface, LINE_COLOR, p1, p2, 2)

        # Calcular y mostrar la distancia
        dist = math.dist(p1, p2)
        mid_x = (p1[0] + p2[0]) / 2
        mid_y = (p1[1] + p2[1]) / 2

        text = font.render(f"{dist:.1f}", True, TEXT_COLOR)
        text_rect = text.get_rect(center=(mid_x, mid_y - 10))  # un poco arriba de la línea
        surface.blit(text, text_rect)

def main():
    running = True
    circle_positions = generate_circle_positions(target_lengths)

    while running:
        screen.fill(BG_COLOR)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Dibujar círculos
        for pos in circle_positions:
            pygame.draw.circle(screen, CIRCLE_COLOR, (int(pos[0]), int(pos[1])), CIRCLE_RADIUS)

        # Dibujar líneas y longitudes
        draw_lines_with_lengths(screen, circle_positions)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
