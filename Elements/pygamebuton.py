import pygame
import pygame_gui


pygame.init()
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Botón con Pygame GUI")

manager = pygame_gui.UIManager((screen_width, screen_height))

# Crear un botón
button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((350, 275), (100, 50)),  # Posición (x, y) y tamaño (ancho, alto)
    text="Haz clic",  # Texto del botón
    manager=manager
)


def mi_funcion():
    print("¡Botón presionado!")

# Bucle principal
clock = pygame.time.Clock()
running = True
while running:
    time_delta = clock.tick(60) / 1000.0  

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Manejar eventos de Pygame GUI
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == button:
                    mi_funcion()  # Llamar a la función

        manager.process_events(event)

    # Actualizar la interfaz
    manager.update(time_delta)

    # Dibujar
    screen.fill((240, 240, 240))  
    manager.draw_ui(screen)

    pygame.display.flip()

pygame.quit()