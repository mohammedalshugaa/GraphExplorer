import pygame
import pygame_gui

pygame.init()

# Crear ventana
ventana = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Entrada de texto con pygame_gui")

# Reloj para el framerate
clock = pygame.time.Clock()

# Crear el UIManager
manager = pygame_gui.UIManager((600, 400))

# Crear una entrada de texto (UITextEntryLine)
entrada_texto = pygame_gui.elements.UITextEntryLine(
    relative_rect=pygame.Rect((200, 150), (200, 30)),
    manager=manager
)

# Variable para salir del bucle
corriendo = True

while corriendo:
    tiempo_delta = clock.tick(60) / 1000.0

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

        # Pasar eventos al UIManager
        manager.process_events(evento)

        # Ejemplo: detectar cuando se presiona ENTER en la entrada
        if evento.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and evento.ui_element == entrada_texto:
            print("Texto ingresado:", evento.text)

    # Actualizar el UIManager
    manager.update(tiempo_delta)

    # Dibujar la interfaz
    ventana.fill((220,220,220))
    manager.draw_ui(ventana)

    pygame.display.update()

pygame.quit()
