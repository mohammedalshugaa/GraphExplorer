from random import randint
import numpy as np
import color_palettes

# nodo_estandar:np.array = ["index, name, pos_x, pos_y, radio, color_nodo, border, boder_color"]
# nodo_generado:np.array = ["pos_x, pos_y, radio, color_nodo, border, border_color"]

def gen_node(min_x, max_x, min_y , max_y, radio=30, border=0, border_color=None):
    
    pos_x = randint(min_x+int((radio/2)), max_x-int((radio/2)))
    pos_y = randint(min_y+int((radio/2)), max_y-int((radio/2)))
    
    color_nodo = color_palettes.GRIS
    
    return [pos_x, pos_y, radio, color_nodo, border, border_color]


nodo1 = gen_node(0, 1000, 0, 1000)
print(nodo1)
    
    
