import pygame
import pygame_gui

pygame.init()

# Configuración de la pantalla
ancho, alto = 600, 400
ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Botón con tema personalizado")

# Cargar el tema
gestor_ui = pygame_gui.UIManager((ancho, alto), r"C:\Users\alshu\Desktop\Grafos\Pygame\Elementos\Theme.json")

# Crear el botón con el tema personalizado
boton = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((200, 150), (200, 50)),
    text='Haz clic aquí',
    manager=gestor_ui
)

# Reloj para controlar el tiempo
clock = pygame.time.Clock()
corriendo = True

# Bucle principal
while corriendo:
    tiempo_delta = clock.tick(60) / 1000.0

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

        gestor_ui.process_events(evento)

    gestor_ui.update(tiempo_delta)

    ventana.fill((230, 230, 230))
    gestor_ui.draw_ui(ventana)

    pygame.display.update()

pygame.quit()



"""
{
  "button":
  {
    "normal_bg": "#ff11ff",
    "hovered_bg": "#ffff11",
    "active_bg": "#222288",
    "normal_text": "#ffffff",
    "font": {
      "name": "Broadway",
      "size": 14
    },
    "border_width": 4,
    "border_color": "#000000"
  }
}
"shape_corner_radius": "0,0,0,0",
"""