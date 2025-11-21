
"""
import pygame
import math

def pendiente(p1, p2):
    if p1[0] == p2[0]:
        return math.inf
    return (p2[1] - p1[1]) / (p2[0] - p1[0])

def definir_p3(p1, p2, curva=0.3):
    mx = (p1[0] + p2[0]) / 2
    my = (p1[1] + p2[1]) / 2

    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]

    length = math.hypot(dx, dy)

    if length == 0:
        return p1  

    nx = -dy / length
    ny = dx / length

    
    p3x = mx + nx * length * curva
    p3y = my + ny * length * curva

    return (p3x, p3y)

def quadratic_bezier(p1, p2, t, p3):
    "Calcula un punto en una curva Bézier cuadrática"
    x = (1 - t)**2 * p1[0] + 2 * (1 - t) * t * p3[0] + t**2 * p2[0]
    y = (1 - t)**2 * p1[1] + 2 * (1 - t) * t * p3[1] + t**2 * p2[1]
    return (x, y)

# Inicializar Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Curva Bézier Cuadrática Bonita")
clock = pygame.time.Clock()

# Puntos de prueba
p1 = (500, 100)
p2 = (100, 500)

# Punto de control automático
p3 = definir_p3(p1, p2, curva=0.2)

# Generar puntos de la curva
points = [quadratic_bezier(p1, p2, t / 100, p3) for t in range(101)]

# Loop principal
running = True
while running:
    screen.fill((255, 255, 255))

    # Dibuja la curva
    pygame.draw.lines(screen, (0, 0, 255), False, points, 3)

    # Dibuja los puntos de control
    pygame.draw.circle(screen, (255, 0, 0), p1, 5)
    pygame.draw.circle(screen, (0, 255, 0), p2, 5)
    pygame.draw.circle(screen, (0, 0, 0), (int(p3[0]), int(p3[1])), 5)
    pygame.draw.line(screen, (150, 150, 150), p1, p3, 1)
    pygame.draw.line(screen, (150, 150, 150), p3, p2, 1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
"""


import pygame
import pygame_gui
import math
import ctypes


####
def pendiente(p1, p2):
    if p1[0] == p2[0]:
        return math.inf
    return (p2[1] - p1[1]) / (p2[0] - p1[0])
####
def definir_p3(p1, p2, curva=0.3):
    mx = (p1[0] + p2[0]) / 2
    my = (p1[1] + p2[1]) / 2

    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]

    length = math.hypot(dx, dy)

    if length == 0:
        return p1

    nx = -dy / length
    ny = dx / length

    p3x = mx + nx * length * curva
    p3y = my + ny * length * curva

    return (p3x, p3y)
####
def quadratic_bezier(p1, p2, t, p3):
    x = (1 - t)**2 * p1[0] + 2 * (1 - t) * t * p3[0] + t**2 * p2[0]
    y = (1 - t)**2 * p1[1] + 2 * (1 - t) * t * p3[1] + t**2 * p2[1]
    return (x, y)



# Inicializar Pygame
pygame.init()
window = pygame.display.set_mode((1080, 800), pygame.RESIZABLE)
pygame.display.set_caption("Curva Bézier Arrastrable")
SDL_WINDOWPOS_CENTERED = 0x2FFF0000
sdl_window = pygame.display.get_wm_info()['window']
ctypes.windll.user32.ShowWindow(sdl_window, 3)
window_size = window.get_size()
manager = pygame_gui.UIManager(window_size)

# Variables de control
nodo_seleccionado = None
arrastrando = False

# Colores
BLANCO      = (255, 255, 255)
GRIS_CLARO  = (230, 230, 230)
GRIS        = (170, 170, 170)
GRIS_OSCURO = (100, 100, 100)
NEGRO       = (0,   0,   0)
AZUL        = (50,  125, 255)

# Puntos de prueba
coor = [[500,200], [300,400], [700, 400], [800,200]]  # puedes agregar más nodos

####
p1 = coor[0]
p2 = coor[1]
p3 = definir_p3(p1, p2, curva=0.3)
points = [quadratic_bezier(p1, p2, t / 100, p3) for t in range(101)]

reloj = pygame.time.Clock()
running = True

while running:
    time_delta = reloj.tick(60) / 1000.0
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            running = False

        manager.process_events(evento)

        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            for i, (x, y) in enumerate(coor):
                dx = evento.pos[0] - x
                dy = evento.pos[1] - y
                if dx**2 + dy**2 <= 30**2:
                    nodo_seleccionado = i
                    arrastrando = True
                    break

        elif evento.type == pygame.MOUSEBUTTONUP and evento.button == 1:
            arrastrando = False
            nodo_seleccionado = None
        ####
        elif evento.type == pygame.MOUSEMOTION and arrastrando and nodo_seleccionado is not None:
            x = max(50, min(evento.pos[0], 1070))
            y = max(50, min(evento.pos[1], 790))
            coor[nodo_seleccionado][0] = x
            coor[nodo_seleccionado][1] = y

            # Actualiza los puntos de la curva
            p1 = coor[0]
            p2 = coor[1]
            p3 = definir_p3(p1, p2, curva=0.3)
            points = [quadratic_bezier(p1, p2, t / 100, p3) for t in range(101)]

    manager.update(time_delta)

    window.fill(BLANCO)

    # Dibuja curva
    pygame.draw.lines(window, AZUL, False, points, 3)

    # Dibuja nodos
    for x, y in coor:
        pygame.draw.circle(window, NEGRO, (int(x), int(y)), 10)

    # Puntos de control
    pygame.draw.circle(window, (255, 0, 0), p1, 10)
    pygame.draw.circle(window, (0, 255, 0), p2, 10)
    pygame.draw.circle(window, (0, 0, 0), (int(p3[0]), int(p3[1])), 10)
    pygame.draw.line(window, GRIS_OSCURO, p1, p3, 1)
    pygame.draw.line(window, GRIS_OSCURO, p3, p2, 1)

    manager.draw_ui(window)
    pygame.display.flip()

pygame.quit()

"""








import pygame
import pygame_gui
import math
import ctypes


####
def pendiente(p1, p2):
    if p1[0] == p2[0]:
        return math.inf
    return (p2[1] - p1[1]) / (p2[0] - p1[0])
####
def definir_p3(p1, p2, curva=0.3):
    mx = (p1[0] + p2[0]) / 2
    my = (p1[1] + p2[1]) / 2

    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]

    length = math.hypot(dx, dy)

    if length == 0:
        return p1

    nx = -dy / length
    ny = dx / length

    p3x = mx + nx * length * curva
    p3y = my + ny * length * curva

    return (p3x, p3y)
####
def quadratic_bezier(p1, p2, t, p3):
    x = (1 - t)**2 * p1[0] + 2 * (1 - t) * t * p3[0] + t**2 * p2[0]
    y = (1 - t)**2 * p1[1] + 2 * (1 - t) * t * p3[1] + t**2 * p2[1]
    return (x, y)
####
def dibujar_curva_con_flecha(surface, p1, p2, curva=0.3, color=(0, 0, 0), grosor=3, radio=10, incluir_linea=True):
    p3 = definir_p3(p1, p2, curva)
    points = [quadratic_bezier(p1, p2, t / 100, p3) for t in range(101)]

    # Dibuja la curva
    if incluir_linea:
        pygame.draw.lines(surface, color, False, points, grosor)

    # Dibuja flecha al final de la curva
    end = points[-1]
    pre_end = points[-2]  # Para estimar la dirección

    dx = end[0] - pre_end[0]
    dy = end[1] - pre_end[1]
    angle = math.atan2(dy, dx)

    arrow_length = 12
    arrow_width = 6

    # Puntos de la flecha
    left = (end[0] - arrow_length * math.cos(angle - math.pi / 6),
            end[1] - arrow_length * math.sin(angle - math.pi / 6))
    right = (end[0] - arrow_length * math.cos(angle + math.pi / 6),
             end[1] - arrow_length * math.sin(angle + math.pi / 6))

    pygame.draw.polygon(surface, color, [end, left, right])




# Inicializar Pygame
pygame.init()
window = pygame.display.set_mode((1080, 800), pygame.RESIZABLE)
pygame.display.set_caption("Curva Bézier Arrastrable")
SDL_WINDOWPOS_CENTERED = 0x2FFF0000
sdl_window = pygame.display.get_wm_info()['window']
ctypes.windll.user32.ShowWindow(sdl_window, 3)
window_size = window.get_size()
manager = pygame_gui.UIManager(window_size)

# Variables de control
nodo_seleccionado = None
arrastrando = False

# Colores
BLANCO      = (255, 255, 255)
GRIS_CLARO  = (230, 230, 230)
GRIS        = (170, 170, 170)
GRIS_OSCURO = (100, 100, 100)
NEGRO       = (0,   0,   0)
AZUL        = (50,  125, 255)

# Puntos de prueba
coor = [[500,200], [300,400], [700, 400], [800,200]]  # puedes agregar más nodos

####
p1 = coor[0]
p2 = coor[1]
p3 = definir_p3(p1, p2, curva=0.3)
points = [quadratic_bezier(p1, p2, t / 100, p3) for t in range(101)]

reloj = pygame.time.Clock()
running = True

while running:
    time_delta = reloj.tick(60) / 1000.0
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            running = False

        manager.process_events(evento)

        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            for i, (x, y) in enumerate(coor):
                dx = evento.pos[0] - x
                dy = evento.pos[1] - y
                if dx**2 + dy**2 <= 30**2:
                    nodo_seleccionado = i
                    arrastrando = True
                    break

        elif evento.type == pygame.MOUSEBUTTONUP and evento.button == 1:
            arrastrando = False
            nodo_seleccionado = None
        ####
        elif evento.type == pygame.MOUSEMOTION and arrastrando and nodo_seleccionado is not None:
            x = max(50, min(evento.pos[0], 1070))
            y = max(50, min(evento.pos[1], 790))
            coor[nodo_seleccionado][0] = x
            coor[nodo_seleccionado][1] = y

            # Actualiza los puntos de la curva
            p1 = coor[0]
            p2 = coor[1]
            p3 = definir_p3(p1, p2, curva=0.3)
            points = [quadratic_bezier(p1, p2, t / 100, p3) for t in range(101)]

    manager.update(time_delta)

    window.fill(BLANCO)

    # Dibuja curva
    dibujar_curva_con_flecha(window, coor[0], coor[1], curva=0.3, color=AZUL, grosor=3, radio=10, incluir_linea=True)


    # Dibuja nodos
    for x, y in coor:
        pygame.draw.circle(window, NEGRO, (int(x), int(y)), 10)

    # Puntos de control
    pygame.draw.circle(window, (255, 0, 0), p1, 10)
    pygame.draw.circle(window, (0, 255, 0), p2, 10)
    pygame.draw.circle(window, (0, 0, 0), (int(p3[0]), int(p3[1])), 10)
    pygame.draw.line(window, GRIS_OSCURO, p1, p3, 1)
    pygame.draw.line(window, GRIS_OSCURO, p3, p2, 1)

    manager.draw_ui(window)
    pygame.display.flip()

pygame.quit()

"""
