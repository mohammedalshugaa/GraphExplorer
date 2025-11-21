import pygame
import pygame_gui

pygame.init()
ventana = pygame.display.set_mode((1000, 500))
pygame.display.set_caption("Menú contextual simulado")
clock = pygame.time.Clock()

manager = pygame_gui.UIManager((1000, 500))

# Panel que actuará como menú contextual (inicialmente oculto)
menu_contextual = pygame_gui.elements.UIPanel(
    relative_rect=pygame.Rect((0, 0), (130, 200)),
    #starting_layer_height=1,
    manager=manager,
    visible=0  # oculto al inicio
)

opcion1 = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((0, 0), (120, 30)),
    text='Opción 1',
    manager=manager,
    container=menu_contextual
)

opcion2 = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((0, 30), (120, 30)),
    text='Opción 2',
    manager=manager,
    container=menu_contextual
)

opcion3 = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((0, 60), (120, 30)),
    text='Cancelar',
    manager=manager,
    container=menu_contextual
)

corriendo = True
while corriendo:
    tiempo_delta = clock.tick(60) / 1000.0

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

        # Mostrar menú contextual al hacer clic derecho
        elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 3:
            menu_contextual.set_relative_position(evento.pos)
            menu_contextual.show()

        # Ocultar menú si se hace clic izquierdo fuera de él
        elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            if not menu_contextual.get_relative_rect().collidepoint(evento.pos):
                menu_contextual.hide()

        # Procesar botones del menú
        elif evento.type == pygame_gui.UI_BUTTON_PRESSED:
            if evento.ui_element == opcion1:
                print("Seleccionaste opción 1")
                menu_contextual.hide()
            elif evento.ui_element == opcion2:
                print("Seleccionaste opción 2")
                menu_contextual.hide()
            elif evento.ui_element == opcion3:
                menu_contextual.hide()

        manager.process_events(evento)

    manager.update(tiempo_delta)
    ventana.fill((40, 40, 40))
    manager.draw_ui(ventana)
    pygame.display.update()

pygame.quit()
