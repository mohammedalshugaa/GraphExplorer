
# Importaciones
import pygame
import pygame_gui
import sys
import ctypes
import classes      as g
import generations  as gen
from   datetime     import datetime
import color_palettes



# Inicialización del programa
pygame.init()
window = pygame.display.set_mode((1080, 800), pygame.RESIZABLE)
pygame.display.set_caption("Dijkstra Ventana Maximizada (nativa) con pygame_gui")
SDL_WINDOWPOS_CENTERED = 0x2FFF0000
sdl_window = pygame.display.get_wm_info()['window']
ctypes.windll.user32.ShowWindow(sdl_window, 3)  
window_size = window.get_size()
manager = pygame_gui.UIManager(window_size, r"C:\Users\alshu\Desktop\Grafos\Pygame\Theme.json")
print(window_size)
font=pygame.font.SysFont('tahoma',  30)



# incializacion de variables y constantes
color_arco = color_palettes.NEGRO #?
fuente = pygame.font.SysFont("dubairegular", 23)
texto = "Hola, este es un cuadro de diálogo en Pygame."
nodo_seleccionado = None
arrastrando = False



# Inicializacion de canvas y panel
x_canvas = int(window_size[0]*6.8/10)
x_panel = window_size[0]-x_canvas
y_todo = window_size[1]
canvas = pygame.Rect(0, 0, x_canvas, y_todo)
panel  = pygame.Rect(x_canvas, 0, x_panel, y_todo)
regilla = False



# Inicializacion de los tabs
tabs = {
    "Grafos":       pygame.Rect(x_canvas, 0, int(x_panel/3), 40),
    "Algoritmos":   pygame.Rect(x_canvas+int(x_panel/3), 0, int(x_panel/3), 40),
    "Propiedades":  pygame.Rect(x_canvas+int(2*x_panel/3), 0, int(x_panel/3), 40),
}
tab_activa = "Grafos"




#### botones
# Boton captura
boton_captura = pygame.Rect(x_canvas+3, 60, int(x_panel/3), 40)
clic_presionado_captura = False
def dibujar_boton(texto):
    """Dibuja el botón con texto y color según estado."""
    mouse_pos = pygame.mouse.get_pos()
    if clic_presionado_captura:
        color = color_palettes.COLOR_CLICK
    elif boton_captura.collidepoint(mouse_pos):
        color = color_palettes.COLOR_HOVER
    else:
        color = color_palettes.COLOR_NORMAL

    # Dibuja el rectángulo del botón
    pygame.draw.rect(window, color, boton_captura)

    # Renderiza el texto
    texto_superficie = fuente.render(texto, True, color_palettes.COLOR_TEXTO)
    texto_rect = texto_superficie.get_rect(center=boton_captura.center)
    window.blit(texto_superficie, texto_rect)
def captura():
# Definir un área (x, y, ancho, alto)
    area = canvas
    # Crear una subsuperficie a partir del área
    subimagen = window.subsurface(area)
    copia = window.subsurface(area).copy()
    # Guardar la imagen recortada
    ahora = datetime.now()  
    formateada = ahora.strftime("%d_%m_%Y_%H_%M_%S")
    pygame.image.save(subimagen, f"Grafo  {str(formateada)}.png")



# Boton regilla
boton_regilla = pygame.Rect(x_canvas+3, 103, int(x_panel/3), 40)
clic_presionado_regilla = False
def fun_boton_regilla(texto):
    """Dibuja el botón con texto y color según estado."""
    mouse_pos = pygame.mouse.get_pos()
    if clic_presionado_regilla:
        color = color_palettes.COLOR_CLICK
        
    elif boton_regilla.collidepoint(mouse_pos):
        color = color_palettes.COLOR_HOVER
    else:
        color = color_palettes.COLOR_NORMAL

    # Dibuja el rectángulo del botón
    pygame.draw.rect(window, color, boton_regilla)

    # Renderiza el texto
    texto_superficie = fuente.render(texto, True, color_palettes.COLOR_TEXTO)
    texto_rect = texto_superficie.get_rect(center=boton_regilla.center)
    window.blit(texto_superficie, texto_rect)



# Boton generar
boton_generar = pygame.Rect(x_canvas+int(x_panel/3)+5, 60, int(x_panel/3), 40)
clic_presionado_generar = False
def fun_boton_generar(texto):
    """Dibuja el botón con texto y color según estado."""
    mouse_pos = pygame.mouse.get_pos()
    if clic_presionado_generar:
        color = color_palettes.COLOR_CLICK
    elif boton_generar.collidepoint(mouse_pos):
        color = color_palettes.COLOR_HOVER
    else:
        color = color_palettes.COLOR_NORMAL

    # Dibuja el rectángulo del botón
    pygame.draw.rect(window, color, boton_generar)

    # Renderiza el texto
    texto_superficie = fuente.render(texto, True, color_palettes.COLOR_TEXTO)
    texto_rect = texto_superficie.get_rect(center=boton_generar.center)
    window.blit(texto_superficie, texto_rect)






######  el menu emergente
# Panel que actuará como menú contextual (inicialmente oculto)
menu_contextual = pygame_gui.elements.UIPanel(
    relative_rect=pygame.Rect((0, 0), (200, 200)),
    #starting_layer_height=1,
    manager = manager,
    visible = 0  # oculto al inicio
)


# crear nodo
# c nombre: entrada
# c color: color picker o paleta
# c tamaño: entrada o slider
# c borde: slider + color del borde
# c forma: mas avanzado: menu
# borrar nodo

opcion1 = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((-2, -2), (202, 30)),
    text='Opción 1',
    manager=manager,
    container=menu_contextual
)

opcion2 = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((-2, 24), (202, 30)),
    text='Opción 2',
    manager=manager,
    container=menu_contextual
)

opcion3 = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((-2, 50), (202, 30)),
    text='Cancelar',
    manager=manager,
    container=menu_contextual
)

# crear arco
# c dirigido o no: radio
# c color arco: color picker o paleta
# c grosor arco: slider o entrada
# c tamaño y color flecha: slider + picker o paleta 
# c peso: entrada
# c direccion de arco: radio?
# c repeticion?
# borrar arco












##############################################
# Los datos principales
#n_nodos = 20

dirigido  = True
es_simple = False

coor = gen.gen_nodos(x_canvas, y_todo)
n_nodos = len(coor)
arcos = gen.gen_arcos(n_nodos, color_arco, dirigido, False, x_canvas, y_todo)

p1 = g.Graph(coor, arcos, dirigido)
##############################################
xevento, yevento = 100, 100



reloj = pygame.time.Clock()
running = True
while True:
    
    tiempo = reloj.tick(60) / 1000.0
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
            
            
        # El evento de los taps
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            # Detectar clic en pestañas
            for nombre, rect in tabs.items():
                if rect.collidepoint(evento.pos):
                    tab_activa = nombre
                    

        # MOVER LOS NODOS
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:  # Botón izquierdo
                # Buscar si se hizo clic sobre un nodo
                for i, (x, y, *_resto) in enumerate(p1.coor):
                    dx = evento.pos[0] - x
                    dy = evento.pos[1] - y
                    if dx**2 + dy**2 <= 30**2:  # Dentro del radio del nodo
                        nodo_seleccionado = i
                        arrastrando = True
                        break

        elif evento.type == pygame.MOUSEBUTTONUP:
            if evento.button == 1:
                arrastrando = False
                nodo_seleccionado = None

        elif evento.type == pygame.MOUSEMOTION and arrastrando and nodo_seleccionado is not None:
            x_mouse, y_mouse = evento.pos

            if regilla:
                # Snap a la rejilla de 200x200
                grid_size = 50
                x_mouse = round(x_mouse / grid_size) * grid_size
                y_mouse = round(y_mouse / grid_size) * grid_size

            # Limitar a los bordes de la pantalla
            nuevo_x = max(50, min(x_mouse, 1000 - 10))
            nuevo_y = max(50, min(y_mouse, 753 - 10))

            # Actualizar posición del nodo
            p1.coor[nodo_seleccionado][0] = nuevo_x
            p1.coor[nodo_seleccionado][1] = nuevo_y



        # eventos de los botones
        # eventos del boton captura
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if boton_captura.collidepoint(evento.pos):
                clic_presionado_captura = True
                print("Botón captura presionado")                
        elif evento.type == pygame.MOUSEBUTTONUP:
            clic_presionado_captura = False
            if boton_captura.collidepoint(evento.pos):
                print("Botón captura soltado")
                captura()
        
        
        # eventos del boton regilla
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if boton_regilla.collidepoint(evento.pos):
                clic_presionado_regilla = True
                print("Botón regilla presionado") 
        elif evento.type == pygame.MOUSEBUTTONUP:
            clic_presionado_regilla = False
            if boton_regilla.collidepoint(evento.pos):
                print("Botón regilla soltado")
                regilla = not regilla
                
                
                
                
        # eventos del boton generar
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if boton_generar.collidepoint(evento.pos):
                clic_presionado_generar = True
                print("generar")            
        elif evento.type == pygame.MOUSEBUTTONUP:
            clic_presionado_generar = False
            if boton_generar.collidepoint(evento.pos):
                ###################
                #dirigido = True
                coor = gen.gen_nodos(x_canvas, y_todo)
                n_nodos = len(coor)
                arcos = gen.gen_arcos(n_nodos, color_arco, dirigido, es_simple, x_canvas, y_todo)
                p1 = g.Graph(coor, arcos, dirigido)   
                
        
        # eventos del menu emergente        
        # Mostrar menú contextual al hacer clic derecho
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 3:
            xevento, yevento = evento.pos
            menu_contextual.set_relative_position(evento.pos)
            menu_contextual.show()

        # Ocultar menú si se hace clic izquierdo fuera de él
        elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            if not menu_contextual.get_relative_rect().collidepoint(evento.pos):
                menu_contextual.hide()


        # Procesar botones del menú
        elif evento.type == pygame_gui.UI_BUTTON_PRESSED:
            if evento.ui_element == opcion1:
                print("Crear nodo")
                coor.append([xevento, yevento, len(coor)-1, color_palettes.GRIS, 30, False, 0])
                menu_contextual.hide()
            elif evento.ui_element == opcion2:
                print("Seleccionaste opción 2")
                menu_contextual.hide()
            elif evento.ui_element == opcion3:
                menu_contextual.hide()

        manager.process_events(evento)        
        
        
     

        
    # Fondo del programa
    window.fill(color_palettes.GRIS) 
    pygame.draw.rect(window, color_palettes.BLANCO, canvas, border_radius=0)
    

    
    # Dibujar todo
    p1.dibujar_dirigido(window, color_palettes.GRIS, color_palettes.NEGRO, 30)
    pygame.draw.rect(window, color_palettes.GRIS, panel, border_radius=0)
    # Dibujar tabs
    for nombre, rect in tabs.items():
        color = color_palettes.GRIS if tab_activa == nombre else color_palettes.GRIS_OSCURO
        pygame.draw.rect(window, color, rect)
        texto = fuente.render(nombre, True, color_palettes.NEGRO)
        window.blit(texto, (rect.x + 10, rect.y+2))
        
    
    # Contenido del tab seleccionado
    if tab_activa == "Grafos":
        pass
        #contenido = fuente.render("Contenido blabla PBIOU&PV", True, NEGRO)
        #window.blit(contenido, (1225, 95))
        
        #pygame.draw.rect(window, GRIS_OSCURO, boton_1, border_radius=0)
        #texto_boton = fuente.render("Random", True, BLANCO)
        #window.blit(texto_boton, (boton_1.x + 35, boton_1.y + 5))

    elif tab_activa == "Algoritmos":
        texto = "Aquí vamos a aplicar algoritmos como dijkstra."
        render = fuente.render(texto, True, color_palettes.NEGRO)
        window.blit(render, (1060, 120))

    elif tab_activa == "Propiedades":
        pass
    
    
        
        
    if tab_activa == "Grafos":
        pass
        #boton_captura.show()
        dibujar_boton("Guardar grafo")
        fun_boton_generar("Generar")
        if regilla == True:
            fun_boton_regilla("Quitar regilla")
        else:
            fun_boton_regilla("Aplicar regilla")
        
    else:
        #boton_captura.hide()
        pass
    
    #if p1.es_conexo() == False:
    #   p1.convertir_en_conexo(AZUL)

    
   
    
    manager.update(tiempo)
    manager.draw_ui(window)
    manager.process_events(evento)
    pygame.display.flip()
    